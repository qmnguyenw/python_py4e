Python | Reversed Split Strings



The functionality of splitting is quite popular with manyfold applications and
usages. With all, comes the scopes of many types of variations. This article
discusses one among those variations in which one desires to get the split and
reversal of element string order, both the operations at once. Let’s discuss
certain ways to solve this particular problem.

 **Method #1 : Usingjoin() + reversed() + split()**

In this particular method, we first get the element words using the split
function, perform the reversal of order of them using the reversed function
and then perform the join to bind together the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse string split

# using join() + reversed() + split()

 

# initializing string

test_string = "Gfg is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using join() + reversed() + split()

# Reverse string split

res = ", ".join(reversed(test_string.split(" ")))

 

# print result

print("The string after reverse split : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : Gfg is best
    The string after reverse split : best, is, Gfg
    

  

  

**Method #2 : Usingjoin() + split() \+ list slicing**

This method is similar to the above method in which we perform split and join,
but the only difference in this method is that we use list slicing to perform
the reversal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse string split

# using join() + split() + list slicing

 

# initializing string

test_string = "Gfg is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using join() + split() + list slicing

# Reverse string split

res = ', '.join(test_string.split()[::-1])

 

# print result

print("The string after reverse split : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : Gfg is best
    The string after reverse split : best, is, Gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

