Python | Count true booleans in a list



Given a list of booleans, write a Python program to find the count of true
booleans in the given list.

 **Examples:**

    
    
    **Input :** [True, False, True, True, False]
    **Output :** 3
    
    **Input :** [False, True, False, True]
    **Output :** 2
    

  
**Method #1 :** Using List comprehension

One simple method to count True booleans in a list is using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to count True booleans in a list

 

def count(lst):

 

 return sum(bool(x) for x in lst)

 

# Driver code

lst = [True, False, True, True, False]

print(count(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3
    

