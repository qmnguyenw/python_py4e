Python – Column Maximum in Dictionary Value Matrix



Given a Dictionary with Matrix Values, compute maximum of each column of those
Matrix.

    
    
    **Input**  :  test_dict = {"Gfg" : [[7, 6], [3, 2]],
                                            "is" : [[3, 6], [6, 10]],
                                            "best" : [[5, 8], [2, 3]]}
    **Output** : {'Gfg': [7, 6], 'is': [6, 10], 'best': [5, 8]}
    **Explanation** :  7 > 3, 6 > 2, hence ordering.
    
    **Input**  :  test_dict = {"Gfg" : [[7, 6], [3, 2]],
                                            "is" : [[3, 6], [6, 10]]}
    **Output** : {'Gfg': [7, 6], 'is': [6, 10]}
    **Explanation** :  6 > 3, 10 > 6, hence ordering.
    

**Method #1 : Using dictionary comprehension + sorted() + items()**

This is one of the ways in which this task can be performed. In this, The
inner columns are extracted and sorted and last value of sorted list(maximum)
is returned as result. This happens for all list values using dictionary
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

# Column Maximums of Dictionary Value Matrix

# Using dictionary comprehension + sorted() + items()

 

# initializing dictionary

test_dict = {"Gfg" : [[5, 6], [3, 4]],

 "is" : [[4, 6], [6, 8]],

 "best" : [[7, 4], [2, 3]]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorted() used to sort and "-1" used to get last i.e

# maximum element

res = {key : sorted(val, key = lambda ele : (ele[0],
ele[1]))[-1] for key, val in test_dict.items()}

 

# printing result

print("The evaluated dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {'Gfg': [[5, 6], [3, 4]], 'is': [[4, 6], [6, 8]], 'best': [[7, 4], [2, 3]]}
    The evaluated dictionary : {'Gfg': [5, 6], 'is': [6, 8], 'best': [7, 4]}
    
    

**Method #2 : Using max() + map() + zip()**

  

  

This is one of thw ways in which this task can be performed. In this, we
extract maximum using max(), and align columns to list using zip() and map()
is used to extend logic of zip to each column.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Maximums of Dictionary Value Matrix

# Using max() + map() + zip()

 

# initializing dictionary

test_dict = {"Gfg" : [[5, 6], [3, 4]],

 "is" : [[4, 6], [6, 8]],

 "best" : [[7, 4], [2, 3]]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# map extending logic to entire columns

# result compiled using dictionary comprehension

res = {key: list(map(max, zip(*val))) for key,
val in test_dict.items()}

 

# printing result

print("The evaluated dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {'Gfg': [[5, 6], [3, 4]], 'is': [[4, 6], [6, 8]], 'best': [[7, 4], [2, 3]]}
    The evaluated dictionary : {'Gfg': [5, 6], 'is': [6, 8], 'best': [7, 4]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

