Python – Check if particular value is present corresponding to K key



Given a list of dictionaries, check whether particular key-value pair exists
or not.

>  **Input** : [{“Gfg” : “4”, “is” : “good”, “best” : “1”}, {“Gfg” : “9”, “is”
> : “CS”, “best” : “10”}], K = “Gfg”, val = “find”  
>  **Output** : False  
>  **Explanation** : No value of “Gfg” is “find”.
>
>  **Input** : [{“Gfg” : “4”, “is” : “good”, “best” : “1”}, {“Gfg” : “9”, “is”
> : “CS”, “best” : “10”}], K = “Gfg”, val = 4  
>  **Output** : True  
>  **Explanation** : 4 present as “Gfg” value.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
extract dictionaries using list comprehension, and then use “in” operator to
check if it has any values in it.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if particular value is present corrresponding to K key

# Using list comprehension

 

# initializing lists

test_list = [{"Gfg" : "4", "is" : "good", "best" :
"1"},

 {"Gfg" : "find", "is" : "better", "best" : "8"},

 {"Gfg" : "9", "is" : "CS", "best" : "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key 

K = "Gfg"

 

# initializing target value 

val = "find"

 

# extracting values using list comprehension

# using in operator to check for values 

res = val in [sub[K] for sub in test_list]

 

# printing result 

print("Is key-val pair present? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': '4', 'is': 'good', 'best': '1'}, {'Gfg': 'find', 'is': 'better', 'best': '8'}, {'Gfg': '9', 'is': 'CS', 'best': '10'}]
    Is key-val pair present?  : True
    

**Method #2 : Using map() + in operator**

This is yet another way in which this task can be performed. In this task of
getting values corresponding to particular key is performed using map(),
extending function to each dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if particular value is present corrresponding to K key

# Using map() + in operator

 

# initializing lists

test_list = [{"Gfg" : "4", "is" : "good", "best" :
"1"},

 {"Gfg" : "find", "is" : "better", "best" : "8"},

 {"Gfg" : "9", "is" : "CS", "best" : "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key 

K = "Gfg"

 

# initializing target value 

val = "find"

 

# extracting values using map 

# using in operator to check for values 

res = val in list(map(lambda sub : sub[K], test_list))

 

# printing result 

print("Is key-val pair present? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': '4', 'is': 'good', 'best': '1'}, {'Gfg': 'find', 'is': 'better', 'best': '8'}, {'Gfg': '9', 'is': 'CS', 'best': '10'}]
    Is key-val pair present?  : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

