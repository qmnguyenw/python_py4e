Python – Append given number with every element of the list



Given a list and a number, write a Python program to append the number with
every element of the list.

 **Examples:**

>  **input = [1,2,3,4,5]**
>
>  **key = 5** (number to be appended)
>
>  **output = [1,5,2,5,3,5,4,5,5,5]**
>
>  
>
>
>  
>

The following are ways to achieve this functionality:

 **Method 1:** _Using_ _for loop_

## Python

 __

 __  
 __

 __

 __  
 __  
 __

input = [1, 2, 3, 4, 5]

key = 7

 

result = []

for ele in input:

 result.append(ele)

 result.append(key)

 

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 7, 2, 7, 3, 7, 4, 7, 5, 7]

 **Method 2:** _Using_ _list comprehension_ _and_ _itertools.chain_

## Python

 __

 __  
 __

 __

 __  
 __  
 __

import itertools

 

input = [1, 2, 3, 4, 5]

key = 7

 

result = list(itertools.chain(*[[ele, key] for ele in
input]))

 

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 7, 2, 7, 3, 7, 4, 7, 5, 7]

 **Method 3:** _Using_ _zip_ _and_ _for loop_

## Python

 __

 __  
 __

 __

 __  
 __  
 __

input = [1, 2, 3, 4, 5]

key = 7

 

result = []

for x, y in zip(input, [key]*len(input)):

 result.extend([x, y])

 

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 7, 2, 7, 3, 7, 4, 7, 5, 7]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

