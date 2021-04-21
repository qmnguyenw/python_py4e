Python – Odd Frequency Characters



Sometimes, while working with Python strings, we can have a problem in which
we need to extract all the string characters which have odd number of
occurrences. This problem can have applications in domains such as data domain
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_str = ‘geekforgeeks’  
>  **Output** : [‘r’, ‘o’, ‘f’, ‘s’]
>
>  **Input** : test_str = ‘g’  
>  **Output** : [‘g’]

 **Method #1 : Usingdefaultdict() \+ list comprehension + loop**  
The combination of above functions can be used to solve this problem. In this,
we initialize the defaultdict() with integer and then perform frequency count.
List comprehension is used to extract all the odd frequencies.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Odd Frequency Characters

# Using list comprehension + defaultdict()

from collections import defaultdict

 

# helper_function

def hlper_fnc(test_str):

 cntr = defaultdict(int)

 for ele in test_str:

 cntr[ele] += 1

 return [val for val, chr in cntr.items() if chr % 2
!= 0]

 

# initializing string

test_str = 'geekforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Odd Frequency Characters

# Using list comprehension + defaultdict()

res = hlper_fnc(test_str)

 

# printing result 

print("The Odd Frequency Characters are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original string is : geekforgeeks is best for geeks
    The Odd Frequency Characters are : ['k', 'i', 't', 'g', 'e', 'b']
    

