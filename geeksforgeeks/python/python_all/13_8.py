Python program to Occurrences of i before first j in list



Given a list, the task is to write a Python program to count the occurrences
of ith element before the first occurrence of jth element.

 **Examples:**

>  **Input** : test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9], i, j = 4, 8  
> **Output** : 3  
> **Explanation** : 4 occurrs 3 times before 8 occurs.
>
>  **Input** : test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9], i, j = 5, 8  
> **Output** : 1  
> **Explanation** : 5 occurrs 1 time before 8 occurs.  
>

**Method #1 : Using** **loop.**

  

  

In this, we increment counter whenever i is encountered and stop when any j
has occurred, i.e breaking from the loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Occurrences of i before first j

# Using loop

 

# initializing Matrix

test_list = [4, 5, 6, 4, 1, 4, 8, 5,
4, 3, 4, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j 

i, j = 4, 8

 

res = 0

for ele in test_list:

 

 # breaking on 1st j

 if ele == j:

 break

 

 # counting i till 1st j

 if ele == i:

 res += 1

 

# printing result

print("Number of i's till 1st j : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]
    Number of i's till 1st j : 3

 **Method #2 : Using** **index()** **+** **slicing** **+** **count()**

In this, we perform the task of getting the index of j, and then slice list
till there, count() is used to get a count of i in the sliced list to get the
required result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Occurrences of i before first j

# Using index() + slicing + count()

 

# initializing Matrix

test_list = [4, 5, 6, 4, 1, 4, 8, 5,
4, 3, 4, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing i, j 

i, j = 4, 8

 

# getting index

jidx = test_list.index(j)

 

# slicing list 

temp = test_list[:jidx]

 

# getting count 

res = temp.count(i)

 

# printing result

print("Number of i's till 1st j : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]
    Number of i's till 1st j : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

