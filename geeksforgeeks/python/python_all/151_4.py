Python | Split list of strings into sublists based on length



Given a list of strings, write a Python program to split the list into
sublists based on string length.

 **Examples:**

    
    
    **Input :** ['The', 'art', 'of', 'programming']
    **Output :** [['of'], ['The', 'art'], ['programming']]
    
    **Input :** ['Welcome', 'to', 'geeksforgeeks']
    **Output :** [['to'], ['Welcome'], ['geeksforgeeks']]
    

**Approach #1 :** Pythonic naive

A naive approach for the above method uses a dictionary and a for loop to
traverse the list. In each iteration, it checks whether the element length is
already in the list or not. If not, it adds the element length and element as
key:value pair, otherwise, the element is just added to the value sublist.
Finally, we make a list of all the values of the dict and return it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Divide list of strings

# into sublists based on string length

 

def divideList(lst):

 dct = {}

 

 for element in lst:

 if len(element) not in dct:

 dct[len(element)] = [element]

 elif len(element) in dct:

 dct[len(element)] += [element]

 

 res = []

 for key in sorted(dct):

 res.append(dct[key])

 

 return res

 

# Driver code

lst = ['The', 'art', 'of', 'programming']

print(divideList(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [['of'], ['The', 'art'], ['programming']]
    

