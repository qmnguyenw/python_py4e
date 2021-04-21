Python | Creating a 3D List



A 3-D List means that we need to make a list that has three parameters to it,
i.e., (a x b x c), just like a 3 D array in other languages. In this program
we will try to form a 3-D List with its content as “#”. Lets look at these
following examples:

    
    
    Input : 
    3 x 3 x 3
    Output :
    [[['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
     [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']],
     [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]]
    
    Input :
    5 x 3 x 2
    Output :
    [[['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#']],
     [['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#']]]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print 3D list

# importing pretty printed

import pprint

 

def ThreeD(a, b, c):

 lst = [[ ['#' for col in range(a)] for col in
range(b)] for row in range(c)]

 return lst

 

# Driver Code

col1 = 5

col2 = 3

row = 2

# used the pretty printed function

pprint.pprint(ThreeD(col1, col2, row))  
  
---  
  
 __

 __

Output:

    
    
    [[['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#']],
     [['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#'],
      ['#', '#', '#', '#', '#']]]
    

Refer pprint() to get more insight into this topic.

Now let’s suppose we need to merge two 3D lists into one.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to merge two 3D list into one

# importing pretty printed

import pprint

 

def ThreeD(a, b, c):

 lst1 = [[ ['1' for col in range(a)] for col in
range(b)] for row in range(c)]

 lst2= [[ ['2' for col in range(a)] for col in
range(b)] for row in range(c)]

 # Merging using "+" operator

 lst = lst1+lst2

 return lst

 

# Driver Code

col1 = 3

col2 = 3

row = 3

 

# used the pretty printed function

pprint.pprint(ThreeD(col1, col2, row))  
  
---  
  
 __

 __

Output:

    
    
    [[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']],
     [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']],
     [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']],
     [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']],
     [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']],
     [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

