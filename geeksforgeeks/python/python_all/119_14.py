Python | Convert String to Tuple



Interconversion of data types is very common problem one can face while
programming. There can be a problem in which we need to convert a string of
integers to a tuple. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingmap() + int + split() + tuple()**  
This method can be used to solve this particular task. In this, we just split
each element of string and convert to list and then we convert the list to
resultant tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to Tuple

# using map() + tuple() + int + split()

 

# initialize string

test_str = "1, -5, 4, 6, 7"

 

# printing original string 

print("The original string : " + str(test_str))

 

# Convert String to Tuple

# using map() + tuple() + int + split()

res = tuple(map(int, test_str.split(', ')))

 

# printing result

print("Tuple after getting conversion from String : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 1, -5, 4, 6, 7
    Tuple after getting conversion from String : (1, -5, 4, 6, 7)
    

**Method #2 : Usingeval()**  
This is the shorthand to perform this task. This converts the string to
desired tuple internally.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to Tuple

# Using eval()

 

# initialize string

test_str = "1, -5, 4, 6, 7"

 

# printing original string 

print("The original string : " + str(test_str))

 

# Convert String to Tuple

# Using eval()

res = eval(test_str)

 

# printing result

print("Tuple after getting conversion from String : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : 1, -5, 4, 6, 7
    Tuple after getting conversion from String : (1, -5, 4, 6, 7)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

