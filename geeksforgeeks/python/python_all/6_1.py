Python – Multiple Sets Intersection



In this article given List of sets, the task is to write a Python program to
perform their intersection.

 **Examples:**

>  **Input :** test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4,
> 5, 3}]
>
>  **Output :** {3, 5}
>
>  **Explanation :** 3 and 5 is present in all the sets.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4,
> 5, 4}]
>
>  **Output :** {5}
>
>  **Explanation :** 5 is present in all the sets.

 **Method #1 : Using** **intersection()** **\+ * operator**

In this, we perform tasks of getting intersection using intersection() and *
operator is used to pack all the sets together.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple Sets Intersection

# Using intersection() + * operator

 

# initializing list

test_list = [{5, 3, 6, 7}, {1, 3, 5, 2},
{7, 3, 8, 5}, {8, 4, 5, 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting all sets intersection using intersection()

res = set.intersection(*test_list)

 

# printing result

print("Intersected Sets : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{3, 5, 6, 7}, {1, 2, 3, 5}, {8, 3, 5, 7}, {8, 3, 4,
> 5}]
>
> Intersected Sets : {3, 5}
>
>  
>
>
>  
>

 **Method #2 : Using** **reduce()** **\+ and_ operator**

In this, we perform task of intersection using and_ operator and reduce() does
the task of getting all the sets packed together for required operation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiple Sets Intersection

# Using reduce() + and_ operator

from operator import and_

from functools import reduce

 

# initializing list

test_list = [{5, 3, 6, 7}, {1, 3, 5, 2},
{7, 3, 8, 5}, {8, 4, 5, 3}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting all sets intersection using and_ operator

res = set(reduce(and_, test_list))

 

# printing result

print("Intersected Sets : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{3, 5, 6, 7}, {1, 2, 3, 5}, {8, 3, 5, 7}, {8, 3, 4,
> 5}]
>
> Intersected Sets : {3, 5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

