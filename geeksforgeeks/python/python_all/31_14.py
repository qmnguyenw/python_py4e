Python – Double Split String to Matrix



Given a String, perform the double split, 1st for rows, and next for
individual elements so that the given string can be converted to a matrix.

 **Examples:**

>  **Input** : test_str = ‘Gfg,best*for,all*geeks,and,CS’, row_splt = “*”,
> ele_splt = “,”  
> **Output** : [[‘Gfg’, ‘best’], [‘for’, ‘all’], [‘geeks’, ‘and’, ‘CS’]]  
> **Explanation** : String split by rows, and elements by respective delims.
>
>  **Input** : test_str = ‘Gfg!best*for!all*geeks!and!CS’, row_splt = “*”,
> ele_splt = “!”  
> **Output** : [[‘Gfg’, ‘best’], [‘for’, ‘all’], [‘geeks’, ‘and’, ‘CS’]]  
> **Explanation** : String split by rows, and elements by respective delims.

**Method #1 : Using split() + loop**

  

  

In this, 1st split() is used to construct rows of Matrix, and then nested
split() to get separation between individual elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Double Split String to Matrix

# Using split() + loop

 

# initializing string

test_str = 'Gfg,best#for,all#geeks,and,CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing row split char 

row_splt = "#"

 

# initializing element split char 

ele_splt = ","

 

# split for rows

temp = test_str.split(row_splt)

res = []

 

for ele in temp:

 

 # split for elements

 res.append(ele.split(ele_splt))

 

# printing result 

print("String after Matrix conversion : " + str(res))   
  
---  
  
__

__

**Output:**

> The original string is : Gfg,best#for,all#geeks,and,CS  
> String after Matrix conversion : [[‘Gfg’, ‘best’], [‘for’, ‘all’], [‘geeks’,
> ‘and’, ‘CS’]]

 **Method #2 : Using list comprehension + split()**

This is yet another way in which this task can be performed. In this, we use a
similar process, but one-liner to solve the problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Double Split String to Matrix

# Using list comprehension + split()

 

# initializing string

test_str = 'Gfg,best#for,all#geeks,and,CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing row split char 

row_splt = "#"

 

# initializing element split char 

ele_splt = ","

 

# split for rows

temp = test_str.split(row_splt)

 

# using list comprehension as shorthand

res = [ele.split(ele_splt) for ele in temp]

 

# printing result 

print("String after Matrix conversion : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Gfg,best#for,all#geeks,and,CS  
> String after Matrix conversion : [[‘Gfg’, ‘best’], [‘for’, ‘all’], [‘geeks’,
> ‘and’, ‘CS’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

