Python program to find the sum of all items in a dictionary



Given a dictionary in Python, write a Python program to find the sum of all
Items in the dictionary.

 **Examples:**

    
    
    **Input :** {'a': 100, 'b':200, 'c':300}
    **Output :** 600
    
    **Input :** {'x': 25, 'y':18, 'z':45}
    **Output :** 88
    

  * **Approach #1 :** Using Inbuilt sum() Function

Use sum function to find the sum of dictionary values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to find sum of

# all items in a Dictionary

 

# Function to print sum

def returnSum(myDict):

 

 sum = 0

 for i in myDict:

 sum = sum + myDict[i]

 

 return sum

 

# Driver Function

dict = {'a': 100, 'b':200, 'c':300}

print("Sum :", returnSum(dict))  
  
---  
  
 __

 __

 **Output:**

    
        Sum : 600

  *  **Approach #2 :** Using For loop to iterate through values using values() function

Iterate through each value of the dictionary using values() function and
keep adding it to the sum.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to find sum of

# all items in a Dictionary

 

# Function to print sum

def returnSum(dict):

 

 sum = 0

 for i in dict.values():

 sum = sum + i

 

 return sum

 

# Driver Function

dict = {'a': 100, 'b':200, 'c':300}

print("Sum :", returnSum(dict))  
  
---  
  
 __

 __

 **Output:**

    
        Sum : 600

  *  **Approach #3 :** Using For loop to iterate through items of Dictionary

Iterate through each item of the dictionary and simply keep adding the values
to the sum variable.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to find sum of

# all items in a Dictionary

 

# Function to print sum

def returnSum(dict):

 

 sum = 0

 for i in myDict:

 sum = sum + dict[i]

 

 return sum

 

# Driver Function

dict = {'a': 100, 'b':200, 'c':300}

print("Sum :", returnSum(dict))  
  
---  
  
 __

 __

 **Output:**

    
        Sum : 600

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

