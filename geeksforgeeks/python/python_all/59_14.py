Python – Convert Dictionary Value list to Dictionary List



Sometimes, while working with Python Dictonaries, we can have a problem in
which we need to convert dictionary list to nested records dictionary taking
each index of dictionary list value and flattening it. This kind of problem
can have application in many domains. Let’s discuss certain ways in which this
task can be performed.

>  **Input** : test_list = [{‘Gfg’: [5, 6]}, {‘best’: [3, 1]}]  
>  **Output** : [{‘Gfg’: 5, ‘best’: 3}, {‘Gfg’: 6, ‘best’: 1}]
>
>  **Input** : test_list = [{‘Gfg’: [5]}]  
>  **Output** : [{‘Gfg’: 5}]

 **Method #1 : Using loop**  
This is one of the ways in which this problem can be solved. In this, we
perform the task in brute force manner iterating each list value index and
designating a key to it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionary Value list to Dictionary List

# Using loop

 

# initializing list

test_list = [{'Gfg' : [5, 6, 5]}, {'is' : [10,
2, 3]}, {'best' : [4, 3, 1]}] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Dictionary Value list to Dictionary List

# Using loop

res =[{} for idx in range(len(test_list))]

idx = 0

for sub in test_list:

 for key, val in sub.items(): 

 for ele in val:

 res[idx][key] = ele

 idx += 1

 idx = 0

 

# printing result 

print("Records after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list is : [{‘Gfg’: [5, 6, 5]}, {‘is’: [10, 2, 3]}, {‘best’: [4,
> 3, 1]}]  
> Records after conversion : [{‘Gfg’: 5, ‘is’: 10, ‘best’: 4}, {‘Gfg’: 6,
> ‘is’: 2, ‘best’: 3}, {‘Gfg’: 5, ‘is’: 3, ‘best’: 1}]

