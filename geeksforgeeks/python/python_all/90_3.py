Python – Convert Tuple String to Integer Tuple



Interconversion of data is a popular problem developers generally deal with.
One can face a problem to convert tuple string to integer tuple. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingtuple() + int() + replace() + split()**  
The combination of above methods can be used to perform this task. In this, we
perform the conversion using tuple() and int(). Extraction of elements is done
by replace() and split().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple String to Integer Tuple

# Using tuple() + int() + replace() + split()

 

# initializing string 

test_str = "(7, 8, 9)"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert Tuple String to Integer Tuple

# Using tuple() + int() + replace() + split()

res = tuple(int(num) for num in test_str.replace('(',
'').replace(')', '').replace('...', '').split(', '))

 

# printing result 

print("The tuple after conversion is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : (7, 8, 9)
    The tuple after conversion is : (7, 8, 9)
    

**Method #2 : Usingeval()**  
This is recommended method to solve this task. This performs the
interconversion task internally.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple String to Integer Tuple

# Using eval()

 

# initializing string 

test_str = "(7, 8, 9)"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert Tuple String to Integer Tuple

# Using eval()

res = eval(test_str)

 

# printing result 

print("The tuple after conversion is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : (7, 8, 9)
    The tuple after conversion is : (7, 8, 9)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

