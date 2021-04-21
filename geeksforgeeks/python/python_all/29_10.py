Python – Extract Sorted Strings



Given a String List, extract all sorted Strings.

>  **Input** : test_list = [“hint”, “geeks”, “fins”, “Gfg”]  
> **Output** : [‘hint’, ‘fins’, ‘Gfg’]  
> **Explanation** : Strings in increasing order of characters are extracted.
>
>  **Input** : test_list = [“hint”, “geeks”, “Gfg”]  
> **Output** : [‘hint’, ‘Gfg’]  
> **Explanation** : Strings in increasing order of characters are extracted.

**Method #1 : Using list comprehension + sorted()**

In this, we perform task of sorting strings and comparison using _sorted()_ ,
list comprehension is used to iterate through Strings.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract sorted strings

# Using list comprehension + sorted()

 

# initializing list

test_list = ["hint", "geeks", "fins", "Gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted(), converts to sorted version and compares with

# original string

res = [sub for sub in test_list if ''.join(sorted(sub))
== sub]

 

# printing result

print("Sorted Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['hint', 'geeks', 'fins', 'Gfg']
    Sorted Strings : ['hint', 'fins', 'Gfg']
    
    

**Method #2 : Using filter() + lambda + sorted() + join()**

In this, we perform filtering using _filter() + lambda_ , and _join()_ is used
to convert final sorted character list result to string for comparison.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract sorted strings

# Using filter() + lambda + sorted() + join()

 

# initializing list

test_list = ["hint", "geeks", "fins", "Gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorted(), converts to sorted version and compares with 

# original string

res = list(filter(lambda sub : ''.join(sorted(sub)) ==
sub, test_list))

 

# printing result 

print("Sorted Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['hint', 'geeks', 'fins', 'Gfg']
    Sorted Strings : ['hint', 'fins', 'Gfg']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

