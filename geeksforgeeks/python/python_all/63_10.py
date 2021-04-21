Python – Tuple to Dictionary Summation conversion



Sometimes, while working with Python tuples, we can have a problem in which we
can have data points in tuples, and we need to convert them to dictionary
after performing summation of similar keys. This kind of operation can also be
extended to max, min or product. This can occur in data domains. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [(5, 8), (5, 6), (5, 2), (5, 8), (5, 10)]  
>  **Output** : {5: 34}
>
>  **Input** : test_list = [(5, 8), (9, 6)]  
>  **Output** : {5: 8, 9: 6}

 **Method #1 : Using loop +defaultdict()**  
The combination of above functions can be used to solve this problem. In this,
we initialize the counter dictionary with integers using defaultdict() and
loop is used to iterate for all data points.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple to Dictionary Summation conversion

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing list

test_list = [(7, 8), (5, 6), (7, 2), (6,
8), (5, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Tuple to Dictionary Summation conversion

# Using defaultdict() + loop

res = defaultdict(int)

for sub in test_list:

 res[sub[0]] += sub[1]

 

# printing result 

print("The summation tuple dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(7, 8), (5, 6), (7, 2), (6, 8), (5, 10)]
    The summation tuple dictionary : {7: 10, 5: 16, 6: 8}
    

