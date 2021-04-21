Python – Test for Unique Frequencies



Given a list, find if frequencies of each element of values are in itself
unique values.

>  **Input** : test_list = [4, 3, 2]  
>  **Output** : False  
>  **Explanation** : All have 1 as frequency, hence duplicacy, hence False
>
>  **Input** : test_list = [4, 3, 3, 2, 2, 2]  
>  **Output** : True  
>  **Explanation** : 1, 2, 3 are frequecies of 4, 3, 2 respectively, unique,
> hence True

 **Method #1 : Using loop +set()**  
The combination of above functionalities provide brute force way to solve this
problem. In this, we memoize the frequency of elements by incrementing the
index of value occurred. Then set() is used to remove duplicates and test if
it’s length is same as before the conversion.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Unique Frequencies

# Using loop + set()

 

# initializing list

test_list = [4, 3, 2, 2, 3, 4, 4, 4,
1, 2]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Test for Unique Frequencies

res = False

temp = [0] * 5

for ele in test_list:

 

 # performing memoization in temp list

 temp[ele] += 1

mem_list = temp[1:]

 

# checking for set converted list length with original list

if len(list(set(mem_list))) == len(mem_list):

 res = True

 

# printing result 

print("Are element's Frequencies Unique ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [4, 3, 2, 2, 3, 4, 4, 4, 1, 2]
    Are element's Frequencies Unique ? : True
    

