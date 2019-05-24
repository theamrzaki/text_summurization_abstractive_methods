# Implementation B (Pointer Generator seq2seq network)
it is a continuation of the amazing work of
	https://github.com/abisee/pointer-generator
	https://arxiv.org/abs/1704.04368
this implementation uses the concept of having a pointer generator network to diminish some problems that appears with the normal 
seq2seq network

Know more about how this model was built , and about pointer genrator through this tutorial 
generator 
- **Tutorial 7** [Pointer generator for combination of Abstractive & Extractive methods for Text Summarization](http://bit.ly/2EhcRIZ)

Try out this pointer genrator model through [this website (eazymind)](http://bit.ly/2VxhPqU) ,
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
from nlp.eazysum import Summarizer

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




### Model_4_generator_.ipynb
uses a pointer generator with seq2seq with attention 
it is built using python2.7
### zaksum_eval.ipynb
built by python3 for evaluation
### Results/Pointer Generator
- output from generator (article / reference / summary) used as input to the zaksum_eval.ipynb
- result from zaksum_eval
	
	
i will still work on their implementation of coverage mechanism , so much work is yet to come if God wills it isA
