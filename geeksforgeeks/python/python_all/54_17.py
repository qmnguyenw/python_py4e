Python – Cross List Sync on duplicate elements removal



Given two lists, perform syncing of all the elements of list with other list
when removal of duplcate elements in first list.

>  **Input** : test_list1 = [1, 1, 2, 2, 3, 3], test_list2 = [8, 3, 7, 5, 4,
> 1]  
>  **Output** : [1, 2, 3], [8, 7, 4]  
>  **Explanation** : After removal of duplicates (1, 2, 3), corresponding
> elements are removed from 2nd list, and hence (8, 7, 4) are mapped.
>
>  **Input** : test_list1 = [1, 2, 2, 2, 2], test_list2 = [8, 3, 7, 5, 4, 1]  
>  **Output** : [1, 2], [8, 3]  
>  **Explanation** : Elements removed are (2, 2, 2), [1, 2] are mapped to [8,
> 3] as expected.

 **Method #1 : Using loop +dict()**  
The above functions provide brute force way to solve this problem. In this, we
memoize the elements with its counterpart using dictionary and loop
conditionals.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross List Sync on duplicate elements removal

# Using loop + dict()

 

# initializing lists

test_list1 = [2, 2, 3, 4, 4, 4, 5, 5,
6, 6]

test_list2 = [8, 3, 7, 5, 4, 1, 0, 9,
4, 2]

 

# printing original lists 

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Cross List Sync on duplicate elements removal

temp = dict()

a = []

for idx in range(len(test_list1)):

 if test_list1[idx] not in a:

 a.append(test_list1[idx])

 

 # performing memoize using dictionary

 temp[test_list1[idx]] = test_list2[idx]

 

res2 = list(temp.values())

res1 = a

 

# printing result 

print("List 1 : " + str(res1))

print("Sync List : " + str(res2))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list 1 : [2, 2, 3, 4, 4, 4, 5, 5, 6, 6]
    The original list 2 : [8, 3, 7, 5, 4, 1, 0, 9, 4, 2]
    List 1 : [2, 3, 4, 5, 6]
    Sync List : [8, 7, 5, 0, 4]
    

