Python | Type casting whole List and Matrix



Sometimes, while working with Python List or Matrix, we usually have a problem
in which we require to get a generalized function which could perform the type
casting of whole container at once. There is always a need of a mechanism code
which can transform entirely the allowed change of data type for all elements
in container. Let’s discuss a way in which this task can be performed.

 **Method : Usingmap() \+ list comprehension**  
This task can be performed using a map(). The transformation of a normal list
can be performed using a single map function by just passing the desired data
type. But when it comes to transformation of whole matrix, we need the help of
list comprehension for the same.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Type casting whole List and Matrix

# using map() + list comprehension

 

# helper function to type cast list 

def cast_list(test_list, data_type):

 return list(map(data_type, test_list))

 

# helper function to type cast Matrix 

def cast_matrix(test_matrix, data_type):

 return list(map(lambda sub: list(map(data_type, sub)),
test_matrix))

 

# initialize list 

test_list = [1, 4, 9, 10, 19]

 

# initialize Matrix

test_matrix = [[5, 6, 8], [8, 5, 3], [9,
10, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing original matrix

print("The original Matrix is : " + str(test_matrix))

 

# Type casting whole List and Matrix

# using map() + list comprehension

res_list = cast_list(test_list, str)

res_matrix = cast_matrix(test_matrix, str)

 

# printing result

print("The List after type casting is : " + str(res_list))

print("The Matrix after type casting is : " + str(res_matrix))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 9, 10, 19]
    The original Matrix is : [[5, 6, 8], [8, 5, 3], [9, 10, 3]]
    The List after type casting is : ['1', '4', '9', '10', '19']
    The Matrix after type casting is : [['5', '6', '8'], ['8', '5', '3'], ['9', '10', '3']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

