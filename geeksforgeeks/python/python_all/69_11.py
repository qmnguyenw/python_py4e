Python – Rearrange dictionary for consective value-keys



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to rearrange dictionary keys so as a value is followed by same
key in dictionary. This problem can have application in competitive
programming algorithms and Graph problems. Let’s discuss certain ways in which
this task can be performed.

>  **Input** : test_dict = {1 : 2, 3 : 2, 2 : 3}  
>  **Output** : {1: 2, 2: 3, 3: 2}
>
>  **Input** : test_dict = {1 : 2}  
>  **Output** : {1 : 2}

 **Method #1 : Using loop +keys()**  
The combination of above functions can be used to solve this problem. In this,
we extract the dictionary keys using keys() and iterate till we find value
succeded by equal key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rearrange dictionary for consective value-keys

# Using loop + keys()

 

# initializing dictionary

test_dict = {1 : 3, 4 : 5, 3 : 4, 5 : 6}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Rearrange dictionary for consective value-keys

# Using loop + keys()

temp = list(test_dict.keys())[0]

res = {}

while len(test_dict) > len(res):

 res[temp] = temp = test_dict[temp]

 

# printing result 

print("The rearranged dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary : {1: 3, 4: 5, 3: 4, 5: 6}
    The rearranged dictionary : {1: 3, 3: 4, 4: 5, 5: 6}
    

