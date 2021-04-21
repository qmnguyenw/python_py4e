Python – Grouped Consecutive Range Indices of Elements



Given List of elements, for list of tuples, where each represents the
continuity of occurrence of each element.

>  **Input** : test_list = [1, 1, 5, 6, 5, 5]  
>  **Output** : {1: [(0, 1)], 5: [(2, 2), (4, 5)], 6: [(3, 3)]}  
>  **Explanation** : 5 present at 2nd idx and also in continuation in 4th and
> 5th index, and hence recorded range.
>
>  **Input** : test_list = [5, 5, 5, 5, 5, 5]  
>  **Output** : {5: [(0, 5)]}  
>  **Explanation** : Only 5 present, hence recorded.

 **Method : Using groupby() + defaultdict() + len() + loop**

In this, we perform consecutive elements grouping using groupby(),
defaultdict() is used to initialize the tuple list, The len() is used to get
length of repetition.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Grouped Consecutive Range Indices of Elements

# Using groupby() + defaultdict() + len() + loop

from itertools import groupby

from collections import defaultdict

 

# initializing lists

test_list = [1, 1, 5, 6, 5, 5, 6, 6,
6, 1, 5, 5]

 

# printing string

print("The original list : " + str(test_list))

 

idx = 0

res = defaultdict(list)

 

# grouping Consecutives

for key, sub in groupby(test_list):

 ele = len(list(sub))

 

 # append strt index, and till index

 res[key].append((idx, idx + ele - 1))

 idx += ele

 

# printing results 

print("The grouped dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [1, 1, 5, 6, 5, 5, 6, 6, 6, 1, 5, 5]
    The grouped dictionary : {1: [(0, 1), (9, 9)], 5: [(2, 2), (4, 5), (10, 11)], 6: [(3, 3), (6, 8)]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

