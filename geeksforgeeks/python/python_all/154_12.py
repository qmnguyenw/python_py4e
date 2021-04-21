Python | Merging duplicates to list of list



Sometimes, we need to perform the conventional task of grouping some like
elements to a separate list and thus forming a list of list. This can also
helps in counting and also get the sorted order of elements. Let’s discuss
certain ways in which this can be done.

 **Method #1 : Usingcollections.Counter()**  
This particular function can prove to be quite useful to perform this
particular task as it counts the frequency of elements in list and then we can
pair them using the list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# grouping like elements as list 

# using collections.Counter()

import collections

 

# initializing list 

test_list = [1, 3, 4, 2, 1, 3, 4, 2,
3, 4, 1]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using collections.Counter()

# grouping like elements as list 

temp = collections.Counter(test_list)

res = [[i] * j for i, j in temp.items()]

 

# print result

print("The elements after grouping are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1]
    The elements after grouping are : [[1, 1, 1], [2, 2], [3, 3, 3], [4, 4, 4]]
    

**Method #2 : Usingitertools.groupby()**  
This problem can easily solved by traditional groupby functionality that is
offered by Python via groupby function, which groups the like elements as
suggested by name.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# grouping like elements as list 

# using itertools.groupby()

import itertools

 

# initializing list 

test_list = [1, 3, 4, 2, 1, 3, 4, 2,
3, 4, 1]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itertools.groupby()

# grouping like elements as list 

res = [list(i) for j, i in
itertools.groupby(sorted(test_list))]

 

# print result

print("The elements after grouping are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1]
    The elements after grouping are : [[1, 1, 1], [2, 2], [3, 3, 3], [4, 4, 4]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

