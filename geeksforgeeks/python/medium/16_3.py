Python program to find all Strong Numbers in given list



Given a list, write a Python program to find all the Strong numbers in a given
list of numbers.

A **Strong Number** is a number that is equal to the sum of factorial of its
digits.

 **Examples:**

    
    
    **Input :** [1, 2, 5, 145, 654, 34] 
    **Output :** [1, 2, 145]
    
    **Input :** [15, 58, 75, 675, 145, 2]
    **Output :** [145, 2]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Explanation :**

  * We defined 2 functions here: First is factorial() and second is strong_number().
  * As soon as strong_number() is called, the list is passed to the function and stored in the formal argument list.
  * For loop iterates for every element in list, temp is a temporary variable on which calculation is done, then factorial() function is called on the remainder of _temp mod 10_ and passed it to the factorial function.
  * Now when temp equates to 0, it exits the while loop and checks whether sum is equal to x or not. If _True_ then it is added in the list using append() function which is predefined for list and is used to add elements in the list and if there is no strong number then it will return an empty list.

Below is the Python implementation:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find all

# Strong Numbers in given list

def factorial(number):

 if(number == 0 or number == 1):

 fact = 1

 else:

 fact = number * factorial(number - 1)

 return fact

 

def strong_number(list):

 new_list =[]

 

 for x in list:

 temp = x

 sum = 0

 while(temp):

 rem = temp % 10

 sum += factorial(rem)

 temp = temp // 10

 if(sum == x):

 new_list.append(x)

 else:

 pass

 

 return new_list

 

# Driver Code

val_list = [1, 2, 5, 145, 654, 34]

strong_num_list = strong_number(val_list)

print(strong_num_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 145]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

