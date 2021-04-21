ML | Linear Regression



 **Linear Regression** is a machine learning algorithm based on **supervised
learning**. It performs a **regression task**. Regression models a target
prediction value based on independent variables. It is mostly used for finding
out the relationship between variables and forecasting. Different regression
models differ based on – the kind of relationship between dependent and
independent variables, they are considering and the number of independent
variables being used.  
![](https://media.geeksforgeeks.org/wp-content/uploads/linear-regression-
plot.jpg)

Linear regression performs the task to predict a dependent variable value (y)
based on a given independent variable (x). So, this regression technique finds
out a linear relationship between x (input) and y(output). Hence, the name is
Linear Regression.  
In the figure above, X (input) is the work experience and Y (output) is the
salary of a person. The regression line is the best fit line for our model.

 **Hypothesis function for Linear Regression :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/linear-regression-
hypothesis.jpg)

While training the model we are given :  
 **x:** input training data (univariate – one input variable(parameter))  
 **y:** labels to data (supervised learning)

When training the model – it fits the best line to predict the value of y for
a given value of x. The model gets the best regression fit line by finding the
best θ1 and θ2 values.  
 **θ 1:** intercept  
 **θ 2:** coefficient of x

  

  

Once we find the best θ1 and θ2 values, we get the best fit line. So when we
are finally using our model for prediction, it will predict the value of y for
the input value of x.

 **How to update θ 1 and θ2 values to get the best fit line ?**

 **Cost Function (J):**  
By achieving the best-fit regression line, the model aims to predict y value
such that the error difference between predicted value and true value is
minimum. So, it is very important to update the θ1 and θ2 values, to reach the
best value that minimize the error between predicted y value (pred) and true y
value (y).

![](https://media.geeksforgeeks.org/wp-content/uploads/LR-cost-function-1.jpg)

![](https://media.geeksforgeeks.org/wp-content/uploads/LR-cost-function-2.jpg)

Cost function(J) of Linear Regression is the **Root Mean Squared Error
(RMSE)** between predicted y value (pred) and true y value (y).

 **Gradient Descent:**  
To update θ1 and θ2 values in order to reduce Cost function (minimizing RMSE
value) and achieving the best fit line the model uses Gradient Descent. The
idea is to start with random θ1 and θ2 values and then iteratively updating
the values, reaching minimum cost.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

