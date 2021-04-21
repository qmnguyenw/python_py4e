Python – Negative index of Element in List



Given a list of elements, find its negative index in the List.

>  **Input** : test_list = [5, 7, 8, 2, 3, 5, 1], K = 2  
> **Output** : -4  
> **Explanation** : 2 is 4th element from rear.
>
>  **Input** : test_list = [5, 7, 8, 2, 3, 5, 1], K = 5  
> **Output** : -2  
> **Explanation** : 5 is 2nd element from rear.

**Method #1 : Using** **index()** **+** **len()**

In this, we get the index of the element using index(), and then subtract it
from the list length to get the required result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Negative index of Element

# Using index() + len()

# initializing list

test_list = [5, 7, 8, 2, 3, 5, 1]

# printing original list

print("The original list is : " + str(test_list))

# initializing Element

K = 3

# getting length using len() and subtracting index from it

res = len(test_list) - test_list.index(K)

# printing result

print("The required Negative index : -" + str(res))  
  
---  
  
 __

 __

  
**Output:**

    
    
    The original list is : [5, 7, 8, 2, 3, 5, 1]
    The required Negative index : -3

**Method #2 : Using ~ operator +** **list slicing** **\+ index()**

In this, we reverse the list using slicing, and use ~ operator to get
negation, index() is used to get the desired negative index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Negative index of Element

# Using ~ operator + list slicing + index()

# initializing list

test_list = [5, 7, 8, 2, 3, 5, 1]

# printing original list

print("The original list is : " + str(test_list))

# initializing Element

K = 3

# -1 operator to reverse list, index() used to get index

res = ~test_list[::-1].index(K)

# printing result

print("The required Negative index : " + str(res))  
  
---  
  
 __

 __

 ****  
**Output:**

    
    
    The original list is : [5, 7, 8, 2, 3, 5, 1]
    The required Negative index : -3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

