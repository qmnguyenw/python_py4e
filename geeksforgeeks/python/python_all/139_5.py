Python | Prefix extraction before specific character



Sometimes, we might have a use case in which we need to find a prefix in
string. But sometimes, the requirement can be something dynamic like a
specific input character than number of elements for the decision of getting
prefix.  
Let’s discuss certain ways in which we can find prefix of string before a
certain character.

 **Method #1 : Usingrsplit()**  
This method originally performs the task of splitting the string from the rear
end rather than the conventional left to right fashion. This can though be
limited to 1, for solving this particular problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix extraction before specific character

# Using rsplit()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# initializing split character

spl_char = "r"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using rsplit()

# Prefix extraction before specific character

res = test_str.rsplit(spl_char, 1)[0]

 

# printing result 

print("The prefix string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The prefix string is : Geeksfo
    

**Method #2 : Usingrpartition()**  
If we need to solve this particular problem, this inbuilt function is
recommended to perform this particular task. This function performs the
partition as required just once from the rear end.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix extraction before specific character

# Using rpartition()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# initializing split character

spl_char = "r"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using rpartition()

# Prefix extraction before specific character

res = test_str.rpartition(spl_char)[0]

 

# printing result 

print("The prefix string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The prefix string is : Geeksfo
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

