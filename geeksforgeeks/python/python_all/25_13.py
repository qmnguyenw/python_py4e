Python – Sort Matrix by Row Median



Given a Matrix, sort by median of each row.

>  **Input** : test_list = [[3, 4, 7], [1, 7, 2], [10, 2, 4], [8, 6, 5]]  
> **Output** : [[1, 7, 2], [3, 4, 7], [10, 2, 4], [8, 6, 5]]  
> **Explanation** : 2 < 3 < 4 < 6, sorted increasingly by median element.
>
>  **Input** : test_list = [[3, 4, 7], [1, 7, 2], [8, 6, 5]]  
> **Output** : [[1, 7, 2], [3, 4, 7], [8, 6, 5]]  
> **Explanation** : 2 < 3 < 6, sorted increasingly by median element.

**Method #1 : Using sort() + median()**

In this, we perform sort using _sort()_ and median is computed using
statistics function of computing median, _median()_.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Row Median

# Using sort() + median()

from statistics import median

 

def med_comp(row):

 

 # computing median

 return median(row)

 

# initializing list

test_list = [[3, 4, 7], [1, 7, 2], [10,
2, 4], [8, 6, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# inplace sorting using sort()

test_list.sort(key = med_comp)

 

# printing result 

print("Sorted Matrix : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[3, 4, 7], [1, 7, 2], [10, 2, 4], [8, 6, 5]]
    Sorted Matrix : [[1, 7, 2], [3, 4, 7], [10, 2, 4], [8, 6, 5]]
    
    

**Method #2 : Using sorted() + lambda + median()**

In this, we perform task of perform sort using _sorted()_ , and _lambda_
function is used as key function rather than external function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Row Median

# Using sorted() + lambda + median()

from statistics import median

 

# initializing list

test_list = [[3, 4, 7], [1, 7, 2], [10,
2, 4], [8, 6, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# inplace sorting using sort()

res = sorted(test_list, key = lambda row : median(row))

 

# printing result 

print("Sorted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[3, 4, 7], [1, 7, 2], [10, 2, 4], [8, 6, 5]]
    Sorted Matrix : [[1, 7, 2], [3, 4, 7], [10, 2, 4], [8, 6, 5]]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

