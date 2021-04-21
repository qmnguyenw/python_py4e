Python – Merge List value Keys to Matrix



Sometimes, while working with Python dictionary, we can have a problem in
which we need to perform the merger of certain keys in dictionary. In this, we
tend to form a matrix of resultant singular key. This kind of problem can have
applications in data domains. Let’s discuss certain way in which this task can
be performed.

>  **Input** : test_dict = {‘Maths’: [1, 2], ‘gfg’: [4, 5], ‘CS’: [6]}  
>  **Output** : {‘merge_key’: [[4, 5], [6], [1, 2]]}
>
>  **Input** : test_dict = {‘Maths’: [1], ‘gfg’: [4], ‘CS’: [9]}  
>  **Output** : {‘merge_key’: [[4], [9], [1]]}

 **Method : Using loop + pop()**  
This task can be performed using brute force manner. In this, we iterate the
keys and remove the keys using pop, reinitialize them after merging into a
matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge List value Keys to Matrix

# Using loop + pop()

 

# initializing dictionary

test_dict = {'gfg' : [4, 5, 6], 

 'is' : [8, 8, 9],

 'CS' : [1, 3, 8], 

 'Maths' : [1, 2]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing list 

que_list = ['gfg', 'CS', 'Maths']

 

# Merge List value Keys to Matrix

# Using loop + pop()

new_data = [test_dict.pop(ele) for ele in que_list]

test_dict["merge_key"] = new_data

 

# printing result 

print("The dictionary after merging : " + str(test_dict))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘is’: [8, 8, 9], ‘gfg’: [4, 5, 6], ‘Maths’: [1,
> 2], ‘CS’: [1, 3, 8]}  
> The dictionary after merging : {‘is’: [8, 8, 9], ‘merge_key’: [[4, 5, 6],
> [1, 3, 8], [1, 2]]}

