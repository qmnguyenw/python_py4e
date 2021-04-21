Python Program to remove a specific digit from every element of the list



Given list of elements, the task here is to write a Python program that can
remove presence of all a specific digit from every element and then return the
resultant list.

**Examples:**

>  **Input** : test_list = [333, 893, 1948, 34, 2346], K = 3  
> **Output** : [”, 89, 1948, 4, 246]  
> **Explanation** : All occurrences of 3 are removed.
>
>  **Input** : test_list = [345, 893, 1948, 34, 2346], K = 5  
> **Output** : [34, 893, 1948, 34, 2346]  
> **Explanation** : All occurrences of 5 are removed.  
>

**Method 1 :** Using loop, str() and join()

  

  

In this, we perform the task of reforming elements by converting them to
string and checking for each digit and ignoring while joining to get new
element. Lastly each element is converted to integer using int().

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [345, 893, 1948, 34, 2346]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

res = []

for ele in test_list:

 

 # joining using join(),

 if list(set(str(ele)))[0] == str(K) and
len(set(str(ele))) == 1:

 res.append('')

 else:

 res.append(int(''.join([el for el in str(ele) if
int(el) != K])))

 

# printing result

print("Modified List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [345, 893, 1948, 34, 2346]
>
> Modified List : [45, 89, 1948, 4, 246]

 **Method 2 :** Using list comprehension, int(), str() and join()

Similar to above method, joining is done using join() and interconversion is
performed using int() and str().

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [345, 893, 1948, 34, 2346]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# list comprehension performing task as one liner

res = ['' if list(set(str(ele)))[0] == str(K)
and len(set(str(ele))) == 1 else int(

 ''.join([el for el in str(ele) if int(el) != K]))
for ele in test_list]

 

# printing result

print("Modified List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [345, 893, 1948, 34, 2346]
>
> Modified List : [45, 89, 1948, 4, 246]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

