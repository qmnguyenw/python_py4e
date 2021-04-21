Python | Append String to list



Sometimes, while working with data, we can have a problem in which we need to
add elements to a container. List can contain any type of data type. Let’s
discuss certain ways in which we can perform string append operation in list
of integers.

 **Method #1 : Using + operator + list conversion**  
In this method, we first convert the string into a list and then perform the
task of append using + operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Appending String to list

# using + operator + list conversion

 

# initialize list 

test_list = [1, 3, 4, 5]

 

# initialize string 

test_str = 'gfg'

 

# printing original list 

print("The original list : " + str(test_list))

 

# printing original string 

print("The original string : " + str(test_str))

 

# Appending String to list

# using + operator + list conversion

test_list += [test_str]

 

# printing result

print("The list after appending is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 5]
    The original string : gfg
    The list after appending is : [1, 3, 4, 5, 'gfg']
    

**Method #2 : Usingappend()**  
This particular function can be used to perform the operation of appending
string element to end of list without changing the state of string to list of
characters.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Appending String to list

# using append()

 

# initialize list 

test_list = [1, 3, 4, 5]

 

# initialize string 

test_str = 'gfg'

 

# printing original list 

print("The original list : " + str(test_list))

 

# printing original string 

print("The original string : " + str(test_str))

 

# Appending String to list

# using append()

test_list.append(test_str)

 

# printing result

print("The list after appending is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 5]
    The original string : gfg
    The list after appending is : [1, 3, 4, 5, 'gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

