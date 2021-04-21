Python | Subgroups of i’th index size in list



Sometimes we need to group elements and grouping techniques and requirements
vary accordingly. One such way to group the elements is by the i’th size in
list which stores the dictionary of index keys with values as list elements of
subsequent size i.

> Input : [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]  
> Output: {1: [4], 2: [7, 8], 3: [10, 12, 15], 4: [13, 17, 14, 5]}

Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingislice() \+ dictionary comprehension**  
The slice method can be used to group the chunks of list required to be made
as values of the dictionaries which are then assigned to their destined index
key using the dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Subgrouping of i'th index size in list

# using islice() + dictionary comprehension

from itertools import islice

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14, 5]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using islice() + dictionary comprehension

# Subgrouping of i'th index size in list

temp = iter(test_list)

res = {key: val for key, val in ((i, list(islice(temp, i)))

 for i in range(1, len(test_list))) if val}

 

# printing result

print("The grouped dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14, 5]  
> The grouped dictionary is : {1: [4], 2: [7, 8], 3: [10, 12, 15], 4: [13, 17,
> 14, 5]}

