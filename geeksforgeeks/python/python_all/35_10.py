Python – Sort List items on basis of their Digits



Given List of elements, perform sorting on basis of digits of numbers.

>  **Input** : test_list = [434, 211, 12, 3]  
>  **Output** : [12, 211, 3, 434]  
>  **Explanation** : 3 < 12, still later in list, as initial digit, 1 < 3\.
> Hence sorted by digits rather than number.
>
>  **Input** : test_list = [534, 211, 12, 7]  
>  **Output** : [12, 211, 534, 7]  
>  **Explanation** : 7 < 534, still later in list, as initial digit, 5 < 7\.
> Hence sorted by digits rather than number.

 **Method #1 : Using map() + str() + ljust() + sorted()**

In this, the list elements are converted into string using map() and str(),
ljust() is used to append constant character to make each number equal length.
Then sort is performed using sorted().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort List by Digits

# Using map() + str() + ljust() + sorted()

 

# initializing list

test_list = [434, 211, 12, 54, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# converting elements to string 

temp1 = map(str, test_list)

 

# getting max length

max_len = max(map(len, temp1))

 

# performing sort operation

res = sorted(test_list, key = lambda idx :
(str(idx).ljust(max_len, 'a')))

 

# printing result 

print("List after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [434, 211, 12, 54, 3]
    List after sorting : [12, 211, 3, 434, 54]
    
    

**Method #2 : Using list comprehension + sorted() + lambda**

In this, we as parameter to sorted(), pass a list of digits. Performing sort
according to that gives desired results.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort List by Digits

# Using list comprehension + sorted() + lambda

 

# initializing list

test_list = [434, 211, 12, 54, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort operation

# converting number to list of Digits

res = sorted(test_list, key = lambda ele: [int(j) for j
in str(ele)])

 

# printing result 

print("List after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [434, 211, 12, 54, 3]
    List after sorting : [12, 211, 3, 434, 54]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

