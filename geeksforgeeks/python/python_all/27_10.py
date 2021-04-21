Python – Next N elements from K value



Given a List, get next N values from occurrence of K value in List.

>  **Input** : test_list = [3, 4, 6, 7, 8, 4, 7, 2, 1, 8, 4, 2, 3, 9], N = 1,
> K = 4  
> **Output** : [6, 7, 2]  
> **Explanation** : All successive elements to 4 are extracted as N = 1.
>
>  **Input** : test_list = [3, 4, 6, 7, 8, 4, 7, 2, 1, 8, 4, 2, 3, 9], N = 2,
> K = 7  
> **Output** : [8, 4, 2, 1]  
> **Explanation** : Two elements after each occurrence of 7 are extracted.

**Method #1 : Using list comprehension + slicing**

In this we extract all the indices using list comprehension, and then loop is
employed to append the elements and join in as single string from the desired
K value occurrences in List.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Next N elements of K value

# Using list comprehension + slicing

 

# initializing list

test_list = [3, 4, 6, 7, 8, 4, 7, 2,
1, 8, 4, 2, 3, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# initializing N

N = 2

 

# getting indices of K

temp = [idx for idx in range(len(test_list)) if
test_list[idx] == K]

 

# getting next N elements from K using loop

res = []

for ele in temp:

 

 # appending slice

 res.extend(test_list[ele + 1: ele + N + 1])

 

# printing result

print("Constructed Result List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 4, 6, 7, 8, 4, 7, 2, 1, 8, 4, 2, 3, 9]
    Constructed Result List : [6, 7, 7, 2, 2, 3]
    
    

**Method #2 : Using filter() + lambda + loop**

This is similar to above method, difference being filtering of indices is
performed using filter() and lambda functions.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Next N elements of K value

# Using filter() + lambda + loop

 

# initializing list

test_list = [3, 4, 6, 7, 8, 4, 7, 2,
1, 8, 4, 2, 3, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# initializing N

N = 2

 

# getting indices of K

# using filter() and lambda

temp = list(filter(lambda ele: test_list[ele] == K,
range(len(test_list))))

 

# getting next N elements from K using loop

res = []

for ele in temp:

 

 # appending slice

 res.extend(test_list[ele + 1: ele + N + 1])

 

# printing result

print("Constructed Result List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [3, 4, 6, 7, 8, 4, 7, 2, 1, 8, 4, 2, 3, 9]
    Constructed Result List : [6, 7, 7, 2, 2, 3]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

