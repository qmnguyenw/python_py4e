Python Program to Remove Palindromic Elements from a List



Given a list, the task here is to write Python programs that can remove all
the elements which have palindromic equivalent element present in the list.

 **Examples:**

>  **Input** : test_list = [54, 67, 12, 45, 98, 76, 9]
>
>  **Output** : [12, 98]
>
>  **Explanation :** 67 has 76 as palindromic element, both are omitted.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [54, 67, 12, 45, 98, 76, 9, 89]
>
>  **Output :** [12]
>
>  **Explanation :** 98 has 89 as palindromic element, both are omitted.

 **Method 1 :** _Using_ _str()_ _,_ _list comprehension_ _and_ _int()_

In this, elements are first converted to string using str(), reversed and
reconverted to integer using int() and occurrence of palindromes is checked,
if present, both the element and its palindrome are omitted from result.

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

test_list = [54, 67, 12, 45, 98, 76, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# reversing and comparing for presence using in operator

res = [ele for ele in test_list if
int(str(ele)[::-1]) not in test_list]

 

# printing result

print("List after palindromic removals ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [54, 67, 12, 45, 98, 76, 9]
>
>  
>
>
>  
>
>
> List after palindromic removals ? : [12, 98]

 **Method 2 :** _Using_ _filter()_ _,_ _str()_ _and_ _int()_

In this, we perform the task of filtering each element using filter(). str()
and int() is used for the same funtion as in the above method.

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

test_list = [54, 67, 12, 45, 98, 76, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# reversing and comparing for presence using in operator

res = list(filter(lambda ele: int(str(ele)[::-1])
not in test_list, test_list))

 

# printing result

print("List after palindromic removals ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [54, 67, 12, 45, 98, 76, 9]
>
> List after palindromic removals ? : [12, 98]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

