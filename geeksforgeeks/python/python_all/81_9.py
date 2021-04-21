Python | Replace characters after K occurrences



Sometimes, while working with Python strings, we can have problem in which we
need to perform replace of characters after certain repetitions of characters.
This can have application in many domains including day-day and competitive
programming.

 **Method #1 : Using loop + string slicing**  
This is brute force way in which this problem can be solved. In this, we run a
loop on string and keep track of occurrences and perform replace when above K
occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace characters after K occurrences

# Using loop + string slices

 

# initializing string

test_str = "geeksforgeeks is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 2

 

# initializing Repl char

repl_char = "*"

 

# Replace characters after K occurrences

# Using loop + string slices

for sub in set(test_str):

 for idx in [idx for idx in range(len(test_str)) if
test_str[idx] == sub][K:]:

 test_str = test_str[:idx] + repl_char + test_str[idx +
1:]

 

# printing result 

print("The string after performing replace : " + test_str)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The string after performing replace : geeksforg**ks i* b**t*for******
    

**Method #2 : Usingjoin() + count() + enumerate()**  
This is shorthand by which this task can be performed. In this, we employ
count() to check for the count of strings and join() and enumerate() can be
used to perform the task of new string construction.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace characters after K occurrences

# Using join() + count() + enumerate()

 

# initializing string

test_str = "geeksforgeeks is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 2

 

# initializing Repl char

repl_char = "*"

 

# Replace characters after K occurrences

# Using join() + count() + enumerate()

res = "".join(chr if test_str.count(chr, 0, idx) < K

 else repl_char for idx, chr in enumerate(test_str))

 

# printing result 

print("The string after performing replace : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The string after performing replace : geeksforg**ks i* b**t*for******
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

