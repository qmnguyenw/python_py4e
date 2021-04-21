Python – Test substring order



Given two strings, check if substring characters occur in correct order in
string.

>  **Input** : test_str = ‘geeksforgeeks’, K = ‘sees’  
>  **Output** : True  
>  **Explanation** : “s” after that “ee” and then “s” is present in order in
> string 1.
>
>  **Input** : test_str = ‘geeksforgeeks’, K = ‘seef’  
>  **Output** : False  
>  **Explanation** : Unordered String.

 **Method #1 : Using join() + generator expression + in operator**

In this, we check we join all the characters which occur in substring using
join(), post that check if substring is present using in operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test substring order

# Using join() + in operator + generator expression

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

K = 'seek'

 

# concatenating required characters 

temp = lambda sub: ''.join(chr for chr in sub if chr
in set(K))

 

# checking in order

res = K in temp(test_str)

 

# printing result 

print("Is substring in order : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    Is substring in order : True
    

**Method #2 : Using all() + next() + generator expression**

In this, we get the string with just substring characters using next() and
generator expression, to check for order, all() operation is used for each
character in substring.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test substring order

# Using all() + next() + generator expression

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

K = 'seek'

 

# concatenating required characters using next()

# all() used to test order

test_str = iter(test_str)

res = all(next((ele for ele in test_str if ele ==
chr), None) is not None for chr in K)

 

# printing result 

print("Is substring in order : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    Is substring in order : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

