Python – Convert Matrix to Custom Tuple Matrix



Sometimes, while working with Python Matrix, we can have a problem in which we
need to perform conversion of a Python Matrix to matrix of tuples which a
value attached row-wise custom from external list. This kind of problem can
have application in data domains as Matrix is integral DS that is used. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[4, 5], [7, 3]], add_list = [‘Gfg’, ‘best’]  
>  **Output** : [(‘Gfg’, 4), (‘Gfg’, 5), (‘best’, 7), (‘best’, 3)]
>
>  **Input** : test_list = [[4, 5]], add_list = [‘Gfg’]  
>  **Output** : [(‘Gfg’, 4), (‘Gfg’, 5)]

 **Method #1 : Using loop +zip()**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of binding custom value to each element of row using
zip(). This is brute force way to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to Custom Tuple Matrix

# Using zip() + loop

 

# initializing lists

test_list = [[4, 5, 6], [6, 7, 3], [1, 3,
4]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing List elements 

add_list = ['Gfg', 'is', 'best']

 

# Convert Matrix to Custom Tuple Matrix

# Using zip() + loop

res = []

for idx, ele in zip(add_list, test_list):

 for e in ele:

 res.append((idx, e))

 

# printing result 

print("Matrix after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list is : [[4, 5, 6], [6, 7, 3], [1, 3, 4]]  
> Matrix after conversion : [(‘Gfg’, 4), (‘Gfg’, 5), (‘Gfg’, 6), (‘is’, 6),
> (‘is’, 7), (‘is’, 3), (‘best’, 1), (‘best’, 3), (‘best’, 4)]

