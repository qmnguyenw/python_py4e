Python program to Convert a elements in a list of Tuples to Float



Given a Tuple list, convert all possible convertible elements to float.

>  **Input** : test_list = [(“3”, “Gfg”), (“1”, “26.45”)]  
> **Output** : [(3.0, ‘Gfg’), (1.0, 26.45)]  
> **Explanation** : Numerical strings converted to floats.
>
>  **Input** : test_list = [(“3”, “Gfg”)]  
> **Output** : [(3.0, ‘Gfg’)]  
> **Explanation** : Numerical strings converted to floats.

**Method #1 : Using loop +** **isalpha()** **+** **float()**

In this, we use a loop to iterate for all the tuples, check for alphabets
using isalpha(), which cannot be converted to float, and for the rest of the
elements float() is used to convert.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple List elements to Float

# Using loop + isalpha() + float

 

# initializing list

test_list = [("3", "Gfg"), ("1", "26.45"), ("7.32",
"8"), ("Gfg", "8")]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for tup in test_list:

 temp = []

 for ele in tup:

 

 # check for string

 if ele.isalpha():

 temp.append(ele)

 else:

 

 # convert to float

 temp.append(float(ele))

 res.append((temp[0],temp[1]))

 

# printing result 

print("The converted list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘3’, ‘Gfg’), (‘1’, ‘26.45’), (‘7.32’, ‘8’), (‘Gfg’,
> ‘8’)]  
> The converted list : [(3.0, ‘Gfg’), (1.0, 26.45), (7.32, 8.0), (‘Gfg’, 8.0)]

 **Method #2 : Using loop + isalpha() + float() +** **list comprehension**

In this, we perform the task of iterating through inner tuples using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple List elements to Float

# Using loop + isalpha() + float

 

# initializing list

test_list = [("3", "Gfg"), ("1", "26.45"), ("7.32",
"8"), ("Gfg", "8")]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for tup in test_list:

 

 # list comprehension to check for each case

 temp = [ele if ele.isalpha() else float(ele) for ele
in tup]

 res.append((temp[0],temp[1]))

 

# printing result 

print("The converted list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘3’, ‘Gfg’), (‘1’, ‘26.45’), (‘7.32’, ‘8’), (‘Gfg’,
> ‘8’)]  
> The converted list : [(3.0, ‘Gfg’), (1.0, 26.45), (7.32, 8.0), (‘Gfg’, 8.0)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

