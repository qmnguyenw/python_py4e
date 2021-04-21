Break a list into chunks of size N in Python



 **Method 1: Using _yield_**  
The yield keyword enables a function to comeback where it left off when it is
called again. This is the critical difference from a regular function. A
regular function cannot comes back where it left off. The yield keyword helps
a function to remember its state. The yield enables a function to suspend and
resume while it turns in a value at the time of the suspension of the
execution.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['geeks', 'for', 'geeks', 'like',

 'geeky','nerdy', 'geek', 'love',

 'questions','words', 'life']

 

# Yield successive n-sized

# chunks from l.

def divide_chunks(l, n):

 

 # looping till length l

 for i in range(0, len(l), n): 

 yield l[i:i + n]

 

# How many elements each

# list should have

n = 5

 

x = list(divide_chunks(my_list, n))

print (x)  
  
---  
  
 __

 __

Output:

    
    
    [['geeks', 'for', 'geeks', 'like', 'geeky'], 
     ['nerdy', 'geek', 'love', 'questions', 'words'], 
     ['life']]
    

**Method 2: Using List comprehension**  
List comprehension is an elegant way to break a list in one line of code.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= [1, 2, 3, 4, 5,

 6, 7, 8, 9]

 

# How many elements each

# list should have

n = 4

 

# using list comprehension

final = [my_list[i * n:(i + 1) * n] for i in
range((len(my_list) + n - 1) // n )] 

print (final)  
  
---  
  
 __

 __

Output:

    
    
    [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
    

**Alternate Implementation :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

l= [1, 2, 3, 4, 5, 6, 7, 8, 9] 

 

# How many elements each 

# list should have 

n = 4

 

# using list comprehension 

x = [l[i:i + n] for i in range(0, len(l), n)] 

print(x)  
  
---  
  
 __

 __

Output:

    
    
    [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

