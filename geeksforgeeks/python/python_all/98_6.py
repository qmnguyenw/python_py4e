Python | Alternate Rear iteration



The iteration of numbers is done by looping techniques in python. There are
many techniques in Python which facilitate looping. Sometimes we require to
perform the looping backwards in alternate way and having shorthands to do so
can be quite useful. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingreversed()**  
The simplest way to perform this is to use the reversed function for the for
loop and the iteration will start occurring from the rear side than the
conventional counting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Rear iteration

# using reversed()

 

# Initializing number from which 

# iteration begins 

N = 6

 

# using reversed() to perform the Alternate Rear iteration

print ("The reversed numbers are : ", end = "")

for num in reversed(range(0, N + 1, 2)) :

 print (num, end = " ")  
  
---  
  
 __

 __

 **Output :**

    
    
    The reversed numbers are : 6 4 2 0 
    

**Method #2 : Usingrange(N, -1, -2)**  
This particular task can also be performed using the conventional range
function which, if provided with the third argument performs the alternate
skip and second argument is used to start from backwards.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Rear iteration

# using range(N, -1, -2)

 

# Initializing number from which 

# iteration begins 

N = 6

 

# using reversed() to perform the Alternate Rear iteration

print ("The reversed numbers are : ", end = "")

for num in range(N, -1, -2) :

 print (num, end = " ")  
  
---  
  
 __

 __

 **Output :**

    
    
    The reversed numbers are : 6 4 2 0 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

