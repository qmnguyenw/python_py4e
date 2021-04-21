Python – Extract dictionaries with Empty String value in K key



Given List of dictionaries, extract all the dictionaries which have empty
string as values of particular key.

>  **Input** : test_list = [{“Gfg” : “4”, “is” : “good”, “best” : “1”}, {“Gfg”
> : “9”, “is” : “CS”, “best” : “10”}], K = “Gfg”  
>  **Output** : []  
>  **Explanation** : No “Gfg” key is empty.
>
>  **Input** : test_list = [{“Gfg” : “”, “is” : “good”, “best” : “1”}, {“Gfg”
> : “9”, “is” : “CS”, “best” : “10”}], K = “Gfg”  
>  **Output** : [{“Gfg” : “”, “is” : “good”, “best” : “1”}]  
>  **Explanation** : Dictionary with empty “Gfg” extracted.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we run a
loop through all dictionaries and check for key’s empty string value. All this
compiled in list comprehension rather than loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract dictionaries with Empty String value in K key

# Using list comprehension

 

# initializing lists

test_list = [{"Gfg" : "4", "is" : "good", "best" :
"1"},

 {"Gfg" : "", "is" : "better", "best" : "8"},

 {"Gfg" : "9", "is" : "CS", "best" : "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key 

K = "Gfg"

 

# using list comprehension to fetch empty string key's dictionaries

res = [sub for sub in test_list if sub[K] == '']

 

# printing result 

print("The extracted dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': '4', 'is': 'good', 'best': '1'}, {'Gfg': '', 'is': 'better', 'best': '8'}, {'Gfg': '9', 'is': 'CS', 'best': '10'}]
    The extracted dictionaries : [{'Gfg': '', 'is': 'better', 'best': '8'}]
    

**Method #2 : Using filter() + lambda**

This is yet another way in which this task can be performed. In this, we
extract all the empty values key’s dictionaries using filter() and
functionality and iteration by lambda.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract dictionaries with Empty String value in K key

# Using filter() + lambda

 

# initializing lists

test_list = [{"Gfg" : "4", "is" : "good", "best" :
"1"},

 {"Gfg" : "", "is" : "better", "best" : "8"},

 {"Gfg" : "9", "is" : "CS", "best" : "10"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K key 

K = "Gfg"

 

# filter() used to iteration

# lambda for functionality

res = list(filter(lambda sub: sub[K] == '', test_list))

 

# printing result 

print("The extracted dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': '4', 'is': 'good', 'best': '1'}, {'Gfg': '', 'is': 'better', 'best': '8'}, {'Gfg': '9', 'is': 'CS', 'best': '10'}]
    The extracted dictionaries : [{'Gfg': '', 'is': 'better', 'best': '8'}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

