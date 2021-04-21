Python – Maximum of each Column



Sometimes, we are encountered with such problem in which we need to find the
maximum of each column in a matrix i.e maximum of each index in list of lists.
This kind of problem is quite common and useful in competitive programming.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingmax() + list comprehension + zip()**  
The combination of above methods are required to solve this particular
problem. The max function is used to get the required maximum value and zip
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

# Maximum of each Column

# using max() + list comprehension + zip()

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using max() + list comprehension + zip()

# Maximum of each Column

res = [max(idx) for idx in zip(*test_list)]

 

# print result

print("The Maximum of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Maximum of each index list is : [9, 7, 6]
    

**Method #2 : Usingmap() + max() + zip()**  
This works in almost similar way as the above method, but the difference is
just that we use map function to build the max element list rather than using
list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximum index value

# using max() + map() + zip()

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using max() + map() + zip()

# Maximum index value

res = list(map(max, zip(*test_list)))

 

# print result

print("The Maximum of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Maximum of each index list is : [9, 7, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

