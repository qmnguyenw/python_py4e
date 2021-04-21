Python – Convert dictionary to K sized dictionaries



Given a Dictionary, divide dictionary into K sized different dictionaries
list.

>  **Input** : test_dict = {‘Gfg’ : 1, ‘is’ : 2, ‘best’ : 3, ‘for’ : 4,
> ‘geeks’ : 5, ‘CS’ : 6}, K = 3  
>  **Output** : [{‘Gfg’: 1, ‘is’: 2, ‘best’: 3}, {‘for’: 4, ‘geeks’: 5, ‘CS’:
> 6}]  
>  **Explanation** : Divided into size of 3 keys.
>
>  **Input** : test_dict = {‘Gfg’ : 1, ‘is’ : 2, ‘best’ : 3, ‘for’ : 4}, K = 2  
>  **Output** : [{‘Gfg’: 1, ‘is’: 2}, {‘best’: 3, ‘for’: 4}]  
>  **Explanation** : Divided into size of 2 keys.

 **Method : Using loop**

In this, we iterate for all the keys in dictionary using loop and bifurcate
according to size and append to new list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert dictionary to K Keys dictionaries

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'geeks' : 5, 'CS' : 6}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 2

 

res = []

count = 0

flag = 0

indict = dict()

for key in test_dict:

 indict[key] = test_dict[key] 

 count += 1

 

 # checking for K size and avoiding empty dict using flag

 if count % K == 0 and flag:

 res.append(indict)

 

 # reinitializing dictionary

 indict = dict()

 count = 0

 flag = 1

 

 

# printing result 

print("The converted list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'geeks': 5, 'CS': 6}
    The converted list : [{'Gfg': 1, 'is': 2}, {'best': 3, 'for': 4}, {'geeks': 5, 'CS': 6}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

