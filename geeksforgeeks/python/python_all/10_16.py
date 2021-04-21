Python Program to print strings based on the list of prefix



Given a Strings List, the task here is to write a python program that can
extract all the strings whose prefix match any one of custom prefixes given in
another list.

>  **Input** : test_list = [“geeks”, “peeks”, “meeks”, “leeks”, “mean”],
> pref_list = [“ge”, “ne”, “me”, “re”]  
> **Output** : [‘geeks’, ‘meeks’, ‘mean’]  
> **Explanation** : geeks, meeks and mean have prefix, ge, me and me
> respectively, present in prefix list.
>
>  **Input** : test_list = [“geeks”, “peeks”, “meeks”, “leeks”, “mean”],
> pref_list = [“ge”, “le”, “me”, “re”]  
> **Output** : [‘geeks’, ‘meeks’, ‘mean’, leeks]  
> **Explanation** : geeks, meeks, leeks and mean have prefix, ge, me, me and
> le respectively, present in prefix list.  
>

**Method 1 :** Using list comprehension, any() and startswith()

In this, we perform task of checking all elements to match using any() and
startswith() extracts all the prefix. List comprehension is used to iterate
through all the strings in list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing List

test_list = ["geeks", "peeks", "meeks", "leeks",
"mean"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix list

pref_list = ["ge", "ne", "me", "re"]

 

# checking for all possible allowed prefixes using any()

res = [ele for ele in test_list if any(ele.startswith(el)
for el in pref_list)]

 

# printing result

print("The extracted prefix strings list : " + str(res))  
  
---  
  
 __

 __

  
**Output:**

> The original list is : [‘geeks’, ‘peeks’, ‘meeks’, ‘leeks’, ‘mean’]
>
> The extracted prefix strings list : [‘geeks’, ‘meeks’, ‘mean’]

**Method 2 :** Using filter(), lambda, any() and startswith()

This is similar to above method, difference being that filtering is performed
using filter() and lambda.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing List

test_list = ["geeks", "peeks", "meeks", "leeks",
"mean"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix list

pref_list = ["ge", "ne", "me", "re"]

 

# checking for all possible allowed prefixes using any()

# filtering using filter() and lambda

res = list(filter(lambda ele: any(ele.startswith(el)

 for el in pref_list), test_list))

 

# printing result

print("The extracted prefix strings list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeks’, ‘peeks’, ‘meeks’, ‘leeks’, ‘mean’]
>
> The extracted prefix strings list : [‘geeks’, ‘meeks’, ‘mean’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

