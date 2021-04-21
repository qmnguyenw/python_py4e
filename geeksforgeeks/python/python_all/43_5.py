Python – Count of matching elements among lists (Including duplicates)



Given 2 lists, count all the elements that are similar in both the lists
including duplicated.

>  **Input** : test_list1 = [3, 5, 6, 7, 2, 3, 5], test_list2 = [5, 5, 3, 9,
> 8, 5]  
>  **Output** : 4  
>  **Explanation** : 3 repeats 2 times, and 5 two times, totalling to 4.
>
>  **Input** : test_list1 = [3, 5, 6], test_list2 = [5, 3, 9]  
>  **Output** : 2  
>  **Explanation** : 3 repeats 1 time, and 5 one time, totalling to 2.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
each element of other list while iterating for one list, and increase the
counter.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count of matching elements among lists [ Including duplicates ]

# Using loop

 

# initializing lists

test_list1 = [3, 5, 6, 7, 2, 3]

test_list2 = [5, 5, 3, 9, 8]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using loop to iterate each element

res = 0

for ele in test_list1:

 if ele in test_list2:

 res += 1

 

# printing result 

print("All matching elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [3, 5, 6, 7, 2, 3]
    The original list 2 : [5, 5, 3, 9, 8]
    All matching elements : 3
    

**Method #2 : Using sum() + generator expression**

The combination of above methods is used to solve this problem. In this, we
count elements using sum() and generator expression performs the task of
iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count of matching elements among lists [ Including duplicates ]

# Using sum() + generator expression

 

# initializing lists

test_list1 = [3, 5, 6, 7, 2, 3]

test_list2 = [5, 5, 3, 9, 8]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using sum to count occurrences

res = sum(ele in test_list1 for ele in test_list2)

 

# printing result 

print("All matching elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [3, 5, 6, 7, 2, 3]
    The original list 2 : [5, 5, 3, 9, 8]
    All matching elements : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

