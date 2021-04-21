Python – K Maximum elements with Index in List



GIven a List, extract K Maximum elements with their indices.

>  **Input** : test_list = [5, 3, 1, 4, 7, 8, 2], K = 2  
>  **Output** : [(4, 7), (5, 8)]  
>  **Explanation** : 8 is maximum on index 5, 7 on 4th.
>
>  **Input** : test_list = [5, 3, 1, 4, 7, 10, 2], K = 1  
>  **Output** : [(5, 10)]  
>  **Explanation** : 10 is maximum on index 5.

 **Method #1 : Using sorted() + index()**

The combination of above functions provide a way of finding solution to this
problem. In this, we initially perform sort and extract K maximum elements,
then are encapsulated in tuple with their ordering in original list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Maximum elements with Index in List

# Using sorted() + index()

 

# initializing list

test_list = [5, 3, 1, 4, 7, 8, 2]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K

K = 3

 

# Using sorted() + index()

# using sorted() to sort and slice K maximum elements 

temp = sorted(test_list)[-K:]

res = []

for ele in temp:

 

 # encapsulating elements with index using index()

 res.append((test_list.index(ele), ele))

 

# printing result 

print("K Maximum with indices : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 3, 1, 4, 7, 8, 2]
    K Maximum with indices : [(0, 5), (4, 7), (5, 8)]
    

**Method #2 : Using enumerate() + itemgetter()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of getting indices using enumerate() and itemgetter() is
used to get the elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Maximum elements with Index in List

# Using enumerate() + itemgetter()

from operator import itemgetter

 

# initializing list

test_list = [5, 3, 1, 4, 7, 8, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K

K = 3

 

# Using enumerate() + itemgetter()

# Making index values pairs at 1st stage

res = list(sorted(enumerate(test_list), key =
itemgetter(1)))[-K:]

 

# printing result

print("K Maximum with indices : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 3, 1, 4, 7, 8, 2]
    K Maximum with indices : [(0, 5), (4, 7), (5, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

