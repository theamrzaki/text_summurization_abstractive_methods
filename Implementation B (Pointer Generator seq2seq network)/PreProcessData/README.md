# Preproccessing Data for Model 4 & Model 5

this implementation is a continuation of the amazing work done by
- abisee's https://github.com/abisee/cnn-dailymail
that is used in both 
    - https://github.com/abisee/pointer-generator **([Model 4](https://github.com/theamrzaki/text_summurization_abstractive_methods/tree/master/Implementation%20B%20(Pointer%20Generator%20seq2seq%20network)))**
    - https://github.com/yaserkl/RLSeq2Seq **([Model 5](https://github.com/theamrzaki/text_summurization_abstractive_methods/blob/master/Implementation%20C%20(Reinforcement%20Learning%20with%20seq2seq)/Model%205%20RL.ipynb))**

-------------------------------------------------
## My modification has been
1. input data has been simplified to be in a csv format 

| content        | title         
| -------------  |:-------------:
| tex1           | summary1
| tex2           | summary2      
| tex3           | asummary3   

2. replacing Stanford CoreNLP with nltk tokenizer to make it easy to process data without the need to download java files

-------------------------------------------------
## How to Run 
the requirements are , having
1. csv of your dataset must have 2 columbs 

| content        | title         
| -------------  |:-------------:

2.  modify the variable `cnn_stories_dir`
     to point to your main directory 

3.  replace `reviews_csv`
    with your csv path
 
-------------------------------------------------

## Output 
1. folder (cnn_stories_tokenized) used internally here 
2. **finished files** (the folder that we would use)
    |--> **(folder) chunks** ==> (used in upload)
    |--> test.bin  |--> not used in upload
    |--> train.bin |--> not used in upload
    |--> val.bin  |--> not used in upload
    |--> **vocab**  ==> (used in upload)


then 
put both 
  >>|--> **(folder) chunks** ==> (used in upload)
  >>|--> **vocab**  ==> (used in upload)
  in a zip and upload online



-------------------------------------------------


## Use In model 4
 in the last code cell modify both
`FLAGS.data_path`  : to point to the chunked files
`FLAGS.vocab_path` : to point to the vocab file
