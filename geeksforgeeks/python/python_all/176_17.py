Linear Regression Using Tensorflow



We will briefly summarize Linear Regression before implementing it using
Tensorflow. Since we will not get into the details of either Linear Regression
or Tensorflow, please read the following articles for more details:

  * Linear Regression (Python Implementation)
  * Introduction to TensorFlow
  * Introduction to Tensor with Tensorflow

## Brief Summary of Linear Regression

Linear Regression is a very common statistical method that allows us to learn
a function or relationship from a given set of continuous data. For example,
we are given some data points of x and corresponding y and we need to
learn the relationship between them that is called a **hypothesis**.

In case of Linear regression, the hypothesis is a straight line, i.e,  
![ h\(x\) = wx + b ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3a8cd3f2414423efb5ebc7231107cfc2_l3.png)  
Where w is a vector called **Weights** and b is a scalar called **Bias**.
The Weights and Bias are called the **parameters** of the model.

All we need to do is estimate the value of w and b from the given set of data
such that the resultant hypothesis produces the least cost J which is
defined by the following **cost function**  
![ J\(w, b\) = \\frac{1}{2m} \\sum_{i=1}^{m} \(y_i - h\(x_i\)\) ^ 2
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-840580afb321e4b7770dff872f9b7272_l3.png)  
where m is the number of data points in the given dataset. This cost
function is also called **Mean Squared Error**.

For finding the optimized value of the parameters for which J is minimum, we
will be using a commonly used optimizer algorithm called **Gradient Descent**.
Following is the pseudo-code for Gradient Descent:  


  

  

    
    
    Repeat untill Convergence {
        w = w - α * δJ/δw
        b = b - α * δJ/δb
    }
    

