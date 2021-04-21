Python program to design an unbiased dice throw function



The task is to write a Python program to generate an unbiased dice throw and
give output accordingly. To perform this we can use various methods present in
the python _random_ module.

**Approaches:**

  * Using random.choice() method
  * Using random.randrange() method
  * Using random.randint() method
  * Using random.random() method

 **Method 1:** Using random.choice()

The _choice()_ is a method in _random_ module that returns a random item from
a list, tuple, or string. This method is designed for the specific purpose of
getting a random number from the container and hence is the most common method
to achieve this task of getting a random number from a list.

>  **Syntax:** random.choice(sequence)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   * **sequence** is a mandatory parameter that can be a list, tuple, or
> string.
>

>
>  **Returns:** The choice() returns a random item.

Now, as we know that dice has numbers from the range 1-6 inclusive, so we will
give [1, 2, 3, 4, 5, 6] as the sequence in the function and function will give
an unbiased dice throw as output. Below are the implementations based on the
above explanation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to design an unbiased dice throw

# function

 

# Importing random library

import random

 

# Function to give an unbiased dice throw

def dice_throw():

 

 # Declaring the sequence

 sequence = [1, 2, 3, 4, 5, 6]

 

 # Printing the random result

 print(random.choice(sequence))

 

# Driver Code

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    1
    4

 **Method 2:** Using random.randrange()

This method is used to generate a random number in a range, for lists, we can
specify the range to be 0 to its length, and get the index, and then
corresponding value. This also gives the option of getting even placed
elements or elements at the index of certain multiple.

>  **Syntax :** random.randrange(start(opt), stop, step(opt))
>
>  **Parameters :**
>
>  
>
>
>  
>
>
>   *  **start(opt) :** Number consideration for generation starts from this,
> default value is 0. This parameter is optional.
>   *  **stop :** Numbers less than this are generated. This parameter is
> mandatory.
>   *  **step(opt) :** Step point of range, this won’t be included. This is
> optional. Default value is 1.
>

>
>  **Return Value :** This function generated the numbers in the sequence
> start-stop skipping step.

Now, as we know that dice has numbers from the range 1-6 inclusive, so we will
give [1, 2, 3, 4, 5, 6] as the sequence in the function and then use
_randrange()_ to find a random index and thus function will give an unbiased
dice throw as output. Below are the implementations based on the above
explanation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to design an unbiased dice throw

# function

 

# Importing random library

import random

 

# Function to give an unbiased dice throw

def dice_throw():

 

 # Declaring the sequence

 sequence = [1, 2, 3, 4, 5, 6]

 

 # using random.randrange() to 

 # get a random index number 

 rand_idx = random.randrange(len(sequence))

 

 # Printing the random result

 print(sequence[rand_idx])

 

# Driver Code

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    1
    3

 **Method 3:** Using random.randint()

Yet another method to generate the random number, this also can be used to
generate any number in a range and then using that number index, we can find
the value at corresponding index, just like the above-mentioned technique. But
it differs by the fact that it required 2 mandatory arguments for range.

>  **Syntax :** randint(start, end)
>
>  **Parameters :**
>
>   *  **(start, end) :** Both of them must be integer type values.
>

>
>  **Returns :** A random integer in range [start, end] including the end
> points.

Now, as we know that dice has numbers from the range 1-6 inclusive, so we will
give [1, 2, 3, 4, 5, 6] as the sequence in the function and then use
_randint()_ to find a random index and thus function will give an unbiased
dice throw as output. Below are the implementations based on the above
explanation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to design an unbiased dice throw

# function

 

# Importing random library

import random

 

# Function to give an unbiased dice throw

def dice_throw():

 

 # Declaring the sequence

 sequence = [1, 2, 3, 4, 5, 6]

 

 # using random.randint() to 

 # get a random index number 

 rand_idx = random.randint(0, len(sequence)-1)

 

 # Printing the random result

 print(sequence[rand_idx])

 

# Driver Code

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    5
    4

 **Method 4:** Using random.random()

This method generates the floating-point numbers in the range of 0 to 1. We
can also get the index value of list using this function by multiplying the
result and then typecasting to int to get integer index and then corresponding
list value. Then we will use that index value to print a random number from
the list.

>  **Syntax :** random.random()
>
>  **Parameters :** This method does not accept any parameter.
>
>  **Returns :** This method returns a random floating number between 0 and 1.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to design an unbiased dice throw

# function

 

# Importing random library

import random

 

# Function to give an unbiased dice throw

def dice_throw():

 

 # Declaring the sequence

 sequence = [1, 2, 3, 4, 5, 6]

 

 # using random.random() to 

 # get a random number 

 rand_idx = int(random.random() * len(sequence)) 

 

 # Printing the random result

 print(sequence[rand_idx])

 

# Driver Code

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()

 

# Calling the function

dice_throw()  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    6
    1

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

