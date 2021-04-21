Python – Maximum available value Dictionaries



Given list of dictionaries and a list, extract all the dictionaries which
contain maximum available value of key from list.

>  **Input** : test_list [{“Gfg” : 6, “is” : 9, “best” : 10},  
> {“Gfg” : 8, “is” : 11, “best” : 19},  
> {“Gfg” : 2, “is” : 16, “best” : 10}], K = “best”, arg_list = [10, 7, 6, 12]  
>  **Output** : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}, {‘Gfg’: 2, ‘is’: 16, ‘best’:
> 10}]  
>  **Explanation** : Maximum available value of “best” is 19, but not present
> in list, hence next max. is 10, all dictionaries corresponding are returned.
>
>  **Input** : test_list [{“Gfg” : 6, “is” : 9, “best” : 10},  
> {“Gfg” : 8, “is” : 11, “best” : 19}], K = “Gfg”, arg_list = [10, 7, 6, 12]  
>  **Output** : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}]  
>  **Explanation** : Maximum value present in this case is 6, hence returned.

 **Method #1 : Using loop**

This is brute way in which this problem can be solved. In this, first maximum
value is obtained from dictionary values, which is also present in provided
list. Post that all the dictionaries, which have that value are extracted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum available value Dictionaries

# Using loop

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "best"

 

# initializing list 

arg_list = [10, 7, 6, 12]

 

# extracting value to find from dictionary

# corresponding to key 

max_ele = 0

for sub in test_list:

 if sub[K] in arg_list:

 

 # maximum of all possible present for a key

 max_ele = max(sub[K], max_ele)

 

# extracting dictionary with maximum and present value of key 

res = [sub for sub in test_list if sub[K] == max_ele]

 

# printing result 

print("The extracted dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}, {‘Gfg’: 8, ‘is’: 11,
> ‘best’: 19}, {‘Gfg’: 2, ‘is’: 16, ‘best’: 10}, {‘Gfg’: 12, ‘is’: 1, ‘best’:
> 8}, {‘Gfg’: 22, ‘is’: 6, ‘best’: 8}]  
> The extracted dictionaries : [{‘Gfg’: 6, ‘is’: 9, ‘best’: 10}, {‘Gfg’: 2,
> ‘is’: 16, ‘best’: 10}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

