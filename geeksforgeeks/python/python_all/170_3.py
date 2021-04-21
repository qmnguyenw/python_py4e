Python | Binary element list grouping



Sometimes while working with the databases, we need to perform certain list
operations that are more like query language, for instance, grouping of nested
list element with respect to its other index elements. This article deals with
binary nested list and group each nested list element with respect to its
other index elements

 **Method #1 : Using list comprehension**  
List comprehension can perform the task that would usually take 4-5 lines in
1-2 lines. This groups the element by assigning to each number values
according to the match with another element of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform binary list grouping

# using list comprehension

 

# initializing list 

test_list = [["G", 0], ["F", 0], ["B", 2],

 ["E", 2], ['I', 1], ['S', 1],

 ['S', 2], ['T', 2], ['G', 0]]

 

# using list comprehension

# to perform binary list grouping

temp = set(map(lambda i : i[1], test_list))

res = [[j[0] for j in test_list if j[1] == i]
for i in temp]

 

# printing result

print ("The grouped list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The grouped list is : [['G', 'F', 'G'], ['I', 'S'], ['B', 'E', 'S', 'T']]
    

  
**Method #2 : Usingitertools.groupby() + itemgetter()**  
We can also use groupby function to perform this particular task. This method
follows 2-3 steps. First, the sequence is sort with respect to second element,
now this can be fed to get grouped and is then grouped. Then lastly, we print
the first element as required by the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform binary list grouping

# using itertools.groupby() + itemgetter()

from itertools import groupby

from operator import itemgetter

 

# initializing list 

test_list = [["G", 0], ["F", 0], ["B", 2],

 ["E", 2], ['I', 1], ['S', 1], 

 ['S', 2], ['T', 2], ['G', 0]]

 

# using itertools.groupby() + itemgetter()

# to perform binary list grouping

test_list.sort(key = itemgetter(1))

groups = groupby(test_list, itemgetter(1))

res = [[i[0] for i in val] for (key, val) in groups]

 

# printing result

print ("The grouped list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The grouped list is : [['G', 'F', 'G'], ['I', 'S'], ['B', 'E', 'S', 'T']]
    

