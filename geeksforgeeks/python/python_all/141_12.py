Univariate Linear Regression in Python



Univariate data is the type of data in which the result depends only on one
variable. For instance, dataset of points on a line can be considered as a
univariate data where abscissa can be considered as input feature and ordinate
can be considered as output/result.  
  
 **For example:**  
For line **Y = 2X + 3** ;  
Input feature will be X and Y will be the result.X| Y| 1| 5| 2| 7| 3| 9| 4|
11| 5| 13  
---|---  
  
 **Concept:**  
For univariate linear regression, there is only one input feature vector. The
line of regression will be in the form of:

>  **Y = b0 + b1 * X**  
>  Where,  
> b0 and b1 are the coefficients of regression.

Hence, it is being tried to predict regression coefficients b0 and b1 by
training a model.

 **Utility functions**

  

  

  1.  **Predict**

 __

 __  
 __

 __

 __  
 __  
 __

def predict(x, b0, b1):

 """Predicts the value of prediction based on 

 current value of regression coefficients when input is x"""

 # Y = b0 + b1 * X

 return b0 + b1 * x  
  
---  
  
 __

 __

  2.  **Cost function :**  
Cost function computes the error percentage with the current value of
regression coefficients. It quantitatively defines how far the model is wrt
actual regression coefficients which has lowest rate of error.

 __

 __  
 __

 __

 __  
 __  
 __

def cost(x, y, b0, b1):

 # y is a list of expected value

 errors = []

 for x, y in zip(x, y):

 prediction = predict(x, b0, b1)

 expected = y

 difference = prediction-expected

 errors.append(difference)

 # Now, we have errors for all the observations,

 

 # for some input, the value of error might be positive 

 # and for some input might be negative, 

 # and if we directly add them up, 

 # the values might cancel out leading to wrong output."

 

 # Hence, we use concept of mean squared error.

 # in mse, we return mean of square of all the errors.

 mse = sum([e * e for e in errors])/len(errors)

 return mse  
  
---  
  
 __

 __

  3.  **Cost Derivative**  
After each iteration, the cost is upgraded in proportion to the error. The
nature of error is very data sensitive. By data sensitive i mean the error
value changes very fast, because we had square in error function. Hence, to
make it more tolerant to high values of errors, we derivate the error
function.  
The mathematics is as follows:

![ \\begin{document} \\begin{align*} cost\(x, y\)  &= \\frac{1}{m} \\left\(
\\sum_{i=1}^{n}\\, \(prediction\(x_i\)-y_i\)^2 \\right\) \\\\ &= \\frac{1}{m}
\\left\( \\sum_{i=1}^{n}\\, \(b0+b1*x_i-y_i\)^2 \\right\) \\end{align}
\\vspace{15} \\begin{align*} cost\\_derivative\(x, y\)  &=
\\frac{\\partial}{\\partial b}\\left\( \\frac{1}{m} \\left\(
\\sum_{i=1}^{n}\\, \(b0+b1*x_i-y_i\)^2 \\right\) \\right\) \\\\ &=
\\frac{1}{m} \\left\( \\sum_{i=1}^{n}\\, \\left\(\\frac{\\partial}{\\partial
b}\(b0+b1*x_i-y_i\)^2\\right\)  \\right\)  \\hspace{4ex} ....using DUIS \\\\
&= \\frac{1}{m} \\left\( \\sum_{i=1}^{n}\\, \\left\(2*\(b0+b1*x_i-y_i\)*x_i^b
\\right\) \\right\) \\\\ &=  \\frac{1}{m} \\left\( \\sum_{i=1}^{n}\\,
\\left\(2*\(prediction\(x_i\)-y_i\)*x_i^b \\right\) \\right\) \\\\
\\end{align} Where, \\newline m = len\(x\) - is the number of rows in the
dataset. \\newline $x_i^b$ - is x who's coefficient is b. \\newline y =
b_0+b_1 x_1 \\newline $In this, b_1$ is coefficient of $x_1$ but coefficient
of $b_0$ is 1 \\\[     x_i^b =     \\begin{cases}        1 & i=0 \\\\
x_i & otherwise    \\end{cases} \\\] For this, we append an extra row
consisting of 1's for $b_0$. \\newline Or, add a switch case to the
$cost\\_derivative$ function. \\newline In our case, we will proceed with
switch case. \\newline \\end{document} ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c52bb85e3ec566e9cb1df09f6f5c5457_l3.png)

**Code:**

 __

 __  
 __

 __

 __  
 __  
 __

def cost_derivative(x, y, b0, b1, i):

 return sum([

 2*(predict(xi, b0, b1)-yi)*1

 if i == 0

 else 2*(predict(xi, b0, b1)-yi)*xi

 for xi, yi in zip(x, y)

 ])/len(x)  
  
---  
  
 __

 __

  4.  **Update Coefficients :**  
At each iteration (epoch), the values of the regression coefficient are
updated by a specific value wrt to the error from the previous iteration. This
updation is very crucial and is the crux of the machine learning applications
that you write.  
Updating the coefficients with exact an update of a coefficient is done by
penalizing its value with a fraction of error that it’s previous values
caused.  
This fraction is called as learning rate. This defines how fast our model
reaches out to point of convergence(point where error is ideally 0).

![ \\begin{align*} b_i & = b_i - \\alpha * \\left\(
\\frac{\\partial}{\\partial b} cost\(x, y\) \\right\) \\\\ & = b_i - \\alpha *
\\left\( cost\\_derivative\(x, y, i\) \\right\) $$ \\end{align} $$b_i = b_i -
\\alpha * \\left\( \\frac{\\partial}{\\partial b} cost\(x, y\) \\right\) $$
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7b1d1d7b68490508aa64fc3de42ae89e_l3.png)

Python function for the same is as follows:

 __

 __  
 __

 __

 __  
 __  
 __

def update_coeff(x, y, b0, b1, i, alpha):

 bi -= alpha * cost_derivative(x, y, b0, b1, i)

 return bi  
  
---  
  
 __

 __

  5.  **Stop Iterations:**  
This is the function which is used to specify when should the iterations
should stop.  
As per user, the algorithm stop_iteration generally returns true in following
conditions:

    1.  **Max Iteration :** Model is trained for a specified number of iterations.
    2.  **Error value :** Depending upon the value of previous error, the algorithm decides whether to continue or stop.
    3.  **Accuracy :** Depending upon the last accuracy of the model, if it is larger than the mentioned accuracy, the algorithm returns True,
    4.  **Hybrid :** This is more often used. This combines more than one above mentioned conditions along with an exceptional break option. Exceptional break is condition where training continues until when something bad happens. Something bad might include overflow of result, time constraints exceeded, etc.

Having all the utility functions defined, lets see the pseudo code followed by
its implementation:

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

x, y is the given data.

(b0, b1) <-- (0, 0)

i = 0

while True:

 if stop_iteration(i):

 break

 else:

 b0 = update_coeff(x, y, b0, b1, 0, alpha)

 b1 = update_coeff(x, y, b0, b1, 1, alpha)  
  
---  
  
 __

 __

 **Final Oop implementation :**

 __

 __  
 __

 __

 __  
 __  
 __

class LinearRegressor:

 def __init__(self, x, y, alpha = 0.01, b0 = 0, b1 =
0):

 """ 

 x: input feature

 y: result / target

 alpha: learning rate, default is 0.01

 b0, b1: linear regression coefficient.

 """

 self.i = 0

 self.x = x

 self.y = y

 self.alpha = alpha

 self.b0 = b0

 self.b1 = b1

 if len(x) != len(y):

 raise TypeError("x and y should have same number of rows.")

 

 def predict(model, x):

 """Predicts the value of prediction based on 

 current value of regression coefficients when input is x"""

 # Y = b0 + b1 * X

 return model.b0 + model.b1 * x

 

 def cost_derivative(model, i):

 x, y, b0, b1 = model.x, model.y, model.b0, model.b1

 predict = model.predict

 return sum([

 2 * (predict(xi) - yi) * 1

 if i == 0

 else (predict(xi) - yi) * xi

 for xi, yi in zip(x, y)

 ]) / len(x)

 

 def update_coeff(model, i):

 cost_derivative = model.cost_derivative

 if i == 0:

 model.b0 -= model.alpha * cost_derivative(i)

 elif i == 1:

 model.b1 -= model.alpha * cost_derivative(i)

 

 def stop_iteration(model, max_epochs = 1000):

 model.i += 1

 if model.i == max_epochs:

 return True

 else:

 return False

 

 def fit(model):

 update_coeff = model.update_coeff

 model.i = 0

 while True:

 if model.stop_iteration():

 break

 else:

 update_coeff(0)

 update_coeff(1)

 

 

if __name__ == '__main__':

 linearRegressor = LinearRegressor(

 x =[i for i in range(12)],

 y =[2 * i + 3 for i in range(12)],

 alpha = 0.03

 )

 linearRegressor.fit()

 print(linearRegressor.predict(12))

 

 # expects 2 * 12 + 3 = 27  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

