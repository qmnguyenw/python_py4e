Python – Join Tuples to Integers in Tuple List



Sometimes, while working with Python records, we can have a problem in which
we need to concatenate all the elements, in order, to convert elements in
tuples in List to integer. This kind of problem can have applications in many
domains such as day-day and competitive programming. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_list = [(4, 5, 6), (5, 1), (1, 3, 8, 0), (6, 9)]  
>  **Output** : [456, 51, 1380, 69]
>
>  **Input** : test_list = [(4, 5, 6, 8, 9)]  
>  **Output** : [45689]

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
perform join of all the elements using number creation mathematically compute
the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Join Tuples to Integers in Tuple List

# Using loop

 

# helpr_fnc

def join_tup(tup):

 res = tup[0]

 for idx in tup[1:]:

 res = res * 10 + idx

 return res

 

# initializing list

test_list = [(4, 5), (5, 6), (1, 3), (6,
9)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Join Tuples to Integers in Tuple List

# Using loop

res = [join_tup(idx) for idx in test_list]

 

# printing result 

print("The joined result : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5), (5, 6), (1, 3), (6, 9)]
    The joined result : [45, 56, 13, 69]
    

