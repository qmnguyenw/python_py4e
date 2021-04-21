Python | Reverse Slicing of given string



Sometimes, while working with strings we might have a problem in which we need
to perform the reverse slicing of string, i.e slicing the string for certain
characters from the rear end. Let’s discuss certain ways in which this can be
done.

 **Method #1 : Usingjoin() + reversed()**  
The combination of above function can be used to perform this particular task.
In this, we reverse the string in memory and join the sliced no. of characters
so as to return the string sliced from rear end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Slicing string 

# Using join() + reversed()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing K 

K = 7

 

# Using join() + reversed()

# Reverse Slicing string 

res = ''.join(reversed(test_str[0:K]))

 

# printing result 

print("The reversed sliced string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The reversed sliced string is : ofskeeG
    

**Method #2 : Using string slicing**  
The string slicing can be used to perform this particular task, by using “-1”
as the third argument in slicing we can make function perform the slicing from
rear end hence proving to be a simple solution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reverse Slicing string 

# Using string slicing

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing K 

K = 7

 

# Using string slicing

# Reverse Slicing string 

res = test_str[(K-1)::-1]

 

# printing result 

print("The reversed sliced string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The reversed sliced string is : ofskeeG
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

