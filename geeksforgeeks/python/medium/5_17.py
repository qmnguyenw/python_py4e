One Hot Encoding using Tensorflow



In this post, we will be seeing how to initialize a vector in TensorFlow with
all zeros or ones. The function you will be calling is tf.ones(). To
initialize with zeros you could use tf.zeros() instead. These functions take
in a shape and return an array full of zeros and ones accordingly.

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as tf

 

ones_matrix = tf.ones([2, 3])

sess = tf.Session()

ones = sess.run(ones_matrix)

sess.close()

 

print(ones)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1. 1. 1.]  [1. 1. 1.]]

 **Using One Hot Encoding:**  
Many times in deep learning and general vector computations you will have a y
vector with numbers ranging from 0 to C-1 and you want to do the following
conversion. If C is for example 5, then you might have the following y vector
which you will need to convert as follows:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200716042622/vector.png)

One Hot Encoding Example

This can be done as follows:

  

  

 **Parameters passed to the function:**

>  **indices:** A Tensor of indices.  
>  **depth:** A scalar defining the depth of the one hot dimension.  
>  **on_value:** A scalar defining the value to fill in output when indices[j]
> = i. (default :

