Python – Maximum N repeated Elements



Given List of elements, remove an element if it’s occurrence in list increases
more than N.

>  **Input** : test_list = [6, 4, 6, 3, 6], N = 1
>
>  **Output** : [6, 4, 3]
>
>  **Explanation** : The occurrence 2nd onwards of 6 are removed.
>
>  **Input** : test_list = [6, 4, 6, 3, 6], N = 2
>
>  
>
>
>  
>
>
>  **Output** : [6, 4, 6, 3]
>
>  **Explanation** : The occurrence 3nd onwards of 6 are removed.

 **Method #1 : Using loop + count()**

The combination of above functionalities can be used to solve this problem. In
this, we perform iteration of elements and check if count is more than N of
that element using count(), if yes, then we remove that element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum N repeated Elements

# Using loop + count()

 

# initializing list

test_list = [5, 7, 7, 2, 5, 5, 7, 2,
2]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N

N = 2

 

# Using loop + count()

res = []

for ele in test_list:

 

 # checking of elements occurrence is not greater than N

 if res.count(ele) < N:

 res.append(ele)

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 7, 2, 5, 5, 7, 2, 2]
    Extracted elements : [5, 7, 7, 2, 5, 2]
    
    

**Method #2 : Using Counter() + loop**

This is yet another way in which this task can be performed. In this, we use
Counter() to perform counting of elements, and then append its size elements
if less than N, if greater, list comprehension is used to extend elements till
N. Does’nt preserve order.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum N repeated Elements

# Using Counter() + loop

from collections import Counter

 

# initializing list

test_list = [5, 7, 7, 2, 5, 5, 7, 2,
2]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N

N = 2

 

# Using Counter() + loop

res = []

temp = Counter(test_list)

for key, ele in temp.items():

 

 # Conditional check for size decision during append

 if ele <= N:

 res.extend([key for idx in range(ele)])

 else:

 res.extend([key for idx in range(N)])

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 7, 2, 5, 5, 7, 2, 2]
    Extracted elements : [5, 5, 7, 7, 2, 2]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

