Python – Group Similar items to Dictionary Values List



Given a list of elements, perform grouping of similar elements, as different
key-value list in dictionary.

>  **Input** : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]  
>  **Output** : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}  
>  **Explanation** : Similar items grouped together on occurrences.
>
>  **Input** : test_list = [7, 7, 7, 7]  
>  **Output** : {7 : [7, 7, 7, 7]}  
>  **Explanation** : Similar items grouped together on occurrences.

 **Method #1 : Using defaultdict() + loop**

This is one of the ways in which this task can be performed. In this, we
construct a defaultdict() with default list and keep appending similar values
into similar list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Similar items to Dictionary Values List

# Using defaultdict + loop

from collections import defaultdict

 

# initializing list

test_list = [4, 6, 6, 4, 2, 2, 4, 4,
8, 5, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using defaultdict for default list 

res = defaultdict(list)

for ele in test_list:

 

 # appending Similar values

 res[ele].append(ele)

 

# printing result 

print("Similar grouped dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
    Similar grouped dictionary : {4: [4, 4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
    
    

**Method #2 : Using dictionary comprehension + Counter()**

This is yet another way in which this task can be performed. In this, we
extract frequency using Counter() and then repeat occurrences using
multiplication.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Similar items to Dictionary Values List

# Using dictionary comprehension + Counter()

from collections import Counter

 

# initializing list

test_list = [4, 6, 6, 4, 2, 2, 4, 4,
8, 5, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using * operator to perform multiplication

res = {key : [key] * val for key, val in
Counter(test_list).items()}

 

# printing result 

print("Similar grouped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
    Similar grouped dictionary : {4: [4, 4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

