Python | Reverse sequence of strictly increasing integers in a list



Given a list of integers, write a Python program to reverse the order of
consecutively incrementing chunk in given list.

 **Examples:**

    
    
    **Input :** [0, 1, 9, 8, 7, 5, 3, 14]
    **Output :** [9, 1, 0, 8, 7, 5, 14, 3]
    **Explanation:** There are two chunks of strictly
                 increasing elements (0, 1, 9) and (3, 14). 
    
    **Input :** [-5, -3, 0, 1, 3, 5, -2, -12]
    **Output :** [5, 3, 1, 0, -3, -5, -2, -12]
    **Explanation:** Only one chunk of strictly increasing 
                 elements exists i.e. (-5, -3, 0, 1, 3, 5).
    

  
**Approach #1 :** Naive (Using extended slices)

A naive approach to solve the given problem is to use extended slice. We
initialize two variables ‘res’ (to store final output) and block( to store
chunks of incrementing integers) with empty lists. Now using a for loop, every
time we check if the current element is less than the last element of block or
not. If yes, add reversed chunk to ‘res’ using extended slicing (block[::-1])
and clean block (block[:] = [i]). otherwise, simply append the element to
‘block’. At last, extend ‘res’ by reversing block and output it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Reverse order

# of incrementing integers in list

 

def reverseOrder(lst):

 res = [] 

 block = []

 for i in lst:

 

 # check if the current element is less 

 # than the last element of block 

 if block and i < block[-1]:

 

 # add reversed chunk to 'res'

 res.extend(block[::-1]) 

 block[:] = [i] 

 else:

 

 # append the element to 'block'

 block.append(i)

 

 # extend 'res' by reversing block 

 res.extend(block[::-1])

 return(res)

 

# Driver code

lst = [0, 1, 9, 8, 7, 5, 3, 14]

print(reverseOrder(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [9, 1, 0, 8, 7, 5, 14, 3]
    

