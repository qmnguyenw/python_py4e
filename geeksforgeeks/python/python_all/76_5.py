Python – Phrase extraction in String



Sometimes, while working with Python strings, we can have a problem in which
we need to extract certain words in a string excluding the initial and rear K
words. This can have application in many domains including all those include
data. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +enumerate() \+ list slicing**  
The combination of above methods can be used to solve this problem. In this,
we extract the indices of spaces and perform the slicing according to space
indices.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Phrase extraction in String

# Using list comprehension + enumerate() + list slicing

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks and CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# Phrase extraction in String

# Using list comprehension + enumerate() + list slicing

temp = [idx for idx, ele in enumerate(test_str) if ele
== ' ']

res = test_str[temp[K - 1]: temp[-(K - 1)]].strip()

 

# printing result 

print("String after phrase removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks and CS
    String after phrase removal : best for geeks and
    

**Method #2 : Usingjoin() + split()**  
The combination of above methods can be used to perform this task. In this, we
split all words and join all the words except the initial and rear K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Phrase extraction in String

# Using join() + split()

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks and CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 2

 

# Phrase extraction in String

# Using join() + split()

res = ' '.join(test_str.split()[K:-(K - 1)])

 

# printing result 

print("String after phrase removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks and CS
    String after phrase removal : best for geeks and
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

