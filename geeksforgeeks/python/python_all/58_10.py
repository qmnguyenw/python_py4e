Python – Matrix Row subset



Sometimes, while working with Python Matrix, one can have a problem in which,
one needs to extract all the rows that are a possible subset of any row of
other Matrix. This kind of problem can have application in data domains as a
matrix is a key data type in those domains. Let’s discuss certain ways in
which this problem can be solved.

>  **Input** : test_list = [[4, 5, 7], [2, 3, 4], [9, 8, 6]], check_matr =
> [[2, 3], [1, 2], [9, 0]]  
>  **Output** : [[2, 3]]
>
>  **Input** : test_list = [[4, 1, 2], [2, 3, 4], [9, 8, 0]], check_matr =
> [[2, 3], [1, 2], [9, 0]]  
>  **Output** : [[2, 3], [1, 2], [9, 0]]

 **Method #1 : Usingany() + all() \+ list comprehension**  
The combination of above functions offer a way in which this problem can be
solved. In this, we check for occurrence of all elements of row using all()
and any() is used to match to any row of Matrix. List comprehension is used to
bind the logic together.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Row subset

# Using any() + all() + list comprehension

 

# initializing lists

test_list = [[4, 5, 7], [2, 3, 4], [9, 8,
0]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check Matrix

check_matr = [[2, 3], [1, 2], [9, 0]]

 

# Matrix Row subset

# Using any() + all() + list comprehension

res = [ele for ele in check_matr if any(all(a in
sub for a in ele)

 for sub in test_list)]

 

# printing result 

print("Matrix row subsets : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [[4, 5, 7], [2, 3, 4], [9, 8, 0]]
    Matrix row subsets : [[2, 3], [9, 0]]
    

