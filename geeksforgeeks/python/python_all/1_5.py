Python – Start and End Indices of words from list in String



Given a String, our task is to write a Python program to extract the start and
end index of all the elements of words of another list from a string.

>  **Input :** test_str = “gfg is best for all CS geeks and engineering job
> seekers”, check_list = [“geeks”, “engineering”, “best”, “gfg”]
>
>  **Output :** {‘geeks’: [23, 27], ‘engineering’: [33, 43], ‘best’: [7, 10],
> ‘gfg’: [0, 2]}
>
>  **Explanation :** “geeks” starts from index number 23 till 27, hence the
> result.
>
>  **Input :** test_str = “gfg is best for all CS geeks and engineering job
> seekers”, check_list = [“geeks”, “gfg”]
>
>  
>
>
>  
>
>
>  **Output :** {‘geeks’: [23, 27], ‘gfg’: [0, 2]}
>
>  **Explanation :** “geeks” starts from index number 23 till 27, hence the
> result.

 **Method #1 : Using** **loop** **+** **index()** **\+ len()**

In this, loop is used to get each element from list. The index() gets the
initial index and len() gets the last index of all the elements from list in
the string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Start and End Indices of words from list in String

# Using loop + index() + len()

 

# initializing string

test_str = "gfg is best for all CS geeks and engineering job seekers"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing check_list 

check_list = ["geeks", "engineering", "best", "gfg"]

 

res = dict()

for ele in check_list :

 if ele in test_str:

 

 # getting front index 

 strt = test_str.index(ele)

 

 # getting ending index

 res[ele] = [strt, strt + len(ele) - 1]

 

# printing result

print("Required extracted indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg is best for all CS geeks and engineering job
> seekers
>
> Required extracted indices : {‘geeks’: [23, 27], ‘engineering’: [33, 43],
> ‘best’: [7, 10], ‘gfg’: [0, 2]}

 **Method #2 : Using** **dictionary comprehension** **\+ len() + index()**

In this, we perform tasks similar to the above function but the construction
of the result dictionary is done using shorthand using dictionary
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

# Start and End Indices of words from list in String

# Using dictionary comprehension + len() + index()

 

# initializing string

test_str = "gfg is best for all CS geeks and engineering job seekers"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing check_list

check_list = ["geeks", "engineering", "best", "gfg"]

 

# Dictionary comprehension to be used as shorthand for

# forming result Dictionary

res = {key: [test_str.index(key), test_str.index(key) + len(key)
- 1]

 for key in check_list if key in test_str}

 

# printing result

print("Required extracted indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg is best for all CS geeks and engineering job
> seekers
>
> Required extracted indices : {‘geeks’: [23, 27], ‘engineering’: [33, 43],
> ‘best’: [7, 10], ‘gfg’: [0, 2]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

