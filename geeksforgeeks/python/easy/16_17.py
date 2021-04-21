10 Interesting Python Cool Tricks



In python we can return multiple values –

  1. It’s very unique feature of Python that returns multiple value at time.

 __

 __  
 __

 __

 __  
 __  
 __

def GFG():

 g = 1

 f = 2

 return g, f 

 

x, y = GFG()

print(x, y)  
  
---  
  
 __

 __

 **Output:**

    
    
    (1, 2)
    

  2. Allows Negative Indexing: Python allows negative indexing for its sequences. Index -1 refer to the last element, -2 second last element and so on.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['geeks', 'practice', 'contribute']

print(my_list[-1])  
  
---  
  
 __

 __

 **Output:**

    
    
    contribute
    

  3. Combining Multiple Strings. We can easily concatenate all the tokens available in the list.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['geeks', 'for', 'geeks']

print(''.join(my_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks
    

  4. Swapping is as easy as none.

