Generative Adversarial Network (GAN)



Generative Adversarial Networks (GANs) are a powerful class of neural networks
that are used for unsupervised learning. It was developed and introduced by
Ian J. Goodfellow in 2014. GANs are basically made up of a system of two
competing neural network models which compete with each other and are able to
analyze, capture and copy the variations within a dataset.

 **Why were GANs developed in the first place?**  
It has been noticed most of the mainstream neural nets can be easily fooled
into misclassifying things by adding only a small amount of noise into the
original data. Surprisingly, the model after adding noise has higher
confidence in the wrong prediction than when it predicted correctly. The
reason for such adversary is that most machine learning models learn from a
limited amount of data, which is a huge drawback, as it is prone to
overfitting. Also, the mapping between the input and the output is almost
linear. Although, it may seem that the boundaries of separation between the
various classes are linear, but in reality, they are composed of linearities
and even a small change in a point in the feature space might lead to
misclassification of data.

 **How does GANs work?**

Generative Adversarial Networks (GANs) can be broken down into three parts:

  *  **Generative:** To learn a generative model, which describes how data is generated in terms of a probabilistic model.

