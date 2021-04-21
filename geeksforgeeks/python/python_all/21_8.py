Python – Extract rows with Even length strings



In this article we have a given Matrix, extract rows which are of even
lengths.

>  **Input** : test_list = [[“gfg”, “is”, “best”], [“best”, “good”, “geek”],
> [“is”, “better”], [“for”, “cs”]]  
> **Output** : [[‘best’, ‘good’, ‘geek’], [‘is’, ‘better’]]  
> **Explanation** : All strings are of even length.  
>  **Input** : test_list = [[“gfg”, “is”, “best”], [“best”, “good”, “geeks”],
> [“is”, “better”], [“for”, “cs”]]  
> **Output** : [[‘is’, ‘better’]]  
> **Explanation** : All strings are of even length.

**Method #1 : Using all() + list comprehension + len()**

In this, we check for all the strings in each row, its length, and check if
length is even, if all strings in row have even length, then its added to
result list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract rows with Even length strings

# Using all() + list comprehension + len()

 

# initializing list

test_list = [["gfg", "is", "best"], ["best", "good",
"geek"], ["is", "better"], ["for", "cs"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for all elements in row

res = [row for row in test_list if all(len(ele) %
2 == 0 for ele in row)]

 

# printing result 

print("Rows with even length : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

> The original list is : [[‘gfg’, ‘is’, ‘best’], [‘best’, ‘good’, ‘geek’],
> [‘is’, ‘better’], [‘for’, ‘cs’]]  
> Rows with even length : [[‘best’, ‘good’, ‘geek’], [‘is’, ‘better’]]

