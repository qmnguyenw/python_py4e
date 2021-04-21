Python | Convert List of lists to list of Strings



Interconversion of data is very popular nowdays and has many applications. In
this scenario, we can have a problem in which we need to convert a list of
lists, i.e matrix into list of strings. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using list comprehension +join()**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task of iteration using list comprehension and join() is
used to perform task of joining string to list of strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of lists to list of Strings

# using list comprehension + join()

 

# initialize list 

test_list = [["g", "f", "g"], ["i", "s"], ["b",
"e", "s", "t"]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert List of lists to list of Strings

# using list comprehension + join()

res = [''.join(ele) for ele in test_list]

 

# printing result

print("The String of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    The String of list is : ['gfg', 'is', 'best']
    

**Method #2: Usingmap() + join()**  
The task above can also be performed using combination of above methods. In
this, we perform the task of conversion using join and iteration using map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of lists to list of Strings

# using map() + join()

 

# initialize list 

test_list = [["g", "f", "g"], ["i", "s"], ["b",
"e", "s", "t"]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert List of lists to list of Strings

# using map() + join()

res = list(map(''.join, test_list))

 

# printing result

print("The String of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    The String of list is : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

