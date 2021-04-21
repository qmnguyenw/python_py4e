Python – Custom Consecutive character repetition in String



Given a String, repeat characters consecutively by number mapped in
dictionary.

>  **Input** : test_str = ‘Geeks4Geeks’, test_dict = {“G” : 3, “e” : 1, “4” :
> 3, “k” : 5, “s” : 3}  
> **Output** : GGGeekkkkksss444GGGeekkkkksss  
> **Explanation** : Each letter repeated as per value in dictionary.
>
>  **Input** : test_str = ‘Geeks4Geeks’, test_dict = {“G” : 3, “e” : 1, “4” :
> 3, “k” : 5, “s” : 1}  
> **Output** : GGGeekkkkks444GGGeekkkkks  
> **Explanation** : Each letter repeated as per value in dictionary.  
>

**Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate through each character and check in map its repetition and repeat for
that amount.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Consecutive character repetition in String

# Using loop

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing dictionary 

test_dict = {"G" : 3, "e" : 2, "4" : 4, "k" :
5, "s" : 3}

 

res = ""

for ele in test_str:

 

 # using * operator for repetition

 # using + for concatenation

 res += ele * test_dict[ele]

 

# printing result 

print("The filtered string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : Geeks4Geeks
    The filtered string : GGGeeeekkkkksss4444GGGeeeekkkkksss
    
    

**Method #2 : Using list comprehension + join()**

This is yet another way in which this task can be performed. In this, we
perform similar task as above function. The only difference being we use
join() to merge the created repetition list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Consecutive character repetition in String

# Using list comprehension + join()

 

# initializing string

test_str = 'Geeks4Geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing dictionary 

test_dict = {"G" : 3, "e" : 2, "4" : 4, "k" :
5, "s" : 3}

 

# using join to perform concatenation of strings

res = "".join([ele * test_dict[ele] for ele in test_str])

 

# printing result 

print("The filtered string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : Geeks4Geeks
    The filtered string : GGGeeeekkkkksss4444GGGeeeekkkkksss
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

