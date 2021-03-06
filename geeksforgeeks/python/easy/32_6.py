Random Numbers in Python



Python defines a set of functions that are used to generate or manipulate
random numbers through the **random module.** Functions in the random module
rely on a pseudo-random number generator function **random()** , which
generates a random float number between 0.0 and 1.0. These particular type of
functions is used in a lot of games, lotteries, or any application requiring a
random number generation.

## Random Number Operations

 **1.** **choice()** **** :- choice() is an inbuilt function in the Python
programming language that returns a random item from a list, tuple, or string.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the use of

# choice() method

# import random

import random

# prints a random value from the list

list1 = [1, 2, 3, 4, 5, 6]

print(random.choice(list1))

# prints a random item from the string

string = "striver"

print(random.choice(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    t

 **2.** **randrange(beg, end, step)**:- The random module offers a function
that can generate random numbers from a specified range and also allowing
rooms for steps to be included, called **randrange().**

  

  

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# choice() and randrange()

# importing "random" for random operations

import random

# using choice() to generate a random number from a

# given list of numbers.

print("A random number from list is : ", end="")

print(random.choice([1, 4, 8, 10, 3]))

# using randrange() to generate in range from 20

# to 50. The last parameter 3 is step size to skip

# three numbers when selecting.

print("A random number from range is : ", end="")

print(random.randrange(20, 50, 3))  
  
---  
  
 __

 __

 **Output:**

    
    
    A random number from list is : 4
    A random number from range is : 41

 **3\. random()** :- This method is used to generate a **float random number
less than 1 and greater or equal to 0.**

 **4.** **seed()**:- Seed function is used to save the state of a random
function so that it can generate some random numbers on multiple executions of
the code on the same machine or on different machines (for a specific seed
value). The seed value is the previous value number generated by the
generator. For the first time when there is no previous value, it uses current
system time.

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# random() and seed()

# importing "random" for random operations

import random

# using random() to generate a random number

# between 0 and 1

print("A random number between 0 and 1 is : ", end="")

print(random.random())

# using seed() to seed a random number

random.seed(5)

# printing mapped random number

print("The mapped random number with 5 is : ", end="")

print(random.random())

# using seed() to seed different random number

random.seed(7)

# printing mapped random number

print("The mapped random number with 7 is : ", end="")

print(random.random())

# using seed() to seed to 5 again

random.seed(5)

# printing mapped random number

print("The mapped random number with 5 is : ", end="")

print(random.random())

# using seed() to seed to 7 again

random.seed(7)

# printing mapped random number

print("The mapped random number with 7 is : ", end="")

print(random.random())  
  
---  
  
 __

 __

 **Output:**

> A random number between 0 and 1 is : 0.510721762520941
>
> The mapped random number with 5 is : 0.6229016948897019
>
>  
>
>
>  
>
>
> The mapped random number with 7 is : 0.32383276483316237
>
> The mapped random number with 5 is : 0.6229016948897019
>
> The mapped random number with 7 is : 0.32383276483316237

 **5.** **shuffle()**:- It is used to shuffle a sequence (list). Shuffling
means changing the position of the elements of the sequence. Here, the
shuffling operation is in place.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the random module

import random

# declare a list

sample_list = ['A', 'B', 'C', 'D', 'E']

print("Original list : ")

print(sample_list)

# first shuffle

random.shuffle(sample_list)

print("\nAfter the first shuffle : ")

print(sample_list)

# second shuffle

random.shuffle(sample_list)

print("\nAfter the second shuffle : ")

print(sample_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : 
    ['A', 'B', 'C', 'D', 'E']
    
    After the first shuffle : 
    ['A', 'B', 'E', 'C', 'D']
    
    After the second shuffle : 
    ['C', 'E', 'B', 'D', 'A']

 **6.** **uniform(a, b)**:- This function is used to generate a **floating
point random number between the numbers** mentioned in its arguments. **It
takes two arguments, lower limit(included in generation) and upper limit(not
included in generation).**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# shuffle() and uniform()

# importing "random" for random operations

import random

# Initializing list

li = [1, 4, 5, 10, 2]

# Printing list before shuffling

print("The list before shuffling is : ", end="")

for i in range(0, len(li)):

 print(li[i], end=" ")

print("\r")

# using shuffle() to shuffle the list

random.shuffle(li)

# Printing list after shuffling

print("The list after shuffling is : ", end="")

for i in range(0, len(li)):

 print(li[i], end=" ")

print("\r")

# using uniform() to generate random floating number in range

# prints number between 5 and 10

print("The random floating point number between 5 and 10 is : ",
end="")

print(random.uniform(5, 10))  
  
---  
  
 __

 __

 **Output:**

> The list before shuffling is : 1 4 5 10 2
>
> The list after shuffling is : 2 1 4 5 10
>
> The random floating point number between 5 and 10 is : 5.183697823553464

This article is contributed by Manjeet Singh. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

