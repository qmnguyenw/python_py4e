Python – Extract Unique value key pairs



Sometimes, while working on Python dictionaries, we can have a problem in
which we need to perform the extraction of selected pairs of keys from
dictionary list, that too unique. This kind of problem can have application in
many domains including day-day programming. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_list = [{‘gfg’ : 5, ‘best’ : 12}, {‘gfg’ : 5, ‘best’ :
> 12}, ]  
>  **Output** : {(5, 12)}
>
>  **Input** : test_list = [{‘gfg’ : 5, ‘is’: 5, ‘best’ : 12}]  
>  **Output** : {(5, 12)}

 **Method #1 : Using list comprehension**  
This problem can be solved using above functionality. In this, we perform the
match, using conditionals and “in” operator. The whole logic compiled using
list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Unique value key pairs

# Using list comprehension

 

# initializing list

test_list = [{'gfg' : 5, 'is' : 8, 'best' : 12},


 {'gfg' : 5, 'is' : 12, 'best' : 12},

 {'gfg' : 20, 'is' : 17, 'best' : 12}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing required keys

req_key1 = 'gfg'

req_key2 = 'best'

 

# Extract Unique value key pairs

# Using list comprehension

res = {tuple(sub[idx] for idx in [req_key1, req_key2]) for
sub in test_list}

 

# printing result 

print("The required values : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘gfg’: 5, ‘is’: 8, ‘best’: 12}, {‘gfg’: 5, ‘is’:
> 12, ‘best’: 12}, {‘gfg’: 20, ‘is’: 17, ‘best’: 12}]  
> The required values : {(5, 12), (20, 12)}

