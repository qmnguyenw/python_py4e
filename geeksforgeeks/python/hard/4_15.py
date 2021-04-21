tf.transpose() function in TensorFlow



tf.transpose() is a function provided in TensorFlow. This function is used
to transpose the input tensor.

>  **Syntax:** tf.transpose(input_tensor, perm, conjugate)
>
>  **Parameters:**  
>  **input_tensor:** as the name suggests it is the tensor which is to be
> transposed.  
>  **Type:** Tensor
>
>  **perm:** This parameters specifies the permutation according to which the
> input_tensor is to be transposed.  
>  **Type:** Vector
>
>  **conjugate:** This parameters is set to **True** if the input_tensor is of
> type complex.  
>  **Type:** Boolean
>
>  
>
>
>  
>

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as geek

 

 

x = geek.constant([[1, 2, 3, 4],

 [5, 6, 7, 8]])

transposed_tensor = geek.transpose(x)  
  
---  
  
 __

 __

 **Output :**

    
    
    array([[1, 5],
           [2, 6],
           [3, 7],
           [4, 8]])
    

**Example 2:** **With using perm parameter:**

When this parameter is passes the tensor is transposed along the given axis.
In simple words it defines the output shape of the transposed tensor.

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as geek

 

 

x = geek.constant([[[ 1, 2, 3],

 [ 4, 5, 6]],

 [[ 7, 8, 9],

 [ 10, 11, 12]],

 [[ 13, 14, 15],

 [ 16, 17, 18]],

 [[ 19, 20, 21],

 [ 22, 23, 24]]])

transposed_tensor = geek.transpose(x, perm = [0, 2, 1])  
  
---  
  
 __

 __

 **Output:**

    
    
    array([[[ 1,  4],
            [ 2,  5],
            [ 3,  6]],
    
           [[ 7, 10],
            [ 8, 11],
            [ 9, 12]],
    
           [[13, 16],
            [14, 17],
            [15, 18]],
    
           [[19, 22],
            [20, 23],
            [21, 24]]])
    shape (4, 3, 2)
    

The shape is (4, 3, 2) because our perm was [0, 2, 1]. The following is the
mapping from perm to input tensor shape.

    
    
    0 => 4
    2 => 3
    1 => 2

 **Example 3:** **Now we will study the conjugate parameter**  
It is set to **True** when we have complex variables in our tensor.

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as geek

 

 

x = geek.constant([[1 + 1j, 2 + 2j, 3 + 3j],

 [4 + 4j, 5 + 5j, 6 + 6j]])

transposed_tensor = geek.transpose(x)  
  
---  
  
 __

 __

 **Output:**

    
    
    array([[1 + 1j, 4 + 4j],
           [2 + 2j, 5 + 5j],
           [3 + 3j, 6 + 6j]])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

