Python – Add item after given Key in dictionary



Given a dictionary and a Key, add new item after a particular key in
dictionary.

>  **Input** : test_dict = {“Gfg” : 3, “is” : 5, “for” : 8, “Geeks” : 10}, K =
> “is”, add_item = {“good” : 19}  
>  **Output** : {‘Gfg’: 3, ‘is’: 5, ‘good’: 19, ‘for’: 8, ‘Geeks’: 10}  
>  **Explanation** : Item added after desired key in dictionary.
>
>  **Input** : test_dict = {“Gfg” : 3, “is” : 5, “for” : 8, “Geeks” : 10}, K =
> “for”, add_item = {“good” : 19}  
>  **Output** : {‘Gfg’: 3, ‘is’: 5, ‘for’: 8, ‘good’: 19, ‘Geeks’: 10}  
>  **Explanation** : Item added after desired key in dictionary.

 **Method : Using loop + update()**

In this we iterate for all the keys, and when target key is encountered, the
iteration is haulted and dictionary is updated with required key. Then
iteration is resumed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Keys whose Values summation equals K 

# Using loop + update()

 

# initializing dictionary

test_dict = {"Gfg" : 3, "is" : 5, "for" : 8,
"Geeks" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = "is"

 

# initializing dictionary to be added 

add_item = {"best" : 19}

 

# using dictionary comprehension 

res = dict()

for key in test_dict:

 res[key] = test_dict[key]

 

 # modify after adding K key

 if key == K:

 res.update(add_item)

 

# printing result 

print("Modified dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 5, 'for': 8, 'Geeks': 10}
    Modified dictionary : {'Gfg': 3, 'is': 5, 'best': 19, 'for': 8, 'Geeks': 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

