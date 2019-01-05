# Text Summarization models

This repo is built to collect multiple implementations for abstractive approaches to address text summarization , 
- it is built to simply run on google colab , in one notebook and to simply connect to your drive , so you would only need an internet connection to run these examples without the need to have a powerful machine , so all the code examples would be in a jupiter format .

- to understand how to work with google colab eco system , and how to integrate it with your google drive , this blog can prove useful
https://hackernoon.com/begin-your-deep-learning-project-for-free-free-gpu-processing-free-storage-free-easy-upload-b4dba18abebc
---------------------------------------------------------------------------------

## Implementation A (seq2seq with attention and feature rich representation)
contains 3 different models that implements the concept of hving a seq2seq network with attention 
also adding concepts like having a feature rich word representation 
This work is a continuation of these amazing repos

### Model 1 
is a modification on of David Currie's https://github.com/Currie32/Text-Summarization-with-Amazon-Reviews seq2seq 

### Model 2 
#### 1- Model_2/Model_2.ipynb
a modification to https://github.com/dongjun-Lee/text-summarization-tensorflow 
#### 2- Model_2/Model 2 features(tf-idf , pos tags).ipynb
a modification to Model 2.ipynb by using concepts from http://www.aclweb.org/anthology/K16-1028
#### Results
A folder contains the results of both the 2 models , from validation text samples 
in a zaksum format , which is combining all of 
- bleu
- rouge_1
- rouge_2
- rouge_L
- rouge_be
for each sentence , and average of all of them

### Model 3
a modification to https://github.com/theamrzaki/text_summurization_abstractive_methods/blob/master/Model_3.ipynb 

		
---------------------------------------------------------------------------------

## Implementation B (Pointer Generator seq2seq network)
it is a continuation of the amazing work of
	https://github.com/abisee/pointer-generator
	https://arxiv.org/abs/1704.04368
this implementation uses the concept of having a pointer generator network to diminish some problems that appears with the normal 
seq2seq network
	
### Model_4_generator_.ipynb
uses a pointer generator with seq2seq with attention 
it is built using python2.7
### zaksum_eval.ipynb
built by python3 for evaluation
### Results/Pointer Generator
- output from generator (article / reference / summary) used as input to the zaksum_eval.ipynb
- result from zaksum_eval
	
	
i will still work on their implementation of coverage mechanism , so much work is yet to come if God wills it isA
	