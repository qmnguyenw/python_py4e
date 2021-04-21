Python | Split given string into equal halves



Sometimes, we need to simply divide the string into two equal halves. This
type of application can occur in various domain ranging from simple
programming to web development. Let’s discuss certain ways in which this can
be performed.

 **Method #1 : Using list comprehension + String slicing**  
This is the naive method to perform this particular task. In this we just use
brute divisions and slicing to separate first and last part of string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting string into equal halves

# Using list comprehension + string slicing

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using list comprehension + string slicing

# Splitting string into equal halves

res_first = test_str[0:len(test_str)//2]

res_second = test_str[len(test_str)//2 if
len(test_str)%2 == 0

 else ((len(test_str)//2)+1):]

 

# printing result 

print("The first part of string : " + res_first)

print("The second part of string : " + res_second)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The first part of string : Geeksf
    The second part of string : rGeeks
    

**Method #2 : Using string slicing**  
To overcome the shortcomings of above method and find a more elegant solution,
we use string slicing to perform this particular task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Splitting string into equal halves

# Using string slicing

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using string slicing

# Splitting string into equal halves

res_first, res_second = test_str[:len(test_str)//2], 

 test_str[len(test_str)//2:]

 

# printing result 

print("The first part of string : " + res_first)

print("The second part of string : " + res_second)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The first part of string : Geeksf
    The second part of string : orGeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

