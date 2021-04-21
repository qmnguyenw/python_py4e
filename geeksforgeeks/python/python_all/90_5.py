Python – Characters which Occur in More than K Strings



Sometimes, while working with Python, we have a problem in which we compute
how many characters are present in string. But sometimes, we can have a
problem in which we need to get all characters that occur in aleast K Strings.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingset() + Counter() + items() + loop**  
The combination of above functions can be used to perform this particular
task. In this, we find the count using Counter and set is used to limit the
character duplicacy.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Characters which Occur in More than K Strings

# using set() + Counter() + loop + items()

from collections import Counter

from itertools import chain

 

def char_ex(strs, k):

 temp = (set(sub) for sub in strs)

 counts = Counter(chain.from_iterable(temp))

 return {chr for chr, count in counts.items() if count
>= k}

 

# Initializing list

test_list = ['Gfg', 'ise', 'for', 'Geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K

K = 2

 

# Characters which Occur in More than K Strings

# using set() + Counter() + loop + items()

res = char_ex(test_list, K)

 

# printing result 

print ("Filtered Characters are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'ise', 'for', 'Geeks']
    Filtered Characters are : {'e', 'G', 's', 'f'}
    

**Method #2 : Using dictionary comprehension +set() + Counter()**  
The combination of these functions perform this task in similar way as above.
The difference is just that we use dictionary comprehension to give a compact
solution to problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Characters which Occur in More than K Strings

# using set() + Counter() + dictionary comprehension

from collections import Counter

 

# Initializing list

test_list = ['Gfg', 'ise', 'for', 'Geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K

K = 2

 

# Characters which Occur in More than K Strings

# using set() + Counter() + dictionary comprehension

res = {key for key, val in Counter([ele for sub in

 test_list for ele in set(sub)]).items()

 if val >= K}

 

# printing result 

print ("Filtered Characters are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'ise', 'for', 'Geeks']
    Filtered Characters are : {'e', 'G', 's', 'f'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

