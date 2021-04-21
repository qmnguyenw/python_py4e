Python – Average of digit greater than K



Given elements list, extract elements whose average of digit is greater than
K.

>  **Input** : test_list = [633, 719, 8382, 119, 327], K = 5  
> **Output** : [719, 8382]  
> **Explanation** : (7 + 1 + 9) / 3 = 5.6 and (8 + 3 + 8 + 2) / 4 = 5.2 , both
> of which are greater than 5, hence returned.
>
>  **Input** : test_list = [633, 719, 8382, 96], K = 5  
> **Output** : [719, 8382, 96]  
> **Explanation** : All the elements are displayed in output whose digit
> average is greater than 5.

 **Method #1 : Using list comprehension + sum() + len()**

In this, we compute digits sum using _sum()_ , and then divide the sum by
element length to get average, and add in result if it’s greater than K.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average digit greater than K

# Using sum() + len() + list comprehension

 

# initializing list

test_list = [633, 719, 8382, 119, 327]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# getting average and checking if greater than K

res = [sub for sub in test_list if sum(

 [int(ele) for ele in str(sub)]) / len(str(sub))
>= K]

 

# printing result

print("Filtered List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [633, 719, 8382, 119, 327]
    Filtered List : [719, 8382]
    

**Method #2 : Using sum() + len() + filter() + lambda**

Here, filtering operation is performed using _filter()_ and _lambda_ , rest
all operations are handled as per above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average digit greater than K

# Using sum() + len() + filter() + lambda

 

# initializing list

test_list = [633, 719, 8382, 119, 327]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# getting average and checking if greater than K

# using filter() and lambda to filter

res = list(filter(lambda sub: sum(

 [int(ele) for ele in str(sub)]) / len(str(sub))
>= K, test_list))

 

# printing result

print("Filtered List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [633, 719, 8382, 119, 327]
    Filtered List : [719, 8382]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

