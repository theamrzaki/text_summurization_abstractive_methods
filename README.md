# Text Summarization models

if you are able to endorse me on Arxiv, i would be more than glad https://arxiv.org/auth/endorse?x=FRBB89 thanks 
This repo is built to collect multiple implementations for abstractive approaches to address text summarization , for different languages (Hindi, Amharic, English, and soon isA Arabic)

If you found this project helpful please consider citing our work, it would truly mean so much for me

```
@INPROCEEDINGS{9068171,
  author={A. M. {Zaki} and M. I. {Khalil} and H. M. {Abbas}},
  booktitle={2019 14th International Conference on Computer Engineering and Systems (ICCES)}, 
  title={Deep Architectures for Abstractive Text Summarization in Multiple Languages}, 
  year={2019},
  volume={},
  number={},
  pages={22-27},}
```

```
@misc{zaki2020amharic,
    title={Amharic Abstractive Text Summarization},
    author={Amr M. Zaki and Mahmoud I. Khalil and Hazem M. Abbas},
    year={2020},
    eprint={2003.13721},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

**it is built to simply run on google colab , in one notebook  so you would only need an internet connection to run these examples without the need to have a powerful machine , so all the code examples would be in a jupiter format , and you don't have to download data to your device as we connect these jupiter notebooks to google drive**

- **Arabic Summarization** Model using the corner stone implemtnation (seq2seq using Bidirecional LSTM Encoder and attention in the decoder) for summarizing Arabic news
-  **implementation A** Corner stone seq2seq with attention (using bidirectional ltsm ) , three different models for this implemntation 
-  **implementation B** seq2seq with pointer genrator model
-  **implementation C** seq2seq with reinforcement learning

# Blogs
This repo has been explained in a series of Blogs
- to understand how to work with google colab eco system , and how to integrate it with your google drive , this blog can prove useful [DeepLearning Free Ecosystem](https://hackernoon.com/begin-your-deep-learning-project-for-free-free-gpu-processing-free-storage-free-easy-upload-b4dba18abebc "DeepLearning Free Ecosystem")
- **Tutorial 1** [ Overview on the different appraches used for abstractive text summarization](https://hackernoon.com/text-summarizer-using-deep-learning-made-easy-490880df6cd?source=post_stats_page--------------------------- "Overview on  abstractive text summarization")
- **Tutorial 2**  [ How to represent text for our text summarization task ](https://hackernoon.com/abstractive-text-summarization-tutorial-2-text-representation-made-very-easy-ef4511a1a46?source=post_stats_page--------------------------- "text represneataion for text summarization")
- **Tutorial 3**  [ What seq2seq and why do we use it in text summarization ](https://hackernoon.com/tutorial-3-what-is-seq2seq-for-text-summarization-and-why-68ebaa644db0?source=post_stats_page--------------------------- "What and why seq2seq")
- **Tutorial 4** [Multilayer Bidirectional Lstm/Gru for text summarization](https://medium.com/@theamrzaki/multilayer-bidirectional-lstm-gru-for-text-summarization-made-easy-tutorial-4-a63db108b44f)
- **Tutorial 5** [Beam Search & Attention for text summarization](https://medium.com/@theamrzaki/beam-search-attention-for-text-summarization-made-easy-tutorial-5-3b7186df7086)
- **Tutorial 6** [Build an Abstractive Text Summarizer in 94 Lines of Tensorflow](http://bit.ly/2ZeEmvO)
- **Tutorial 7** [Pointer generator for combination of Abstractive & Extractive methods for Text Summarization](http://bit.ly/2EhcRIZ)
- **Tutorial 8** [Teach seq2seq models to learn from their mistakes using deep curriculum learning](http://bit.ly/2My51kX)
- **Tutorial 9** [Deep Reinforcement Learning (DeepRL) for Abstractive Text Summarization made easy](http://bit.ly/2MDlUHC)
- **Tutorial 10** [Hindi Text Summarization](https://medium.com/analytics-vidhya/hindi-abstractive-text-summarization-tutorial-10-eac471bdafad)
---------------------------------------------------------------------------------

Try out this text summarization through [this website (eazymind)](http://bit.ly/2VxhPqU) ,
![eazymind](https://scontent.fcai3-1.fna.fbcdn.net/v/t1.0-9/60785552_445522029607880_7282873905209933824_o.jpg?_nc_cat=101&_nc_ht=scontent.fcai3-1.fna&oh=927d1fae6521813b3d6e7a7d7a5b01aa&oe=5D5C3AD5) which enables you to summarize your text through
- curl call
```
curl -X POST 
http://eazymind.herokuapp.com/arabic_sum/eazysum
-H 'cache-control: no-cache' 
-H 'content-type: application/x-www-form-urlencoded' 
-d "eazykey={eazymind api key}&sentence={your sentence to be summarized}"
```
- python package ([pip install eazymind](http://bit.ly/2Ef5XnS))
	```pip install eazymind```
	
```
from eazymind.nlp.eazysum import Summarizer

#---key from eazymind website---
key = "xxxxxxxxxxxxxxxxxxxxx"

#---sentence to be summarized---
sentence = """(CNN)The White House has instructed former
    White House Counsel Don McGahn not to comply with a subpoena
    for documents from House Judiciary Chairman Jerry Nadler, 
    teeing up the latest in a series of escalating oversight 
    showdowns between the Trump administration and congressional Democrats."""
    
summarizer = Summarizer(key)
print(summarizer.run(sentence))
```

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
a modification to https://github.com/thomasschmied/Text_Summarization_with_Tensorflow/blob/master/summarizer_amazon_reviews.ipynb

		
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
https://arxiv.org/abs/1805.09461

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

