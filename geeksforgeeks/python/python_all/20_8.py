Python – Convert tuple list to dictionary with key from a given start value



Given a tuple list, the following article focuses on how to convert it to a
dictionary, with keys starting from a specified start value. This start value
is only to give a head start, next keys will incremented value of their
previous keys.

> **Input** : test_list = [(4, 5), (1, 3), (9, 4), (8, 2), (10, 1)], start = 4  
> **Output** : {4: (4, 5), 5: (1, 3), 6: (9, 4), 7: (8, 2), 8: (10, 1)}  
> **Explanation** : Tuples indexed starting key count from 4.  
>  **Input** : test_list = [(4, 5), (1, 3), (9, 4), (8, 2), (10, 1)], start =
> 6  
> **Output** : {6: (4, 5), 7: (1, 3), 8: (9, 4), 9: (8, 2), 10: (10, 1)}  
> **Explanation** : Tuples indexed starting key count from 6.

**Method 1 :** _Using_ _loop_

In this we construct the dictionary by iterating through each tuple and adding
its position index, starting from start, as key – value pair in dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [(4, 5), (1, 3), (9, 4), (8,
2), (10, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing start

start = 4

 

res = dict()

for sub in test_list:

 

 # assigning positional index

 res[start] = sub

 start += 1

 

# printing result

print("Constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [(4, 5), (1, 3), (9, 4), (8, 2), (10, 1)]
>
> Constructed dictionary : {4: (4, 5), 5: (1, 3), 6: (9, 4), 7: (8, 2), 8:
> (10, 1)}

 **Method 2 :** _Using_ _dict()_ _and_ _enumerate()_

In this, we convert tuple list to dictionary using dict(), and indexing is
provided using enumerate().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [(4, 5), (1, 3), (9, 4), (8,
2), (10, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing start

start = 4

 

res = dict(enumerate(test_list, start=start))

 

# printing result

print("Constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(4, 5), (1, 3), (9, 4), (8, 2), (10, 1)]
>
> Constructed dictionary : {4: (4, 5), 5: (1, 3), 6: (9, 4), 7: (8, 2), 8:
> (10, 1)}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

