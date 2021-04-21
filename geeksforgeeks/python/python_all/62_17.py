Python – Cross tuple summation grouping



Sometimes, while working with Python tuple records, we can have a problem in
which we need to perform summation grouping of 1st element of tuple pair w.r.t
similar 2nd element of tuple. This kind of problem can have application in
day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(1, 5), (7, 4), (9, 6), (11, 6)]  
>  **Output** : [(7, 4), (1, 5), (20, 6)]
>
>  **Input** : test_list = [(1, 8)]  
>  **Output** : [(1, 8)]

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this we check
for similar second elements and perform summation till then and perform the
accumulated grouping.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross tuple summation grouping

# Using loop

 

# initializing list

test_list = [(4, 5), (7, 5), (8, 6), (10,
6), (10, 4), (6, 7), (3, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Concatenate Similar Key values

# Using loop

temp = dict()

for ele1, ele2 in test_list:

 temp[ele2] = temp.get(ele2, 0) + ele1

res = [(ele2, ele1) for (ele1, ele2) in temp.items()]

 

# printing result 

print("The grouped records are : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5), (7, 5), (8, 6), (10, 6), (10, 4), (6, 7), (3, 7)]
    The grouped records are : [(10, 4), (11, 5), (18, 6), (9, 7)]
    

