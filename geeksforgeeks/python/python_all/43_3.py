Python – Get Matrix Mean



Given a Matrix, Find its mean.

>  **Input** : test_list = [[5, 6, 7], [7, 5, 6]]  
>  **Output** : 6.0  
>  **Explanation** : 36 / 6 = 6.0
>
>  **Input** : test_list = [[5, 6, 7, 4, 8]]  
>  **Output** : 6.0  
>  **Explanation** : 30 / 5 = 6.0

 **Method #1 : Using list comprehension + sum() + len() + zip()**

The combination of above functions can be used to solve this problem. In this,
we perform the mean calculation using sum() and len(), zip() along with *
operator does task of extracting each element of rows of matrix.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Mean

# Using list comprehension + sum() + len() + zip()

 

# initializing lists

test_list = [[5, 6, 3], [8, 3, 1], [9,
10, 4], [8, 4, 2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# zip() to get all elements 

# sum() / len() gives mean

# extracts column mean

res = [sum(idx) / len(idx) for idx in
zip(*test_list)]

 

# extracts all elements mean

res = sum(res) / len(res)

 

# printing result 

print("Matrix Mean : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
    Matrix Mean : 5.25
    

**Method #2 : Using mean() + zip() + list comprehension**

This is another method in which this task can be performed. In this, we
extract mean using inbuilt method of mean() .

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Mean

# Using mean() + zip() + list comprehension

from statistics import mean

 

# initializing lists

test_list = [[5, 6, 3], [8, 3, 1], [9,
10, 4], [8, 4, 2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# zip() to get all elements 

# mean() gives mean

# extracts column mean

res = [mean(idx) for idx in zip(*test_list)]

 

# extracts all elements mean

res = mean(res)

 

# printing result 

print("Matrix Mean : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
    Matrix Mean : 5.25
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

