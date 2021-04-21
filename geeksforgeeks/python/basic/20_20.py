Python dictionary | values()



 **values()** is an inbuilt method in Python programming language that returns
a list of all the values available in a given dictionary.

 **Syntax:**

    
    
    dictionary_name.values()

 **Parameters:**  
There are no parameters

 **Returns:**

    
    
    returns a list of all the values available in a given dictionary.
    the values have been stored in a **reversed** manner.

 **Error:**

  

  

    
    
    As we are not passing any parameters there
    is no scope for any error.

 **Code#1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for illustration

# of values() method of dictionary 

 

 

# numerical values

dictionary = {"raj": 2, "striver": 3, "vikram":
4}

print(dictionary.values()) 

 

 

# string values

dictionary = {"geeks": "5", "for": "3", "Geeks":
"5"}

print(dictionary.values())   
  
---  
  
__

__

**Output:**

    
    
    dict_values([2, 3, 4])
    dict_values(['5', '3', '5'])
    

**Practical Application:**  
Given name and salary, return the total salary of all employees.

 **Code#2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for illustration

# of values() method in finding total salary

 

 

# stores name and corresponding salaries

salary = {"raj" : 50000, "striver" : 60000, "vikram"
: 5000} 

 

# stores the salaries only

list1 = salary.values() 

print(sum(list1)) # prints the sum of all salaries  
  
---  
  
 __

 __

 **Output:**

    
    
    115000
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

