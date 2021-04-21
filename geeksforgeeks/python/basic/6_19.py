Python – Convert Snake case to Pascal case



Sometimes, while working with Python Strings, we have problem in which we need
to perform a case conversion of String. This a very common problem. This can
have application in many domains such as web development. Lets discuss certain
ways in which this task can be performed.

> Input : geeks_for_geeks  
> Output : GeeksforGeeks
>
> Input : left_index  
> Output : leftIndex

 **Method #1 : Usingtitle() + replace()**  
This task can be solved using combination of above functions. In this, we
first convert the underscore to empty string and then title case each word.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Snake case to Pascal case

# Using title() + replace()

 

# initializing string

test_str = 'geeksforgeeks_is_best'

 

# printing original string

print("The original string is : " + test_str)

 

# Convert Snake case to Pascal case

# Using title() + replace()

res = test_str.replace("_", " ").title().replace(" ", "")

 

# printing result 

print("The String after changing case : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original string is : geeksforgeeks_is_best
    The String after changing case : GeeksforgeeksIsBest
    

