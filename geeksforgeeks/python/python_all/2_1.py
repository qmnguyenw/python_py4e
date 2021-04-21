Python Program to Join Equi-hierarchy Strings



Given a list of strings with several hierarchies, the task is to write a
python program to join those which have the same hierarchies.

Elements in the same dimension before a dimension change are known to be in
the same hierarchy.

>  **Input :** test_list = [“gfg “, ” best “, [” for “, ” all “], ” all “, [”
> CS ” , ” geeks “]]
>
>  **Output :** [‘gfg best ‘, [‘ for all ‘], ‘ all ‘, [‘ CS geeks ‘]]
>
>  **Explanation :** Strings at similar hierarchy as joined.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [“gfg “, ” best “, [” for “, ” all “], [” CS ” , ”
> geeks “]]
>
>  **Output :** [‘gfg best ‘, [‘ for all ‘], [‘ CS geeks ‘]]
>
>  **Explanation :** Strings at similar hierarchy as joined.

 **Method 1 :** Using type(), loop, recursion and join()

In this, the list element is checked to be string using type(), if found, the
joining task is performed using join for that hierarchy. If element is found
to be list, the inner list is recurred for similar logic for next level of
hierarchy.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def hierjoin(test_list):

 res = []

 temp = []

 val = None

 for sub in test_list:

 

 # if string then appended

 if type(sub) == str:

 temp.append(sub)

 

 # if list, the string is joined for hierarchy

 # recurred for inner list

 else:

 res.append(''.join(temp))

 temp = []

 val = hierjoin(sub)

 res.append(val)

 if temp != []:

 res.append(''.join(temp))

 return res

 

 

# initializing list

test_list = ["gfg ", " best ", [" for ", " all "],

 " all ", [" CS ", " geeks "]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling recursion

res = hierjoin(test_list)

 

# printing result

print("The joined strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg ‘, ‘ best ‘, [‘ for ‘, ‘ all ‘], ‘ all ‘, [‘ CS
> ‘, ‘ geeks ‘]]
>
>  
>
>
>  
>
>
> The joined strings : [‘gfg best ‘, [‘ for all ‘], ‘ all ‘, [‘ CS geeks ‘]]

 **Method 2 :** Using join(), map(), recursion and groupby()

In this equihierarchy groups are formed using groupby(). Then map() is used to
call the recursion function for inner hierarchy of list strings.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import groupby

 

 

def hierjoin(test_list):

 

 # groups are formed for similar hierarchy using groupby

 return [idx for x, y in groupby(test_list,
key=str.__instancecheck__)

 for idx in ([''.join(y)] if x else map(hierjoin, y))]

 

 

# initializing list

test_list = ["gfg ", " best ", [" for ", " all "],

 " all ", [" CS ", " geeks "]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling recursion

res = hierjoin(test_list)

 

# printing result

print("The joined strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg ‘, ‘ best ‘, [‘ for ‘, ‘ all ‘], ‘ all ‘, [‘ CS
> ‘, ‘ geeks ‘]]
>
> The joined strings : [‘gfg best ‘, [‘ for all ‘], ‘ all ‘, [‘ CS geeks ‘]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

