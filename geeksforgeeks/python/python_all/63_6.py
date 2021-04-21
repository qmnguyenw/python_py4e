Python – tensorflow.clip_by_global_norm()



<p><a href=”https://www.geeksforgeeks.org/introduction-to-
tensorflow/”>TensorFlow</a> is open-source python library designed by Google
to develop Machine Learning models and deep learning neural networks.

 **clip_by_global_norm()** is used to clip values of multiple tensors by the
ratio of the sum of their norms.

> **Syntax:** tensorflow.clip_by_global_norm( t_list, clip_norm, use_norm,
> name)
>
>  **Parameters:**
>
>   *  **t_list:** It is tuple or list of mixed Tensors, IndexedSlices.
>   *  **clip_norm:** It is 0-D scalar tensor. It defines the clipping ratio
> and must be greater than 0.
>   *  **use_norm(optional):** It is 0-D scalar tensor. It defines the norm to
> be used. If none is passed _global_norm()_ is used to compute the norm.
>   *  **name(optional):** It defines the name for the operation.
>

>
>  **Returns:**
>
>  
>
>
>  
>
>
>   *  **list_clipped:** It is list of clipped tensor of same type as t_list.
>   *  **global_norm:** It is 0-D tensor which represent the global_norm.
>

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the library

import tensorflow as tf

 

# Initializing the input tensor

t_list = [tf.constant([1, 2, 3, 4], dtype =
tf.float64), tf.constant([5, 6, 7, 8], dtype =
tf.float64)]

clip_norm = .8

use_norm = tf.constant(1.0, dtype = tf.float64)

 

# Printing the input tensor

print('t_lis: ', t_list)

print('clip_norm: ', clip_norm)

print('use_norm: ', use_norm)

 

# Calculating tangent

res = tf.clip_by_global_norm(t_list, clip_norm, use_norm)

 

# Printing the result

print('Result: ', res)  
  
---  
  
 __

 __

 **Output:**

    
    
    t_lis:  [<tf.Tensor: shape=(4, ), dtype=float64, numpy=array([1., 2., 3., 4.])>, <tf.Tensor: shape=(4, ), dtype=float64, numpy=array([5., 6., 7., 8.])>]
    clip_norm:  0.8
    use_norm:  tf.Tensor(1.0, shape=(), dtype=float64)
    Result:  ([<tf.Tensor: shape=(4, ), dtype=float64, numpy=array([0.8, 1.6, 2.4, 3.2])>, <tf.Tensor: shape=(4, ), dtype=float64, numpy=array([4., 4.8, 5.6, 6.4])>], <tf.Tensor: shape=(), dtype=float64, numpy=1.0>)
    
    
    
    
    

**Example 2:** In this example none is passed to use_norm so global_norm()
will be used to find the norm.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing the library

import tensorflow as tf

 

# Initializing the input tensor

t_list = [tf.constant([1, 2, 3, 4], dtype =
tf.float64), tf.constant([5, 6, 7, 8], dtype =
tf.float64)]

clip_norm = .8

 

# Printing the input tensor

print('t_lis: ', t_list)

print('clip_norm: ', clip_norm)

 

# Calculating tangent

res = tf.clip_by_global_norm(t_list, clip_norm)

 

# Printing the result

print('Result: ', res)  
  
---  
  
 __

 __

 **Output:**

    
    
    t_lis:  [<tf.Tensor: shape=(4, ), dtype=float64, numpy=array([1., 2., 3., 4.])>, <tf.Tensor: shape=(4, ), dtype=float64, numpy=array([5., 6., 7., 8.])>]
    clip_norm:  0.8
    Result:  ([<tf.Tensor: shape=(4, ), dtype=float64, numpy=array([0.0560112, 0.11202241, 0.16803361, 0.22404481])>, <tf.Tensor: shape=(4, ), dtype=float64, numpy=array([0.28005602, 0.33606722, 0.39207842, 0.44808963])>], <tf.Tensor: shape=(), dtype=float64, numpy=14.2828568570857>)
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

