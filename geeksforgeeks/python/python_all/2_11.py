Python – Count the frequency of matrix row length



Given a Matrix, the task is to write a Python program to get the count
frequency of its rows lengths.

>  **Input :** test_list = [[6, 3, 1], [8, 9], [2], [10, 12, 7], [4, 11]]
>
>  **Output :** {3: 2, 2: 2, 1: 1}
>
>  **Explanation :** 2 lists of length 3 are present, 2 lists of size 2 and 1
> of 1 length is present.
>
>  **Input :** test_list = [[6, 3, 1], [8, 9], [10, 12, 7], [4, 11]]
>
>  
>
>
>  
>
>
>  **Output :** {3: 2, 2: 2}
>
>  **Explanation :** 2 lists of length 3 are present, 2 lists of size 2.

 **Method #1 : Using** **dictionary** **+** **loop**

In this we check for each row length, if length has occurred in the memorize
dictionary, then the result is incremented or if a new size occurs, the
element is registered as new.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Row lengths counts

# Using dictionary + loop

 

# initializing list

test_list = [[6, 3, 1], [8, 9], [2], 

 [10, 12, 7], [4, 11]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

for sub in test_list:

 

 # initializing incase of new length

 if len(sub) not in res:

 res[len(sub)] = 1

 

 # increment in case of length present

 else:

 res[len(sub)] += 1

 

# printing result

print("Row length frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[6, 3, 1], [8, 9], [2], [10, 12, 7], [4, 11]]
    Row length frequencies : {3: 2, 2: 2, 1: 1}

 **Method #2 : Using** **Counter()** **+** **map()** **+** **len()**

In this, map() and len() get the lengths of each sublist in the matrix,
Counter is used to keep the frequency of each of the lengths.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Row lengths counts

# Using Counter() + map() + len()

from collections import Counter

 

# initializing list

test_list = [[6, 3, 1], [8, 9], [2],

 [10, 12, 7], [4, 11]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Counter gets the frequencies of counts

# map and len gets lengths of sublist

res = dict(Counter(map(len, test_list)))

 

# printing result

print("Row length frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[6, 3, 1], [8, 9], [2], [10, 12, 7], [4, 11]]
    Row length frequencies : {3: 2, 2: 2, 1: 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

