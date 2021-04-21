Python – Sort Matrix by total characters



Given a String Matrix, sort by total data, i.e total characters in each row.

>  **Input** : test_list = [[“Gfg”, “is”, “Best”], [“Geeksforgeeks”, “Best”],
> [“ILvGFG”]]  
> **Output** : [[‘ILvGFG’], [‘Gfg’, ‘is’, ‘Best’], [‘Geeksforgeeks’, ‘Best’]]  
> **Explanation** : 6 < 11 < 17 total characters respectively after sorting.
>
>  **Input** : test_list = [[“Geeksforgeeks”, “Best”], [“ILvGFG”]]  
> **Output** : [[‘ILvGFG’], [‘Geeksforgeeks’, ‘Best’]]  
> **Explanation** : 6 < 17 total characters respectively after sorting.  
>

**Method #1 : Using sort() +** **len()** **+** **sum()**

In this, we perform task of sorting using sort(), and task of getting total
characters is done using len() and sum().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by total characters

# Using sort() + len() + sum()

 

 

def total_chars(row):

 

 # getting total characters

 return sum([len(sub) for sub in row])

 

 

# initializing list

test_list = [["Gfg", "is", "Best"], ["Geeksforgeeks",
"Best"],

 ["GFg", "4", "good"], ["ILvGFG"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling utility fnc

test_list.sort(key=total_chars)

 

# printing result

print("Sorted results : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘Gfg’, ‘is’, ‘Best’], [‘Geeksforgeeks’, ‘Best’],
> [‘GFg’, ‘4’, ‘good’], [‘ILvGFG’]]  
> Sorted results : [[‘ILvGFG’], [‘GFg’, ‘4’, ‘good’], [‘Gfg’, ‘is’, ‘Best’],
> [‘Geeksforgeeks’, ‘Best’]]

 **Method #2 : Using** **sorted()** **+** **lambda**

In this, sorted() is used to get the sorted result and the lambda function is
used inplace of external function to get the logic of sorting strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by total characters 

# Using sorted() + lambda

 

# initializing list

test_list = [["Gfg", "is", "Best"], ["Geeksforgeeks",
"Best"],

 ["GFg", "4", "good"], ["ILvGFG"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted() gives sorted result 

# lambda function providing logic

res = sorted(test_list, key = lambda row : sum([len(sub)
for sub in row]))

 

# printing result 

print("Sorted results : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘Gfg’, ‘is’, ‘Best’], [‘Geeksforgeeks’, ‘Best’],
> [‘GFg’, ‘4’, ‘good’], [‘ILvGFG’]]
>
> Sorted results : [[‘ILvGFG’], [‘GFg’, ‘4’, ‘good’], [‘Gfg’, ‘is’, ‘Best’],
> [‘Geeksforgeeks’, ‘Best’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

