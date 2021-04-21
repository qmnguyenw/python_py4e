Python | Check if a nested list is a subset of another nested list



Given two lists _list1_ and _list2_ , check if _list2_ is a subset of _list1_
and return True or False accordingly.

 **Examples:**

    
    
    **Input :** list1 = [[2, 3, 1], [4, 5], [6, 8]]
            list2 = [[4, 5], [6, 8]]
    **Output :** True
    
    **Input :** list1 = [['a', 'b'], ['e'], ['c', 'd']]
            list2 = [['g']]
    **Output :** False
    

  
Let’s discuss few approaches to solve the problem.

 **Approach #1 : Naive Approach**  
Take a variable ‘exist’ which keeps track of each element, whether it is
present in list1 or not. Start a loop and in each iteration ‘i’, check if ith
element is present in list1. If present, set exist to True else false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Check is a nested

# list is a subset of another nested list

 

def checkSubset(list1, list2):

 l1, l2 = list1[0], list2[0]

 exist = True

 for i in list2:

 if i not in list1:

 exist = False

 return exist

 

# Driver Code

list1 = [[2, 3, 1], [4, 5], [6, 8]]

list2 = [[4, 5], [6, 8]]

print(checkSubset(list1, list2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

