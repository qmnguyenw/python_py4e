Python – Total equal pairs in List



Given a list, the task is to write a python program to compute total equal
digit pairs, i.e extract number of all elements with can be dual paired with
similar elements present in the list.

    
    
    Input : test_list = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]
    Output : 4
    
    Explanation : 4, 2 and 5 have 3 occurrences, 7 has 2 occurrences, 1 pair each.
    
    Input : test_list = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3, 3]
    Output : 5
    
    Explanation : 4, 2 and 5 have 3 occurrences, 1 pair each and 3, 7 have 2 occurrences, total 5 pairs.

 **Method #1 : Using** **count()** **+** **set()**

In this, we convert the container to set and use _count()_ upon each element
on the original list. Post that quotient with 2 is obtained and summed to get
required pairs.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Total equal pairs in List

# Using loop + count()

 

# initializing lists

test_list = [2, 4, 5, 2, 5, 4, 2, 4,
5, 7, 7, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

all_ele = set(test_list)

res = 0

for ele in all_ele:

 

 # summing count from element list

 res += test_list.count(ele) // 2

 

# printing result

print("Total Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]
    Total Pairs : 4

 **Method #2 :** **Using Counter()** **+** **list comprehension** **+**
**sum()**

In this, getting the count of each element is done using _Counter()_ , _sum()_
is used to compute total pairs.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Total equal pairs in List

# Using Counter() + list comprehension + sum()

from collections import Counter

 

# initializing lists

test_list = [2, 4, 5, 2, 5, 4, 2, 4,
5, 7, 7, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using Counter for getting elements count

res = sum(ele // 2 for ele in
Counter(test_list).values())

 

# printing result

print("Total Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]
    Total Pairs : 4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

