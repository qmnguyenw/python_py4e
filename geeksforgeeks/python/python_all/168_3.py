Python | Linear search on list or tuples



Let’s see a basic linear search operation on Python list and tuples.

A simple approach is to do **linear search** , i.e

  * Start from the leftmost element of list and one by one compare x with each element of the list.
  * If x matches with an element, return True.
  * If x doesn’t match with any of elements, return False.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Linear-Search.png)

 **Example #1:** Linear Search on Lists

 __

 __  
 __

 __

 __  
 __  
 __

# Search function with parameter list name

# and the value to be searched

def search(list,n):

 

 for i in range(len(list)):

 if list[i] == n:

 return True

 return False

 

# list which contains both string and numbers.

list = [1, 2, 'sachin', 4,'Geeks', 6]

 

# Driver Code

n = 'Geeks'

 

if search(list, n):

 print("Found")

else:

 print("Not Found")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Found
    

