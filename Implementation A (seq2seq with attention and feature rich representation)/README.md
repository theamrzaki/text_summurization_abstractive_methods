# Text Summurization models

This repo is built to collect multiple implementations for abstractive approaches to address text summurization , 
- it is built to simply run on google colab , in one notebook and to simply connect to your drive , so you would only need an internet connection to run these examples without the need to have a powerful machine , so all the code examples would be in a jupiter format .

---------------------------------------------------------------------------------

# Model_1.ipynb
  is a modification on of David Currie's https://github.com/Currie32/Text-Summarization-with-Amazon-Reviews seq2seq , modifications made were , 
  #### the model
  - uses an encoder with multi layer RNN with LSTM
  - Decoder is built using bahadau attention model
  - Inference was cstom built by hand
  #### Data is 
  - Amazon Reviews
  #### Word2Vec
  - Conceptnet Numberbatch's (CN) embeddings, similar to GloVe, but probably better 
  (https://github.com/commonsense/conceptnet-numberbatch)
   ####  My Modifications
   - enable the model to run on tf 1.11
   - save data onto google drive , and connect the notebook to the drive
   
---------------------------------------------------------------------------------

# Model_2 Folder
## Files:
### 1- Model_2/Model_2.ipynb
a modification to https://github.com/dongjun-Lee/text-summarization-tensorflow 
  #### the model
  - uses an encoder with multi layer RNN with LSTM
  - Decoder is built using bahadau attention model
  - BeamSearchDecoder for inference
  #### Data is 
  - Dataset is available at harvardnlp/sent-summary (https://github.com/harvardnlp/sent-summary). Locate the summary.tar.gz file in project root directory. which is a collection of news and their titles
  #### Word2Vec
  - Used Glove pre-trained vectors to initialize word embedding
   ####  My Modifications
   - collected all of different modules in one notebook
   - made it compatible with jupiter notebook
   - save data onto google drive , and connect the notebook to the drive
   - Add bleu and Rouge evaluation
   - Save results with evaluations in xml format

### 2- Model_2/Model 2 features(tf-idf , pos tags).ipynb
a modification to Model 2.ipynb by using concepts from http://www.aclweb.org/anthology/K16-1028

It is a modification to the embedding vector , increasing its size from 300 to 320 by using additional features
    - TF-IDF (term freq - inverse document freq)
    - Parts of speach tags (POS Tags)

## Results
A folder contains the results of both the 2 models , from validation text samples 
in a zaksum format , which is combineing all of 
    - bleu
    - rouge_1
    - rouge_2
    - rouge_L
    - rouge_be
for each sentence , and average of all of them

we can see that there is an increase el7 in the results when using additional features of tf-idf and pos tags ,
, you can export your own zaksum format by using code from the notebooks of model 2
---------------------------------------------------------------------------------

# Model_3.ipynb
a modification to https://github.com/thomasschmied/Text_Summarization_with_Tensorflow/blob/master/summarizer_amazon_reviews.ipynb 
   ####  My Modifications
   - made it compatible with jupiter notebook
   - save data onto google drive , and connect the notebook to the drive
