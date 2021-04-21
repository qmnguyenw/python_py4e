Python – Retain records with N occurrences of K



Somtimes, while working with Python tuples list, we can have a problem in
which we need to perform retention of all the records where occurrences of K
is N times. This kind of problem can come in domains such as web development
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2  
>  **Output** : [(4, 5, 5, 4)]
>
>  **Input** : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3  
>  **Output** : []

 **Method #1 : Using list comprehension +count()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of counting occurrences and conditions and iterations
using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain records with N occurrences of K

# Using count() + list comprehension

 

# initializing list

test_list = [(4, 5, 6, 4, 4), (4, 4, 3),
(4, 4, 4), (3, 4, 9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# initializing N 

N = 3

 

# Retain records with N occurrences of K

# Using count() + list comprehension

res = [ele for ele in test_list if ele.count(K) == N]

 

# printing result 

print("Filtered tuples : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
    Filtered tuples : [(4, 5, 6, 4, 4), (4, 4, 4)]
    

