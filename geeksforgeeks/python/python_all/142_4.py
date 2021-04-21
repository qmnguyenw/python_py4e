Python program to find all possible pairs with given sum



Given a list of integers and an integer variable _K_ , write a Python program
to find all pairs in the list with given sum _K_.

 **Examples:**

    
    
    **Input :** lst =[1, 5, 3, 7, 9]
            K = 12
    **Output :** [(5, 7), (3, 9)]
    
    **Input :** lst = [2, 1, 5, 7, -1, 4]
            K = 6
    **Output :** [(2, 4), (1, 5), (7, -1)]
    

  
**Method #1 :** Pythonic Naive

This is a naive approach to the above problem. First, we take an empty list
‘res’ and start a loop and traverse each element of the given list of
integers. In each iteration, pop the element, store it in ‘num’, find
remaining difference for sum K, and check if the difference exists in the
given list or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find all pairs in

# a list of integers with given sum 

 

def findPairs(lst, K): 

 res = []

 while lst:

 num = lst.pop()

 diff = K - num

 if diff in lst:

 res.append((diff, num))

 

 res.reverse()

 return res

 

# Driver code

lst = [1, 5, 3, 7, 9]

K = 12

print(findPairs(lst, K))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(5, 7), (3, 9)]
    

