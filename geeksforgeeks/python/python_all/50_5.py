Python – Group concatenate Till K



Given list of strings, perform concatenation in groups till K.

>  **Input** : test_list = [“Gfg”, “is”, “Best”, “”, “I”, “Love”, “”, “Gfg”],
> K = “”  
>  **Output** : [‘Gfg is Best’, ‘I Love’, ‘Gfg’]  
>  **Explanation** : Concatenated words with “” as new String separator.
>
>  **Input** : test_list = [“Gfg”, “is”, “Best”, “”, “I”, “Love”], K = “”  
>  **Output** : [‘Gfg is Best’, ‘I Love’]  
>  **Explanation** : Concatenated words with “” as new String separator.

 **Method : Using loop + join() + list comprehension**

This is a way in which this task can be performed. In this, we construct parts
of strings into lists, and then perform join of individual lists using join()
and list comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group concatenate Till K 

# Using loop + join() + list comprehension

 

# initializing lists

test_list = ["Gfg", "is", "Best", None, "I",
"Love", None, "Gfg"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = None

 

# all() to encapsulate whole logic into one expression

res = [[]]

for sub in test_list:

 

 # checking for K value, and performing append to 

 # latest list 

 if sub != K:

 res[-1].append(sub)

 else:

 

 # constructing new list if new group

 res.append([])

 

# Joining all groups 

fin_res = [' '.join(ele) for ele in res]

 

# printing result 

print("Concatenated Groups : " + str(fin_res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', None, 'I', 'Love', None, 'Gfg']
    Concatenated Groups : ['Gfg is Best', 'I Love', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

