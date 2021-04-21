Python – Remove Equilength and Equisum Tuple Duplicates



Sometimes, while working with Python tuples, we can have a problem in which we
need to remove duplicates on basis of equal length and equal sum. This kind of
problem can also be broken to accomodate any one of the required condition.
This kind of problem can occur in data domains and day-day programming. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(1, 2, 0), (3, 0), (2, 1)]  
>  **Output** : [(1, 2, 0), (3, 0)]
>
>  **Input** : test_list = [(1, 2, 0), (3, 0, 0), (0, 2, 1)]  
>  **Output** : [(1, 2, 0)]

 **Method #1 : Using nested loops**  
This is one of the ways in which this task can be performed. This is brute
force method, in which we loop for each tuple, a matching tuple w.r.t size and
sum and perform removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Equilength and Equisum Tuple Duplicates

# Using nested loop

 

# initializing lists

test_list = [(4, 5, 6), (3, 0), (2, 1),
(1, 2, 3), (5, 5, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove Equilength and Equisum Tuple Duplicates

# Using nested loop

res = []

for sub in test_list:

 for sub1 in res:

 if len(sub) == len(sub1) and sum(sub) ==
sum(sub1):

 break

 else:

 res.append(sub)

 

# printing result 

print("Tuples after filteration : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5, 6), (3, 0), (2, 1), (1, 2, 3), (5, 5, 5)]
    Tuples after filteration : [(4, 5, 6), (3, 0), (1, 2, 3)]
    

