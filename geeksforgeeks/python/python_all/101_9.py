Python – Concatenate string rows in Matrix



The problems concerning matrix are quite common in both competitive
programming and Data Science domain. One such problem that we might face is of
finding the concatenation of rows of matrix in uneven sized matrix. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using join() \+ list comprehension**  
The combination of above functions can help to get the solution to this
particular problem in just a one line and hence quite useful. The join
function computes the concatenation of sublists and all this bound together
using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Row String Concatenation Matrix

# using join() + list comprehension

 

# initializing list

test_list = [['gfg', ' is', ' best'], ['Computer', '
Science'], ['GeeksforGeeks']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using join() + list comprehension

# Row String Concatenation Matrix

res = [''.join(idx for idx in sub) for sub in test_list
]

 

# print result

print("The row concatenation in matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['gfg', ' is', ' best'], ['Computer', ' Science'], ['GeeksforGeeks']]
    The row concatenation in matrix : ['gfg is best', 'Computer Science', 'GeeksforGeeks']
    

**Method #2 : Using loop**  
This task can also be performed in brute force manner in which we just iterate
the sublists and perform join in brute manner creating new string for each
sublist and appending in list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Row String Concatenation Matrix

# using loop

 

# initializing list

test_list = [['gfg', ' is', ' best'], ['Computer', '
Science'], ['GeeksforGeeks']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop

# Row String Concatenation Matrix

res = []

for sub in test_list:

 res_sub = ""

 for idx in sub:

 res_sub = res_sub + idx

 res.append(res_sub)

 

# print result

print("The row concatenation in matrix : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['gfg', ' is', ' best'], ['Computer', ' Science'], ['GeeksforGeeks']]
    The row concatenation in matrix : ['gfg is best', 'Computer Science', 'GeeksforGeeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

