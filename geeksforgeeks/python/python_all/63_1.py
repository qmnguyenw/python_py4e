Combine keys in a list of dictionaries in Python



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform a merge of dictionaries in list with similar keys.
This kind of problem can come in data optimization domains. Let’s discuss a
way in which this task can be performed.

>  **Input** : test_list = [{‘a’: 6}, {‘b’: 2}, {‘a’: 9}, {‘b’: 7}]  
>  **Output** : [{‘b’: 2, ‘a’: 6}, {‘b’: 7, ‘a’: 9}]
>
>  **Input** : test_list = [{‘a’: 8}, {‘a’: 2}, {‘a’: 3}]  
>  **Output** : [{‘a’: 8}, {‘a’: 2}, {‘a’: 3}]

 **Method : loop +** operator**  
The combination of above functions can be used to solve this problem. In this,
we use brute force to construct a new dictionary and add keys only if that is
not added in current. The task of merging dictionaries is by unpacking the
initial dictionaries using “**” operator, and then packing again with
dictionary with no repeated key and new one, using the usual dictionary
initialization construct {}.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Similar Dictionaries in List

# Using loop + "**" operator

 

# initializing list

test_list = [{'gfg' : 1}, {'is' : 2}, {'best' :
3},

 {'gfg' : 5}, {'is' : 17}, {'best' : 14},

 {'gfg' : 7}, {'is' : 8}, {'best' : 10},]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Merge Similar Dictionaries in List

# Using loop + "**" operator

res = [{}]

for sub in test_list:

 if list(sub)[0] not in res[-1]:

 res[-1] = {**res[-1], **sub}

 else:

 res.append(sub)

 

# printing result 

print("The merged dictionaries : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘gfg’: 1}, {‘is’: 2}, {‘best’: 3}, {‘gfg’: 5},
> {‘is’: 17}, {‘best’: 14}, {‘gfg’: 7}, {‘is’: 8}, {‘best’: 10}]  
> The merged dictionaries : [{‘best’: 3, ‘is’: 2, ‘gfg’: 1}, {‘best’: 14,
> ‘is’: 17, ‘gfg’: 5}, {‘best’: 10, ‘is’: 8, ‘gfg’: 7}]

