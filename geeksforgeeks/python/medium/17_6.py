random.seed( ) in Python



 **random()** function is used to generate random numbers in Python. Not
actually random, rather this is used to generate pseudo-random numbers. That
implies that these randomly generated numbers can be determined.

random() function generates numbers for some values. This value is also
called _seed_ value.

 **How Seed Function Works ?**  
Seed function is used to save the state of a random function, so that it can
generate same random numbers on multiple executions of the code on the same
machine or on different machines (for a specific seed value). The seed value
is the previous value number generated by the generator. For the first time
when there is no previous value, it uses current system time.

 **Usingrandom.seed() function**

Here we will see how we can generate the same random number every time with
the same seed value.

  

  

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# random module is imported

import random 

for i in range(5):

 

 # Any number can be used in place of '0'.

 random.seed(0)

 

 # Generated random number will be between 1 to 1000.

 print(random.randint(1, 1000)) 

   
  
---  
  
__

__

**Output:**

    
    
    865
    865
    865
    865
    865
    

  
**Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing random module

import random

 

random.seed(3)

 

# print a random number between 1 and 1000.

print(random.randint(1, 1000))

 

# if you want to get the same random number again then,

random.seed(3) 

print(random.randint(1, 1000))

 

# If seed function is not used

 

# Gives totally unpredictable responses.

print(random.randint(1, 1000))  
  
---  
  
 __

 __

 **Output:**

    
    
    244
    244
    607
    

On executing the above code, the above two print statements will generate a
response _244_ but the third print statement gives an unpredictable response.

 **Uses of random.seed()**

  1. This is used in the generation of a pseudo-random encryption key. Encryption keys are an important part of computer security. These are the kind of secret keys which used to protect data from unauthorized access over the internet.
  2. It makes optimization of codes easy where random numbers are used for testing. The output of the code sometime depends on input. So the use of random numbers for testing algorithms can be complex. Also seed function is used to generate same random numbers again and again and simplifies algorithm testing process.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save
