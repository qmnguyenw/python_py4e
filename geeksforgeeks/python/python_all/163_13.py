Python | Convert a list of lists into tree-like dict



Given a list of lists, write a Python program to convert the given list of
lists into a tree-like dictionary.

 **Examples:**

    
    
    **Input :** [[1], [2, 1], [3, 1], [4, 2, 1], [5, 2, 1], [6, 3, 1], [7, 3, 1]]
    **Output :** {1: {2: {4: {}, 5: {}}, 3: {6: {}, 7: {}}}}
    
    **Input :** [['A'], ['B', 'A'], ['C', 'A'], ['D', 'C', 'A']]
    **Output :** {'A': {'C': {'D': {}}, 'B': {}}}
    

  
**Method #1 :** Naive Method  
This is a Naive approach in which we use two for loops to traverse the list of
lists. We initialize the empty dictionary ‘tree’ to _currTree_ and each time
we check if the key (list of list’s item) is included in the _currTree_ or
not. If not, include it in the _currTree_ , otherwise do nothing. Finally,
assign the currTree[key] to currTree.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a list

# of lists into Dictionary (Tree form)

 

def formTree(list):

 tree = {}

 for item in list:

 currTree = tree

 

 for key in item[::-1]:

 if key not in currTree:

 currTree[key] = {}

 currTree = currTree[key]

 

 return tree

 

# Driver Code

lst = [['A'], ['B', 'A'], ['C', 'A'], ['D',
'C', 'A']]

print(formTree(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    {'A': {'B': {}, 'C': {'D': {}}}}
    

  
**Method #2 :** Using reduce()  
The reduce() function is used to apply a particular function passed in its
argument to all of the list elements mentioned in the sequence passed along.
We will use reduce() to traverse the dictionary and reuse getTree() to
find the location to store the value for setTree(). All but the last element
in _mapList_ is needed to find the ‘parent’ dictionary to add the value to,
then use the last element to set the value to the right key.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a list

# of lists into Dictionary (Tree form)

 

from functools import reduce

from operator import getitem

 

def getTree(tree, mappings):

 return reduce(getitem, mappings, tree)

 

def setTree(tree, mappings):

 getTree(tree, mappings[:-1])[mappings[-1]] = dict()

 

# Driver Code

lst = [['A'], ['B', 'A'], ['C', 'A'], ['D',
'C', 'A']]

tree ={}

for item in lst:

 setTree(tree, item[::-1])

 

print(tree)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'A': {'B': {}, 'C': {'D': {}}}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

