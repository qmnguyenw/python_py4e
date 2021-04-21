Python Program that prints elements common at specified index of list elements



Given a list of strings, the task is to write a Python program to extract all
characters that are same at a specified index of each element of a list.

>  **Input** : test_list = [“geeks”, “weak”, “beak”, “peek”]  
> **Output** : [‘e’, ‘k’]  
> **Explanation** : e and k are at same at an index on all strings.
>
>  **Input** : test_list = [“geeks”, “weak”, “beak”, “peer”]  
> **Output** : [‘e’]  
> **Explanation** : e is at same at an index on all strings.  
>

**Method 1 :** _Using_ _min()_ _,_ _len()_ _and_ _loop_

In this, initially minimum length string is extracted to check indices to
iterate to ensure all indices in strings. Then each index is checked for
similar character using loop, if found, character is appended to result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = ["geeks", "weak", "beak", "peek"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting min length string

min_len = min(len(ele) for ele in test_list)

 

res = []

for idx in range(0, min_len):

 flag = True

 for ele in test_list:

 

 # checking for all equal columns

 if ele[idx] != test_list[0][idx]:

 flag = False

 break

 

 if flag:

 res.append(test_list[0][idx])

 

 

# printing result

print("Extracted similar characters : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeks’, ‘weak’, ‘beak’, ‘peek’]
>
> Extracted similar characters : [‘e’, ‘k’]

 **Method 2 :** _Using_ _all()_ _,_ _min()_ _,_ _len()_ _and_ _loop_

In this, we perform the task of checking all elements to match using all(),
reducing a nested loop, increasing readability.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = ["geeks", "weak", "beak", "peek"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting min length string

min_len = min(len(ele) for ele in test_list)

 

res = []

for idx in range(0, min_len):

 

 # using all() for condition injection

 if all(ele[idx] == test_list[0][idx] for ele in
test_list):

 res.append(test_list[0][idx])

 

# printing result

print("Extracted similar characters : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeks’, ‘weak’, ‘beak’, ‘peek’]
>
> Extracted similar characters : [‘e’, ‘k’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

