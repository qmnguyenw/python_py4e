Multi-dimensional lists in Python



There can be more than one additional dimension to lists in Python. Keeping in
mind that a list can hold other lists, that basic principle can be applied
over and over. Multi-dimensional lists are the lists within lists. Usually, a
dictionary will be the better choice rather than a multi-dimensional list in
Python.

 **Accessing a multidimensional list:**

 **Approach 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate printing

# of complete multidimensional list

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12,
15], [4, 8, 12, 16, 20]]

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
    

**Approach 2:** Accessing with the help of loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate printing

# of complete multidimensional list row

# by row.

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12,
15], [4, 8, 12, 16, 20]]

for record in a:

 print(record)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [2, 4, 6, 8, 10]
    [3, 6, 9, 12, 15]
    [4, 8, 12, 16, 20]
    

