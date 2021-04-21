Python | Extract Nth words in Strings List



Sometimes, while working while working with Python Lists, we can have problem
in which we need to perform the task of extracting Nth word of each string in
List. This can have application in web-development domain. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +split()**  
The combination of above methods can be used to solve this problem. In this,
we perform the task of getting Nth word using split and recreate list using
list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Nth words in Strings List

# Using list comprehension + split()

 

# initializing list

test_list = ['Gfg best for', 'All geeks', 'It is for', 'all
CS professionals']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N 

N = 2

 

# Extract Nth words in Strings List

# Using list comprehension + split()

res = [sub.split()[N - 1] for sub in test_list if
len(sub.split()) > 1]

 

# printing result 

print("The Nth words in list are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['Gfg best for', 'All geeks', 'It is for', 'all CS professionals']
    The Nth words in list are : ['best', 'geeks', 'is', 'CS']
    

**Method #2 : Using list comprehension +enumerate() + split()**  
The combination of above functions can be used to perform this task. In this,
we use enumerate to check for the Nth word rather than split().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Nth words in Strings List

# Using list comprehension + <code>enumerate() + split()

 

# initializing list

test_list = ['Gfg best for', 'All geeks', 'It is for', 'all
CS professionals']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing N 

N = 2

 

# Extract Nth words in Strings List

# Using list comprehension + <code>enumerate() + split()

res = [ele for sub in test_list for idx, ele in
enumerate(sub.split()) if idx == (N - 1)]

 

# printing result 

print("The Nth words in list are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['Gfg best for', 'All geeks', 'It is for', 'all CS professionals']
    The Nth words in list are : ['best', 'geeks', 'is', 'CS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

