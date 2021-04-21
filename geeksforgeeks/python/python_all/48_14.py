Python – Add custom values key in List of dictionaries



Given a list of dictionaries, custom list and Key, add the key to each
dictionary with list values in order.

>  **Input** : test_list = [{“Gfg” : 6, “is” : 9, “best” : 10}, {“Gfg” : 8,
> “is” : 11, “best” : 19}, {“Gfg” : 2, “is” : 16, “best” : 10}], K = “Geeks”,
> append_list = [6, 7, 4]  
>  **Output** : [{“Gfg” : 6, “is” : 9, “best” : 10, “Geeks” : 6}, {“Gfg” : 8,
> “is” : 11, “best” : 19, “Geeks” : 7}, {“Gfg” : 2, “is” : 16, “best” : 10,
> “Geeks” : 4}]  
>  **Explanation** : “Geeks” key added in each dictionary.
>
>  **Input** : test_list = [{“Gfg” : 6, “is” : 9, “best” : 10}], K = “CS”,
> append_list = [6]  
>  **Output** : [{“Gfg” : 6, “is” : 9, “best” : 10, “CS” : 6}]  
>  **Explanation** : “CS” key added in each dictionary with 6 as value.

 **Method #1 : Using loop + enumerate()**

This is one of the ways in which this task can be performed. In this, we
iterate through the dictionary using enumerate() to get indices, and keep
assigning to each dictionary key with its index value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add custom values key in List of dictionaries

# Using loop

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing Key 

K = "CS"

 

# initializing list 

append_list = [6, 7, 4, 3, 9]

 

# using enumerate() to iterate for index and values

for idx, ele in enumerate(test_list):

 ele[K] = append_list[idx]

 

# printing result 

print("The dictionary list after addition : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The dictionary list after addition : [{'Gfg': 6, 'is': 9, 'best': 10, 'CS': 6}, {'Gfg': 8, 'is': 11, 'best': 19, 'CS': 7}, {'Gfg': 2, 'is': 16, 'best': 10, 'CS': 4}, {'Gfg': 12, 'is': 1, 'best': 8, 'CS': 3}, {'Gfg': 22, 'is': 6, 'best': 8, 'CS': 9}]
    
    

**Method #2 : Using zip() + loop**

This is yet another way in which this task can be performed. In this, we
perform mapping of list values with each dictionary using zip().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add custom values key in List of dictionaries

# Using zip() + loop

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing Key 

K = "CS"

 

# initializing list 

append_list = [6, 7, 4, 3, 9]

 

# zip() used to bind index wise 

# list and dictionary

for dic, lis in zip(test_list, append_list):

 dic[K] = lis

 

# printing result 

print("The dictionary list after addition : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The dictionary list after addition : [{'Gfg': 6, 'is': 9, 'best': 10, 'CS': 6}, {'Gfg': 8, 'is': 11, 'best': 19, 'CS': 7}, {'Gfg': 2, 'is': 16, 'best': 10, 'CS': 4}, {'Gfg': 12, 'is': 1, 'best': 8, 'CS': 3}, {'Gfg': 22, 'is': 6, 'best': 8, 'CS': 9}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

