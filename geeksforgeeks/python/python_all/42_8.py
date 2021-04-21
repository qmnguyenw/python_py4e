Python – Append according to Kth character



Given a String list, append to String i or j value depending on Kth index
value.

>  **Input** : test_list = [“geeksforgeeks”, “best”, “for”, “geeks”], K = 2, N
> = ‘e’, i, j = “@@”, “..”  
>  **Output** : [‘geeksforgeeks..’, ‘best@@’, ‘for@@’, ‘geeks..’]  
>  **Explanation** : geeksforgeeks and geeks having similar 2nd occ. value as
> ‘e’, hence gets appended by “..”.
>
>  **Input** : test_list = [“giiksforgeeks”, “bst”, “for”, “geeks”], K = 2, N
> = ‘e’, i, j = “@@”, “..”  
>  **Output** : [‘giiksforgeeks@@’, ‘best@@’, ‘for@@’, ‘geeks@@’]  
>  **Explanation** : No values with K value ‘e’, all appended by @@.

 **Method #1 : Using loop**

This is brute way to solve this problem, we check for each string’s Kth index,
if found to be N, then i value is appended else j is appended.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append according to Kth character

# Using loop

 

# initializing lists

test_list = ["geeksforgeeks", "best", "for", "geeks"]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing K

K = 2

 

# initializing N 

N = 'e'

 

# initializing i, j 

i, j = "**", "##"

 

res = []

for sub in test_list:

 

 # checking for Kth index to be N

 if sub[K] == N:

 res.append(sub + i)

 else :

 res.append(sub + j)

 

# printing results 

print("The resultant List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeksforgeeks', 'best', 'for', 'geeks']
    The resultant List : ['geeksforgeeks**', 'best##', 'for##', 'geeks**']
    

**Method #2 : Using list comprehension**

This solves this problem in similar manner, just difference being, it’s a
shorthand and can be used as one liner approach to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append according to Kth character

# Using list comprehension

 

# initializing lists

test_list = ["geeksforgeeks", "best", "for", "geeks"]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing K

K = 2

 

# initializing N 

N = 'e'

 

# initializing i, j 

i, j = "**", "##"

 

# shorthand to solve this problem

res = [sub + i if sub[K] == N else sub + j for
sub in test_list]

 

# printing results 

print("The resultant List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeksforgeeks', 'best', 'for', 'geeks']
    The resultant List : ['geeksforgeeks**', 'best##', 'for##', 'geeks**']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

