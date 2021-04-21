Python program to sort tuples by frequency of their absolute difference



Given list of dual tuples, the task here is to write a python program that can
sort them by frequency of their elements’ absolute difference.

>  **Input** : [(1, 6), (11, 3), (9, 1), (6, 11), (2, 10), (5, 7)]
>
>  **Output :** [(5, 7), (1, 6), (6, 11), (11, 3), (9, 1), (2, 10)]
>
>  **Explanation :** 7 – 5 = 2 occurs only 1 time. 5 occurs twice [( 6 – 1),
> (11 – 6)] and 8 occurs 3 times as difference.
>
>  **Input :** [(1, 6), (6, 11), (5, 7)]
>
>  
>
>
>  
>
>
>  **Output :** [(5, 7), (1, 6), (6, 11)]
>
>  **Explanation :** 7 – 5 = 2 occurs only 1 time. 5 occurs twice [( 6 – 1),
> (11 – 6)].

 **Method :** _Using_ _sorted()_ _,_ _abs()_ _,_ _count()_ _and_ _list
comprehension_

In this, we perform task of computing each absolute difference using abs() and
list comprehension. Then, sorted() and count() are used to sort tuples based
on computed results of absolute difference.

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

test_list = [(1, 6), (11, 3), (9, 1), (6,
11), (2, 10), (5, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting differences pairs

diff_list = [abs(x - y) for x, y in test_list]

 

# sorting list by computed differences

res = sorted(test_list, key = lambda sub:
diff_list.count(abs(sub[0] - sub[1])))

 

# printing result

print("Sorted Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(1, 6), (11, 3), (9, 1), (6, 11), (2, 10), (5, 7)]
>
> Sorted Tuples : [(5, 7), (1, 6), (6, 11), (11, 3), (9, 1), (2, 10)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

