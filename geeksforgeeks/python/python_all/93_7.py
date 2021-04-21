Python – Remove String from String List



This particular article is indeed a very useful one for Machine Learning
enthusiast as it solves a good problem for them. In Machine Learning we
generally encounter this issue of getting a particular string in huge amount
of data and handling that sometimes becomes a tedious task. Lets discuss
certain way outs to solve this problem.

 **Method #1 : Usingremove()**  
This particular method is quite naive and not recommended to use, but is
indeed a method to perform this task. remove() generally removes the first
occurrence of K string and we keep iterating this process until no K string is
found in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Remove K String from String List

# using remove()

 

# initializing list 

test_list = ["bad", "GeeksforGeeks", "bad", "is",
"best", "bad"]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# initializing K 

K = "bad"

 

# using remove() to

# Remove K String from String List

while(K in test_list) :

 test_list.remove(K)

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : ['bad', 'GeeksforGeeks', 'bad', 'is', 'best', 'bad']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

**Method #2 : Using List Comprehension**  
More concise and better approach to remove all the K strings, it just checks
if the string is not K and re-makes the list with all strings that are not K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Remove K String from String List

# using list comprehension

 

# initializing list 

test_list = ["bad", "GeeksforGeeks", "bad", "is",
"best", "bad"]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# initializing K 

K = "bad"

 

# using list comprehension to

# Remove K String from String List

test_list = [i for i in test_list if i != K]

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : ['bad', 'GeeksforGeeks', 'bad', 'is', 'best', 'bad']
    Modified list is : ['GeeksforGeeks', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

