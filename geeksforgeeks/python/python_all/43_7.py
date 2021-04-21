Python – Check if Kth index elements are unique



Given a String list, check if all Kth index elements are unique.

>  **Input** : test_list = [“gfg”, “best”, “for”, “geeks”], K = 1  
>  **Output** : False  
>  **Explanation** : e occurs as 1st index in both best and geeks.
>
>  **Input** : test_list = [“gfg”, “best”, “geeks”], K = 2  
>  **Output** : True  
>  **Explanation** : g, s, e, all are unique.

 **Method #1 : Using loop**

This is brute way to solve this problem. In this, we iterate for each string
and flag off when any element is repeated, and return false.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Kth index elements are unique

# Using loop

 

# initializing list

test_list = ["gfg", "best", "for", "geeks"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

res = []

flag = True

for ele in test_list:

 

 # checking if element is repeated

 if ele[K] in res:

 flag = False

 break

 else:

 res.append(ele[K])

 

# printing result 

print("Is Kth index all unique : " + str(flag))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'best', 'for', 'geeks']
    Is Kth index all unique : True
    
    

**Method #2 : Using Counter() + all()**

In this, we count frequency of each char. at Kth index, and all() is used to
check if Counter is less than 2 for all.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Kth index elements are unique

# Using Counter() + all()

from collections import Counter

 

# initializing list

test_list = ["gfg", "best", "for", "geeks"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# getting count of each Kth index item

count = Counter(sub[K] for sub in test_list)

 

# extracting result 

res = all(val < 2 for val in count.values())

 

# printing result 

print("Is Kth index all unique : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'best', 'for', 'geeks']
    Is Kth index all unique : True
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

