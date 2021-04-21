Python | Indexing a sublist



In Python, we have several ways to perform the indexing in list, but
sometimes, we have more than just an element to index, the real problem starts
when we have a sublist and its element has to be indexed. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Usingindex() \+ list comprehension**  
This method solves this problem in 2 parts, for the first part it generates a
new list and then it performs indexing on it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# indexing of sublist 

# using list comprehension + index()

 

# initializing test list

test_list = [[1, 'Geeks'], [2, 'For'], [3,
'Geeks']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + index()

# indexing of sublist

res = [ele for i, ele in test_list].index('For')

 

# print result

print("Index of nested element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 'Geeks'], [2, 'For'], [3, 'Geeks']]
    Index of nested element is : 1
    

**Method #2 : Usingnext() + enumerate()**  
This problem can be solved in an efficient manner using the combination of the
above functions. The next function checks for the elements and enumerate
functions separates the nested list elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# indexing of sublist 

# using enumerate() + next()

 

# initializing test list

test_list = [[1, 'Geeks'], [2, 'For'], [3,
'Geeks']]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using enumerate() + next()

# indexing of sublist

res = next((i for i, (j, ele) in enumerate(test_list) if
ele == 'For'), None)

 

# print result

print("Index of nested element is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 'Geeks'], [2, 'For'], [3, 'Geeks']]
    Index of nested element is : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

