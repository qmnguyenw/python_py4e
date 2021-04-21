Python – Check for Sublist in List



Sometimes, while working with Python Lists, we can have a problem in which we
need to check if a particular sublist is contained in exact sequence in a
list. This task can have application in many domains such as school
programming and web development. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_list = [5, 6, 3, 8, 2, 1, 7, 1], sublist = [8, 2, 3]  
>  **Output** : False
>
>  **Input** : test_list = [5, 6, 3, 8, 2, 3, 7, 1], sublist = [8, 2, 3]  
>  **Output** : True

 **Method #1 : Using loop + list slicing**  
The combination of above functions can be used to solve this problem. In this,
we perform task of checking for sublist by incremental slicing using list
slicing technique.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Sublist in List

# Using loop + list slicing

 

# initializing list

test_list = [5, 6, 3, 8, 2, 1, 7, 1]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing sublist 

sublist = [8, 2, 1]

 

# Check for Sublist in List

# Using loop + list slicing

res = False

for idx in range(len(test_list) - len(sublist) + 1):

 if test_list[idx : idx + len(sublist)] == sublist:

 res = True

 break

 

# printing result 

print("Is sublist present in list ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [5, 6, 3, 8, 2, 1, 7, 1]
    Is sublist present in list ? : True
    

