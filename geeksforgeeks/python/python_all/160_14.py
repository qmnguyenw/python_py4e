Python program to check if number is palindrome (one-liner)



Sometimes, we have an application of checking a number is palindrome or not
and it’s quite common while day-day programming or competitive programming,
it’s easy to reverse a number and check it but sometimes for readability and
reducing lines of code, we require to perform this in one-liner logic. Let’s
discuss certain ways in which this can be achieved.

> Input : test_number = 12321  
> Output : True
>
> Input : test_number = 1234  
> Output : False

 **Method #1 : Usingmath.log() \+ recursion + list comprehension**  
The combination of above three functions can perform this particular task
easily, the logs function extracts the number of digits which is powered by 10
to get the number for that iteration for comparison. The process is recurred
to test for palindrome.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# checking a number is palindrome

# using math.log() + recursion + list comprehension

import math

 

# the recursive function to reverse

def rev(num):

 return int(num != 0) and ((num % 10) * \

 (10**int(math.log(num, 10))) + \

 rev(num // 10))

 

# initializing number 

test_number = 9669669

 

# printing the original number 

print ("The original number is : " + str(test_number))

 

# using math.log() + recursion + list comprehension

# for checking a number is palindrome

res = test_number == rev(test_number)

 

# printing result

print ("Is the number palindrome ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original number is : 9669669
    Is the number palindrome ? : True
    

