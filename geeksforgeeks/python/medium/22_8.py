Python | Convert a nested list into a flat list



The task is to convert a nested list into a single list in python i.e no
matter how many levels of nesting is there in python list, all the nested has
to be removed in order to convert it to a single containing all the values of
all the lists inside the outermost brackets but without any brackets inside.

Examples:

> Input : l = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]  
> Output : l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>
> Input : l = [[[‘item1’, ‘item2’]], [[‘item3’, ‘item4’]]]  
> Output : l = [‘item1’, ‘item2’, ‘itm3, ‘item4”]

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We use recursion because the levels of nesting cannot be predetermined.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to flat a nested list with

# multiple levels of nesting allowed.

 

# input list

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9,
[10]]]

 

# output list

output = []

 

# function used for removing nested 

# lists in python. 

def reemovNestings(l):

 for i in l:

 if type(i) == list:

 reemovNestings(i)

 else:

 output.append(i)

 

# Driver code

print ('The original list: ', l)

reemovNestings(l)

print ('The list after removing nesting: ', output)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list:  [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
    The list after removing nesting:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

