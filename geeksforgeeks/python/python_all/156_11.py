Python | Count the sublists containing given element in a list



Given a list of lists, write a Python program to count the number of sublists
containing the given element _x_.

 **Examples:**

    
    
    **Input :** lst = [1, 3, 5], [1, 3, 5, 7], [1, 3, 5, 7, 9]] 
            x = 1 
    **Output :** 3
    
    **Input :** lst = (['a'], ['a', 'c', 'b'], ['d']) 
            x = 'a'
    **Output :** 2
    

  
**Approach #1 :** Naive Approach

Count the number of lists containing _x_. Initialize _count_ to 0, then start
a for loop and check if _x_ exists in each list or not. If yes, increment
_count_.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to count number of

# list containing a certain element 

# in a list of lists

 

def countList(lst, x):

 count = 0

 for i in range(len(lst)):

 if x in lst[i]:

 count+= 1

 

 return count

 

# Driver Code

lst = (['a'], ['a', 'c', 'b'], ['d']) 

x = 'a'

print(countList(lst, x))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2
    

