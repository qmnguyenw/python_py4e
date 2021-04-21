Python – Initialize dictionary with custom value list



In python one usually comes across situations in which one has to use
dictionary for storing the lists. But in those cases, one usually checks for
first element and then creates a list corresponding to key when it comes. But
its always wanted a method to initialize the dict. keys with a custom list.
Let’s discuss certain ways to achieve this particular task.

 **Method #1 : Using Dictionary comprehension**  
This is most sought of method to do this initialization. In this method, we
create the no. of keys we require and then initialize the customlist as we
keep on creating the keys, so as to facilitate the append operation afterwards
without an error.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom list dictionary initialization

# using dictionary comprehension

 

# initialize custom list 

cus_list = [4, 6]

 

# using dictionary comprehension to construct

new_dict = {new_list: cus_list for new_list in range(4)}

 

# printing result

print ("New dictionary with custom list as keys : " +
str(new_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    New dictionary with custom list as keys : {0: [4, 6], 1: [4, 6], 2: [4, 6], 3: [4, 6]}
    

**Method #2 : Usingfromkeys()**  
fromkeys() can be used to perform this by specifying the additional custom
list as argument and the range of elements which need to be the key of
dictionary being made.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom list dictionary initialization

# using fromkeys()

 

# initialization custom list 

cus_list = [4, 6]

 

# using fromkeys() to construct

new_dict = dict.fromkeys(range(4), cus_list)

 

# printing result

print ("New dictionary with custom list as keys : " +
str(new_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    New dictionary with custom list as keys : {0: [4, 6], 1: [4, 6], 2: [4, 6], 3: [4, 6]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

