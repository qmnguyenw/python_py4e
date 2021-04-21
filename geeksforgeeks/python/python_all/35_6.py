Python – Longest Consecution without K in String



Given a String, find length of longest consecution, in which K doesn’t appear.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks’, K = ‘e’  
>  **Output** : 9  
>  **Explanation** : from s in best to e in geeks, 9th letter is “e”.
>
>  **Input** : test_str = ‘geeksforgeeks’, K = ‘e’  
>  **Output** : 7  
>  **Explanation** : from k to e, 7th letter is e, longest run.

 **Method #1 : Using loop**

We perform this in 2 steps, in 1st we iterate for all elements to get indices
of K, and then in next step find the maximum difference between consecutive
characters.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Consecution without K in String

# Using loop

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'e'

 

# getting all indices 

indxs = []

for idx, ele in enumerate(test_str):

 if ele == 'e':

 indxs.append(idx)

 

# getting difference 

diffs = []

for idx in range(len(indxs) - 1):

 diffs.append(indxs[idx + 1] - indxs[idx])

 

# getting max diff using max()

res = max(diffs)

 

# printing result 

print("Longest run : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    Longest run : 9
    

**Method #2 : Using filter() + lambda + zip() + list comprehension + max()**

In this, we get index of K elements using filter() + lambda and zip() + list
comprehension is used to get differences between indices. Post that, max() is
used for extracting maximum difference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Longest Consecution without K in String

# Using filter() + lambda + zip() + list comprehension + max()

 

# initializing string

test_str = 'geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 'e'

 

# getting all indices using filter + lambda

indxs = list(filter(lambda ele: test_str[ele] == 'e',
range(len(test_str)))) 

 

# getting difference using zip()

# negative index, for getting successive elements 

diffs = [j - i for i, j in zip(indxs[: -1],
indxs[1 :])] 

 

# getting max diff 

res = max(diffs)

 

# printing result 

print("Longest run : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks
    Longest run : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

