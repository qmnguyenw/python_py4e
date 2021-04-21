Overview of Style Transfer (Deep Harmonization)



Since humans have started educating themselves of the surrounding world,
painting has remained the salient way of expressing emotions and
understanding. For example, the image of the tiger below has the content of a
tiger from real-world tigers. But notice the style of texturing and colouring
is way dependent on the creator.

 **What is Style Transfer in Neural Networks?**  
Suppose you have your photograph (P), captured from your phone. You want to
stylize your photograph as shown below.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200522142556/Capture489-1024x338.png)

This process of taking the content of one image (P) and style of another image
(A) to generating an image (X) matching content of P and style of A is called
Style Transfer or Deep Harmonization. You cannot obtain X by simply
overlapping P and A.

 **Architecture & Algorithm**  
 **Gatys et al** in 2015 showed that it is possible to separate content and
style of an image and hence possible to combine content and style of different
images. He used a convolutional neural network (CNN), called vgg-19 (vgg
stands for Visual Geometric Group) which is 19 layers deep (with 16 CONV
layers and 3 FC layers).  
vgg-19 is pre-trained on ImageNet dataset by Standford Vision Lab of Stanford
University. Gatys used average pooling and no FC layers.  
Pooling is typically used to reduce the spatial volume of feature vectors.
This helps to reduce the amount of computations. There are 2 types of pooling
as depicted below:  

![MAX & AVG Pool](https://media.geeksforgeeks.org/wp-
content/uploads/20200602125916/gauravPool-1024x595.png)

Pooling Process

  
 **Losses in Style Transfer:**

  *  **Content Loss**  
Let us select a hidden layer (L) in vgg-19 to calculate the content loss. Let
p: original image and x: generated image. Let Pl and Fl denote feature
representations of the respective images corresponding to layer L. Then the
content loss will be defined as:  
![L _{\\text {content}}\(\\rho, x, L\)=\\frac{1}{2} \\sum_{i j}\\left\(F_{i
j}^{l}-P_{i j}^{l}\\right\)^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-838b41876a53d461fc538b7987c0de1e_l3.png)

  *  **Style Loss**  
For this, we first have to calculate **Gram Matrix**. Calculation of
correlation between different filters/ channels involves the dot product
between the vectorized feature maps i and j at layer l. The matrix thus
obtained is called Gram Matrix (G). Style loss is the square of difference
between the Gram Matrix of the style image with the Gram Matrix of generated
Image.  
![G_{i j}^{l}=\\sum_{k} F_{i k}^{l} F_{j
k}^{l}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-39d12c57e677eeaf5aec3ef8847f2e5d_l3.png)

  *  **Total Loss**  
is defined by the below formula (with α and β are hyperparameters that are set
as per requirement).  
![L_{\\text {total}}\(P, A, X\)=\\alpha \\times L_{\\text {content}}+\\beta
\\times L_{\\text {style}}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-70d6995524a691cda4dbf6053e4b8c67_l3.png)  
The generated image X, in theory, is such that the content loss and style loss
is least. That means X matches both the content of P and style of A at the
same time. Doing this will generate the desired output.

 **Note:** This is very exciting new field made possible due to hardware
optimizations, parallelism with CUDA (Compute Unified Device Architecture) and
Intel’s hyperthreading concept.  
 **Code & Output**  
You can find the **entire code, data files and outputs** of Style Transfer
(bonus for sticking around : It has code for audio styling as well!) here
__CA__’s Github Repo.

Attention reader! Don’t stop learning now. Get hold of all the important CS
Theory concepts for SDE interviews with the **CS Theory Course** at a student-
friendly price and become industry ready.

My Personal Notes _arrow_drop_up_

Save

