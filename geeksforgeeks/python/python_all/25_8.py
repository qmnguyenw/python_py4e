Python – Sort Matrix by Maximum String Length



Given a matrix, perform row sort basis on the maximum length of the string in
it.

>  **Input** : test_list = [[‘gfg’, ‘best’], [‘geeksforgeeks’], [‘cs’,
> ‘rocks’], [‘gfg’, ‘cs’]]  
> **Output** : [[‘gfg’, ‘cs’], [‘gfg’, ‘best’], [‘cs’, ‘rocks’],
> [‘geeksforgeeks’]]  
> **Explanation** : 3 < 4 < 5 < 13, maximum lengths of strings, sorted
> increasingly.
>
>  **Input** : test_list = [[‘gfg’, ‘best’], [‘cs’, ‘rocks’], [‘gfg’, ‘cs’]]  
> **Output** : [[‘gfg’, ‘cs’], [‘gfg’, ‘best’], [‘cs’, ‘rocks’]]  
> **Explanation** : 3 < 4 < 5 maximum lengths of strings, sorted increasingly.

**Method #1 : Using sort() +** **len()** **+** **max()**

In this, inplace sorting is performed using sort(), len() and max() compute
the maximum length of the string in each row to perform the sort.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Maximum String Length

# Using sort() + len() + max()

 

 

def max_len(row):

 

 # getting Maximum length of string

 return max([len(ele) for ele in row])

 

 

# initializing list

test_list = [['gfg', 'best'], ['geeksforgeeks'],

 ['cs', 'rocks'], ['gfg', 'cs']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort()

test_list.sort(key=max_len)

 

# printing result

print("Sorted Matrix : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘best’], [‘geeksforgeeks’], [‘cs’, ‘rocks’],
> [‘gfg’, ‘cs’]]  
> Sorted Matrix : [[‘gfg’, ‘cs’], [‘gfg’, ‘best’], [‘cs’, ‘rocks’],
> [‘geeksforgeeks’]]

 **Method #2 : Using** **sorted()** **+** **lambda** **\+ max() +** **len()**

In this, we perform task of filtering maximum using lambda function rather
than external function. The task of sorting is performed using sorted().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Maximum String Length

# Using sorted() + lambda + max() + len()

 

# initializing list

test_list = [['gfg', 'best'], ['geeksforgeeks'],

 ['cs', 'rocks'], ['gfg', 'cs']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing logic using lambda fnc.

res = sorted(test_list, key=lambda row: max([len(ele)
for ele in row]))

 

# printing result

print("Sorted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg’, ‘best’], [‘geeksforgeeks’], [‘cs’, ‘rocks’],
> [‘gfg’, ‘cs’]]  
> Sorted Matrix : [[‘gfg’, ‘cs’], [‘gfg’, ‘best’], [‘cs’, ‘rocks’],
> [‘geeksforgeeks’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

