Python – Extracting Priority Elements in Tuple List



Sometimes, while working with Python Records, we can have a problem in which
we need to perform extraction of all the priority elements from records, which
usually occur as one of the binary element tuple. This kind of problem can
have possible application in web development and gaming domains. Let’s discuss
certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(7, 1), (3, 2), (4, 6)]  
> prior_list = [1, 3, 4]  
>  **Output** : [1, 3, 4]
>
>  **Input** :  
> test_list = [(7, 3), (3, 4), (1, 6)]  
> prior_list = [1, 3, 4]  
>  **Output** : [3, 4, 1]

 **Method #1 : Using loop**  
This is brute force approach to solve this problem. In this, we iterate each
element of the priority list and check for individual tuple, filter out the
matching element and append to list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Priority Elements in Tuple List

# loop

 

# initializing list

test_list = [(5, 1), (3, 4), (9, 7), (10,
6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Priority list 

prior_list = [6, 4, 7, 1]

 

# Extracting Priority Elements in Tuple List

# loop

res = []

for sub in test_list:

 for val in prior_list:

 if val in sub:

 res.append(val)

 

# printing result 

print("The extracted elements are : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(5, 1), (3, 4), (9, 7), (10, 6)]
    The extracted elements are : [1, 4, 7, 6]
    

