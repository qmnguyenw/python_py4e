Python – Count of Words with specific letter



Given a string of words, extract count of words with specific letter.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, letter = “g”  
>  **Output** : 2  
>  **Explanation** : “g” occurs in 2 words.
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, letter = “s”  
>  **Output** : s  
>  **Explanation** : “s” occurs in 4 words.

 **Method #1 : Using list comprehension + len() + split()**

This is one of the ways in which this task can be performed. In this, we
perform task of extracting words from string using split() and loop is used to
iterate words to check for letter existence of letter and len() is used to
fetch the number of words with letter.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count of Words with specific letter

# Using list comprehension + len() + split()

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing letter 

letter = "e"

 

# extracting desired count using len()

# list comprehension is used as shorthand

res = len([ele for ele in test_str.split() if letter in
ele])

 

# printing result 

print("Words count : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    Words count : 3
    

**Method #2 : Using filter() + lambda + len() + split()**

This is yet another way in which this task can be performed. In this, we
perform the task of filtering using filter() + lambda.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count of Words with specific letter

# Using filter() + lambda + len() + split()

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing letter 

letter = "e"

 

# extracting desired count using len()

# filter() used to check for letter existence

res = len(list(filter(lambda ele : letter in ele,
test_str.split())))

 

# printing result 

print("Words count : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    Words count : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

