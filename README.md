# Text Summarization models

This repo is built to collect multiple implementations for abstractive approaches to address text summarization , 

**it is built to simply run on google colab , in one notebook  so you would only need an internet connection to run these examples without the need to have a powerful machine , so all the code examples would be in a jupiter format , and you don't have to download data to your device as we connect these jupiter notebooks to google drive**

-  **implementation A** Corner stone seq2seq with attention (using bidirectional ltsm ) , three different models for this implemntation 
-  **implementation B** seq2seq with pointer genrator model
-  **implementation C** seq2seq with reinforcement learning

# Blogs
This repo has been explained in a series of Blogs
- to understand how to work with google colab eco system , and how to integrate it with your google drive , this blog can prove useful [DeepLearning Free Ecosystem](https://hackernoon.com/begin-your-deep-learning-project-for-free-free-gpu-processing-free-storage-free-easy-upload-b4dba18abebc "DeepLearning Free Ecosystem")
- **Tutorial 1** [ Overview on the different appraches used for abstractive text summarization](https://hackernoon.com/text-summarizer-using-deep-learning-made-easy-490880df6cd?source=post_stats_page--------------------------- "Overview on  abstractive text summarization")
- **Tutorial 2**  [ How to represent text for our text summarization task ](https://hackernoon.com/abstractive-text-summarization-tutorial-2-text-representation-made-very-easy-ef4511a1a46?source=post_stats_page--------------------------- "text represneataion for text summarization")
- **Tutorial 3**  [ What seq2seq and why do we use it in text summarization ](https://hackernoon.com/tutorial-3-what-is-seq2seq-for-text-summarization-and-why-68ebaa644db0?source=post_stats_page--------------------------- "What and why seq2seq")
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

---------------------------------------------------------------------------------
## Implementation C (Reinforcement Learning For Sequence to Sequence )

this implementation is a continuation of the amazing work done by
https://github.com/yaserkl/RLSeq2Seq

```
@article{keneshloo2018deep,
 title={Deep Reinforcement Learning For Sequence to Sequence Models},
 author={Keneshloo, Yaser and Shi, Tian and Ramakrishnan, Naren and Reddy, Chandan K.},
 journal={arXiv preprint arXiv:1805.09461},
 year={2018}
}
```


### Model 5 RL
this is a library for building multiple approaches using Reinforcement Learning with seq2seq , i have gathered their code to run in a jupiter notebook , and to access google drive 
built for python 2.7

### zaksum_eval.ipynb
built by python3 for evaluation

### Results/Reinforcement Learning
- output from Model 5 RL used as input to the zaksum_eval.ipynb

