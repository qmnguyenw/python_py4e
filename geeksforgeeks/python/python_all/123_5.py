Python | Check if tuple exists as dictionary key



Sometimes, while working with dictionaries, there is a possibility that it’s
keys be in form of tuples. This can be a sub problem to some of web
development domain. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usingin operator**  
This is the most recommened and Pythonic way to perform this particular task.
It checks for particular tuple and returns True in case of it occurs or False
if doesn’t.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple exists as dictionary key

# using in operator

 

# initialize dictionary

test_dict = { (3, 4) : 'gfg', 6 : 'is', (9,
1) : 'best'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initialize target tuple 

tar_tup = (3, 4)

 

# Check if tuple exists as dictionary key

# using in operator

res = tar_tup in test_dict

 

# printing result

print("Does tuple exists as dictionary key ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {(3, 4): 'gfg', (9, 1): 'best', 6: 'is'}
    Does tuple exists as dictionary key ? : True
    

**Method #2 : Usingget()**  
We can use dictionary’s get(), which searches for key in dictionary and if
it doesn’t get it, it returns a None. This can be extended in case of tuple
keys as well.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple exists as dictionary key

# using get()

 

# initialize dictionary

test_dict = { (3, 4) : 'gfg', 6 : 'is', (9,
1) : 'best'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initialize target tuple 

tar_tup = (3, 5)

 

# Check if tuple exists as dictionary key

# using get()

res = False

res = test_dict.get(tar_tup) != None

 

# printing result

print("Does tuple exists as dictionary key ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {(3, 4): 'gfg', (9, 1): 'best', 6: 'is'}
    Does tuple exists as dictionary key ? : False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

