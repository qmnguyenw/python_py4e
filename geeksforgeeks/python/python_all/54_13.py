Python – Extract Missing Ranges



Given list of tuples, start range and end range values, extract the ranges
that are missing from the list.

>  **Input** : test_list = [(7, 2), (15, 19), (38, 50)], strt_val = 5,
> stop_val = 60  
>  **Output** : [(5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)]  
>  **Explanation** : Missing element ranges starting from 5 and ending at
> 50-60 are output as desired.
>
>  **Input** : test_list = [(7, 2), (15, 19), (38, 50)], strt_val = 1,
> stop_val = 52  
>  **Output** : [(1, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 52)]  
>  **Explanation** : Similar as above, just ranges are altered.

 **Method : Using loop**  
This is brute force method in which this task can be performed. In this, we
keep track of start and stop values, and keep adding the missing ranges. At
last, its important to check if any range is left less than higher range.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Missing Ranges

# Using loop

 

# initializing lists

test_list = [(6, 9), (15, 34), (48, 70)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing start val 

strt_val = 2

 

# initializing stop val 

stop_val = 100

 

# Using loop

res = []

for sub in test_list:

 

 # checking for start range

 if sub[0] > strt_val:

 res.append((strt_val, sub[0]))

 strt_val = sub[1]

 

 # checking for end range

 if strt_val < stop_val:

 res.append((strt_val, stop_val))

 

# printing result 

print("Missing range tuples : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(6, 9), (15, 34), (48, 70)]
    Missing range tuples : [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

