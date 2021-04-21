ML | Why Logistic Regression in Classification ?



Using Linear Regression, all predictions >= 0.5 can be considered as 1 and
rest all < 0.5 can be considered as 0. But then the question arises why
classification can’t be performed using it?

 **Problem –**

Suppose we are classifying a mail as spam or not spam and our output is **y**
, it can be 0(spam) or 1(not spam). In case of Linear Regression, hθ(x) can be
> 1 or < 0\. Although our prediction should be in between 0 and 1, the model
will predict value out of the range i.e. maybe > 1 or < 0.

So, that’s why for a Classification task, Logistic/Sigmoid Regression plays
its role.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190502133352/Logistic_Regression.jpg)

![ h_{\\Theta} \(x\) = g \(\\Theta ^{T}x\)  z =  \\Theta ^{T}x  g\(z\) =
\\frac{1}{1+e^{-z}} ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7873be67e6d7e004f497816a09b2952d_l3.png)

Here, we plug **θ Tx** into logistic function where θ are the
weights/parameters and **x** is the input and **h θ(x)** is the hypothesis
function. **g()** is the sigmoid function.

  

  

![  h_{\\Theta} \(x\) = P\( y =1 | x ; \\Theta \)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-496eb9250dfc25b83efdfb2ee33602dc_l3.png)

It means that y = 1 probability when x is parameterized to **θ**

To get the discrete values 0 or 1 for classification, discrete boundaries are
defined. The hypothesis function cab be translated as

![  h_{\\Theta} \(x\) \\geq 0.5 \\rightarrow y = 1  h_{\\Theta} \(x\) < 0.5
\\rightarrow y = 0 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ec435a7f979e6dcda9ba52367ddaa4e8_l3.png)

![  {g\(z\) \\geq 0.5} \\\\  {\\Rightarrow \\Theta ^{T}x \\geq 0.5} \\\\
{\\Rightarrow z \\geq 0.5 } ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c760ab5ffcb9c957c7823a4b77b0bea6_l3.png)

Decision Boundary is the line that distinguishes the area where y=0 and where
y=1. These decision boundaries result from the hypothesis function under
consideration.

 **Understanding Decision Boundary with an example –**  
Let our hypothesis function be

![  h_{\\Theta}\(x\)= g\[\\Theta_{0}+ \\Theta_1x_1+\\Theta_2x_2+
\\Theta_3x_1^2 + \\Theta_4x_2^2 \]  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c60ea8610a9a02b482060cd4a5acd62d_l3.png)

Then the decision boundary looks like  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190503112448/Logistics_Regression2-3.jpg)  
Let out weights or parameters be –

![  \\Theta=\\begin{bmatrix} -1\\\\  0\\\\  0\\\\  1\\\\ 1 \\end{bmatrix}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a2966e11ba96a0c773b86740d1380c5b_l3.png)

So, it predicts y = 1 if

![  -1 + x_{1}^2 + x_{2}^2 \\geqslant 0  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-04ec5ad55d40d31a9217e706ab6c5584_l3.png)

![  \\Rightarrow x_{1}^2 + x_{2}^2 \\geqslant 1
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8b1608dd0a28fd35019bfb841c85793e_l3.png)

And that is the equation of a circle with radius = 1 and origin as the center.
This is the Decision Boundary for our defined hypothesis.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

