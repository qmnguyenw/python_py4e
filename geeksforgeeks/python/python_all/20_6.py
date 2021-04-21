Python – Create a string made of the first and last two characters from a
given string



Here we are going to see the approach of forming a string made from the first
and last 2 characters of a given string.

    
    
     **Input:** Geeksforgeeks
    **Output:** Geks
    
    **Input:** Hi, There
    **Output:** Hire
    

**Method #1:** Using list slicing

In this example, we are going to loop through the string and store the length
of the string in the count variable and then make the new substring by taking
the first 2 characters and the last two characters with the help of the count
variable.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Taking input from the user

inputString = "Geeksforgeeks"

 

count = 0

 

# Loop through the string

for i in inputString:

 count = count + 1

newString = inputString[ 0:2 ] + inputString [count -
2: count ] 

 

# Printing the new String

print("Input string = " + inputString)

print("New String = "+ newString)  
  
---  
  
 __

 __

 **Output:**

    
    
    Input string = Geeksforgeeks
    New String = Geks
    

**Methods #2:** Using a loop

  

  

In this example we are going to store the length of the string in a variable
and break the loop if its length is less than 4 characters otherwise we will
store the characters if the variable matches the defined conditions and make a
new string out of it.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Taking input from user

inputString = "Geeksforgeeks"

 

l = len(inputString)

newString = ""

 

# looping through the string

for i in range(0, len(inputString)):

 if l < 3:

 break

 else:

 if i in (0, 1, l-2, l-1):

 newString = newString + inputString[i]

 else:

 continue

 

# Printing New String

print("Input string : " + inputString)

print("New String : " + newString)  
  
---  
  
 __

 __

 **Output:**

    
    
    Input string : Geeksforgeeks
    New String : Geks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

