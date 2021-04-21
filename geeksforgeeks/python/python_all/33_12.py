Python program to find the sum of the value in the dictionary where the key
represents the frequency



Given a dictionary with a values list, where the key represents frequency,
compute the total occurrence of each value in values lists.

>  **Input** : test_dict = {70 : [7, 4, 6], 50 : [6, 8, 5, 2]}  
> **Output** : {7: 70, 4: 70, 6: 120, 8: 50, 5: 50, 2: 50}  
> **Explanation** : 6 occurs in both keys, hence 70 + 50 = 120, assigned to 6.
>
>  **Input** : test_dict = {70 : [7, 4], 50 : [6, 8, 5, 2]}  
> **Output** : {7: 70, 4: 70, 6: 50, 8: 50, 5: 50, 2: 50}  
> **Explanation** : 6 now occurs in only 50 key, hence only 50 is assigned.

**Method : reduce() + Counter() + lambda + __add__**

This is the way in which this task can be performed. In this, Counter() is
used to compute the frequency of each value, the summation with keys is done
using __add__, all the values from each key are added using reduce(). The
map() is used to extend the logic of Counter to each value in the values list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency Key Values Summation

# Using reduce() + Counter() + lambda + __add__

from functools import reduce

from collections import Counter

 

# initializing dictionary

test_dict = {70 : [7, 4, 6], 

 100 : [8, 9, 5], 

 200 : [2, 5, 3, 7], 

 50 : [6, 8, 5, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Counter() used to get values mapped with keys 

# __add__ used to add key with values.

res = reduce(Counter.__add__, map(lambda sub: Counter({ele :
sub[0] for ele in sub[1]}), 

 test_dict.items()) )

# printing result 

print("Extracted Summation dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {70: [7, 4, 6], 100: [8, 9, 5], 200: [2, 5, 3,
> 7], 50: [6, 8, 5, 2]}  
> Extracted Summation dictionary : {7: 270, 4: 70, 6: 120, 8: 150, 9: 100, 5:
> 350, 2: 250, 3: 200}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

