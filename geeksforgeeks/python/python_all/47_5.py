Python | Sort a Dictionary



Python, Given a dictionary, perform sort, basis on keys or values. [
applicable Python >=3.6v ].

>  **Input** : test_dict = {“Gfg” : 5, “is” : 7, “Best” : 2}  
>  **Output** : {‘Best’: 2, ‘Gfg’: 5, ‘is’: 7}, {‘is’: 7, ‘Gfg’: 5, ‘Best’: 2}  
>  **Explanation** : Sorted by keys, in ascending and reverse order.
>
>  **Input** : test_dict = {“Best” : 2, “for” : 9, “geeks” : 8}  
>  **Output** : {‘Best’: 2, ‘Gfg’: 5, ‘for’: 9}, {‘for’: 9, ‘geeks’: 8,
> ‘Best’: 2}  
>  **Explanation** : Sorted by values, in ascending and reverse order.

 **Case 1 : Sort by Keys**

This task is performed using sorted(), in this, we extract the keys using 1st
index of items of dictionary extracted by items(), and pass it in key as
custom lambda function to get sorted by keys. The “reverse=True” is added to
perform reverse sort.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort a Dictionary

# Sort by Keys

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 7, "Best" : 2,
"for" : 9, "geeks" : 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using items() to get all items 

# lambda function is passed in key to perform sort by key 

res = {key: val for key, val in sorted(test_dict.items(), key
= lambda ele: ele[0])}

 

# printing result 

print("Result dictionary sorted by keys : " + str(res)) 

 

# using items() to get all items 

# lambda function is passed in key to perform sort by key 

# adding "reversed = True" for reversed order

res = {key: val for key, val in sorted(test_dict.items(), key
= lambda ele: ele[0], reverse = True)}

 

# printing result 

print("Result dictionary sorted by keys ( in reversed order ) : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    Result dictionary sorted by keys : {'Best': 2, 'Gfg': 5, 'for': 9, 'geeks': 8, 'is': 7}
    Result dictionary sorted by keys ( in reversed order ) : {'is': 7, 'geeks': 8, 'for': 9, 'Gfg': 5, 'Best': 2}
    

**Case 2 : Sort by Values**

This task can be performed in similar way as above, the only difference being
for extracting values, 2nd element of items() is passed as comparator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort a Dictionary

# Sort by Values 

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 7, "Best" : 2,
"for" : 9, "geeks" : 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using items() to get all items 

# lambda function is passed in key to perform sort by key 

# passing 2nd element of items()

res = {key: val for key, val in sorted(test_dict.items(), key
= lambda ele: ele[1])}

 

# printing result 

print("Result dictionary sorted by values : " + str(res)) 

 

# using items() to get all items 

# lambda function is passed in key to perform sort by key 

# passing 2nd element of items()

# adding "reversed = True" for reversed order

res = {key: val for key, val in sorted(test_dict.items(), key
= lambda ele: ele[1], reverse = True)}

 

# printing result 

print("Result dictionary sorted by values ( in reversed order ) : " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    Result dictionary sorted by values : {'Best': 2, 'Gfg': 5, 'is': 7, 'geeks': 8, 'for': 9}
    Result dictionary sorted by values ( in reversed order ) : {'for': 9, 'geeks': 8, 'is': 7, 'Gfg': 5, 'Best': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

