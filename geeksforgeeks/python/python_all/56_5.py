Python – Extract Symmetric Tuples



Sometimes while working with Python tuples, we can have a problem in which we
need to extract all the pairs which are symmetric, i.e for any (x, y), we have
(y, x) pair present. This kind of problem can have application in domains such
as day-day programming and web development. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_list = [(6, 7), (2, 3), (7, 6)]  
>  **Output** : {(6, 7)}
>
>  **Input** : test_list = [(6, 7), (2, 3)]  
>  **Output** : {}

 **Method #1 : Using dictionary comprehension +set()**  
The combination of above functionalities can be used to solve this problem. In
this, we initially construct reverse pairs, and then compare with original
list pairs, and extract one of equals. The set() is used to remove duplicates,
to avoid unnecessary computions of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Symmetric Tuples

# Using dictionary comprehension + set()

 

# initializing list

test_list = [(6, 7), (2, 3), (7, 6), (9,
8), (10, 2), (8, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extract Symmetric Tuples

# Using dictionary comprehension + set()

temp = set(test_list) & {(b, a) for a, b in test_list}

res = {(a, b) for a, b in temp if a < b}

 

# printing result 

print("The Symmetric tuples : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
    The Symmetric tuples : {(8, 9), (6, 7)}
    

