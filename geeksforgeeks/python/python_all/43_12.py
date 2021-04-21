Python – K length decimal Places



Given a Decimal Number, extent its digits to K length.

>  **Input** : num = 76.8, K = 5  
>  **Output** : 76.80000  
>  **Explanation** : Length of decimal places is 5.
>
>  **Input** : num = 76.8, K = 6  
>  **Output** : 76.800000  
>  **Explanation** : Length of decimal places is 6.

 **Method : Using format()**

This is way in which this task can be done. In this, we harness multiple
format compatibilites to perform task of getting appropriate length of decimal
places.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length decimal Places

# Using format()

 

# initializing number 

num = 76.8

 

# printing original number 

print("The original number is : " + str(num))

 

# initializing K 

K = 7

 

# using format to solve this problem

res = "{{:.{}f}}".format(K).format(num)

 

# printing result 

print("The resultant number : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original number is : 76.8
    The resultant number : 76.8000000
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

