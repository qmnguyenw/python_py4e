Python – Equable Minimial Records



Sometimes, while working with Python records, we can have a problem in which
we need to extract one of the records that are equal to certain index, which
is mimimal of other index. This kind of problem occurs in domains such as web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(‘Gfg’, 13, 5), (‘is’, 13, 6), (‘best’, 13, 2), (‘CS’, 13, 2)]  
> eq_idx = 2, min_idx = 3  
>  **Output** : [(‘best’, 13, 2)]
>
>  **Input** :  
> test_list = [(‘Gfg’, 12, 5), (‘is’, 12, 6), (‘best’, 13, 2), (‘CS’, 13, 3)]  
> eq_idx = 2, min_idx = 3  
>  **Output** : [(‘Gfg’, 12, 5), (‘best’, 13, 2)]

 **Method #1 : Using list comprehension +min() + lambda**  
The combination of above functions can be used to solve this problem. In this,
we use min() to extract the minimum index value, and list comprehension and
lambda functions are used to perform the task of grouping elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equable Minimial Records

# Using min() + list comprehension + lambda

 

# initializing list

test_list = [('Gfg', 12, 5), ('is', 13, 6),
('best', 12, 2), ('CS', 13, 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Equate index 

eq_idx = 2

 

# initializing min index 

min_idx = 3

 

# Equable Minimial Records

# Using min() + list comprehension + lambda

res = [min((ele for ele in test_list if ele[eq_idx -
1] == sub),

 key = lambda a: int(a[min_idx - 1]))

 for sub in {b[eq_idx - 1] for b in test_list}]

 

 

# printing result 

print("Equable Minimal Records : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 12, 5), ('is', 13, 6), ('best', 12, 2), ('CS', 13, 2)]
    Equable Minimal Records : [('best', 12, 2), ('CS', 13, 2)]
    

