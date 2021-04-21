Tensorflow | tf.data.Dataset.from_tensor_slices()



With the help of **tf.data.Dataset.from_tensor_slices()** method, we can get
the slices of an array in the form of objects by using
tf.data.Dataset.from_tensor_slices() method.

>  **Syntax :** tf.data.Dataset.from_tensor_slices(list)  
>  **Return :** Return the objects of sliced elements.

 **Example #1 :**  
In this example we can see that by using
tf.data.Dataset.from_tensor_slices() method, we are able to get the slices
of list or array.

 __

 __  
 __

 __

 __  
 __  
 __

# import tensorflow

import tensorflow as tf

 

# using tf.data.Dataset.from_tensor_slices() method

gfg = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4,
5])

 

for ele in gfg:

 print(ele.numpy())  
  
---  
  
 __

 __

 **Output :**

> 1  
> 2  
> 3  
> 4  
> 5
>
>  
>
>
>  
>

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import tensorflow

import tensorflow as tf

 

# using tf.data.Dataset.from_tensor_slices() method

gfg = tf.data.Dataset.from_tensor_slices([[5, 10], [3,
6]])

 

for ele in gfg:

 print(ele.numpy())  
  
---  
  
 __

 __

 **Output :**

> [5, 10]  
> [3, 6]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

