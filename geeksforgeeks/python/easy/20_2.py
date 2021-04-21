ML | Normal Equation in Linear Regression



 **Normal Equation** is an analytical approach to Linear Regression with a
Least Square Cost Function. We can directly find out the value of θ without
using Gradient Descent. Following this approach is an effective and a time-
saving option when are working with a dataset with small features.

 **Normal Equation is a follows :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-
drawing-1-10.png)  
In the above equation,  
 **θ :** hypothesis parameters that define it the best.  
 **X :** Input feature value of each instance.  
 **Y :** Output value of each instance.

#### Maths Behind the equation –

Given the hypothesis function ![](https://media.geeksforgeeks.org/wp-
content/uploads/1-80.jpg)  
where,  
 **n :** the no. of features in the data set.  
 **x 0 :** 1 (for vector multiplication)

Notice that this is dot product between θ and x values. So for the convenience
to solve we can write it as :  
![](https://media.geeksforgeeks.org/wp-content/uploads/1.1-2.jpg)  
The motive in Linear Regression is to minimize the **cost function** :

![  J\(\\Theta\) = \\frac{1}{2m} \\sum_{i = 1}^{m} \\frac{1}{2}
\[h_{\\Theta}\(x^{\(i\)}\) - y^{\(i\)}\]^{2}
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
aa707afad8bcd0f7a4424e31cb616000_l3.png)

where,  
 **x i :** the input value of iih training example.  
 **m :** no. of training instances  
 **n :** no. of data-set features  
 **y i :** the expected result of ith instance

  

  

Let us representing cost function in a vector form.  
![](https://media.geeksforgeeks.org/wp-content/uploads/3-43.jpg)  
we have ignored 1/2m here as it will not make any difference in the working.
It was used for the mathematical convenience while calculation gradient
descent. But it is no more needed here.  
![](https://media.geeksforgeeks.org/wp-content/uploads/5-20.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/6-12.jpg)  
 **x ij :** value of jih feature in iih training example.

This can further be reduced to ![ X\\theta -
y](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5d5fec1d098a79e423c82b25450a90af_l3.png)  
But each residual value is squared. We cannot simply square the above
expression. As the square of a vector/matrix is not equal to the square of
each of its values. So to get the squared value, multiply the vector/matrix
with its transpose. So, the final equation derived is  
![](https://media.geeksforgeeks.org/wp-content/uploads/8-7.jpg)  
Therefore, the cost function is  
![](https://media.geeksforgeeks.org/wp-content/uploads/9-5.jpg)  
So, now getting the value of θ using derivative  
![](https://media.geeksforgeeks.org/wp-content/uploads/10-4.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/11-11.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/12-4.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/13.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/14.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/16.jpg)  
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-
drawing-1-10.png)  
So, this is the finally derived **Normal Equation with θ giving the minimum
cost value.**

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

