# Implementation B (Pointer Generator seq2seq network)
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
