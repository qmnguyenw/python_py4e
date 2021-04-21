Python – Extract Maximum Keys’ value dictionaries



Given a dictionary, extract all the dictionary which contains a any key which
has maximum values among other keys in dictionary list.

>  **Input** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9, “is” : 2,
> “Best” : 9}, {“Gfg” : 5, “is” : 4, “Best” : 10}, {“Gfg” : 3, “is” : 6,
> “Best” : 14}]  
>  **Output** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9, “is” : 2,
> “Best” : 9}, {“Gfg” : 3, “is” : 6, “Best” : 14}]  
>  **Explanation** : “Gfg” has 9 as best, “is” has 7 and “Best” has 14, those
> dictionaries are extracted.
>
>  **Input** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9, “is” : 2,
> “Best” : 9}, {“Gfg” : 5, “is” : 4, “Best” : 10}, {“Gfg” : 3, “is” : 6,
> “Best” : 16}]  
>  **Output** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9, “is” : 2,
> “Best” : 9}, {“Gfg” : 3, “is” : 6, “Best” : 16}]  
>  **Explanation** : “Gfg” has 9 as best, “is” has 7 and “Best” has 16, those
> dictionaries are extracted.

 **Method : Using max() + filter() + lambda**

The combination of above functionalities can be used to solve this problem. In
this, first maximum is extracted for particular key and then all dictionaries
matching maximum key are extracted. This is carries out for all the keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Maximum Keys' value dictionaries

# Using max() + filter() + lambda

 

# initializing list

test_list = [{"Gfg" : 3, "is" : 7, "Best" : 8}, 

 {"Gfg" : 9, "is" : 2, "Best" : 9}, 

 {"Gfg" : 5, "is" : 4, "Best" : 10},

 {"Gfg" : 3, "is" : 6, "Best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

res = []

 

# getting all keys 

all_keys = list(test_list[0].keys())

for sub in all_keys:

 

 # extracting maximum of each keys

 temp = max(test_list, key = lambda ele: ele[sub]) 

 res_key = list(filter(lambda ele: ele[sub] ==
temp[sub], test_list))

 res.append(res_key)

 

# printing result 

print("The extracted maximum key values dictionaries : " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'is': 7, 'Best': 8}, {'Gfg': 9, 'is': 2, 'Best': 9}, {'Gfg': 5, 'is': 4, 'Best': 10}, {'Gfg': 3, 'is': 6, 'Best': 8}]
    The extracted maximum key values dictionaries : [[{'Gfg': 9, 'is': 2, 'Best': 9}], [{'Gfg': 3, 'is': 7, 'Best': 8}], [{'Gfg': 5, 'is': 4, 'Best': 10}]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

