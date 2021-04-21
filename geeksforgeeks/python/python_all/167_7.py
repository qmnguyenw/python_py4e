Python | Convert list of strings and characters to list of characters



Sometimes we come forward to the problem in which we receive a list that
consists of strings and characters mixed and the task we need to perform is
converting that mixed list to a list consisting entirely of characters. Let’s
discuss certain ways in which this is achieved.  

 **Method #1 : UsingList comprehension**  
In this method, we just consider each list element as string and iterate their
each character and append each character to the newly created target list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to convert list of string and characters

# to list of characters

# using list comprehension

 

# initializing list 

test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to convert list of string and characters

# to list of characters

res = [i for ele in test_list for i in ele]

 

# printing result 

print ("The list after conversion is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg', 'i', 's', 'be', 's', 't']
    The list after conversion is : ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']
    

  
**Method #2 : Usingjoin()**

join function can be used to open the string and then join each letter with
empty string resulting in a single character extraction. The end result has to
be type casted to list for desired result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to convert list of string and characters

# to list of characters

# using join()

 

# initializing list 

test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using join()

# to convert list of string and characters

# to list of characters

res = list(''.join(test_list))

 

# printing result 

print ("The list after conversion is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg', 'i', 's', 'be', 's', 't']
    The list after conversion is : ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']
    

  
**Method #3 : Usingchain.from_iterable()**

from_iterable function performs the similar task of firstly opening each
string and then joining the characters one by one. This is the most pythonic
way to perform this particular task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to convert list of string and characters

# to list of characters

# using chain.from_iterable()

from itertools import chain

 

# initializing list 

test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using chain.from_iterable()

# to convert list of string and characters

# to list of characters

res = list(chain.from_iterable(test_list))

 

# printing result 

print ("The list after conversion is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg', 'i', 's', 'be', 's', 't']
    The list after conversion is : ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

