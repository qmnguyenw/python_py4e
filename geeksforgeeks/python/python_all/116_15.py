Python | Scramble strings in list



Sometimes, while working with different applications, we can come across a
problem in which we require to shuffle all the strings in the list input we
get. This kind of problem can particularly occur in gaming domain. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension +sample() + join()**  
The combination of above functions can be used to solve this problem. In this,
we need to disintegrate string into character list, scramble using sample(),
rejoin them using join() and then remake list using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Scramble strings in list

# using list comprehension + sample() + join()

from random import sample 

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Scramble strings in list

# using list comprehension + sample() + join()

res = [''.join(sample(ele, len(ele))) for ele in test_list]

 

# printing result

print("Scrambled strings in lists are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Scrambled strings in lists are : ['fgg', 'is', 'btse', 'rof', 'sgeke']
    

**Method #2 : Using list comprehension +shuffle() + join()**  
This is similar to the above method. The only difference is that shuffle() is
used to perform scramble task than using sample().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Scramble strings in list

# using list comprehension + shuffle() + join()

from random import shuffle

 

# Utility function 

def perform_scramble(ele):

 ele = list(ele)

 shuffle(ele)

 return ''.join(ele)

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Scramble strings in list

# using list comprehension + shuffle() + join()

res = [perform_scramble(ele) for ele in test_list]

 

# printing result

print("Scrambled strings in lists are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    Scrambled strings in lists are : ['fgg', 'is', 'btse', 'rof', 'sgeke']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

