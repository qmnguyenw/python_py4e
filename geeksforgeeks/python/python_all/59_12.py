Python – Values from custom List in Records



Sometimes, while working with Python records, we can have a problem in which
we need to extract all the values from the custom list in list dictionary
records. This problem can have application in domains such as web development
and school programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** :  
> test_list = [{‘name’ : ‘Gfg’, ‘id’ : 1, ‘Score’ : 3}, {‘name’ : ‘is’, ‘id’ :
> 4, ‘Score’ : 10},  
> {‘name’ : ‘Best’, ‘Score’ : 12}]  
> get_list = [‘name’]  
>  **Output** : [[‘Gfg’], [‘is’], [‘Best’]]
>
>  **Input** :  
> test_list = [{‘name’ : ‘Gfg’, ‘id’ : 1, ‘Score’ : 3}, {‘name’ : ‘is’, ‘id’ :
> 4, ‘Score’ : 10},  
> {‘name’ : ‘Best’, ‘Score’ : 12}]  
> get_list = [‘Serial’]  
>  **Output** : [[None], [None], [None]]

 **Method #1 : Using list comprehension +get()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of iterating through each dictionary using list
comprehension and get() is used to fetch dictionary values and also handle for
non present values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values from custom List in Records

# Using list comprehension + get()

 

# initializing list

test_list = [{'name' : 'Gfg', 'id' : 1, 'Score' :
3},

 {'name' : 'is', 'id' : 4, 'Score' : 10},

 {'name' : 'Best', 'Score' : 12}]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing Get list 

get_list = ['name', 'id']

 

# Values from custom List in Records

# Using list comprehension + get()

res = [list(idx.get(sub) for sub in get_list) for idx
in test_list]

 

# printing result 

print("All extracted values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [{'name': 'Gfg', 'id': 1, 'Score': 3}, {'name': 'is', 'id': 4, 'Score': 10}, {'name': 'Best', 'Score': 12}]
    All extracted values : [['Gfg', 1], ['is', 4], ['Best', None]]
    

