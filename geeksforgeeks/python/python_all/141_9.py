Python program to print all Strong numbers in given list



Given a list, write a Python program to print all the strong numbers in that
list.

 ** _Strong Numbers_** are the numbers whose sum of factorial of digits is
equal to the original number.

 **Example for checking if number is Strong Number or not.**

    
    
    **Input:** n = 145
    **Output:** Yes
    **Explanation:**
    Sum of digit factorials = 1! + 4! + 5!
                            = 1 + 24 + 120
                            = 145
    

**Steps for checking number is strong or not :**

    
    
    1) Initialize sum of factorials as 0. 
    2) For every digit d, do following
       a) Add d! to sum of factorials.
    3) If sum factorials is same as given 
       number, return true.
    4) Else return false.
    

Let’s see the Python program for this problem :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to print

# all strong numbers in a list. 

 

# Define a function for calculating

# factorial of a number

def factorial(number):

 

 fact = 1

 

 if number == 0 or number == 1 :

 return fact

 

 for i in range(2, number + 1) :

 fact *= i

 

 return fact

 

# Define a function for checking a 

# number is strong number or not

def find_strong_numbers(num_list):

 result = []

 

 # loop till list is not empty

 for num in num_list :

 sum = 0

 temp = num

 

 # loop till number is not zero

 while num != 0 :

 

 r = num % 10

 

 # function call

 sum += factorial(r)

 

 num //= 10

 

 # check number is strong or not

 if sum == temp:

 

 # adding number to the list

 result.append(temp)

 

 # return list of strong numbers 

 return result

 

 

# Driver Code

if __name__ == "__main__" :

 

 num_list = [145, 375, 100, 2, 10, 40585,
0]

 

 # function call

 strong_num_list = find_strong_numbers(num_list)

 

 # loop till list is not empty

 for strong_num in strong_num_list :

 print(strong_num, end =" ")

   
  
---  
  
__

__

**Output:**

    
    
    145 2 40585 0
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

