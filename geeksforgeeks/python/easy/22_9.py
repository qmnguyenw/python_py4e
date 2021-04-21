Identifying handwritten digits using Logistic Regression in PyTorch



  
Logistic Regression is a very commonly used statistical method that allows us
to predict a binary output from a set of independent variables. The various
properties of logistic regression and its Python implementation has been
covered in this article previously. Now, we shall find out how to implement
this in PyTorch, a very popular deep learning library that is being developed
by Facebook.

Now, we shall see how to classify handwritten digits from the MNIST dataset
using Logistic Regression in PyTorch. Firstly, you will need to install
PyTorch into your Python environment. The easiest way to do this is to use the
pip or conda tool. Visit pytorch.org and install the version of your
Python interpreter and the package manager that you would like to use.

With PyTorch installed, let us now have a look at the code. Write the three
lines given below to import the reqiored library functions and objects.

 __

 __  
 __

 __

 __  
 __  
 __

import torch

import torch.nn as nn

import torchvision.datasets as dsets

import torchvision.transforms as transforms

from torch.autograd import Variable  
  
---  
  
 __

 __

Here, the _torch.nn_ module contains the code required for the model,
_torchvision.datasets_ contains the MNIST dataset. It contains the dataset of
handwritten digits that we shall be using here. The _torchvision.transforms_
module contains various methods to transform objects into others. Here, we
shall be using it to transform from images to PyTorch tensors. Also, the
_torch.autograd_ module contains the Variable class amongst others, which will
be used by us while defining our tensors.

Next, we shall download and load the dataset to memory.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# MNIST Dataset (Images and Labels)

train_dataset = dsets.MNIST(root ='./data', 

 train = True, 

 transform = transforms.ToTensor(),

 download = True)

 

test_dataset = dsets.MNIST(root ='./data', 

 train = False, 

 transform = transforms.ToTensor())

 

# Dataset Loader (Input Pipline)

train_loader = torch.utils.data.DataLoader(dataset = train_dataset, 

 batch_size = batch_size, 

 shuffle = True)

 

test_loader = torch.utils.data.DataLoader(dataset = test_dataset, 

 batch_size = batch_size, 

 shuffle = False)  
  
---  
  
 __

 __

Now, we shall define our hyper parameters.

 __

 __  
 __

 __

 __  
 __  
 __

# Hyper Parameters

input_size = 784

num_classes = 10

num_epochs = 5

batch_size = 100

learning_rate = 0.001  
  
---  
  
 __

 __

In our dataset, the image size is 28*28. Thus, our input size is 784. Also, 10
digits are present in this and hence, we can have 10 different outputs. Thus,
we set num_classes as 10. Also, we shall train for five times on the entire
dataset. Finally, we will train in small batches of 100 images each so as to
prevent the crashing of the program due to memory overflow.

After this, we shall be defining our model as below. Here, we shall initialise
our model as a subclass of _torch.nn.Module_ and then define the forward pass.
In the code that we are writing, the softmax is internally calculated during
each forward pass and hence we do not need to specify it inside the forward()
function.

 __

 __  
 __

 __

 __  
 __  
 __

class LogisticRegression(nn.Module):

 def __init__(self, input_size, num_classes):

 super(LogisticRegression, self).__init__()

 self.linear = nn.Linear(input_size, num_classes)

 

 def forward(self, x):

 out = self.linear(x)

 return out  
  
---  
  
 __

 __

Having defined our class, now we instantiate an object for the same.

 __

 __  
 __

 __

 __  
 __  
 __

model= LogisticRegression(input_size, num_classes)  
  
---  
  
 __

 __

Next, we set our loss function and the optimiser. Here, we shall be using the
cross entropy loss and for the optimiser, we shall be using the stochastic
gradient descent algorithm with a learning rate of 0.001 as defined in the
hyper parameter above.

 __

 __  
 __

 __

 __  
 __  
 __

criterion= nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)  
  
---  
  
 __

 __

Now, we shall start the training. Here, we shall be performing the following
tasks:

  1. Reset all gradients to 0.
  2. Make a forward pass.
  3. Calculate the loss.
  4. Perform backpropagation.
  5. Update all weights.

 __

 __  
 __

 __

 __  
 __  
 __

# Training the Model

for epoch in range(num_epochs):

 for i, (images, labels) in enumerate(train_loader):

 images = Variable(images.view(-1, 28 * 28))

 labels = Variable(labels)

 

 # Forward + Backward + Optimize

 optimizer.zero_grad()

 outputs = model(images)

 loss = criterion(outputs, labels)

 loss.backward()

 optimizer.step()

 

 if (i + 1) % 100 == 0:

 print('Epoch: [% d/% d], Step: [% d/% d], Loss: %.4f'

 % (epoch + 1, num_epochs, i + 1,

 len(train_dataset) // batch_size, loss.data[0]))  
  
---  
  
 __

 __

Finally, we shall be testing out model by using the following code.

 __

 __  
 __

 __

 __  
 __  
 __

# Test the Model

correct = 0

total = 0

for images, labels in test_loader:

 images = Variable(images.view(-1, 28 * 28))

 outputs = model(images)

 _, predicted = torch.max(outputs.data, 1)

 total += labels.size(0)

 correct += (predicted == labels).sum()

 

print('Accuracy of the model on the 10000 test images: % d %%' % (

 100 * correct / total))  
  
---  
  
 __

 __

Assuming that you performed all steps correctly, you will get an accuracy of
82%, which is far off from today’s state of the art model, which uses a
special type of neural network architecture. For your reference, you can find
the entire code for this article below:

 __

 __  
 __

 __

 __  
 __  
 __

import torch

import torch.nn as nn

import torchvision.datasets as dsets

import torchvision.transforms as transforms

from torch.autograd import Variable

 

 

# MNIST Dataset (Images and Labels)

train_dataset = dsets.MNIST(root ='./data',

 train = True,

 transform = transforms.ToTensor(),

 download = True)

 

test_dataset = dsets.MNIST(root ='./data',

 train = False,

 transform = transforms.ToTensor())

 

# Dataset Loader (Input Pipline)

train_loader = torch.utils.data.DataLoader(dataset = train_dataset,

 batch_size = batch_size,

 shuffle = True)

 

test_loader = torch.utils.data.DataLoader(dataset = test_dataset,

 batch_size = batch_size,

 shuffle = False)

 

# Hyper Parameters

input_size = 784

num_classes = 10

num_epochs = 5

batch_size = 100

learning_rate = 0.001

 

# Model

class LogisticRegression(nn.Module):

 def __init__(self, input_size, num_classes):

 super(LogisticRegression, self).__init__()

 self.linear = nn.Linear(input_size, num_classes)

 

 def forward(self, x):

 out = self.linear(x)

 return out

 

 

model = LogisticRegression(input_size, num_classes)

 

# Loss and Optimizer

# Softmax is internally computed.

# Set parameters to be updated.

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

 

# Training the Model

for epoch in range(num_epochs):

 for i, (images, labels) in enumerate(train_loader):

 images = Variable(images.view(-1, 28 * 28))

 labels = Variable(labels)

 

 # Forward + Backward + Optimize

 optimizer.zero_grad()

 outputs = model(images)

 loss = criterion(outputs, labels)

 loss.backward()

 optimizer.step()

 

 if (i + 1) % 100 == 0:

 print('Epoch: [% d/% d], Step: [% d/% d], Loss: %.4f'

 % (epoch + 1, num_epochs, i + 1,

 len(train_dataset) // batch_size, loss.data[0]))

 

# Test the Model

correct = 0

total = 0

for images, labels in test_loader:

 images = Variable(images.view(-1, 28 * 28))

 outputs = model(images)

 _, predicted = torch.max(outputs.data, 1)

 total += labels.size(0)

 correct += (predicted == labels).sum()

 

print('Accuracy of the model on the 10000 test images: % d %%' % (

 100 * correct / total))  
  
---  
  
 __

 __

 **References** :

  * PyTorchZeroToAll
  * yunjey on Github

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

