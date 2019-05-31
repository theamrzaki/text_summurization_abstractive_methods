# Implementation C (Reinforcement Learning For Sequence to Sequence )

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

This is a library for implementing **Reinforcment learning with deep learning for text summarization** , which has been converted to a jupyter notebook format to run seamlesly within google colab
here apply some experiments from published papers using this library . 

## Scheduled Sampling with intradecoder 
description from [yasterk](https://github.com/yaserkl/RLSeq2Seq#scheduled-sampling-soft-scheduled-sampling-and-end2endbackprop) 

[Bengio et al](https://arxiv.org/abs/1506.03099). proposed the idea of scheduled sampling for avoiding exposure bias problem.
```
@ARTICLE{2015arXiv150603099B,
       author = {{Bengio}, Samy and {Vinyals}, Oriol and {Jaitly}, Navdeep and
         {Shazeer}, Noam},
        title = "{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Machine Learning, Computer Science - Computation and Language, Computer Science - Computer Vision and Pattern Recognition},
         year = "2015",
        month = "Jun",
          eid = {arXiv:1506.03099},
        pages = {arXiv:1506.03099},
archivePrefix = {arXiv},
       eprint = {1506.03099},
 primaryClass = {cs.LG},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2015arXiv150603099B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```


## Policy-Gradient 
description from [yasterk](https://github.com/yaserkl/RLSeq2Seq#scheduled-sampling-soft-scheduled-sampling-and-end2endbackprop) 

[Paulus et al](https://arxiv.org/abs/1705.04304). proposed a self-critic policy-gradient model for abstractive text summarization. The following figure represents how this method works and how we implemented this method:

image from [yasterk](https://github.com/yaserkl/RLSeq2Seq#scheduled-sampling-soft-scheduled-sampling-and-end2endbackprop) 
![Policy-Gradient](https://github.com/yaserkl/RLSeq2Seq/raw/master/docs/_img/selfcritic.png)

```
@ARTICLE{2017arXiv170504304P,
       author = {{Paulus}, Romain and {Xiong}, Caiming and {Socher}, Richard},
        title = "{A Deep Reinforced Model for Abstractive Summarization}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language},
         year = "2017",
        month = "May",
          eid = {arXiv:1705.04304},
        pages = {arXiv:1705.04304},
archivePrefix = {arXiv},
       eprint = {1705.04304},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2017arXiv170504304P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```





