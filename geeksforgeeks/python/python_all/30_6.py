Python – Extract dictionaries with values sum greater than K



Given a dictionaries list, extract all the dictionaries whose keys summation
exceeds K.

>  **Input** : test_list = [{“Gfg” : 4, “is” : 8, “best” : 9}, {“Gfg” : 3,
> “is”: 7, “best” : 5}], K = 15  
>  **Output** : [{‘Gfg’: 4, ‘is’: 8, ‘best’: 9}]  
>  **Explanation** : 4 + 9 + 8 = 21. Greater than K, hence returned.
>
>  **Input** : test_list = [{“Gfg” : 4, “is” : 8, “best” : 9}, {“Gfg” : 3,
> “is”: 7, “best” : 5}], K = 25  
>  **Output** : []  
>  **Explanation** : No dictionary with sum > 25.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the dictionaries and extract summation of each of them, which exceeds K,
we filter them out.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract dictionaries with values sum greater than K

# Using 

 

# initializing lists

test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},

 {"Gfg" : 5, "is": 8, "best" : 1},

 {"Gfg" : 3, "is": 7, "best" : 6}, 

 {"Gfg" : 3, "is": 7, "best" : 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 15

 

# using loop to extract all dictionaries

res = []

for sub in test_list:

 sum = 0

 for key in sub:

 sum += sub[key]

 if sum > K:

 res.append(sub)

 

# printing result 

print("Dictionaries with summation greater than K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 4, 'is': 8, 'best': 9}, {'Gfg': 5, 'is': 8, 'best': 1}, {'Gfg': 3, 'is': 7, 'best': 6}, {'Gfg': 3, 'is': 7, 'best': 5}]
    Dictionaries with summation greater than K : [{'Gfg': 4, 'is': 8, 'best': 9}, {'Gfg': 3, 'is': 7, 'best': 6}]
    

**Method #2 : Using list comprehension + sum()**

This is one liner way in which this task can be performed. In this, we perform
the task of summation using sum() and list comprehension can be used to
perform task of combining all the logic into single line.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract dictionaries with values sum greater than K

# Using list comprehension + sum()

 

# initializing lists

test_list = [{"Gfg" : 4, "is" : 8, "best" : 9},

 {"Gfg" : 5, "is": 8, "best" : 1},

 {"Gfg" : 3, "is": 7, "best" : 6}, 

 {"Gfg" : 3, "is": 7, "best" : 5}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 15

 

# using one-liner to extract all the dictionaries

res = [sub for sub in test_list if
sum(list(sub.values())) > K]

 

# printing result 

print("Dictionaries with summation greater than K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 4, 'is': 8, 'best': 9}, {'Gfg': 5, 'is': 8, 'best': 1}, {'Gfg': 3, 'is': 7, 'best': 6}, {'Gfg': 3, 'is': 7, 'best': 5}]
    Dictionaries with summation greater than K : [{'Gfg': 4, 'is': 8, 'best': 9}, {'Gfg': 3, 'is': 7, 'best': 6}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

