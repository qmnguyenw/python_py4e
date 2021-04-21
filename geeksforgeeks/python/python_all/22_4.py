Python Program to Print Largest Even and Largest Odd Number in a List



Given a list. The task is to print the largest even and largest odd number in
a list.

 **Examples:**

    
    
     **Input:** 1 3 5 8 6 10 
    **Output:**
    Largest even number is  10 
    Largest odd number is  5
    
    **Input:** 123 234 236 694 809
    **Output:**
    Largest odd number is  809
    Largest even number is  694

The first approach uses two methods , one for computing largest even number
and the other for computing the largest odd number in a list of numbers, input
by the user. Each of the methods prints the largest even and odd number
respectively. We maintain one counter for each method, for current largest
even or odd and check if the number is divisible by two or not . Accordingly,
we print the largest values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class LargestOddAndEven:

 

 # find largest even number of

 # the list

 def largestEven(self, list):

 

 # counter for current largest

 # even number

 curr = -1

 

 for num in list:

 

 # converting number to integer

 # explicitly

 num = int(num)

 

 # even number is divisible by 2 and

 # if larger than current largest

 if(num % 2 == 0 and num > curr):

 

 # replace current largest even

 curr = num

 print("Largest even number is ", curr)

 # find largest odd number of the list

 def largestOdd(self, list):

 

 # current largest odd number

 currO = -1

 for num in list:

 

 # converting number to integer

 # explicitly

 num = int(num)

 

 # even number is divisible by 2 and

 # if larger than current largest

 if(num % 2 == 1 and num > currO):

 

 # replace current largest even

 currO = num

 print("Largest odd number is ", currO)

list_num = [1, 3, 5, 8, 6, 10]

# creating an object of class

obj = LargestOddAndEven()

# calling method for largest even number

obj.largestEven(list_num)

# calling method for largest odd number

obj.largestOdd(list_num)  
  
---  
  
 __

 __

 **Output:**

    
    
    Largest even number is  10
    Largest odd number is  5

The second approach, uses an optimised version of first approach, where in we
compute both the largest values in one method itself. We still maintain two
counters, but the for loop that iterates over the list runs only once.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class LargestOddAndEven:

 

 # find largest even number of the list

 def largestEvenandOdd(self, list):

 

 # counter for current largest even

 # number

 curr = -1

 

 # counter for current largest odd

 # number

 currO = -1

 for num in list:

 

 # converting number to integer

 # explicitly

 num = int(num)

 

 # even number is divisible by 2 and

 # if larger than current largest

 if(num % 2 == 0 and num > curr):

 

 # replace current largest even

 curr = num

 

 elif(num % 2 == 1 and num > currO):

 

 # replace current largest even

 currO = num

 print("Largest odd number is ", currO)

 print("Largest even number is ", curr)

# input a list of numbers

list_num = [123, 234, 236, 694, 809]

# creating an object of class

obj = LargestOddAndEven()

# calling method for largest even and odd number

obj.largestEvenandOdd(list_num)  
  
---  
  
 __

 __

 **Output:**

    
    
    Largest odd number is  809
    Largest even number is  694

#### Method 3: Using list Comprehension and max function in python:

  * Store even and odd numbers in separate lists using **list comprehension** **.**
  * print **max()** of corresponding lists.

Below is the implementation of above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for the above approach

def printmax(lis):

 

 # Using list comprehension storing

 # even and odd numbers as separate lists

 even = [x for x in lis if x % 2 == 0]

 odd = [x for x in lis if x % 2 == 1]

 # printing max numbers in corresponding lists

 print("Largest odd number is ", max(odd))

 print("Largest even number is ", max(even))

# Input a list of numbers

lis = [123, 234, 236, 694, 809]

printmax(lis)

# This code is contributed by vikkycirus  
  
---  
  
 __

 __

 **Output:**

    
    
    Largest odd number is  809
    
    Largest even number is  694

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

