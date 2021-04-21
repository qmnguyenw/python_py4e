Python – Extract ith Key’s Value of K’s Maximum value dictionary



Given Dictionary List, extract i’th keys value depending upon Kth key’s
maximum value.

>  **Input** : test_list = [{“Gfg” : 3, “is” : 9, “best” : 10}, {“Gfg” : 8,
> “is” : 11, “best” : 19}, {“Gfg” : 9, “is” : 16, “best” : 1}], K = “best”, i
> = “is”  
>  **Output** : 11  
>  **Explanation** : best is max at 19, its corresponding “is” value is 11.
>
>  **Input** : test_list = [{“Gfg” : 3, “is” : 9, “best” : 10}, {“Gfg” : 8,
> “is” : 11, “best” : 19}, {“Gfg” : 9, “is” : 16, “best” : 1}], K = “Gfg”, i =
> “is”  
>  **Output** : 16  
>  **Explanation** : Gfg is max at 9, its corresponding “is” value is 16.

 **Method #1 : Using max() + lambda**

The combination of above functions can be used to solve this problem. In this,
we extract max of kth key using max() and lambda. Then ith key is extracted
from extracted dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract ith Key's Value of K's Maximum value dictionary

# Using max() + lambda

 

# initializing lists

test_list = [{"Gfg" : 3, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 9, "is" : 16, "best" : 1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "best"

 

# initializing i 

i = "Gfg"

 

# using get() to handle missing key, assigning lowest value

res = max(test_list, key = lambda ele : ele.get(K, 0))[i]

 

# printing result 

print("The required value : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 9, 'is': 16, 'best': 1}]
    The required value : 8
    

**Method #2 : Using max() + external function**

This is yet another way to solve this problem. This computes in similar way as
above method, just the difference being of usage of custom comparator rather
than lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract ith Key's Value of K's Maximum value dictionary

# Using max() + external function

 

# custom function as comparator

def cust_fnc(ele):

 return ele.get(K, 0) 

 

# initializing lists

test_list = [{"Gfg" : 3, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 9, "is" : 16, "best" : 1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "best"

 

# initializing i 

i = "Gfg"

 

# using get() to handle missing key, assigning lowest value

res = max(test_list, key = cust_fnc)[i]

 

# printing result 

print("The required value : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 9, 'is': 16, 'best': 1}]
    The required value : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

