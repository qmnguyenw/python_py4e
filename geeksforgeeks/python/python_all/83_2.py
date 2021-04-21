Python | Vowel indices in String



Sometimes, while working with Python Strings, we can have a problem in which
we need to extract indices of vowels in it. This kind of application is common
in day-day programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is one way in which this task can be performed. In this we use brute
force to perform this task. In this we iterate for each string element and
test for vowel.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Vowel indices in String

# Using loop

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Vowel indices in String

# Using loop

res = []

for ele in range(len(test_str)):

 if test_str[ele] in "aeiou":

 res.append(ele)

 

# printing result 

print("The vowel indices are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The vowel indices are : [1, 2, 6, 9, 10]
    

**Method #2 : Usingenumerate() \+ list comprehension**  
The combination of above methods can also be used to perform this task. In
this, we access the index using enumerate() and list comprehension is used to
check for vowels.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Vowel indices in String

# Using list comprehension + enumerate()

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Vowel indices in String

# Using list comprehension + enumerate()

res = [idx for idx, ele in enumerate(test_str) if ele in
"aeiou"]

 

# printing result 

print("The vowel indices are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The vowel indices are : [1, 2, 6, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

