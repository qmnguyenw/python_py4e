Python | Reshape a list according to given multi list



Given two lists, a single dimensional and a multidimensional list, write
Python program to reshape the single dimensional list according to the length
of multidimensional list.

 **Examples:**

    
    
    **Input :** list1 = [[1], [2, 3], [4, 5, 6]]
            list2 = ['a', 'b', 'c', 'd', 'e', 'f']
    **Output :** [['a'], ['b', 'c'], ['d', 'e', 'f']]
    
    **Input :** list1 = [[8, 2, 5], [1], [12, 4, 0, 24]]
            list2 = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't']
    **Output :** [['m', 'n', 'o'], ['p'], ['q', 'r', 's', 't']]
    

  
**Method #1 :** Using extended slices

A simple and naive method is to use a for loop and Python extended slices to
append each sublist of list2 to a variable ‘res’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to reshape a list

# according to multidimensional list

 

def reshape(lst1, lst2):

 last = 0

 res = []

 for ele in list1:

 res.append(list2[last : last + len(ele)])

 last += len(ele)

 

 return res

 

# Driver code

list1 = [[1], [2, 3], [4, 5, 6]]

list2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(reshape(list1, list2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [['a'], ['b', 'c'], ['d', 'e', 'f']]
    

