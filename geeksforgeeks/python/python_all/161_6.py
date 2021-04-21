Python | Find all triplets in a list with given sum



Given a list of integers, write a Python program to find all triplets that sum
up to given integer ‘k’.

 **Examples:**

    
    
    **Input :** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10
    **Output :** [(1, 5, 4), (1, 6, 3), (1, 7, 2), (2, 5, 3)]
    
    **Input :** [12, 3, 6, 1, 6, 9], k = 24
    **Output :** [(12, 6, 6), (12, 9, 3)]
    

**Approach #1 :** Naive (Using set)  
In this approach, we use two for loops. The first loop sets first element,
another to check whether other two elements including first sums up to k or
not. This approach takes **O(n 2)** time complexity.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find total number

# of triplets in a temp_list with given k

 

def findTriplets(lst, k):

 triplet_count = 0

 final_temp_list =[]

 

 for i in range(0, len(lst)-1): 

 

 s = set() 

 temp_list = []

 

 # Adding first element

 temp_list.append(lst[i])

 

 curr_k = k - lst[i] 

 

 for j in range(i + 1, len(lst)): 

 

 if (curr_k - lst[j]) in s: 

 triplet_count += 1

 

 # Adding second element

 temp_list.append(lst[j])

 

 # Adding third element

 temp_list.append(curr_k - lst[j])

 

 # Appending tuple to the final list

 final_temp_list.append(tuple(temp_list))

 temp_list.pop(2)

 temp_list.pop(1)

 s.add(lst[j])

 

 return final_temp_list

 

# Driver Code

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,
10]

k = 10

print(findTriplets(lst, k))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 5, 4), (1, 6, 3), (1, 7, 2), (2, 5, 3)]
    

  
**Approach #2 :** Using itertools  
Python itertools module provide _combination(iterable, r)_ function. This tool
returns the r length subsequences of elements from the input iterable. Every
time we make a combination of 3 elements and check if they sums up to k or
not.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find total number

# of triplets in a list with given sum

from itertools import combinations

 

def findTriplets(lst, key):

 

 def valid(val):

 return sum(val) == key

 

 return list(filter(valid, list(combinations(lst, 3))))

 

# Driver Code

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,
10]

print(findTriplets(lst, 10))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

