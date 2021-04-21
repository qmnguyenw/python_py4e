Python – Test if greater than preceding element in Tuple List



Given list of tuples, check if preceding element is smaller than the current
element for each element in Tuple list.

>  **Input** : test_list = [(5, 1), (4, 9), (3, 5)]  
>  **Output** : [[False, False], [False, True], [False, True]]  
>  **Explanation** : First element always being False, Next element is checked
> for greater value.
>
>  **Input** : test_list = [(1, 8), (2, 2), (3, 6), (4, 2)]  
>  **Output** : [[False, True], [False, False], [False, True], [False, False]]  
>  **Explanation** : 8 and 6 are greater cases in above cases, hence True.

 **Method #1 : Using list comprehension +enumerate()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of checking for greater value using one liner list
comprehension and enumerate() is used to work with indices while nested
iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if greater than preceding element in Tuple List

# Using list comprehension + enumerate()

 

# initializing list

test_list = [(3, 5, 1), (7, 4, 9), (1, 3,
5)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Test if greater than preceding element in Tuple List

# Indices checked using enumerate() and True and false 

# values assigned in list comprehension

res = [[True if idx > 0 and j > i[idx - 1] else
False

 for idx, j in enumerate(i)] for i in test_list]

 

# printing result 

print("Filtered values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [(3, 5, 1), (7, 4, 9), (1, 3, 5)]
    Filtered values : [[False, True, False], [False, False, True], [False, True, True]]
    

