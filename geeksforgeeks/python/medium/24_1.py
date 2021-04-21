Linear Regression using PyTorch



Linear Regression is a very commonly used statistical method that allows us to
determine and study the relationship between two continuous variables. The
various properties of linear regression and its Python implementation has been
covered in this article previously. Now, we shall find out how to implement
this in PyTorch, a very popular deep learning library that is being developed
by Facebook.

Firstly, you will need to install PyTorch into your Python environment. The
easiest way to do this is to use the pip or conda tool. Visit pytorch.org
and install the version of your Python interpreter and the package manager
that you would like to use.

 __

 __  
 __

 __

 __  
 __  
 __

# We can run this Python code on a Jupyter notebook

# to automatically install the correct version of 

# PyTorch.

 

# http://pytorch.org / from os import path

from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag

platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(),
get_abi_tag())

 

accelerator = 'cu80' if path.exists('/opt / bin / nvidia-smi')
else 'cpu'

 

! pip install -q http://download.pytorch.org /
whl/{accelerator}/torch-1.3.1.post4-{platform}-linux_x86_64.whl
torchvision  
  
---  
  
 __

 __

With PyTorch installed, let us now have a look at the code.  
Write the two lines given below to import the necessary library functions and
objects.

 __

 __  
 __

 __

 __  
 __  
 __

import torch

from torch.autograd import Variable  
  
---  
  
 __

 __

We also define some data and assign them to variables _x_data_ and _y_data_ as
given below:

 __

 __  
 __

 __

 __  
 __  
 __

x_data= Variable(torch.Tensor([[1.0], [2.0], [3.0]]))

y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))  
  
---  
  
 __

 __

Here, _x_data_ is our independent variable and _y_data_ is our dependent
variable. This will be our dataset for now. Next, we need to define our model.
There are two main steps associated with defining our model. They are:

  

  

  1. Initialising our model.
  2. Declaring the forward pass.

We use the class given below:

 __

 __  
 __

 __

 __  
 __  
 __

class LinearRegressionModel(torch.nn.Module):

 

 def __init__(self):

 super(LinearRegressionModel, self).__init__()

 self.linear = torch.nn.Linear(1, 1) # One in and one out

 

 def forward(self, x):

 y_pred = self.linear(x)

 return y_pred  
  
---  
  
 __

 __

As you can see, our _Model_ class is a subclass of _torch.nn.module_. Also,
since here we have only one input and one output, we use a Linear model with
both the input and output dimension as 1.

Next, we create an object of this model.

 __

 __  
 __

 __

 __  
 __  
 __

# our model

our_model = LinearRegressionModel()  
  
---  
  
 __

 __

After this, we select the optimiser and the loss criteria. Here, we will use
the mean squared error (MSE) as our loss function and stochastic gradient
descent (SGD) as our optimiser. Also, we arbitrarily fix a learning rate of
0.01.

 __

 __  
 __

 __

 __  
 __  
 __

criterion= torch.nn.MSELoss(size_average = False)

optimizer = torch.optim.SGD(our_model.parameters(), lr = 0.01)  
  
---  
  
 __

 __

We now arrive at our training step. We perform the following tasks for 500
times during training:

  1. Perform a forward pass by passing our data and finding out the predicted value of y.
  2. Compute the loss using MSE.
  3. Reset all the gradients to 0, peform a backpropagation and then, update the weights.

 __

 __  
 __

 __

 __  
 __  
 __

for epoch in range(500):

 

 # Forward pass: Compute predicted y by passing 

 # x to the model

 pred_y = our_model(x_data)

 

 # Compute and print loss

 loss = criterion(pred_y, y_data)

 

 # Zero gradients, perform a backward pass, 

 # and update the weights.

 optimizer.zero_grad()

 loss.backward()

 optimizer.step()

 print('epoch {}, loss {}'.format(epoch, loss.item()))  
  
---  
  
 __

 __

Once the training is completed, we test if we are getting correct results
using the model that we defined. So, we test it for an unknown value of
_x_data_ , in this case, 4.0.

 __

 __  
 __

 __

 __  
 __  
 __

new_var= Variable(torch.Tensor([[4.0]]))

pred_y = our_model(new_var)

print("predict (after training)", 4, our_model(new_var).item())  
  
---  
  
 __

 __

If you performed all steps correctly, you will see that for the input 4.0, you
are getting a value that is very close to 8.0 as below. So, our model
inherently learns the relationship between the input data and the output data
without being programmed explicitly.

predict (after training) 4 7.966438293457031

For your reference, you can find the entire code of this article given below:

 __

 __  
 __

 __

 __  
 __  
 __

import torch

from torch.autograd import Variable

 

x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))

y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

 

 

class LinearRegressionModel(torch.nn.Module):

 

 def __init__(self):

 super(LinearRegressionModel, self).__init__()

 self.linear = torch.nn.Linear(1, 1) # One in and one out

 

 def forward(self, x):

 y_pred = self.linear(x)

 return y_pred

 

# our model

our_model = LinearRegressionModel()

 

criterion = torch.nn.MSELoss(size_average = False)

optimizer = torch.optim.SGD(our_model.parameters(), lr = 0.01)

 

for epoch in range(500):

 

 # Forward pass: Compute predicted y by passing 

 # x to the model

 pred_y = our_model(x_data)

 

 # Compute and print loss

 loss = criterion(pred_y, y_data)

 

 # Zero gradients, perform a backward pass, 

 # and update the weights.

 optimizer.zero_grad()

 loss.backward()

 optimizer.step()

 print('epoch {}, loss {}'.format(epoch, loss.item()))

 

new_var = Variable(torch.Tensor([[4.0]]))

pred_y = our_model(new_var)

print("predict (after training)", 4, our_model(new_var).item())  
  
---  
  
 __

 __

## References

  * PyTorchZeroToAll
  * Penn State STAT 501

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

