Python – Extract Strings with Successive Alphabets in Alphabetical Order



Given a string list, extract list which has any succession of characters as
they occur in alphabetical order.

>  **Input** : test_list = [‘gfg’, ‘ij’, ‘best’, ‘for’, ‘geeks’]  
> **Output** : [‘ij’, ‘gfg’, ‘best’]  
> **Explanation** : i-j, f-g, s-t are consecutive pairs.
>
>  **Input** : test_list = [‘gf1g’, ‘in’, ‘besht’, ‘for’, ‘geeks’]  
> **Output** : []  
> **Explanation** : No consecutive pairs.

**Method #1 : Using ord() + loop**

In this, we check for each string if it contains and character with is the
alphabetic successor to its preceding character, ASCII conversion is done
using ord().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Strings with successive Alphabets

# Using ord() + loop

 

# initializing string list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # iterating for string 

 for idx in range(len(sub) - 1):

 

 # checking for alphabetic consecution

 if ord(sub[idx]) == ord(sub[idx + 1]) - 1:

 res.append(sub)

 break

 

# printing result 

print("Strings with alphabetic consecution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Strings with alphabetic consecution : ['gfg', 'best']
    

**Method #2 : Using any() + filter() + lambda**

In this, we check for any succession using any(), and task of filtering is
done using filter() and lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Strings with successive Alphabets

# Using any() + filter() + lambda

 

# initializing string list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# filtering using filter, and checking for any substring using any()

res = list(filter(lambda sub: any(ord(sub[idx]) ==
ord(

 sub[idx + 1]) - 1 for idx in range(len(sub) -
1)), test_list))

 

# printing result

print("Strings with alphabetic consecution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Strings with alphabetic consecution : ['gfg', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

