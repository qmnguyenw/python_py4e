Python | Sort list of numbers by sum of their digits



Given a list of non-negative numbers, the task is to sort these integers
according to the sum of their digits.

 **Examples:**

    
    
    **Input :** [12, 10, 106, 31, 15]
    **Output :** [10, 12, 31, 15, 106]
    
    **Input :** [1111, 19, 29, 11, 12, 9]
    **Output :** [11, 12, 1111, 9, 19, 29]
    

Let’s discuss few Pythonic ways to do this task.

 **Approach #1 :** List comprehension

Using for loop to convert each element of list to a different list with its
digits as elements. Now, use the sorted function with the above-mentioned
function as _key_.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Sort list of

# integers according to sum of digits

 

def sortList(lst):

 digits = [int(digit) for digit in str(lst) ]

 return sum(digits)

 

# Driver Code

lst = [12, 10, 106, 31, 15]

print(sorted(lst, key = sortList))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 12, 31, 15, 106]
    

**Approach #2 :** Using map()

This approach is similar to the above approach with a slight difference that
instead of for loop, we use map() to convert each element of list to a
different list with its digit as elements and then follow the similar approach
as above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Sort list of

# integers according to sum of digits

 

def sortList(num):

 return sum(map(int, str(num)))

 

# Driver Code

lst = [12, 10, 106, 31, 15]

result = sorted(lst, key = sortList)

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 12, 31, 15, 106]
    

There is also a one-liner alternative to the above mentioned approach.

 __

 __  
 __

 __

 __  
 __  
 __

def sortList(lst):

 return sorted(lst, key = lambda x:(sum(map(int,
str(x)))))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

