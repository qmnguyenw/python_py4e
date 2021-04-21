Python – Remove Punctuation Tuples



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform the removal of all the tuples which contain punctuation in
tuples. This kind of problem can occur in data filtering applications. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(‘.’, ‘, ‘), (‘!’, 8)]  
>  **Output** : []
>
>  **Input** : test_list = [(1, 3), (3, 8)]  
>  **Output** : [(1, 3), (3, 8)]

 **Method #1 : Usingany() + list comprehension + string.punctuation**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of identifying punctuation using string.punctuations, and
any() is used to test if the elements belong to any of punctuation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Punctuation Tuples

# Using any() + list comprehension + string.punctuation

import string

 

# initializing list

test_list = [('.', ', '), ('!', 8), (5, 6),
(';', 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove Punctuation Tuples

# Using any() + list comprehension + string.punctuation

res = [idx for idx in test_list if not any(punc in
idx 

 for punc in string.punctuation)]

 

# printing result 

print("Tuples after punctuation removal : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('.', ', '), ('!', 8), (5, 6), (';', 10)]
    Tuples after punctuation removal : [(5, 6)]
    

