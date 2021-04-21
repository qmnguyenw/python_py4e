Python – Extract ith column values from jth column values



Sometimes, while working with Python Matrix, we can have a problem in which we
need to extract ith column values from comparing values from jth column. This
kind of problem can occur in domains such as school programming or web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[4, 5, 6], [2, 5, 7], [9, 8, 2], [10, 2, 6]],
> search_list = [4, 9], search_idx = 0, ext_idx = 2  
>  **Output** : [6, 2]
>
>  **Input** : test_list = [[4, 5, 6], [2, 5, 7], [9, 8, 2], [10, 2, 6]],
> search_list = [2, 6], search_idx = 2, ext_idx = 0  
>  **Output** : [4, 9, 10]

 **Method #1 : Using loop**  
This is brute way to solve this problem. In this, we loop through each row and
compare the jth column with list elements, if present, extract the ith
element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract ith column values from jth column values

# Using loop

 

# initializing list

test_list = [[4, 5, 6], [2, 5, 7], [9, 8,
2], [10, 2, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing list 

search_list = [5, 2]

 

# initializing search index 

search_idx = 1

 

# initializing extract index

ext_idx = 2

 

# Extract ith column values from jth column values

# Using loop

res = []

for sub in test_list:

 if sub[search_idx] in search_list:

 res.append(sub[ext_idx])

 

# printing result 

print("The extracted elements : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [[4, 5, 6], [2, 5, 7], [9, 8, 2], [10, 2, 6]]
    The extracted elements : [6, 7, 6]
    

