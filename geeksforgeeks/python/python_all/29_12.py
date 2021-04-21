Python – Sort by Factor count



Given element list, sort by factor count of each element.

>  **Input** : test_list = [12, 100, 22]  
> **Output** : [22, 12, 100]  
> **Explanation** : 3, 5, 8 factors respectively of elements.
>
>  **Input** : test_list = [6, 11]  
> **Output** : [11, 6]  
> **Explanation** : 1, 4 factors respectively of elements.

**Method #1 : Using sort() + len() + list comprehension**

In this, we perform task of sorting using _sort()_ , and _len()_ and list
comprehension is used for task of getting the count of factors.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Factor count

# Using sort() + len() + list comprehension

 

 

def factor_count(ele):

 

 # getting factors count

 return len([ele for idx in range(1, ele) if ele %
idx == 0])

 

 

# initializing list

test_list = [12, 100, 360, 22, 200]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort

test_list.sort(key=factor_count)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

**Output:**

    
    
    The original list is : [12, 100, 360, 22, 200]
    Sorted List : [22, 12, 100, 200, 360]
    

**Method #2 : Using lambda + sorted() + len()**

In this, task of sorting is done using _sorted()_ , and lambda function is
used to feed to sorted to get factors.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Factor count

# Using lambda + sorted() + len()

 

# initializing list

test_list = [12, 100, 360, 22, 200]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort using sorted(), lambda getting factors

res = sorted(test_list, key=lambda ele: len(

 [ele for idx in range(1, ele) if ele % idx ==
0]))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [12, 100, 360, 22, 200]
    Sorted List : [22, 12, 100, 200, 360] 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

