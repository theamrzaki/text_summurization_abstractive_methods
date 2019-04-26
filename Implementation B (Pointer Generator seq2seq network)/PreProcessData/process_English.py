import ProgressBar

import sys
import os
import hashlib
import struct
import subprocess
import collections
import tensorflow as tf
from tensorflow.core.example import example_pb2
import nltk
import pandas as pd

#for cleaning text 
def clean_text(text, remove_stopwords = True):
    '''Remove unwanted characters, stopwords, and format the text to create fewer nulls word embeddings'''
    
    # Convert words to lower case
    text = text.lower()
    
    # Replace contractions with their longer forms 
    if True:
        text = text.split()
        new_text = []
        for word in text:
            if word in contractions:
                new_text.append(contractions[word])
            else:
                new_text.append(word)
        text = " ".join(new_text)
    
    # Format words and remove unwanted characters
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text) 
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)
    
    # Optionally, remove stop words
    if remove_stopwords:
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)

    return text


dm_single_close_quote = u'\u2019' # unicode
dm_double_close_quote = u'\u201d'
END_TOKENS = ['.', '!', '?', '...', "'", "`", '"', dm_single_close_quote, dm_double_close_quote, ")"] # acceptable ways to end a sentence

# We use these to separate the summary sentences in the .bin datafiles
SENTENCE_START = '<s>'
SENTENCE_END = '</s>'

all_train_urls = ""
all_val_urls = ""
all_test_urls = ""

cnn_tokenized_stories_dir = "cnn_stories_tokenized" #location of folder to tokenize text
dm_tokenized_stories_dir = "dm_stories_tokenized" #not used
finished_files_dir = "arabic_finished_files" #final ouput
chunks_dir = os.path.join(finished_files_dir, "chunked")



VOCAB_SIZE = 200000
CHUNK_SIZE = 1000 # num examples per chunk, for the chunked data


def chunk_file(set_name):
  in_file = finished_files_dir + '/%s.bin' % set_name
  reader = open(in_file, "rb")
  chunk = 0
  finished = False
  while not finished:
    chunk_fname = os.path.join(chunks_dir, '%s_%03d.bin' % (set_name, chunk)) # new chunk
    with open(chunk_fname, 'wb') as writer:
      for _ in range(CHUNK_SIZE):
        len_bytes = reader.read(8)
        if not len_bytes:
          finished = True
          break
        str_len = struct.unpack('q', len_bytes)[0]
        example_str = struct.unpack('%ds' % str_len, reader.read(str_len))[0]
        writer.write(struct.pack('q', str_len))
        writer.write(struct.pack('%ds' % str_len, example_str))
      chunk += 1


def chunk_all():
  # Make a dir to hold the chunks
  if not os.path.isdir(chunks_dir):
    os.mkdir(chunks_dir)
  # Chunk the data
  for set_name in ['train', 'val', 'test']:
    print ("Splitting %s data into chunks..." % set_name)
    chunk_file(set_name)
  print ("Saved chunked data in %s" % chunks_dir)


def tokenize_stories(reviews, tokenized_stories_dir):
  """Maps a whole directory of .story files to a tokenized version using Stanford CoreNLP Tokenizer"""
  progress = ProgressBar.ProgressBar(len(reviews), fmt=ProgressBar.ProgressBar.FULL)

  for i, row in reviews.iterrows():
        #if i==20:
        #    break
        filename = str(i) + '.tok'
        with open(os.path.join(tokenized_stories_dir, filename), 'w', encoding="utf-8") as temp_file:
            text = row["content"]
            text = clean_text(text , remove_stopwords = True)
            tok = nltk.word_tokenize(text)
            tok.append("@highlight")
            Summary = row["title"]
            Summary = clean_text(Summary ,remove_stopwords = False)
            tok.extend(nltk.word_tokenize(Summary))
            list = tok.copy()

            for i in tok:
                if(i=='``' or i=="''" ):
                    list.remove(i)
            tok_string = "\n".join(str(x) for x in list)
            temp_file.write(tok_string)

        progress.current += 1
        progress()
  print ("Successfully finished tokenizing to %s .\n" % (tokenized_stories_dir))


def fix_missing_period(line):
  """Adds a period to a line that is missing a period"""
  if "@highlight" in line: return line
  if line=="": return line
  if line[-1] in END_TOKENS: return line
  # print line[-1]
  return line + " ."

def read_text_file(text_file):
  lines = []
  with open(text_file, "r", encoding="utf-8") as f:
    for line in f:
      lines.append(line.strip())
  return lines

def get_art_abs(story_file):
  lines = read_text_file(story_file)

  # Lowercase everything
  lines = [line.lower() for line in lines]

  # Put periods on the ends of lines that are missing them (this is a problem in the dataset because many image captions don't end in periods; consequently they end up in the body of the article as run-on sentences)
  lines = [fix_missing_period(line) for line in lines]

  # Separate out article and abstract sentences
  article_lines = []
  highlights = []
  next_is_highlight = False
  for idx,line in enumerate(lines):
    if line == "":
      continue # empty line
    elif line.startswith("@highlight"):
      next_is_highlight = True
    elif next_is_highlight:
      highlights.append(line)
    else:
      article_lines.append(line)

  # Make article into a single string
  article = ' '.join(article_lines)

  # Make abstract into a signle string, putting <s> and </s> tags around the sentences
  abstract = ' '.join(["%s %s %s" % (SENTENCE_START, sent, SENTENCE_END) for sent in highlights])

  return article, abstract


def write_to_bin(file_names, out_file, makevocab=False):
  """Reads the tokenized .story files corresponding to the urls listed in the url_file and writes them to a out_file."""
 
  story_fnames = [str(s)+".tok" for s in file_names]
  num_stories = len(story_fnames)

  if makevocab:
    vocab_counter = collections.Counter()

  with open(out_file, 'wb') as writer:
    for idx,s in enumerate(story_fnames):
      if idx % 1000 == 0:
        print( "Writing story %i of %i; %.2f percent done" % (idx, num_stories, float(idx)*100.0/float(num_stories)))

      # Look in the tokenized story dirs to find the .story file corresponding to this url
      if os.path.isfile(os.path.join(cnn_tokenized_stories_dir, s)):
        story_file = os.path.join(cnn_tokenized_stories_dir, s)
      elif os.path.isfile(os.path.join(dm_tokenized_stories_dir, s)):
        story_file = os.path.join(dm_tokenized_stories_dir, s)
      else:
        print ("Error: Couldn't find tokenized story file %s in either tokenized story directories %s and %s. Was there an error during tokenization?" % (s, cnn_tokenized_stories_dir, dm_tokenized_stories_dir))
        # Check again if tokenized stories directories contain correct number of files
        print ("Checking that the tokenized stories directories %s and %s contain correct number of files..." % (cnn_tokenized_stories_dir, dm_tokenized_stories_dir))
        #check_num_stories(cnn_tokenized_stories_dir, num_expected_cnn_stories)
        #check_num_stories(dm_tokenized_stories_dir, num_expected_dm_stories)
        #raise Exception("Tokenized stories directories %s and %s contain correct number of files but story file %s found in neither." % (cnn_tokenized_stories_dir, dm_tokenized_stories_dir, s))
        
      # Get the strings to write to .bin file
      article, abstract = get_art_abs(story_file)

      
      # Write to tf.Example
      tf_example = example_pb2.Example()
      tf_example.features.feature['article'].bytes_list.value.extend([article.encode('utf-8')])
      tf_example.features.feature['abstract'].bytes_list.value.extend([abstract.encode('utf-8')])
      tf_example_str = tf_example.SerializeToString()
      str_len = len(tf_example_str)
      writer.write(struct.pack('q', str_len))
      writer.write(struct.pack('%ds' % str_len, tf_example_str))
   

      # Write the vocab to file, if applicable
      if makevocab:
        art_tokens = article.split(' ')
        abs_tokens = abstract.split(' ')
        abs_tokens = [t for t in abs_tokens if t not in [SENTENCE_START, SENTENCE_END]] # remove these tags from vocab
        tokens = art_tokens + abs_tokens
        tokens = [t.strip() for t in tokens] # strip
        tokens = [t for t in tokens if t!=""] # remove empty
        vocab_counter.update(tokens)

  print ("Finished writing file %s\n" % out_file)

  # write vocab to file
  if makevocab:
    print ("Writing vocab file...")
    with open(os.path.join(finished_files_dir, "vocab"), 'w', encoding="utf-8") as writer:
      for word, count in vocab_counter.most_common(VOCAB_SIZE):
        writer.write(word + ' ' + str(count) + '\n')
    print ("Finished writing vocab file")


def check_num_stories(stories_dir, num_expected):
  num_stories = len(os.listdir(stories_dir))
  if num_stories != num_expected:
    raise Exception("stories directory %s contains %i files but should contain %i" % (stories_dir, num_stories, num_expected))





"""
the requirements are , having
    1- csv of your data set having 2 columbs 
        content(text) |  summary 
        by modifying 
        cnn_stories_dir to pointtto your main directory 
        and then replacing \ArabicBook00.csv
        with your csv


output would be 
    1- folder (cnn_stories_tokenized) used internally here 
    2- finished files (the folder that we would use)
        |--> (folder) chunks ==> (used in upload)
        |--> test.bin  |
        |--> train.bin |--> not used in upload
        |--> val.bin   |
        |--> vocab  ==> (used in upload)

    then 
    put both 
      |--> (folder) chunks ==> (used in upload)
      |--> vocab  ==> (used in upload)
      in a zip and upload online
"""



if __name__ == '__main__':
  #main directory
  cnn_stories_dir =  r"E:\Handasa\Majester\thesis\python\DataProcessing\DataProcessing\arhelpers"

  # Create some new directories
  if not os.path.exists(cnn_tokenized_stories_dir): os.makedirs(cnn_tokenized_stories_dir)
  if not os.path.exists(finished_files_dir): os.makedirs(finished_files_dir)

  #data needed is in a csv format
  #containg 2 columbs (content , title)
  reviews_csv =cnn_stories_dir + "\ArabicBook00.csv"
  reviews = pd.read_csv(reviews_csv)
  reviews = reviews.filter(['content', 'title'])
  reviews = reviews.dropna()
  reviews = reviews.reset_index(drop=True)
  reviews.head()

  # Run nltk tokenizer on both text and summary , outputting to tokenized stories directories
  tokenize_stories(reviews, cnn_tokenized_stories_dir)

  #to get the length of your dataset
  num_expected_cnn_stories =reviews.shape[0]

  #testing len = 2000
  #validation lenght = 2000
  all_train_urls = range(0,num_expected_cnn_stories-2000)
  all_val_urls = range(num_expected_cnn_stories-2000,num_expected_cnn_stories-1000)
  all_test_urls = range(num_expected_cnn_stories-1000,num_expected_cnn_stories)

  #for testing
  ##############all_train_urls= range(0,80)
  ##############all_val_urls = range(80,90)
  ##############all_test_urls = range(90,100)

  # Read the tokenized stories, do a little postprocessing then write to bin files
  write_to_bin(all_test_urls, os.path.join(finished_files_dir, "test.bin"))
  write_to_bin(all_val_urls, os.path.join(finished_files_dir, "val.bin"))
  write_to_bin(all_train_urls, os.path.join(finished_files_dir, "train.bin"), makevocab=True)

  # Chunk the data. This splits each of train.bin, val.bin and test.bin into smaller chunks, each containing e.g. 1000 examples, and saves them in finished_files/chunks
  chunk_all()

