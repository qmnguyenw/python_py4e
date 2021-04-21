Python program to Concatenate Kth index words of String



Given a string with words, concatenate Kth index of each word.

>  **Input** : test_str = ‘geeksforgeeks best geeks’, K = 3  
> **Output** : ktk  
> **Explanation** : 3rd index of “geeksforgeeks” is k, “best” has ‘t’ as 3rd
> element.
>
>  **Input** : test_str = ‘geeksforgeeks best geeks’, K = 0  
> **Output** : gbg

**Method #1 : Using join() + list comprehension + split()**

In this, we perform the task of splitting to get all the words and then use
list comprehension to get all Kth index of words, join() is used to perform
concatenation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksforgeeks best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 2

 

# joining Kth index of each word

res = ''.join([sub[K] for sub in test_str.split()])

 

# printing result 

print("The K joined String is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks best for geeks
    The K joined String is : esre
    

**Method #2 : Using loop + join()**

In this, we perform the task of getting the Kth index elements using a loop in
a brute-force manner and then concatenating using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksforgeeks best for geeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 2

 

# getting Kth element of each word

temp = []

for sub in test_str.split():

 temp.append(sub[K])

 

# joining together 

res = ''.join(temp)

 

# printing result 

print("The K joined String is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks best for geeks
    The K joined String is : esre
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

