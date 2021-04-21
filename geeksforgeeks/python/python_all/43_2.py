Python – Extract Key’s Value, if Key Present in List and Dictionary



Given a list, dictionary and a Key K, print value of K from dictionary if key
present in both, list and dictionary.

>  **Input** : test_list = [“Gfg”, “is”, “Good”, “for”, “Geeks”], test_dict =
> {“Gfg” : 5, “Best” : 6}, K = “Gfg”  
>  **Output** : 5  
>  **Explanation** : “Gfg” is present in list and has value 5 in dictionary.
>
>  **Input** : test_list = [“Good”, “for”, “Geeks”], test_dict = {“Gfg” : 5,
> “Best” : 6}, K = “Gfg”  
>  **Output** : None  
>  **Explanation** : “Gfg” not present in List.

 **Method #1 : Using all() + generator expression**

The combination of above functions offer one of the ways in which this problem
can be solved. In this we use all() to check for occurrence in both dictionary
and list. If result is true value is extracted to result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Key's Value, if Key Present in List and Dictionary

# Using all() + list comprehension

 

# initializing list

test_list = ["Gfg", "is", "Good", "for", "Geeks"]

 

# initializing Dictionary

test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

 

# initializing K 

K = "Gfg"

 

# printing original list and Dictionary

print("The original list : " + str(test_list))

print("The original Dictionary : " + str(test_dict))

 

# using all() to check for occurrence in list and dict

# encapsulating list and dictionary keys in list 

res = None

if all(K in sub for sub in [test_dict, test_list]):

 res = test_dict[K]

 

# printing result 

print("Extracted Value : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Good', 'for', 'Geeks']
    The original Dictionary : {'Gfg': 2, 'is': 4, 'Best': 6}
    Extracted Value : 2
    

**Method #2 : Using set() + intersection()**

This is one another way to check for key’s presence in both the containers. In
this, we compute intersection of all values of list and dict keys, and test
for Key’s occurrence in that.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Key's Value, if Key Present in List and Dictionary

# Using set() + intersection()

 

# initializing list

test_list = ["Gfg", "is", "Good", "for", "Geeks"]

 

# initializing Dictionary

test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

 

# initializing K 

K = "Gfg"

 

# printing original list and Dictionary

print("The original list : " + str(test_list))

print("The original Dictionary : " + str(test_dict))

 

# conversion of lists to set and intersection with keys 

# using intersection

res = None

if K in set(test_list).intersection(test_dict):

 res = test_dict[K]

 

# printing result 

print("Extracted Value : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Good', 'for', 'Geeks']
    The original Dictionary : {'Gfg': 2, 'is': 4, 'Best': 6}
    Extracted Value : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

