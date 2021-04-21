Python program to convert a list to a set based on a common element



Given a list of lists, the task is to write a python program that can convert
each sublist to a set and combine to sublists into one set if they have a
common element. The output printed will be a list of sets.

>  **Input :** test_list = [[15, 14, 12, 18], [9, 5, 2, 1], [4, 3, 2, 1], [19,
> 11, 13, 12]]
>
>  **Output :** [{11, 12, 13, 14, 15, 18, 19}, {1, 2, 3, 4, 5, 9}]
>
>  **Explanation :** List 1 and list 4 had 12 in common, hence all got merged
> to one.
>
>  **Input** : test_list = [[15, 14, 12, 18], [9, 5, 2, 1], [4, 3, 2, 1], [19,
> 11, 13, 22]]
>
>  
>
>
>  
>
>
>  **Output :** [{18, 12, 14, 15}, {1, 2, 3, 4, 5, 9}, {11, 19, 13, 22}]
>
>  **Explanation :** List 2 and list 3 had 1, 2 in common, hence all got
> merged to one.

 **Method :** _Using_ _recursion_ _and_ _union()_

In this, we perform the task of getting all containers having like elements
using union(), depending upon conditions. Recursion is used to perform similar
task to most lists required.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# utility function

def common_set(test_set):

 for idx, val in enumerate(test_set):

 for j, k in enumerate(test_set[idx + 1:], idx + 1):

 

 # getting union by conditions

 if val & k:

 test_set[idx] = val.union(test_set.pop(j))

 return common_set(test_set)

 return test_set

 

# utility function

 

 

# initializing lists

test_list = [[15, 14, 12, 18], [9, 5, 2,
1], [4, 3, 2, 1], [19, 11, 13, 12]]

 

# printing original list

print("The original list is : " + str(test_list))

 

test_set = list(map(set, test_list))

 

# calling recursive function

res = common_set(test_set)

 

# printing result

print("Common element groups : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[15, 14, 12, 18], [9, 5, 2, 1], [4, 3, 2, 1], [19,
> 11, 13, 12]]
>
> Common element groups : [{11, 12, 13, 14, 15, 18, 19}, {1, 2, 3, 4, 5, 9}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

