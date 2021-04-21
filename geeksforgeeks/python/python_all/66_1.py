Python – Ranged Maximum Element in String List



Sometimes, while working with Python data, we can have a problem in which we
have data in form of String List and we require to find the maximum element in
that data, but that also in a certain range of indices. This is quite peculiar
problem but can have application in data domains. Let’s discuss certain ways
in which this task can be performed.

>  **Input** :  
> test_list = [’34, 78, 98, 23, 12′, ’76, 65, 54, 43, 21′]  
> i, j = 1, 3  
>  **Output** : 76
>
>  **Input** :  
> test_list = [’34, 78, 98, 23, 12′, ’76, 65, 54, 43, 21′]  
> i, j = 3, 5  
>  **Output** : 98

 **Method #1 : Usingmax() + split() \+ list comprehension**  
The combination of above functions is used to solve this problem. In this, we
perform the split of each strings element in list, in a particular range, and
then max() is used to find the maximum element in that range across each list.
First, maximum amongst the sublist and then amongst the other indices.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ranged Maximum Element in String Matrix

# Using max() + split() + list comprehension

 

# initializing list

test_list = ['34, 78, 98, 23, 12',

 '76, 65, 54, 43, 21',

 '82, 45, 32, 45, 32',

 '78, 34, 12, 34, 10']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Range 

i, j = 2, 4

 

# Ranged Maximum Element in String Matrix

# Using max() + split() + list comprehension

res = max([max(idx.split(', ')[i - 1: j]) for idx
in test_list])

 

# printing result 

print("The maximum ranged element : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [’34, 78, 98, 23, 12′, ’76, 65, 54, 43, 21′, ’82, 45,
> 32, 45, 32′, ’78, 34, 12, 34, 10′]  
> The maximum ranged element : 98

