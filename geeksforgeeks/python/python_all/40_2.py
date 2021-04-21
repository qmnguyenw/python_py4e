Python – Filter tuple with all same elements



Given List of tuples, filter tuples which have same values.

>  **Input** : test_list = [(5, 6, 5, 5), (6, 6, 6), (9, 10)]  
>  **Output** : [(6, 6, 6)]  
>  **Explanation** : 1 tuple with same elements.
>
>  **Input** : test_list = [(5, 6, 5, 5), (6, 5, 6), (9, 10)]  
>  **Output** : []  
>  **Explanation** : No tuple with same elements.

 **Method #1 : Using list comprehension + set() + len()**

In this, we check for length of set converted tuple to be 1, if that checks
out, tuple is added to result, else, omitted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter similar elements Tuples

# Using list comprehension + set() + len()

 

# initializing list

test_list = [(5, 6, 5, 5), (6, 6, 6), (1,
1), (9, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# length is computed using len()

res = [sub for sub in test_list if len(set(sub))
== 1]

 

# printing results

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(5, 6, 5, 5), (6, 6, 6), (1, 1), (9, 10)]
    Filtered Tuples : [(6, 6, 6), (1, 1)]
    

**Method #2 : Using filter() + lamdba + set() + len()**

In this, we perform task of filtering using filter(), and single element logic
is checked in lambda function using set() and len().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter similar elements Tuples

# Using filter() + lamdba + set() + len()

 

# initializing list

test_list = [(5, 6, 5, 5), (6, 6, 6), (1,
1), (9, 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# end result converted to list object 

# filter extracts req. tuples

res = list(filter(lambda sub : len(set(sub)) ==
1, test_list))

 

# printing results

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(5, 6, 5, 5), (6, 6, 6), (1, 1), (9, 10)]
    Filtered Tuples : [(6, 6, 6), (1, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

