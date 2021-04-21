Python | Joining unicode list elements



Sometimes we can receive data in different formats other than the conventional
list or strings or integers or characters. Python has many other data types
and knowledge of handling them is usually useful. This article demonstrates
the joining of unicode characters in list. Let’s discuss certain ways in which
this can be done.

 **Method #1 : Usingjoin() \+ list comprehension**  
In this method, we first convert the unicode elements of strings to the string
elements and then perform the join operation to get the joined resultant
string from unicode elements list. Works in Python2 only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Joining unicode list elements

# using join() + list comprehension

 

# initializing list

test_list = [ 'We', 'love', 'Geeksforgeeks']

map(unicode, test_list)

 

# printing original list

print("The original list is : " + str(test_list))

 

# using join() + list comprehension to

# Join unicode list elements

res = b':'.join(str(i) for i in test_list)

 

# printing result

print ("The joined string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['We', 'love', 'Geeksforgeeks']
    The joined string is : We:love:Geeksforgeeks
    

**Method #2 : Usingjoin() + str()**  
The list comprehension can be avoided as join function implicitly takes the
joins of all the list elements and returns the joined unicodes which can then
be converted to string using str function. Works in Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Joining unicode list elements

# using join() + str()

 

# initializing list

test_list = [ 'We', 'love', 'Geeksforgeeks']

map(unicode, test_list)

 

# printing original list

print("The original list is : " + str(test_list))

 

# using join() + str() to

# Join unicode list elements

res = str(u':'.join(test_list))

 

# printing result

print ("The joined string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['We', 'love', 'Geeksforgeeks']
    The joined string is : We:love:Geeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

