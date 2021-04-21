Python – Concatenate Strings in the Given Order



Given a String List and order list, perform string concatenation in specific
order.

>  **Input** : test_list = [“best”, “Gfg”, “for”, “is”], sort_order = [1, 3,
> 0, 2]  
> **Output** : Gfgisbestfor  
> **Explanation** : Combined as per order of indices.  
>  **Input** : test_list = [“best”, “Gfg”], sort_order = [1, 0]  
> **Output** : Gfgbest  
> **Explanation** : Combined as per order of indices.  
>

**Method #1 : Using loop**

In this, we iterate order elements in loop, and perform concatenation of
strings of similar index in similar order.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Strings in Order

# Using loop

 

# initializing list

test_list = ["best", "Gfg", "for", "is", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing join order 

sort_order = [1, 3, 0, 2, 4]

 

res = ''

for ordr in sort_order:

 

 # concatenating by order 

 res += test_list[ordr]

 

# printing result 

print("Ordered concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The original list is : ['best', 'Gfg', 'for', 'is', 'geeks']
    Ordered concatenation : Gfgisbestforgeeks
    
    

