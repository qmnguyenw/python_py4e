Python | Merge corresponding sublists from two different lists



Given two lists containing sublists, write a Python program to merge the two
sublists based on same index.

 **Examples:**

    
    
    **Input :** l1 = [['+', '-', '+'], ['-', '+'], ['+', '-', '+']]
            l2 = [['2a3', 'b2', '3c'], ['a3', 'b2'], ['a3', '2b2', '5c']]
    **Output :** [['+2a3', '-b2', '+3c'], ['-a3', '+b2'], ['+a3', '-2b2', '+5c']]
    
    **Input :** l1 = [['1', '2'], ['1', '2', '3']]
            l2 = [['anne', 'bob'], ['cara', 'drake', 'ezra']]
    **Output :** [['1anne', '2bob'], ['1cara', '2drake', '3ezra']]
    

**Approach #1 :** List comprehension with zip()  
We can use nested list comprehension with zip() function. The zip()
function take iterables, makes iterator that aggregates elements based on the
iterables passed, and returns an iterator of tuples. Now traversing through
the zipped tuples using two variable _i_ and _j_ , it concatenates both the
variables using ‘+’ operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Concatenate

# corresponding sublists from two 

# different lists

 

def concatList(l1, l2):

 return [[i + j for i, j in zip(x, y)]

 for x, y in zip(l1, l2)]

 

# Driver Code

l1 = [['1', '2'], ['1', '2', '3']]

l2 = [['anne', 'bob'], ['cara', 'drake', 'ezra']]

print(concatList(l1, l2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [['1anne', '2bob'], ['1cara', '2drake', '3ezra']]
    

  
**Approach #2 :** list comprehension with map()  
Instead of the nested list comprehension we can use the function _map()_ with
the operator _concat_. We traverse through zipped _list1_ and _list2_ using
variable _i_ and _j_. Then we apply concat operator on _i_ and _j_ to
concatenate them.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Concatenate

# corresponding sublists from two 

# different lists

from operator import concat

 

def concatList(l1, l2):

 return [list(map(concat, i, j)) for i, j in zip(l1,
l2)]

 

# Driver Code

l1 = [['1', '2'], ['1', '2', '3']]

l2 = [['anne', 'bob'], ['cara', 'drake', 'ezra']]

print(concatList(l1, l2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [['1anne', '2bob'], ['1cara', '2drake', '3ezra']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

