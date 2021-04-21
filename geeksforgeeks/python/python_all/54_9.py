Python – Produce K evenly spaced float values



Given a range and element K, generate K float values which are evenly spaced.

>  **Input** : i = 4, j = 6, K = 10
>
>  **Output** : [4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0]
>
>  **Explanation** : The difference 0.2 is added after 4 to produce 10
> elements till 6.
>
>  **Input** : i = 10, j = 20, K = 2
>
>  
>
>
>  
>
>
>  **Output** : [15.0, 20.0]
>
>  **Explanation** : 5 is difference and is added each time.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate till K while increasing the counter for difference between successive
elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Produce K evenly spaced float values

# Using loop

 

# initializing range

i, j = 2, 10

 

# Initialize K

K = 15

 

# computing difference

diff = (j - i) / K

res = []

 

# using loop to add numbers to result

for idx in range(1, K + 1):

 res.append(i + (diff * idx))

 

# printing result

print("The constructed list : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The constructed list : [2.533333333333333, 3.0666666666666664, 3.6,
> 4.133333333333333, 4.666666666666666, 5.2, 5.733333333333333,
> 6.266666666666667, 6.8, 7.333333333333333, 7.866666666666666, 8.4,
> 8.933333333333334, 9.466666666666667, 10.0]

 **Method #2 : Using list comprehension**

The working of this method is similar to above method. The difference being
compact way in which this solution is formulated using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Produce K evenly spaced float values

# Using loop

 

# initializing range

i, j = 2, 10

 

# Initialize K

K = 15

 

# computing difference

diff = (j - i) / K

 

# using list comprehension to formulate elements

res = [i + (diff * idx) for idx in range(1, K +
1)]

 

# printing result

print("The constructed list : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The constructed list : [2.533333333333333, 3.0666666666666664, 3.6,
> 4.133333333333333, 4.666666666666666, 5.2, 5.733333333333333,
> 6.266666666666667, 6.8, 7.333333333333333, 7.866666666666666, 8.4,
> 8.933333333333334, 9.466666666666667, 10.0]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

