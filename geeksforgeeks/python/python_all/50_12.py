Python – Common list elements and dictionary values



Given list and dictionary, extract common elements of List and Dictionay
Values.

>  **Input** : test_list = [“Gfg”, “is”, “Best”, “For”], subs_dict = {4 :
> “Gfg”, 8 : “Geeks”, 9 : ” Good”, }  
>  **Output** : [‘Gfg’]  
>  **Explanation** : “Gfg” is common in both list and dictionary value.
>
>  **Input** : test_list = [“Gfg”, “is”, “Best”, “For”, “Geeks”], subs_dict =
> {4 : “Gfg”, 8 : “Geeks”, 9 : ” Best”, }  
>  **Output** : [‘Gfg’, “Geeks”, “Best”]  
>  **Explanation** : 3 common values are extracted.

 **Method #1 : Using list comprehension + values()**

The combination of above functionalities provide a way in which this task can
be performed in a single line. In this, we extract values of dictionaries
using values() and list comprehension is used to perform iteration and
intersection checks.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List elements and dictionary values intersection

# Using list comprehension + values()

 

# initializing list

test_list = ["Gfg", "is", "Best", "For", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {4 : "Gfg", 8 : "Geeks", 9 : " Good",
}

 

# Intersection of elements, using "in" for checking presence

res = [ele for ele in test_list if ele in
subs_dict.values()]

 

# printing result 

print("Intersection elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'For', 'Geeks']
    Intersection elements : ['Gfg', 'Geeks']
    

**Method #2 : Using set() + intersection()**

In this approach both list and dictionary values are converted to set() and
then intersection is performed to get common elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common list elements and dictionary values 

# Using set() and intersection()

 

# initializing list

test_list = ["Gfg", "is", "Best", "For", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {4 : "Gfg", 8 : "Geeks", 9 : " Good",
}

 

# Intersection of elements, using set() to convert

# intersection() for common elements

res =
list(set(test_list).intersection(list(subs_dict.values())))

 

# printing result 

print("Intersection elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'For', 'Geeks']
    Intersection elements : ['Geeks', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

