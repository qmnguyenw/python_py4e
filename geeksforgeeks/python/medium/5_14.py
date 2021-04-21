Pytorch Functions – tesnor(), fill_diagnol(), append(), index_copy()



This article aims to share some PyTorch functions that will help you a lot in
your deep learning and data science journey. Each function will be explained
using two write examples and one example where you can’t use those functions.
So let’s get started.

PyTorch is an open-source machine learning library, it contains a tensor
library that enables to create a scalar, a vector, a matrix or in short we can
create an n-dimensional matrix. It is used in computer vision and natural
language processing, primarily developed by Facebook’s Research Lab. It is
open-source software and released under the modified BSD (Barkley Software
Distribution) license.

 **Our Four functions:**

  * torch.tensor()
  * fill_diagonal_()
  * append(*size)
  * index_copy()

## Function 1 – torch.tensor()

This function enables us to create PyTorch tensors. Tensor could be anything
i.e. it could be a scalar, it could be a 1-dimensional matrix, it could be an
n-dimensional matrix.

 **Why we need tensors?**

  

  

Whenever we want to compute any matrix computations in our deep learning model
the first and most important task is converting our data frames into numpy
array and then to tensors or if we are working on some image classification
problem we have to convert those images into PyTorch tensors.

 **Syntax and parameters:**

    
    
    torch.tensor(data, dtype=None, device=None, requires_grad=False, pin_memory=False)
    data:          data that we want to convert into tensor.
    dtype:         data type of that data whether it is torch32, torch64 etc.
    device:        type of your device whether it is cpu or gpu(cuda).
    requires_grad: if it is True, then gradients of that tensor will be saved in
                   torch.grad property.

 **Code: To create vectors using this function.**

 __

 __  
 __

 __

 __  
 __  
 __

# vector of int datatype

t1 = torch.tensor([1, 2, 3, 7, 1]) 

 

# if one float can convert the whole tensor into flaat

t2 = torch.tensor([4, 2, 5, .9]) 

 

# we can convert the tensor data type

t3 = torch.tensor([2, 6, 1, 6, 8.], dtype =
torch.int32  
  
---  
  
 __

 __

In the above example, _t1_ is the tensor that contains a simple 1-dimensional
array. In, _t2_ we inside the torch. Tensor we have used a single float
element but due to that single, our whole _t2_ tensor has converted into float
type. In, _t3_ we have forcefully set dtype = torch.int32 to change the data
types of a tensor .

 **Code: To create a tensor using a matrix.**

 __

 __  
 __

 __

 __  
 __  
 __

t4= torch.tensor([[3, 6, 8], [2, 6, 8], [0,
7, 4]])  
  
---  
  
 __

 __

In the above example, we have created a t4 tensor that is _3*3_ tensor.
Similarly, if we want to create an n-dimensional tensor we can create that,
like tensor having 4 dimensions or many more.

 **Example 3 ( the most common mistake):**

In this example, we will talk the commonly attempted mistake during creation
of a tensor. In example 2, we have learned that we can create n-dimensional
array.

  

  

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

t4= torch.tensor([[3, 6, 8], [2, 6, 8], [0,
7, 4]])  
  
---  
  
 __

 __

Here we have created a tensor of having two dimensions but each dimension is
not containing equal no. of elements i.e. each dimension is not having the
same length. Because of this. The compiler will throw an error, saying…

> ValueError Traceback (most recent call last) <ipython-input-21–28787d136593>
> in <module> 1
>
> # Example 3?-?breaking (to illustrate when it breaks)?-?? 2
> torch.tensor([[1, 2], [3, 4, 5]])
>
> ValueError: expected sequence of length 2 at dim 1 (got 3)

So what we learned is, we can create a n-dimensional array but all the
dimensions should having same length otherwise we will get an error.

## Function 2 – fill_diagonal_()

Fill_diagonal() fill the main diagonal with fill_value but that matrix
should be a 2D matrix , for a ndim > 2 matrix number of rows should be equal
to number of columns and if it is not then we have to set wrap = True so
that diagonal value can repeat itself.

 **Syntax and parameters:**

fill_diagonal_(fill_value, wrap=False) -> tensor

    
    
    fill_value: tensor matrix whose diagonals we want to fill.
    wrap:       it takes boolean, it enables us to work with a non-square matrix.
    

**Example 1**

In this example, firstly we will create a tensor of size(3, 3) using
torch.zeros(3, 3).

 __

 __  
 __

 __

 __  
 __  
 __

a= torch.zeros(3, 3)  
  
---  
  
 __

 __

a is a tensor ofsize(3, 3) which have all of it’s element zero i.e. a is a
zero matrix

now what we want is to replace all of it’s diagonal values with .4 , so this
we can do with the help of fill_diagonal_().

 __

 __  
 __

 __

 __  
 __  
 __

a.fill_diagonal_(fill_value= 4, wrap = False)

 

print(a)  
  
---  
  
 __

 __

If, we look at tensor a it will look like

> tensor([[4., 0., 0.], [0., 4., 0.], [0., 0., 4.]])

 **Example 2 :**

As we learned form example 1, that we can replace diagonal elements using this
function but what if we have a tensor in which no. of rows is not equal to no.
of columns, then in this scenario we have to set the “wrap” parameter of
fill_diagonal_().

You can look at this code,

 __

 __  
 __

 __

 __  
 __  
 __

b= torch.zeros([9, 4])

 

# without putting wrap = True

 

A = b.fill_diagonal_(5, wrap = False)  
  
---  
  
 __

 __

In the above code, firstly we created a zero tensor of size(9, 4), then we
filled it’s diagonal with 5 but we didn’t set wrap = True. Now let’s look at
tensor A,

> tensor([[5., 0., 0., 0.], [0., 5., 0., 0.], [0., 0., 5., 0.], [0., 0., 0.,
> 5.], [0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.],
> [0., 0., 0., 0.]])

Here you can see that once diagonal reaches to the end of the length of a
particular dimension then rest of the diagonal was not changed

So to solve this problem we have to set wrap as True. Look at this code,

 __

 __  
 __

 __

 __  
 __  
 __

B= b.fill_diagonal_(6, True)

 

print(B)  
  
---  
  
 __

 __

Now take a look at tensor B

> tensor([[6., 0., 0., 0.], [0., 6., 0., 0.], [0., 0., 6., 0.], [0., 0., 0.,
> 6.], [0., 0., 0., 0.], [6., 0., 0., 0.], [0., 6., 0., 0.], [0., 0., 6., 0.],
> [0., 0., 0., 6.]])

You will observe that even diagonal reached to the end of a particular
dimension, it again starts changing the diagonals form next dimension.

 **Example 3(common mistake):**

let’s assume that you have a zero tensor of size(4, 5) and you want to change
it’s diagonal with .3 but if you want to change the data type of that tensor
to int32, then probably you will think to set a dype = torch.int32 in
fill_diagonal_() as,

B = b.fill_diagonal_(6, True)

print(B)

 __

 __  
 __

 __

 __  
 __  
 __

B= b.fill_diagonal_(6, True)

 

print(B)  
  
---  
  
 __

 __

But, here you have to remember a little thing that fill_diagonal_() only takes
two arguments as parameter, one is data that you want to put in diagonal and
another one is wrap for working with non-square tensor ,

So, the above code will throw an error as ,

> TypeError
>
> Traceback (most recent call last) <ipython-input-26–133c4c6a6759> in
> <module>
>
> 1 # Example 3?-?breaking (but if try to set it’s data type it throws an
> error)
>
> 2 a = torch.zeros(4, 5)
>
> – ? 3 a.fill_diagonal_(.3, dtype = torch.float32) TypeError:
> fill_diagonal_() got an unexpected keyword argument ‘dtype’

## Function 3 – expand(*size)

  * Returns a new view of the self tensor with singleton dimensions expanded to a larger size.
  * Passing -1 as the size for a dimension means not changing the size of that dimension.
  * Tensor can be also expanded to a larger number of dimensions, and the new ones will be appended at the front. For the new dimensions, the size cannot be set to -1.
  * Expanding a tensor does not allocate new memory, but only creates a new view on the existing tensor where a dimension of size one is expanded to a larger size by setting the stride to 0. Any dimension of size 1 can be expanded to an arbitrary value without allocating new memory.

 **Syntax and parameter:**

    
    
    expand(*size)

 **Example 1 :**

if we have a singleton-dimension matrix then we can expand it’s singleton-
dimension, using expand()

 __

 __  
 __

 __

 __  
 __  
 __

a= torch.tensor([[5], [3], [8], [4]])

 

a.size()

 

a.expand(4, 8)  
  
---  
  
 __

 __

lool at tensor a,

> tensor([[5, 5, 5, 5, 5, 5, 5, 5],
>
> [3, 3, 3, 3, 3, 3, 3, 3],
>
> [8, 8, 8, 8, 8, 8, 8, 8],
>
> [4, 4, 4, 4, 4, 4, 4, 4]])

Initially, a was a matrix that contain a singleton dimension , now using
expand() we expanded it’s singleton dimension into 8

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

b= torch.tensor([[7], [3], [4]])

 

b.size()

 

b.expand(3, -1)  
  
---  
  
 __

 __

In the above example , we put the second size as -1 that means we don’t want
to expand it’s dimension.

 **Example 3(common mistake) :**

 __

 __  
 __

 __

 __  
 __  
 __

c= torch.tensor([[4, 6], [9, 6]])

 

c.size() # this matrix didn't any singleton dimemsion

 

c.expand(2, 6)  
  
---  
  
 __

 __

This throws an error because according to the definition of expand() we have
to match one size to the non-singleton dimension but as we have two singleton
dimensions so we can’t fulfill the condition. Error….

> RuntimeError: The expanded size of the tensor (6) must match the existing
> size (2) at non-singleton dimension 1. Target sizes: [2, 6]. Tensor sizes:
> [2, 2]

## Function 4 – index_copy_(dim, index, tensor) ? Tensor

It enable us to copy a tensor into a self tensor in a given indices that is
defined in index tensor it contains three arguments

  * dim
  * index tensor to hold indices order
  * tensor that we want to copy in our self tensor

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

self_tensor= torch.zeros(6, 3)

 

a

 

t = torch.tensor([[7, 6, 9], [3, 9, 1], [0,
1, 9]], dtype = torch.float)

 

i = torch.tensor([3, 1, 0])

 

self_tensor.index_copy_(0, i, t)  
  
---  
  
 __

 __

Now, if you look at the output tensor…

> tensor([[0., 1., 9.],
>
> [3., 9., 1.],
>
> [0., 0., 0.],
>
> [7., 6., 9.],
>
> [0., 0., 0.],
>
> [0., 0., 0.]])

In the above example

we copied t tensor into self_tensor with a order that is defined in i tensor

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

a= torch.tensor([[1, 8], [9, 5], [1, 5]])

 

b = torch.tensor([[3, 5], [9, 0], [2, 2]])

 

i = torch.tensor([2, 1, 0])

 

a.index_copy_(0, i, b)  
  
---  
  
 __

 __

Output tensor:

> tensor([[2, 2],
>
> [9, 0],
>
> [3, 5]])

we can perform the same thing of example 1 with two non-zero tensors

 **Example 3(common mistake )**

 __

 __  
 __

 __

 __  
 __  
 __

a= torch.tensor([[8, 3], [1, 0]])

 

b = torch.tensor([[3, 9]])

 

i = torch.tensor([1])

 

a.index_copy(1, i, b)  
  
---  
  
 __

 __

> ————————————————————————— RuntimeError  
>  Traceback (most recent call last) <ipython-input-6-fb983dc7560f> in
> <module>  
> 3 b = torch.tensor([[3, 9]]) 4 i = torch.tensor([1]) —-> 5 a.index_copy(1,
> i, b) RuntimeError: index_copy_(): Source/destination tensor must have same
> slice shapes. Destination slice shape: 2 at dimension 1 and source slice
> shape: 1 at dimension 0.

The above example throws an error because we have tried to give dim = 1

but, dimth element of index should contain same no of element as much
element our b tensor have .

 **Conclusion:** so whenever we need to copy a tensor into a self tensor with
a specified order we can use this function

 **

Reference Links –

**

  * PyTorch official docs link
  * notebook for entire code

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

