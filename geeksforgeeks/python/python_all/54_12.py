Python – Get Random Range Average



Given range and Size of elements, extract random numbers within a range, and
perform average of it.

>  **Input** : N = 3, strt_num = 10, end_num = 15  
>  **Output** : 13.58  
>  **Explanation** : Random elements extracted between 10 and 15, averaging
> out to 13.58.
>
>  **Input** : N = 2, strt_num = 13, end_num = 18  
>  **Output** : 15.82  
>  **Explanation** : 2 elements average to 15.82 in this case.

 **Method #1 : Using loop +uniform()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting numbers using uniform() and loop is used to
perform addition of numbers. The average is computed at end by dividing by
size.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random Range Average

# Using loop + uniform()

import random

 

# initializing N

num = 4

 

# Initialize strt_num

strt_num = 15

 

# Initialize end_num

end_num = 60

 

# Using loop + uniform()

res = 0.0

for _ in range(num): 

 

 # performing summation of range elements

 res += random.uniform(strt_num, end_num)

 

# performing average

res = res / num

 

# printing result 

print("The average value : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The average value : 42.980287235196116
    

