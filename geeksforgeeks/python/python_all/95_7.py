Python – Convert Alternate String Character to Integer



Interconversion between data types is facilitated by python libraries quite
easily. But the problem of converting the alternate list of string to integers
is quite common in development domain. Let’s discuss few ways to solve this
particular problem.

 **Method #1 : Naive Method**  
This is most generic method that strikes any programmer while performing this
kind of operation. Just looping over whole list and convert alternate of the
string of list to int by type casting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Alternate String to Integer Conversion

# using naive method 

 

# initializing list 

test_list = ['1', '4', '3', '6', '7']

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using naive method to

# perform conversion

for i in range(0, len(test_list)):

 if i % 2:

 test_list[i] = int(test_list[i])

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : ['1', '4', '3', '6', '7']
    Modified list is : ['1', 4, '3', 6, '7']
    

**Method #2 : Using list comprehension**  
This is just a kind of replica of the above method, just implemented using
list comprehension, kind of shorthand that a developer looks for always. It
saves time and complexity of coding a solution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Alternate String to Integer Conversion

# using list comprehension

 

# initializing list 

test_list = ['1', '4', '3', '6', '7']

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using list comprehension to

# perform conversion

test_list = [int(ele) if idx % 2 else ele for idx,
ele in enumerate(test_list)]

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : ['1', '4', '3', '6', '7']
    Modified list is : ['1', 4, '3', 6, '7']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

