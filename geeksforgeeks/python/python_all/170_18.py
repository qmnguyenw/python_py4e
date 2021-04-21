Python | Merge two lists into list of tuples



Given two lists, write a Python program to merge the two lists into list of
tuples.

 **Examples:**

    
    
    **Input :** list1 = [1, 2, 3]
            list2 = ['a', 'b', 'c']
    **Output :** [(1, 'a'), (2, 'b'), (3, 'c')]
    
    **Input :** list1 = [1, 2, 3, 4]
            list2 = [ 1, 4, 9]
    **Output :** [(1, 1), (2, 4), (3, 9), (4, '')]
    

**Approach #1 :** Naive  
Merge both the list into a list of tuple using a for loop. But the drawback is
given two lists need to be of the same length.

 __

 __  
 __

 __

 __  
 __  
 __

def merge(list1, list2):

 

 merged_list = [(list1[i], list2[i]) for i in range(0,
len(list1))]

 return merged_list

 

# Driver code

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 'a'), (2, 'b'), (3, 'c')]
    

  
**Approach #2 :** Naive but more efficient  
This method remove the above given drawback and work well with uneven lengths
of the two lists. It also provide try catch error for Index error.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def merge(list1, list2):

 

 merged_list = []

 for i in range(max((len(list1), len(list2)))):

 

 while True:

 try:

 tup = (list1[i], list2[i])

 except IndexError:

 if len(list1) > len(list2):

 list2.append('')

 tup = (list1[i], list2[i])

 elif len(list1) < len(list2):

 list1.append('')

 tup = (list1[i], list2[i])

 continue

 

 merged_list.append(tup)

 break

 return merged_list

 

# Driver code

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 'a'), (2, 'b'), (3, 'c')]
    

  
**Approach #3 :** Using zip()  
using zip() method to merge the two list elements and then typecasting into
tuple.

 __

 __  
 __

 __

 __  
 __  
 __

def merge(list1, list2):

 

 merged_list = tuple(zip(list1, list2)) 

 return merged_list

 

# Driver code

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    ((1, 'a'), (2, 'b'), (3, 'c'))
    

  
**Approach #4 :** Using enumerate(), alternative to zip().

This method uses two for loops to enumerate through lists and merge the two
lists.

 __

 __  
 __

 __

 __  
 __  
 __

def merge(list1, list2):

 

 merged_list = [(p1, p2) for idx1, p1 in enumerate(list1) 

 for idx2, p2 in enumerate(list2) if idx1 == idx2]

 return merged_list

 

# Driver code

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(merge(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 'a'), (2, 'b'), (3, 'c')]
    

  
**Approach #5:** Using map() and lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Using map() and lambda

def listOfTuples(l1, l2):

 return list(map(lambda x, y:(x,y), l1, l2))

 

# Driver Code

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

 

print(listOfTuples(list1, list2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 'a'), (2, 'b'), (3, 'c')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

