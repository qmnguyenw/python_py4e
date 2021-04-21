Python – Random insertion of elements K times



Given 2 list, insert random elements from List 2 to List 1, K times at random
position.

>  **Input** : test_list = [5, 7, 4, 2, 8, 1], add_list = [“Gfg”, “Best”,
> “CS”], K = 2  
>  **Output** : [5, 7, 4, 2, 8, 1, ‘Best’, ‘Gfg’]  
>  **Explanation** : Random elements from List 2 are added 2 times.
>
>  **Input** : test_list = [5, 7, 4, 2, 8, 1], add_list = [“Gfg”, “Best”,
> “CS”], K = 1  
>  **Output** : [5, 7, 4, 2, 8, 1, ‘Gfg’]  
>  **Explanation** : Random elements from List 2 are added 1 times.

 **Method : Using randint() + list slicing + loop + choice()**

In this, choice() is used to get random elements from list 2 to insert into
list 1 and, randint() is used to get index at which this needs to be inserted.
Then list slicing is used to remake list according to newer order.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random insertion of elements K times

# Using randint() + list slicing + loop + choice()

import random

 

# initializing list

test_list = [5, 7, 4, 2, 8, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing add list 

add_list = ["Gfg", "Best", "CS"]

 

# initializing K 

K = 3

 

for idx in range(K):

 

 # choosing index to enter element

 index = random.randint(0, len(test_list))

 

 # reforming list and getting random element to add

 test_list = test_list[:index] + [random.choice(add_list)] +
test_list[index:]

 

# printing result 

print("The created List : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 4, 2, 8, 1]
    The created List : [5, 7, 4, 2, 'Best', 8, 1, 'Best', 'Gfg']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

