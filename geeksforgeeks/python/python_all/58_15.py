Python – Eliminate Capital Letter Starting words from String



Sometimes, while working with Python Strings, we can have a problem in which
we need to remove all the words with begin with capital letters. Words which
begin with capital letters are proper nouns and their occurrence mean
different meaning to sentence and can be sometimes undesired. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_str = ‘GeeksforGeeks is best for Geeks’  
>  **Output** : ‘ is best for ‘
>
>  **Input** : test_str = ‘GeeksforGeeks Is Best For Geeks’  
>  **Output** : ”

 **Method #1 : Usingjoin() + split() + isupper()**  
The combination of above functions can provide one of the way in which this
problem can be solved. In this, we perform the task of extracting individual
strings with upper case using isupper() and then perform join() to get the
resultant result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Eliminate Capital Letter Starting words from String

# Using join() + split() + isupper()

 

# initializing string

test_str = 'GeeksforGeeks is Best for Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Eliminate Capital Letter Starting words from String

# Using join() + split() + isupper()

temp = test_str.split()

res = " ".join([ele for ele in temp if not
ele[0].isupper()])

 

# printing result 

print("The filtered string : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original string is : GeeksforGeeks is Best for Geeks
    The filtered string : is for
    

