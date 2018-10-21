# Text Summurization models

This repo is built to contain multiple different implementations for abstractive approaches to address text summurization , using different datasets , different word2vec , different models , and to review the differences between them to reach the best results.

- All implemntations are built to simply run on google colab , in one notebook and to simply connect to your drive , so you would only need an internet connection to run these examples without the need to have a powerful machine , so all the code examples would be in a jupiter format , and all your datasets and word2vec would be saved on google drive.

---------------------------------------------------------------------------------

# The first ipython (Seq2Seq2.ipynb)
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

# The Secound ipython (Model_2_seq2seq_using_lib.ipynb)
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
