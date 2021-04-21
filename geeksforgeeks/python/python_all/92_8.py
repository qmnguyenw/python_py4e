Python | Reverse All Strings in String List



Given a list, we always come across situations in which we require to apply
certain function to each element in a list. This can be easily done by
applying a loop and performing an operation to each element. But having
shorthands to solve this problem is always beneficial and helps to focus more
on important aspects of problem. Let’s discuss certain ways in which reverse
operation on each string in string list can be performed.

 **Method #1 : Using list comprehension**  
This method performs the same task in the background as done by the looping
constructs. The advantage this particular method provides is that this is a
one liner and also improves code readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse All Strings in String List

# using list comprehension

 

# initializing list 

test_list = ["geeks", "for", "geeks", "is", "best"]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Reverse All Strings in String List

res = [i[::-1] for i in test_list]

 

# printing result

print ("The reversed string list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
    The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
    

**Method #2 : Usingmap()**  
Using map function, one can easily associate an element with the operation one
wishes to perform. This is the most elegant way to perform or solve this kind
of problems.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse All Strings in String List

# using map()

 

# initializing list 

test_list = ["geeks", "for", "geeks", "is", "best"]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Reverse All Strings in String List

# using map()

reverse = lambda i : i[::-1]

res = list(map(reverse, test_list))

 

# printing result

print ("The reversed string list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
    The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

