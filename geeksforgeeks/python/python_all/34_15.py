Python program to find tuples which have all elements divisible by K from a
list of tuples



Given a list of tuples. The task is to extract all tuples which have all
elements divisible by K.

>  **Input** : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6  
> **Output** : [(6, 24, 12), (60, 12, 6)]  
> **Explanation** : Both tuples have all elements multiple of 6.
>
>  **Input** : test_list = [(6, 24, 12), (60, 10, 5), (12, 18, 21)], K = 5  
> **Output** : [(60, 10, 5)]  
> **Explanation** : Multiple of 5 tuples extracted.

**Method #1 : Using list comprehension + all()**

In this, we test for all elements to be K multiple using all() for filtering
purpose, and list comprehension is used for iteration of all tuples.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Multiple Elements Tuples

# Using list comprehension + all()

 

# initializing list

test_list = [(6, 24, 12), (7, 9, 6), (12,
18, 21)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

# all() used to filter elements

res = [sub for sub in test_list if all(ele % K ==
0 for ele in sub)]

 

# printing result

print("K Multiple elements tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
    K Multiple elements tuples : [(6, 24, 12)]
    

**Method #2 : Using filter() + lambda + all()**

In this, we perform task of filtering using filter() + lambda, and logic
provided by all(), as in above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Multiple Elements Tuples

# Using filter() + lambda + all()

 

# initializing list

test_list = [(6, 24, 12), (7, 9, 6), (12,
18, 21)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

# filter() + lambda for filter operation

res = list(filter(lambda sub: all(ele % K == 0
for ele in sub), test_list))

 

# printing result

print("K Multiple elements tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
    K Multiple elements tuples : [(6, 24, 12)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

