Python – Extract Kth element of every Nth tuple in List



Given list of tuples, extract Kth column element of every Nth tuple.

>  **Input** :test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8), (6, 4,
> 7), (2, 5, 7), (1, 9, 10), (3, 5, 7)], K = 2, N = 3  
>  **Output** : [3, 8, 10]  
>  **Explanation** : From 0th, 3rd, and 6th tuple, 2nd elements are 3, 8, 10.
>
>  **Input** :test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8), (6, 4,
> 7), (2, 5, 7), (1, 9, 10), (3, 5, 7)], K = 0, N = 3  
>  **Output** : [4, 4, 1]  
>  **Explanation** : From 0th, 3rd, and 6th tuple, 0th elements are 4, 4, 1.

 **Method #1 : Using loop**

In this, we iterate by skipping N values using 3rd parameter of range(), and
append every Kth value in list using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Kth element of every Nth tuple in List

# Using loop

 

# initializing list

test_list = [(4, 5, 3), (3, 4, 7), (4, 3,
2), (4, 7, 8),

 (6, 4, 7), (2, 5, 7), (1, 9, 10),
(3, 5, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 1

 

# initializing N 

N = 3

 

res = []

for idx in range(0, len(test_list), N):

 

 # extract Kth element

 res.append(test_list[idx][K])

 

# printing result 

print("The extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8), (6, 4, 7), (2, 5, 7), (1, 9, 10), (3, 5, 7)]
    The extracted elements : [5, 7, 9]
    

**Method #2 : Using list comprehension**

In this, we perform task of extracted elements using one-liner using list
comprehension, using same method as above.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Kth element of every Nth tuple in List

# Using list comprehension

 

# initializing list

test_list = [(4, 5, 3), (3, 4, 7), (4, 3,
2), (4, 7, 8),

 (6, 4, 7), (2, 5, 7), (1, 9, 10),
(3, 5, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 1

 

# initializing N 

N = 3

 

# Skipping N using 3rd param of range()

res = [test_list[idx][K] for idx in range(0,
len(test_list), N)]

 

# printing result 

print("The extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8), (6, 4, 7), (2, 5, 7), (1, 9, 10), (3, 5, 7)]
    The extracted elements : [5, 7, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

