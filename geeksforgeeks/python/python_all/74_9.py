Python – Convert Coordinate Dictionary to Matrix



Sometimes, while working with Python Matrix, we can have problem in which we
have dictionary records with key as matrix position and its value, and we wish
to convert that to actual Matrix. This can have applications in many domains
including competitive programming and day-day programming. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop +max() \+ list comprehension**  
The combination of above methods can be used to solve this problem. In this,
we use max() to get the dimensions of matrix, list comprehension to create
matrix and loop to assign values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Coordinate Dictionary to Matrix

# Using loop + max() + list comprehension

 

# initializing dictionary

test_dict = { (0, 1) : 4, (2, 2) : 6, (3,
1) : 7, (1, 2) : 10, (3, 2) : 11}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Coordinate Dictionary to Matrix

# Using loop + max() + list comprehension

temp_x = max([cord[0] for cord in test_dict.keys()])

temp_y = max([cord[1] for cord in test_dict.keys()])

res = [[0] * (temp_y + 1) for ele in range(temp_x
+ 1)]

 

for (i, j), val in test_dict.items():

 res[i][j] = val

 

# printing result 

print("The dictionary after creation of Matrix : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {(0, 1): 4, (1, 2): 10, (3, 2): 11, (3, 1): 7,
> (2, 2): 6}  
> The dictionary after creation of Matrix : [[0, 4, 0], [0, 0, 10], [0, 0, 6],
> [0, 7, 11]]

  

  

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. This performs
task similar to above function, just the difference is that it is shorthand to
above method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Coordinate Dictionary to Matrix

# Using list comprehension

 

# initializing dictionary

test_dict = { (0, 1) : 4, (2, 2) : 6, (3,
1) : 7, (1, 2) : 10, (3, 2) : 11}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Coordinate Dictionary to Matrix

# Using list comprehension

temp_x, temp_y = map(max, zip(*test_dict))

res = [[test_dict.get((j, i), 0) for i in range(temp_y +
1)] 

 for j in range(temp_x + 1)]

 

# printing result 

print("The dictionary after creation of Matrix : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {(0, 1): 4, (1, 2): 10, (3, 2): 11, (3, 1): 7,
> (2, 2): 6}  
> The dictionary after creation of Matrix : [[0, 4, 0], [0, 0, 10], [0, 0, 6],
> [0, 7, 11]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

