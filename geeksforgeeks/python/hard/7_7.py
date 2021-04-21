Avengers Endgame and Deep learning | Image Caption Generation using the
Avengers EndGames Characters



Behold, Marvel Fans. Avengers are out there to save the Multiverse, so are we,
ready to do _whatever it takes_ to support them.  
In this article, we will use Deep Learning and computer vision for the caption
generation of Avengers Endgame characters. We will start will the basics,
explaining concepts and use a pre-trained model to implement the project.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417162905/avengers-endgame-poster-top-half.jpg)

### An Overview:

Image Caption generation is a challenging problem in AI that connects computer
vision and NLP where a textual description must be generated for a given
photograph. In General Sense for a given image as input, our model describes
the exact description of an Image. It requires both image understanding from
the domain of computer vision which Convolution Neural Network and a language
model from the field of Natural language processing.  
It is important to assume and test multiple ways to frame a given predictive
modeling problem and there are indeed many ways to frame the problem of
generating captions for photographs. we stick to one which we’ll Explain at
the end of this article so hold for some time. can you hold **Thor Hammer
!!!** **NO**!! but you could hold here, joke apart.

So Basically what our model does is when we pass an image to our CNN and RNN
combined architecture then it will generate the natural description of the
image using NLP.

> We show a generative model based on a deep Recurrent neural architecture
> that combines with machine translation and which can be used to generate
> natural sentences which describe an image. The model is trained to maximize
> the likelihood of the target descriptions sentence given the training
> images. Experiments on various datasets show the accuracy of the model and
> the fluency of the language which it learns solely from image descriptions.
>
>  
>
>
>  
>

 **Example:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190417173600/Capture34-2.png)

Before going deeper let’s understand the basic terminology which is required
to understand this algorithm.

They are basically two types:

