Python Program to Extract Strings with at least given number of characters
from other list



Given a list containing only string elements, the task is to write a Python
program to extract all the strings which have characters from another list
given a number of times.

**Examples:**

>  **Input** : test_list = [“Geeksforgeeks”, “is”, “best”, “for”, “geeks”],
> char_list = [‘e’, ‘t’, ‘s’, ‘m’, ‘n’], K = 2
>
>  **Output :** [‘Geeksforgeeks’, ‘best’, ‘geeks’]
>
>  **Explanation :** is has 1, for has 0 characters from list, hence omitted.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [“Geeksforgeeks”, “is”, “best”, “for”, “geeks”],
> char_list = [‘t’, ‘s’, ‘m’, ‘n’], K = 2
>
>  **Output :** [‘Geeksforgeeks’, ‘best’]
>
>  **Explanation :** Geeksforgeeks has 2 s, and best has 2 elements from
> character list.

 **Method 1 :** _Using_ _list comprehension_ _and_ _sum()_

In this, we perform iteration of characters using list comprehension and sum()
is used to check for matching characters sum, which, if found greater than K,
is added to result list.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["Geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing characters list

char_list = ['e', 't', 's', 'm', 'n']

 

# initializing K

K = 2

 

# sum() computes matching elements frequency

res = [ele for ele in test_list if sum(ch in char_list
for ch in ele) >= K]

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]
>
>  
>
>
>  
>
>
> Filtered Strings : [‘Geeksforgeeks’, ‘best’, ‘geeks’]

 **Method 2 :** _Using_ _filter()_ _,_ _lambda_ _and_ _sum()_

In this, task of filtering is performed using filter(), rest all the
functionalities is performed using similar constructs as above method.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["Geeksforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing characters list

char_list = ['e', 't', 's', 'm', 'n']

 

# initializing K

K = 2

 

# sum() computes matching elements frequency

# filter() used for task of filtering

res = list(filter(lambda ele: sum(ch in char_list
for ch in ele) >= K, test_list))

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘geeks’]
>
> Filtered Strings : [‘Geeksforgeeks’, ‘best’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

