Find average of a list in python



Prerequisites: sum() function, len() function, round() function, reduce(),
lambda, and mean().

Given a list of numbers, the task is to find average of that list. Average is
the sum of elements divided by the number of elements.

Examples:

    
    
    Input : [4, 5, 1, 2, 9, 7, 10, 8]
    Output : Average of the list = 5.75
    **Explanation** :
    Sum of the elements is 4+5+1+2+9+7+10+8 = 46
    and total number of elements is 8.
    So average is 46 / 8 = 5.75
    
    Input : [15, 9, 55, 41, 35, 20, 62, 49]
    Output : Average of the list = 35.75
    **Explanation** :
    Sum of the elements is 15+9+55+41+35+20+62+49 = 286
    and total number of elements is 8.
    So average is 46 / 8 = 35.75
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Using sum()**

In Python we can find the average of a list by simply using the **sum()** and
**len()** function.

  *  **sum()** : Using sum() function we can get the sum of the list.
  *  **len()** : len() function is used to get the length or the number of elements in a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get average of a list

def Average(lst):

 return sum(lst) / len(lst)

 

# Driver Code

lst = [15, 9, 55, 41, 35, 20, 62, 49]

average = Average(lst)

 

# Printing average of the list

print("Average of the list =", round(average, 2))  
  
---  
  
 __

 __

Output:

  

  

    
    
    Average of the list = 35.75
    

**Using reduce() and lambda**

We can use the reduce() to reduce the loop and by using the lambda function
can compute summation of list. We use len() to calculate length as discussed
above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get average of a list

# Using reduce() and lambda 

 

# importing reduce()

from functools import reduce

 

def Average(lst):

 return reduce(lambda a, b: a + b, lst) / len(lst)

 

# Driver Code

lst = [15, 9, 55, 41, 35, 20, 62, 49]

average = Average(lst)

 

# Printing average of the list

print("Average of the list =", round(average, 2))  
  
---  
  
 __

 __

Output:

    
    
    Average of the list = 35.75
    

**Using mean()**

The inbuilt function mean() can be used to calculate the mean( average ) of
the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get average of a list

# Using mean()

 

# importing mean()

from statistics import mean

 

def Average(lst):

 return mean(lst)

 

# Driver Code

lst = [15, 9, 55, 41, 35, 20, 62, 49]

average = Average(lst)

 

# Printing average of the list

print("Average of the list =", round(average, 2))  
  
---  
  
 __

 __

Output:

    
    
    Average of the list = 35.75
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

