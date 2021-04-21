Python – Sort Strings by Maximum ASCII value



Given strings list, perform sort by Maximum Character in String.

> **Input** : test_list = [“geeksforgeeks”, “is”, “best”, “cs”]  
> **Output** : [“geeksforgeeks”, “is”, “cs”, “best”]  
> **Explanation** : s = s = s < t, sorted by maximum character.
>
>  **Input** : test_list = [“apple”, “is”, “fruit”]  
> **Output** : [“apple”, “is”, “fruit”]  
> **Explanation** : p < s < t, hence order retained after sorting by max.
> character.

**Method #1 : Using sort() + max()**

In this, sorting is performed using _sort()_ and _max()_ is used to get
maximum character from Strings.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Maximum Character

# Using sort() + max()

 

# get maximum character fnc.

def get_max(sub):

 

 # returns maximum character

 return ord(max(sub))

 

 

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"cs"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# performing sorting

test_list.sort(key=get_max)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘cs’]  
> Sorted List : [‘for’, ‘geeksforgeeks’, ‘is’, ‘cs’, ‘best’]

 **Method #2 : Using sorted() + lambda + max()**

In this, we perform task of sorting using _sorted()_ , _lambda_ and _max()_
are used to input logic of getting maximum character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Maximum Character

# Using sorted() + lambda + max()

 

# initializing list

test_list = ["geeksforgeeks", "is", "best", "for",
"cs"]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# performing sorting using sorted()

# lambda function provides logic

res = sorted(test_list, key=lambda sub: ord(max(sub)))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘geeksforgeeks’, ‘is’, ‘best’, ‘for’, ‘cs’]  
> Sorted List : [‘for’, ‘geeksforgeeks’, ‘is’, ‘cs’, ‘best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

