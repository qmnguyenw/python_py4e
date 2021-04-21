Python – Remove dictionary if given key’s value is N



Given list of dictionaries, remove dictionary whose Key K is N.

>  **Input** : test_list = [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9,
> “is” : 2, “Best” : 9}, {“Gfg” : 5, “is” : 4, “Best” : 10}, {“Gfg” : 3, “is”
> : 6, “Best” : 15}], K = “Gfg”, N = 9  
>  **Output** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 5, “is” : 4,
> “Best” : 10}, {“Gfg” : 3, “is” : 6, “Best” : 15}]  
>  **Explanation** : All elements are extracted which have “Gfg” other than 9.
>
>  **Input** : test_list = [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9,
> “is” : 2, “Best” : 9}, {“Gfg” : 5, “is” : 4, “Best” : 10}, {“Gfg” : 3, “is”
> : 6, “Best” : 15}], K = “Best”, N = 10  
>  **Output** : [{“Gfg” : 3, “is” : 7, “Best” : 8}, {“Gfg” : 9, “is” : 2,
> “Best” : 9}, {“Gfg” : 3, “is” : 6, “Best” : 15}]  
>  **Explanation** : All elements are extracted which have “Best” other than
> 10.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
extract and iterate using conditional checks using list comprehension in one
liner.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Dictionaries whose Key(K) is N

# Using list comprehension

 

# initializing list

test_list = [{"Gfg" : 3, "is" : 7, "Best" : 8}, 

 {"Gfg" : 9, "is" : 2, "Best" : 9}, 

 {"Gfg" : 5, "is" : 4, "Best" : 10},

 {"Gfg" : 3, "is" : 6, "Best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing N 

N = 5

 

# returning only dictionaries with "Gfg" key not 5 

res = [sub for sub in test_list if sub[K] != N]

 

# printing result 

print("The extracted dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'is': 7, 'Best': 8}, {'Gfg': 9, 'is': 2, 'Best': 9}, {'Gfg': 5, 'is': 4, 'Best': 10}, {'Gfg': 3, 'is': 6, 'Best': 8}]
    The extracted dictionaries : [{'Gfg': 3, 'is': 7, 'Best': 8}, {'Gfg': 9, 'is': 2, 'Best': 9}, {'Gfg': 3, 'is': 6, 'Best': 8}]
    

**Method #2 : Using filter() + lambda**

This is yet another way in which this task can be performed. In this, we use
conditionals using filter() and lambda function is for checking for N value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Dictionaries whose Key(K) is N

# Using filter() + lambda

 

# initializing list

test_list = [{"Gfg" : 3, "is" : 7, "Best" : 8}, 

 {"Gfg" : 9, "is" : 2, "Best" : 9}, 

 {"Gfg" : 5, "is" : 4, "Best" : 10},

 {"Gfg" : 3, "is" : 6, "Best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing N 

N = 5

 

# Using filter() to check for N value

res = list(filter(lambda x: x[K] != N, test_list))

 

# printing result 

print("The extracted dictionaries : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 'is': 7, 'Best': 8}, {'Gfg': 9, 'is': 2, 'Best': 9}, {'Gfg': 5, 'is': 4, 'Best': 10}, {'Gfg': 3, 'is': 6, 'Best': 8}]
    The extracted dictionaries : [{'Gfg': 3, 'is': 7, 'Best': 8}, {'Gfg': 9, 'is': 2, 'Best': 9}, {'Gfg': 3, 'is': 6, 'Best': 8}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

