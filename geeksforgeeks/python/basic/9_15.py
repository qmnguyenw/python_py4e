String Slicing in Python



 **Python slicing** is about obtaining a sub-string from the given string by
slicing it respectively from start to end.  
Python slicing can be done in two ways.

  * slice() Constructor
  * Extending Indexing

#### slice() Constructor

The slice() constructor creates a slice object representing the set of
indices specified by range(start, stop, step).

>  **Syntax:**
>
>   * slice(stop)
>   * slice(start, stop, step)
>

>
>  **Parameters:**  
>  **start:** Starting index where the slicing of object starts.  
>  **stop:** Ending index where the slicing of object stops.  
>  **step:** It is an optional argument that determines the increment between
> each index for slicing.
>
>  **Return Type:** Returns a sliced object containing elements in the given
> range only.
>
>  
>
>
>  
>

 **Index tracker for positive and negative index:**  
Negative comes into considers when tracking the string in reverse.

![python-string-slice](https://media.geeksforgeeks.org/wp-
content/uploads/20191220092949/slice.jpg)

 **Example**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string slicing

 

# String slicing 

String ='ASTRING'

 

# Using slice constructor

s1 = slice(3)

s2 = slice(1, 5, 2) 

s3 = slice(-1, -12, -2)

 

print("String slicing") 

print(String[s1]) 

print(String[s2]) 

print(String[s3])  
  
---  
  
 __

 __

 **Output:**

    
    
    String slicing
    AST
    SR
    GITA
    

#### Extending indexing

In Python, indexing syntax can be used as a substitute for the slice object.
This is an easy and convenient way to slice a string both syntax wise and
execution wise.

 **Syntax**

    
    
    string[start:end:step]

start, end and step have the same mechanism as slice() constructor.

 **Example**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string slicing

 

# String slicing 

String ='ASTRING'

 

# Using indexing sequence

print(String[:3])

print(String[1:5:2])

print(String[-1:-12:-2])

 

# Prints string in reverse 

print("\nReverse String")

print(String[::-1])  
  
---  
  
 __

 __

 **Output:**

    
    
    AST
    SR
    GITA
    
    Reverse String
    GNIRTSA
    

**Note:** To know more about strings click here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

