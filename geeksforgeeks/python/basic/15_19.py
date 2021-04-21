Python | Select random value from a list



Generating random numbers has always been an useful utility in day-day
programming for games or various types of gambling etc. Hence knowledge and
shorthands of it in any programming language is always a plus to have.

Let’s discusses all different ways to select random values from a list.

 **Method #1 :** Using random.choice()

This method is designed for the specific purpose of getting random number from
the container and hence is the most common method to achieve this task of
getting a random number from a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get random number from list

# using random.choice()

import random

 

# initializing list 

test_list = [1, 4, 5, 2, 7]

 

# printing original list 

print ("Original list is : " + str(test_list))

 

# using random.choice() to 

# get a random number 

random_num = random.choice(test_list)

 

# printing random number

print ("Random selected number is : " + str(random_num))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Original list is : [1, 4, 5, 2, 7]
    Random selected number is : 1
    

