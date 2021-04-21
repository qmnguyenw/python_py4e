Python | Program to count duplicates in a list of tuples



Given a list of tuples, write a Python program to check if an element of the
list has duplicates. If duplicate exist, print the number of occurrence of
each duplicate tuple, otherwise print “No Duplicates”.

 **Examples:**

>  **Input :** [(‘a’, ‘e’), (‘b’, ‘x’), (‘b’, ‘x’), (‘a’, ‘e’), (‘b’, ‘x’)]  
>  **Output :**  
>  (‘a’, ‘e’) – 2  
> (‘b’, ‘x’) – 3
>
>  **Input :** [(0, 5), (6, 9), (0, 8)]  
>  **Output :** No Duplicates

Let’s see the various ways we can count duplicates in a list of tuples.

  

  

 **Approach #1 :** Naive Approach

This approach uses two loops to traverse the list elements and check if the
first element and second element of each element matches any other tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to convert tuple

# into string

def count(listOfTuple):

 

 flag = False

 

 # To append Duplicate elements in list

 coll_list = [] 

 coll_cnt = 0

 for t in listOfTuple:

 

 # To check if Duplicate exist

 if t in coll_list: 

 flag = True

 continue

 

 else:

 coll_cnt = 0

 for b in listOfTuple:

 if b[0] == t[0] and b[1] == t[1]:

 coll_cnt = coll_cnt + 1

 

 # To print count if Duplicate of element exist

 if(coll_cnt > 1): 

 print(t, "-", coll_cnt)

 coll_list.append(t)

 

 if flag == False:

 print("No Duplicates")

 

# Driver code

print("Test Case 1:")

listOfTuple = [('a', 'e'), ('b', 'x'), ('b',
'x'), 

 ('a', 'e'), ('b', 'x')] 

 

count(listOfTuple)

 

print("Test Case 2:")

listOfTuple = [(0, 5), (6, 9), (0, 8)]

count(listOfTuple)  
  
---  
  
 __

 __

 **Output:**

    
    
    Test Case 1:
    ('a', 'e') - 2
    ('b', 'x') - 3
    
    Test Case 2:
    No Duplicates
    

Time complexity – O(n)2

  
**Approach #2 :** Using Counter

Counter is a container included in the collections module. It is an unordered
collection where elements and their respective count are stored as dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to convert tuple

# into string

import collections

 

def count(listOfTuple):

 

 flag = False

 val = collections.Counter(listOfTuple)

 uniqueList = list(set(listOfTuple))

 

 for i in uniqueList:

 if val[i]>= 2:

 flag = True

 print(i, "-", val[i])

 

 if flag == False:

 print("Duplicate doesn't exist")

 

# Driver code

listOfTuple = [('a', 'e'), ('b', 'x'), ('b',
'x'), 

 ('a', 'e'), ('b', 'x')] 

count(listOfTuple)  
  
---  
  
 __

 __

 **Output:**

    
    
    ('b', 'x') - 3
    ('a', 'e') - 2
    

Time complexity – O(n)  
  
**Approach #3 :** Using another dict

You can make a dictionary, say count_map, and store the count of each tuple
as the value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to convert tuple

# into string

def count(listOfTuple):

 

 count_map = {}

 for i in listOfTuple:

 count_map[i] = count_map.get(i, 0) +1

 print(count_map)

 

# Driver code

print("Test Case 1:")

listOfTuple = [('a', 'e'), ('b', 'x'), ('b',
'x'), 

 ('a', 'e'), ('b', 'x')] 

 

count(listOfTuple)  
  
---  
  
 __

 __

 **Output:**

    
    
    Test Case 1:
    {('a', 'e'): 2, ('b', 'x'): 3}
    

Time complexity – O(n)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

