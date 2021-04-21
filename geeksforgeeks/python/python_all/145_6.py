Python | Merge two list of lists according to first element



Given two list of lists of equal length, write a Python program to merge the
given two list of lists, according to the first common element of each
sublist.

 **Examples:**

    
    
    **Input :** lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
            lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
    **Output :** [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]
    
    **Input :** lst1 = [ ['c', 'class'], ['g', 'greek'], ]
            lst2 = [['c', 'coder'], ['g', 'god'], ]
    **Output :** [['c', 'class', 'coder'], ['g', 'greek', 'god']]
    

  
**Method #1 :** Python _zip()_ with list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Merge two list of

# lists according to first element

 

def merge(lst1, lst2):

 return [a + [b[1]] for (a, b) in zip(lst1, lst2)]

 

# Driver code

lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]

lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3,
'Chennai']]

print(merge(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]
    

  
**Method #2 :** Python _enumerate()_ with list comprehension

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Merge two list of

# lists according to first element

import collections

 

def merge(lst1, lst2):

 return [(sub + [lst2[i][-1]]) for i, sub in
enumerate(lst1)]

 

# Driver code

lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]

lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3,
'Chennai']]

print(merge(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]
    

  
**Method #3 :** Python dictionary  
In this method, we initialise ‘dict1’ with _collections.defaultdict_ and
traverse through ‘lst1’+’lst2’ and append the first element of ‘lst1’ as key
and tupled second element of both respective sublists as value. Finally we
traverse through ‘dict1’ and initialize ‘dictlist’ with the desired output.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Merge two list of

# lists according to first element

import collections

 

def merge(lst1, lst2):

 dict1 = collections.defaultdict(list)

 

 for e in lst1 + lst2:

 dict1[e[0]].append(e[1])

 dictlist = list()

 

 for key, value in dict1.items():

 dictlist.append([key]+value)

 

 return dictlist

 

# Driver code

lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]

lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3,
'Chennai']]

print(merge(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1, 'Alice', 'Delhi'], [2, 'Bob', 'Mumbai'], [3, 'Cara', 'Chennai']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

