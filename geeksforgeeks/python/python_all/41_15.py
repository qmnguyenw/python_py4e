Python – Filter Strings combination of K substrings



Given a Strings list, extract all the strings that are combination of K
substrings.

>  **Input** : test_list = [“geeks4u”, “allbest”, “abcdef”], substr_list =
> [“s4u”, “est”, “al”, “ge”, “ek”, “def”], K = 3  
>  **Output** : [‘geeks4u’]  
>  **Explanation** : geeks4u made up of 3 substr – ge, ek and s4u.
>
>  **Input** : test_list = [“geeks4u”, “allbest”, “abcdef”], substr_list =
> [“s4u”, “est”, “al”, “ge”, “def”, ‘lb’], K = 3  
>  **Output** : [‘allbest’]  
>  **Explanation** : allbest made up of 3 substr – al, lb and est.

 **Method #1 : Using permutations() + map() + join() + set() + loop**

In this, we perform this task by getting all possible permutation of K
substrings from substring list, and then perform task of join using join and
map(). The set() is used to avoid duplication. At last, match from Strings
list is done using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Strings combination of K substrings

# Using permutations() + map() + join() + set() + loop

from itertools import permutations

 

# initializing list

test_list = ["geeks4u", "allbest", "abcdef"]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing substring list

substr_list = ["s4u", "est", "al", "ge", "ek",
"def", "lb"]

 

# initializing K 

K = 3

 

# getting all permutations

perms = list(set(map(''.join, permutations(substr_list, r =
K))))

 

# using loop to check permutations with list

res = []

for ele in perms:

 if ele in test_list:

 res.append(ele)

 

# printing results 

print("Strings after joins : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeks4u', 'allbest', 'abcdef']
    Strings after joins : ['geeks4u', 'allbest']
    

**Method #2 : Using intersection()**

This uses all functions of above method, the last task of matching permutation
list and original list is done by intersection.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Strings combination of K substrings

# Using permutations() + map() + join() + set() + intersection()

from itertools import permutations

 

# initializing list

test_list = ["geeks4u", "allbest", "abcdef"]

 

# printing string

print("The original list : " + str(test_list))

 

# initializing substring list

substr_list = ["s4u", "est", "al", "ge", "ek",
"def", "lb"]

 

# initializing K 

K = 3

 

# getting all permutations

perms = set(map(''.join, permutations(substr_list, r = K)))

 

# using intersection() to solve this problem 

res = list(set(test_list).intersection(perms))

 

# printing results 

print("Strings after joins : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['geeks4u', 'allbest', 'abcdef']
    Strings after joins : ['geeks4u', 'allbest']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

