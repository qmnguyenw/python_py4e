Python | Unique dictionary filter in list



While working with Python dictionaries, we can always come across a problem in
which we have list of dictionary with possible repetitions and we wish to
remove the duplicates. This is common problem one can face in Machine Learning
Domain. Let’s discuss certain way in which this problem can be solved.

 **Method : Usingmap() + set() + items() + sorted() + tuple()**

In this method, we just combination of functions to perform this task. The
map function performs the task of extending logic to all elements. The set
function does the actual filtering on pairs accessed by items(). The
sorted function is required by set to remove duplicate.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique dictionary filter in list

# Using map() + set() + items() + sorted() + tuple()

 

# Initialize list

test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3},

 {'gfg' : 1, 'is' : 2, 'best' : 3},

 {'gfg' : 9, 'is' : 8, 'best' : 6}] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Unique dictionary filter in list

# Using map() + set() + items() + sorted() + tuple()

res = list(map(dict, set(tuple(sorted(sub.items()))
for sub in test_list)))

 

# printing result

print("The list after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘gfg’: 1, ‘is’: 2, ‘best’: 3}, {‘gfg’: 1, ‘is’: 2,
> ‘best’: 3}, {‘gfg’: 9, ‘is’: 8, ‘best’: 6}]  
> The list after removing duplicates : [{‘gfg’: 1, ‘is’: 2, ‘best’: 3},
> {‘gfg’: 9, ‘is’: 8, ‘best’: 6}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

