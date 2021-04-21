Python – Test String in Character List and vice-versa



Given a String, check if it’s present in order in character list and vice
versa.

>  **Input** : test_str = ‘geeks’, K = [‘g’, ‘e’, ‘e’, ‘k’, ‘f’, ‘o’, ‘r’,
> ‘g’, ‘e’, ‘e’, ‘k’, ‘s’] [ String in Character list ]  
> **Output** : True  
> **Explanation** : geeks is present in list , starting from 7th index till
> end.
>
>  **Input** : test_str = ‘geeksforgeeks’, K = [‘g’, ‘e’, ‘e’, ‘k’, ‘s’]
> [Character list in String]  
> **Output** : True  
> **Explanation** : [‘g’, ‘e’, ‘e’, ‘k’, ‘s’] present in string, starting from
> beggining of string.

**Method #1 : Using** **in operator** **+** **join()** **[ String in character
list ]**

In this, we convert the character list to a string using join() and apply in
operator to test for substring presence.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test String in Character List and vice-versa

# Using in operator and join() [String in list]

 

# initializing string

test_str = 'geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Character list

K = ['g', 'e', 'e', 'k', 'f', 'o', 'r',
'g', 'e', 'e', 'k', 's']

 

# joining list

joined_list = ''.join(K)

 

# checking for presence

res = test_str in joined_list

 

# printing result 

print("Is String present in character list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeks
    Is String present in character list : True
    

**Method #2 : Using in operator + join() [ Character List in String ]**

In this, the target character list is converted to String and then checked in
String using in operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test String in Character List and vice-versa

# Using in operator + join() [ Character List in String ]

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Character list

K = ['g', 'e', 'e', 'k', 's']

 

# joining list

joined_list = ''.join(K)

 

# checking for presence

res = joined_list in test_str

 

# printing result 

print("Is character list present in String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    Is character list present in String : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

