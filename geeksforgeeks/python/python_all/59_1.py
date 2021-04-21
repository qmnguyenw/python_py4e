Python – Check if two strings are Rotationally Equivalent



Sometimes, while working with Python Strings, we can have problem in which we
need to check if one string can be derived from other upon left or right
rotation. This kind of problem can have application in many domains such as
web development and competitive programming. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_str1 = ‘GFG’, test_str2 = ‘FGG’  
>  **Output** : True
>
>  **Input** : test_str1 = ‘geeks’, test_str2 = ‘ksege’  
>  **Output** : False

 **Method #1 : Using loop + string slicing**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting strings for performing all possible
rotations, to check if any rotation equals the other string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if two strings are Rotationally Equivalent

# Using loop + string slicing

 

# initializing strings

test_str1 = 'geeks'

test_str2 = 'eksge'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# Check if two strings are Rotationally Equivalent

# Using loop + string slicing

res = False

for idx in range(len(test_str1)):

 if test_str1[idx: ] + test_str1[ :idx] == test_str2:

 res = True

 break

 

# printing result 

print("Are two strings Rotationally equal ? : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original string 1 is : geeks
    The original string 2 is : eksge
    Are two strings Rotationally equal ? : True
    

