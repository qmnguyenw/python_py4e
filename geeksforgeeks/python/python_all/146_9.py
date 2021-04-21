Python | Find minimum of each index in list of lists



Sometimes, we are encountered with such problem in which we need to find the
**minimum of each column in a matrix** i.e minimum of each index in list of
lists. This kind of problem is quite common and useful in competitive
programming. Let’s discuss certain ways in which this problem can be solved.

 **Examples:**

    
    
    **Input :** [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    **Output :** [1, 3, 2] 
     
    **Input :** [[3, 2, 8], [5, 3, 5], [9, 3, 1]] 
    **Output :** [3, 2, 1]
    

**Method #1 : Usingmin() + list comprehension + zip()**

The combination of above methods are required to solve this particular
problem. The min function is used to get the required minimum value and zip
function provides the combination of like indices and then list is created
using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Minimum index value

# using min() + list comprehension + zip()

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using min() + list comprehension + zip()

# Minimum index value

res = [min(idx) for idx in zip(*test_list)]

 

# print result

print("The Minimum of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Minimum of each index list is : [1, 3, 2]
    

