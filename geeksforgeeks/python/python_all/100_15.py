Python – Incremental value initialization in Dictionary



The interconversion between the datatypes is very popular and hence many
articles have been written to demonstrate different kind of problems with
their solutions. This article deals with yet another similar type problem of
converting a list to dictionary, with values as the index incremental with K
difference. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using dictionary comprehension +enumerate()**  
This problem can be solved easily using the combination of above functions,
dictionary comprehension can perform the task of constructing the dictionary
and enumerate function can be used to access the index value along with the
element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental value initialization in Dictionary

# using Dictionary comprehension + enumerate()

 

# initializing list

test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

 

# printing original list

print("The original list : " + str(test_list))

 

# initialization K 

K = 4

 

# using Dictionary comprehension + enumerate()

# Incremental value initialization in Dictionary

res = {val : (K * (idx + 1)) for idx, val in
enumerate(test_list)}

 

# print result

print("The Dictionary after index keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Nikhil', 'Akshat', 'Akash', 'Manjeet']
    The Dictionary after index keys : {'Akash': 12, 'Nikhil': 4, 'Manjeet': 16, 'Akshat': 8}
    

**Method #2 : Usingdict() + zip()**  
This problem can also be solved using the combination of above 2 functions,
the dict method can be used to convert to dictionary and zip function can be
used to map the indices with the keys.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental value initialization in Dictionary

# using dict() + zip()

 

# initializing list

test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']

 

# printing original list

print("The original list : " + str(test_list))

 

# initialization K 

K = 4

 

# using dict() + zip()

# Incremental value initialization in Dictionary

res = dict(zip(test_list, range(K, len(test_list) * (K
+ 1), K)))

 

# print result

print("The Dictionary after index keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Nikhil', 'Akshat', 'Akash', 'Manjeet']
    The Dictionary after index keys : {'Akash': 12, 'Nikhil': 4, 'Manjeet': 16, 'Akshat': 8}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

