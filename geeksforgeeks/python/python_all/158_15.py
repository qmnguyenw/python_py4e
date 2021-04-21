Python program to find sum of absolute difference between all pairs in a list



Given a list of distinct elements, write a Python program to find the sum of
absolute differences of all pairs in the given list.

 **Examples:**

    
    
    **Input :** [9, 2, 14] 
    **Output :** 24 
    **Explanation:** (abs(9-2) + abs(9-14) + abs(2-14))
    
    **Input :** [1, 2, 3, 4]
    **Output :** 10 
    **Explanation:** (abs(1-2) + abs(1-3) + abs(1-4)
                 + abs(2-3) + abs(2-4) + abs(3-4))
    

The first approach is the brute force approach, which has been previously
discussed. Here, we will discuss the pythonic approaches.

 **Approach #1 :** Using enumerate()  
Enumerate() method adds a counter to an iterable and returns it in a form of
enumerate object. In this method, we have a list ‘diffs’ which contains the
absolute difference. We use two loops having two variables each. One to
iterate through the counter and one for the list element. In every iteration,
we check if the elements are similar or not. If not, find absolute difference
and append it to diffs. Finally, find the sum of list. Since each pair will be
counted twice, we divide the final sum by 2 and return it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find sum of

# absolute differences in all pairs 

 

def sumPairs(lst): 

 

 diffs = []

 for i, x in enumerate(lst):

 for j, y in enumerate(lst):

 if i != j: 

 diffs.append(abs(x-y))

 

 return int(sum(diffs)/2)

 

# Driver program 

lst = [1, 2, 3, 4] 

print(sumPairs(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    10
    

