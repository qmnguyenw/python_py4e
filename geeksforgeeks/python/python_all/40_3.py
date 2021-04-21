Python – Dictionary with maximum count of pairs



Given dictionary list, extract dictionary with maximum keys.

>  **Input** : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2, “is” : 3,
> “best” : 4, “CS” : 9}, {“gfg”: 2}]  
>  **Output** : 4  
>  **Explanation** : 2nd dictionary has maximum keys, 4.
>
>  **Input** : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2}]  
>  **Output** : 2  
>  **Explanation** : 1st dictionary has maximum keys, 2.

 **Method #1 : Using len() + loop**

In this, we iterate for each of dictionary and compare lengths of each, record
and return one with maximum length.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary with maximum keys

# Using loop + len()

 

# initializing list

test_list = [{"gfg": 2, "best" : 4}, 

 {"gfg": 2, "is" : 3, "best" : 4}, 

 {"gfg": 2}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = {} 

max_len = 0

for ele in test_list:

 

 # checking for lengths

 if len(ele) > max_len: 

 res = ele

 max_len = len(ele)

 

# printing results

print("Maximum keys Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]
    Maximum keys Dictionary : {'gfg': 2, 'is': 3, 'best': 4}
    

**Method #2 : Using max() + key=len**

In this, we compute maximum length key using max() by passing additional key
“len” for comparison based on lengths.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary with maximum keys

# Using max() + key = len

 

# initializing list

test_list = [{"gfg": 2, "best" : 4}, 

 {"gfg": 2, "is" : 3, "best" : 4}, 

 {"gfg": 2}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# maximum length dict using len param

res = max(test_list, key = len)

 

# printing results

print("Maximum keys Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]
    Maximum keys Dictionary : {'gfg': 2, 'is': 3, 'best': 4}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

