Python – Fractional Frequency of elements in List



Given a List, get fractional frequency of each element at each position.

>  **Input** : test_list = [4, 5, 4, 6, 7, 5, 4, 5, 4]  
>  **Output** : [‘1/4’, ‘1/3’, ‘2/4’, ‘1/1’, ‘1/1’, ‘2/3’, ‘3/4’, ‘3/3’,
> ‘4/4’]  
>  **Explanation** : 4 occurs 1/4th of total occurrences till 1st index, and
> so on.
>
>  **Input** : test_list = [4, 5, 4, 6, 7, 5]  
>  **Output** : [‘1/2’, ‘1/2’, ‘2/2’, ‘1/1’, ‘1/1’, ‘2/2’]  
>  **Explanation** : 4 occurs 1/2th of total occurrences till 1st index, and
> so on.

 **Method : Using Counter() + loop + dictionary comprehension**

In this, we use Counter() to get the frequency of each element in list and to
form denominator part of fraction. Numerator is initialized to 0 for each
element. Then loop is used to add the elements in numberator and join with
total frequency in denominator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Fractional Frequency of elements in List

# Using Counter() + loop + dictionary comprehension

from collections import Counter

 

# initializing list

test_list = [4, 5, 4, 6, 7, 5, 4, 5,
4, 6, 4, 6]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing numerator

numer = {idx : 0 for idx in set(test_list)}

 

# initializing denominator

denom = Counter(test_list)

 

res = []

for ele in test_list:

 

 # increasing counter 

 numer[ele] += 1

 res.append(str(numer[ele]) + '/' + str(denom[ele]))

 

# printing result 

print("Fractional Frequency List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 4, 6, 7, 5, 4, 5, 4, 6, 4, 6]
    Fractional Frequency List : ['1/5', '1/3', '2/5', '1/3', '1/1', '2/3', '3/5', '3/3', '4/5', '2/3', '5/5', '3/3']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

