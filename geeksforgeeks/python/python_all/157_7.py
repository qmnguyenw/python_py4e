Python | List frequency of elements



Sometimes we have the utility in which we require to find the frequency of
elements in the list and the solution to this problem has been discussed many
times. But sometimes we come across the task in which we require to find the
number of lists that particular elements occur. Let’s discuss certain
shorthands in which this can be done.  

**Method #1 : Using Counter() + set() + list comprehension**  
The combination of the above functions can be used to perform the task. The
Counter function does the grouping, set function extracts the distinct
elements as keys of dict and list comprehension check for its list
occurrences.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# list frequency of elements

# using Counter() + set() + list comprehension

from collections import Counter

# initializing list

test_list = [[3, 5, 4],

 [6, 2, 4],

 [1, 3, 6]]

# printing original list

print("The original list : " + str(test_list))

# using Counter() + set() + list comprehension

# list frequency of elements

res = dict(Counter(i for sub in test_list for i in
set(sub)))

# printing result

print("The list frequency of elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 5, 4], [6, 2, 4], [1, 3, 6]]
    The list frequency of elements is : {1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2}

  
**Method #2 : Using Counter() + itertools.chain.from_iterable() + map() +
set()**  
The above 4 functionalities can also be combined to achieve this particular
task. The set function extracts the dictionary keys formed by the Counter, map
function performs the task for all sublists and from_iterable function
performs using iterators which is faster than list comprehension.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# list frequency of elements

# using Counter() + itertools.chain.from_iterable() + map() + set()

from collections import Counter

from itertools import chain

# initializing list

test_list = [[3, 5, 4],

 [6, 2, 4],

 [1, 3, 6]]

# printing original list

print("The original list : " + str(test_list))

# using Counter() + itertools.chain.from_iterable() + map() + set()

# list frequency of elements

res = dict(Counter(chain.from_iterable(map(set, test_list))))

# printing result

print("The list frequency of elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [[3, 5, 4], [6, 2, 4], [1, 3, 6]]
    The list frequency of elements is : {1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2}

