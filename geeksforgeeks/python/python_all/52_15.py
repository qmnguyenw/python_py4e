Python – Add Space between Potential Words



Given list of Strings, task is to add a space before sequence which begin with
capital letters.

>  **Input** : test_list = [“gfgBest”, “forGeeks”,
> “andComputerScienceStudents”]  
>  **Output** : [‘gfg Best’, ‘for Geeks’, ‘and Computer Science Students’]  
>  **Explanation** : Words segregated by Capitals.
>
>  **Input** : test_list = [“ComputerScienceStudentsLoveGfg”]  
>  **Output** : [‘Computer Science Students Love Gfg’]  
>  **Explanation** : Words segregated by Capitals.

 **Method #1 : Using loop + join()**

This is one of the ways in which this task can be perfomed. In this, we
perform the task of iterating all the stings and then all the characters
before adding space using loop in brute force manner. The isupper() is used to
check for capital character.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add Space between Potential Words

# Using loop + join()

 

# initializing list

test_list = ["gfgBest", "forGeeks", "andComputerScience"]

 

# printing original list

print("The original list : " + str(test_list))

 

res = []

 

# loop to iterate all strings 

for ele in test_list:

 temp = [[]]

 for char in ele:

 

 # checking for upper case character

 if char.isupper():

 temp.append([])

 

 # appending character at latest list

 temp[-1].append(char)

 

 # joining lists after adding space

 res.append(' '.join(''.join(ele) for ele in temp))

 

# printing result 

print("The space added list of strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfgBest', 'forGeeks', 'andComputerScience']
    The space added list of strings : ['gfg Best', 'for Geeks', 'and Computer Science']
    

**Method #2 : Using regex() + list comprehension**

The combination of above functions can also be used to solve this problem. In
this we employ regex code to check for upper case letter and perform space
addition and joining using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add Space between Potential Words

# Using regex() + list comprehension

import re

 

# initializing list

test_list = ["gfgBest", "forGeeks", "andComputerScience"]

 

# printing original list

print("The original list : " + str(test_list))

 

# using regex() to perform task 

res = [re.sub(r"(\w)([A-Z])", r"\1 \2", ele) for ele in
test_list]

 

# printing result 

print("The space added list of strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfgBest', 'forGeeks', 'andComputerScience']
    The space added list of strings : ['gfg Best', 'for Geeks', 'and Computer Science']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

