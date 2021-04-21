Python – Filter immutable rows representing Dictionary Keys from Matrix



Given Matrix, extract all the rows which has elements which have all elements
which can be represented as dictionary key, i.e immutable.

>  **Input** : test_list = [[4, 5, [2, 3, 2]], [“gfg”, 1, (4, 4)], [{5:4}, 3,
> “good”], [True, “best”]]  
> **Output** : [[‘gfg’, 1, (4, 4)], [True, ‘best’]]  
> **Explanation** : All elements in tuples are immutable.  
>
>
> **Input** : test_list = [[4, 5, [2, 3, 2]], [“gfg”, 1, (4, 4), [3, 2]],
> [{5:4}, 3, “good”], [True, “best”]]  
> **Output** : [[True, ‘best’]]  
> **Explanation** : All elements in tuples are immutable.

**Method #1 : Using all() + isinstance()**

In this, we check for all elements to be of the instance of immutable data
types, rows that return _True_ for all elements, is filtered.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Dictionary Key Possible Element rows

# Using all() + isinstance()

 

# initializing list

test_list = [[4, 5, [2, 3, 2]], ["gfg", 1,
(4, 4)], [{5: 4}, 3, "good"], [

 True, "best"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for each immutable data type

res = [row for row in test_list if all(isinstance(ele,
int) or isinstance(ele, bool)

 or isinstance(ele, float) or isinstance(ele, tuple)

 or isinstance(ele, str) for ele in row)]

 

# printing result

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, [2, 3, 2]], [‘gfg’, 1, (4, 4)], [{5: 4}, 3,
> ‘good’], [True, ‘best’]]  
> Filtered rows : [[‘gfg’, 1, (4, 4)], [True, ‘best’]]

 **Method #2 : Using filter() + lambda + isinstance() + all()**

In this, we perform task of filtering using _filter() + lambda_ function, rest
all functionalities are performed as above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Dictionary Key Possible Element rows

# Using filter() + lambda + isinstance() + all()

 

# initializing list

test_list = [[4, 5, [2, 3, 2]], ["gfg", 1,
(4, 4)], [{5: 4}, 3, "good"], [

 True, "best"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for each immutable data type

# filtering using filter()

res = list(filter(lambda row: all(isinstance(ele,
int) or isinstance(ele, bool)

 or isinstance(ele, float) or isinstance(ele, tuple)

 or isinstance(ele, str) for ele in row), test_list))

 

# printing result

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, [2, 3, 2]], [‘gfg’, 1, (4, 4)], [{5: 4}, 3,
> ‘good’], [True, ‘best’]]  
> Filtered rows : [[‘gfg’, 1, (4, 4)], [True, ‘best’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

