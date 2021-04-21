Python – Replace Elements greater than K



Given element list, replace all elements greater than K with given replace
character.

>  **Input** : test_list = [3, 4, 7, 5, 6, 7], K = 5, repl_chr = None  
>  **Output** : [3, 4, None, 5, None, None]  
>  **Explanation** : Characters are replaced by None, greater than 5.
>
>  **Input** : test_list = [3, 4, 7, 5, 6, 7], K = 4, repl_chr = None  
>  **Output** : [3, 4, None, None, None, None]  
>  **Explanation** : Characters are replaced by None, greater than 4.

 **Method #1 : Using loop**

In this, we check for elements greater than K, if found, they are replaced by
replace character, otherwise old value is retained.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Elements greater than K

# Using loop

 

# initializing list

test_list = [3, 4, 7, 5, 6, 7, 3, 4,
6, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# initializing repl_chr 

repl_chr = "NA"

 

res = []

for ele in test_list:

 

 # replace if greater than K

 if ele > K :

 res.append(repl_chr)

 else :

 res.append(ele)

 

# printing result 

print("The replaced list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]
    The replaced list : [3, 4, 'NA', 5, 'NA', 'NA', 3, 4, 'NA', 'NA']
    

**Method #2 : Using list comprehension**

This is one liner way to solve this problem. Similar method as above, just
using one liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Elements greater than K

# Using list comprehension

 

# initializing list

test_list = [3, 4, 7, 5, 6, 7, 3, 4,
6, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 5

 

# initializing repl_chr 

repl_chr = "NA"

 

# one liner to solve problem

res = [repl_chr if ele > K else ele for ele in
test_list]

 

# printing result 

print("The replaced list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]
    The replaced list : [3, 4, 'NA', 5, 'NA', 'NA', 3, 4, 'NA', 'NA']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

