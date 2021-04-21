Python – Convert list to Single Dictionary Key Value list



Sometimes, while working with Python lists, we can have a problem in which we
need to convert the list into a dictionary, which has single key, the Kth
element of list, and others as it’s list value. This kind of problem can have
application in data domains. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_list = [6, 5, 3, 2], K = 1  
>  **Output** : {5 : [6, 3, 2]}
>
>  **Input** : test_list = [6, 5, 3, 2], K = 2  
>  **Output** : {5 : [6, 5, 2]}

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this, we
create a key initially and then append values except K index to create
dictionary list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list to Single Dictionary Key Value list

# Using loop

 

# initializing list

test_list = [5, 6, 3, 8, 9] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# Convert list to Single Dictionary Key Value list

# Using loop

res = {test_list[K] : []}

for idx in range(len(test_list)):

 if idx != K:

 res[test_list[K]].append(test_list[idx])

 

# printing result 

print("Records after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [5, 6, 3, 8, 9]
    Records after conversion : {8: [5, 6, 3, 9]}
    

