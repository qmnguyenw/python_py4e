Python program to sort a dictionary list based on the maximum value



Given list with dictionaries as elements, write a Python program to sort the
dictionary on the basis maximum value in a key value pair of a dictionary. In
simpler terms, first each element of a list (which is a dictionary) will be
checked, meaning each key value pair will be compared to find the element with
maximum value. Then, in the list sorting will be done on the basis of which
element contains maximum value so obtained.

 **Examples:**

>  **Input** : test_list = [{1:5, 6:7, 9:1}, {2:6, 9:10, 1:4}, {6:5, 9:3,
> 1:6}]  
> **Output** : [{6: 5, 9: 3, 1: 6}, {1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}]  
> **Explanation** : 6 < 7 < 10, is maximum elements ordering.
>
>   * 6 is maximum in dictionary having 5, 3, 6 as values in a key-value pair
>   * 7 is maximum in dictionary having 5, 7, 1 as values in a key-value pair
> and
>   * 10 is maximum in dictionary having 6, 10, 4 as values in a key-value
> pair.
>

>
>  **Input** : test_list = [{1:5, 6:7, 9:1}, {2:6, 9:10, 1:4}]  
> **Output** : [{1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}]  
> **Explanation** : 7 < 10,
>
>   * 7 is maximum in dictionary having 5, 7, 1 as values in a key-value pair
>   * 10 is maximum in dictionary having 6, 10, 4 as values in a key-value
> pair  
>
>

**Method #1 :** _Using_ _values()_ _,_ _max()_ _and_ _sort()_

  

  

In this, we perform the task of in-place sorting using sort(), get maximum
value using max(), and values using values(). External function is passed as
parameter to achieve required functionality.  

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# getting max value

def get_max(dicts):

 return max(list(dicts.values()))

 

 

# initializing list

test_list = [{1: 5, 6: 7, 9: 1}, {2: 6,
9: 10, 1: 4}, {6: 5, 9: 3, 1: 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting dictionary list by maximum value

test_list.sort(key=get_max)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}, {6: 5, 9:
> 3, 1: 6}]
>
> Sorted List : [{6: 5, 9: 3, 1: 6}, {1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}]

 **Method #2 :** _Using_ _sorted(),_ ___lambda_ _,_ _max()_ _and_ _values()_

In this, we perform sorting using sorted() and lambda function, to provide
single statement filtering rather than calling the external function.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [{1: 5, 6: 7, 9: 1}, {2: 6,
9: 10, 1: 4}, {6: 5, 9: 3, 1: 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting dictionary list by maximum value

# one statement sort

res = sorted(test_list, key=lambda dicts:
max(list(dicts.values())))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}, {6: 5, 9:
> 3, 1: 6}]
>
> Sorted List : [{6: 5, 9: 3, 1: 6}, {1: 5, 6: 7, 9: 1}, {2: 6, 9: 10, 1: 4}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

