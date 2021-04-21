Python – Remove given character from first element of Tuple



Given a Tuple list, remove K character from 1st element of Tuple being String.

>  **Input** : test_list = [(“GF$g!”, 5), (“!i$s”, 4), (“best!$”, 10)], K =
> ‘$’  
>  **Output** : [(‘GFg!’, 5), (‘!is’, 4), (‘best!’, 10)]  
>  **Explanation** : First element’s strings K value removed.
>
>  **Input** : test_list = [(“GF$g!”, 5), (“best!$”, 10)], K = ‘$’  
>  **Output** : [(‘GFg!’, 5), (‘best!’, 10)]  
>  **Explanation** : First element’s strings K value removed.

 **Method #1 : Using replace() + list comprehenson**

In this, we use replace() to perform task of removal of K character and list
comprehension to reform tuple.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K character from first element of Tuple

# Using replace() + list comprehenson

 

# initializing list

test_list = [("GF ! g !", 5), ("! i ! s", 4), ("best
!!", 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "!"

 

# replace with empty string removes the desired char.

res = [(sub[0].replace(K, ''), sub[1]) for sub in
test_list]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GF!g!', 5), ('!i!s', 4), ('best!!', 10)]
    The filtered tuples : [('GFg', 5), ('is', 4), ('best', 10)]
    

**Method #2 : Using translate() + list comprehension**

In this, we perform task of removal using translate(), which needs conversion
to ascii using ord(), and replaced with empty character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K character from first element of Tuple

# Using translate() + list comprehension

 

# initializing list

test_list = [("GF ! g !", 5), ("! i ! s", 4), ("best
!!", 10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "!"

 

# translation after conversion to ascii number 

res = [(sub[0].translate({ord(K): None}), sub[1]) for
sub in test_list]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GF!g!', 5), ('!i!s', 4), ('best!!', 10)]
    The filtered tuples : [('GFg', 5), ('is', 4), ('best', 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

