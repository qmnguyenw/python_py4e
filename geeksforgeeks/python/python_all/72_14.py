Python – Maximum String value length of Key



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to find the maximum length of all the string values of
particular key. This problem can occur in domains of day-day programming and
web development. Let’s discuss certain ways in which this task can be
performed.

 **Examples –**

>  **Input:**  
>  test_list = [{‘key1’ : “abcd”, ‘key2’ : 2}, {‘key1’ : “qwertyui”, ‘key2’ :
> 2}, {‘key1’ : “xcvz”, ‘key3’ : 3}, {‘key1’ : None, ‘key3’ : 4}]
>
>  **Output:** 8  
>  **Explanation:** Among all values for given key _key1_ , _**qwertyui**_
> has maximum length (which is 8).

 **Method #1 : Usingmax() + len() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we compute the maximum string length using max() and len(). The comparison
with each is bound by list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum String value length of Key

# Using max() + len() + list comprehension

 

# initializing list

test_list = [{'Gfg' : "abcd", 'best' : 2}, 

 {'Gfg' : "qwertyui", 'best' : 2},

 {'Gfg' : "xcvz", 'good' : 3},

 {'Gfg' : None, 'good' : 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Key 

filt_key = 'Gfg'

 

# Maximum String value length of Key

# Using max() + len() + list comprehension

temp = (sub[filt_key] for sub in test_list)

res = max(len(ele) for ele in temp if ele is not
None)

 

# printing result 

print("The maximum length key value : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘best’: 2, ‘Gfg’: ‘abcd’}, {‘best’: 2, ‘Gfg’:
> ‘qwertyui’}, {‘good’: 3, ‘Gfg’: ‘xcvz’}, {‘good’: 4, ‘Gfg’: None}]  
> The maximum length key value : 8

**Method #2 : Using list comprehension +len() + max() (one liner)**  
The similar task can also be combined to perform in one line for compact
solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum String value length of Key

# Using max() + len() + list comprehension (one liner)

 

# initializing list

test_list = [{'Gfg' : "abcd", 'best' : 2}, 

 {'Gfg' : "qwertyui", 'best' : 2},

 {'Gfg' : "xcvz", 'good' : 3},

 {'Gfg' : None, 'good' : 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Key 

filt_key = 'Gfg'

 

# Maximum String value length of Key

# Using max() + len() + list comprehension (one liner)

res = len(max(test_list, key = lambda sub:
len(sub[filt_key])

 if sub[filt_key] is not None else 0)[filt_key])

 

# printing result 

print("The maximum length key value : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘best’: 2, ‘Gfg’: ‘abcd’}, {‘best’: 2, ‘Gfg’:
> ‘qwertyui’}, {‘good’: 3, ‘Gfg’: ‘xcvz’}, {‘good’: 4, ‘Gfg’: None}]  
> The maximum length key value : 8

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

