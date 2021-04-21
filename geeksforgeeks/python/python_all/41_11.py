Python – Split Strings on Prefix Occurrence



Given a list of Strings, perform string split on occurrence of prefix.

>  **Input** : test_list = [“geeksforgeeks”, “best”, “geeks”, “and”], pref =
> “geek”  
>  **Output** : [[‘geeksforgeeks’, ‘best’], [‘geeks’, ‘and’]]  
>  **Explanation** : At occcurrence of string “geeks” split is performed.
>
>  **Input** : test_list = [“good”, “friuts”, “goodness”, “spreading”], pref =
> “good”  
>  **Output** : [[‘good’, ‘fruits’], [‘goodness’, ‘spreading’]]  
>  **Explanation** : At occcurrence of string “good” split is performed.

 **Method #1 : Using loop + startswith()**

In this, we iterate each element of List, and check if new list has to be
changed using startswith() by checking for prefix, and create new list if
prefix is encountered.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Strings on Prefix Occurrence

# Using loop + startswith()

 

# initializing list

test_list = ["geeksforgeeks", "best", "geeks", "and",
"geeks", "love", "CS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix 

pref = "geek"

 

 

res = []

for val in test_list:

 

 # checking for prefix

 if val.startswith(pref):

 

 # if pref found, start new list 

 res.append([val])

 else:

 

 # else append in current list

 res[-1].append(val)

 

# printing result 

print("Prefix Split List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love', 'CS']
    Prefix Split List : [['geeksforgeeks', 'best'], ['geeks', 'and'], ['geeks', 'love', 'CS']]
    

**Method #2 : Using loop + zip_longest() + startswith()**

In this, we zip all the elements with their subsequent element sublist and
check for prefix using startswith(), if found, result is appended.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split Strings on Prefix Occurrence

# Using loop + zip_longest() + startswith()

from itertools import zip_longest

 

# initializing list

test_list = ["geeksforgeeks", "best", "geeks", "and",
"geeks", "love", "CS"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing prefix 

pref = "geek"

 

 

res, temp = [], []

 

for x, y in zip_longest(test_list, test_list[1:]):

 temp.append(x)

 

 # if prefix is found, split and start new list

 if y and y.startswith(pref):

 res.append(temp)

 temp = []

res.append(temp)

 

# printing result 

print("Prefix Split List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love', 'CS']
    Prefix Split List : [['geeksforgeeks', 'best'], ['geeks', 'and'], ['geeks', 'love', 'CS']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

