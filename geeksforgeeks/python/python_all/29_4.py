Python Program to remove elements that are less than K difference away in a
list



Given a list, perform removal of those elements whose difference is less than
K from its previous element.

>  **Input** : test_list = [3, 19, 5, 8, 10, 13], K = 4  
> **Output** : [3, 8, 13, 19]  
> **Explanation** : 5 – 3 = 2, 2<4, hence 5 is removed, similarly, 10 – 8 is
> 2, less than K.
>
>  **Input** : test_list = [15, 7, 20], K = 4  
> **Output** : [7, 15, 20]  
> **Explanation** : No deletion required.

**Approach:** _ ****_ Using loop and sorted()

In this, first, the list has to be sorted and then removal of elements that do
not have appropriate distance between its preceding and succeeding element is
performed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [3, 19, 4, 8, 10, 13]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# sorting list 

test_list = sorted(test_list)

 

idx = 0

while idx < len(test_list) - 1:

 

 # checking for difference

 if test_list[idx] + K > test_list[idx + 1]:

 

 # deleting if K closer

 del test_list[idx + 1]

 else:

 idx += 1

 

# printing result 

print("Required List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [3, 19, 4, 8, 10, 13]
>
> Required List : [3, 8, 13, 19]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

