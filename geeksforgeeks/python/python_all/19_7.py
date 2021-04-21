Python – Equidistant consecutive characters Strings



Given a Strings List, extract all the strings, whose consecutive characters
are at common difference in ASCII order.

>  **Input** : test_list = [“abcd”, “egil”, “mpsv”, “abd”]  
> **Output** : [‘abcd’, ‘mpsv’]  
> **Explanation** : In mpsv, consecutive characters are at distance 3.
>
>  **Input** : test_list = [“abcd”, “egil”, “mpsw”, “abd”]  
> **Output** : [‘abcd’]  
> **Explanation** : In abcd, consecutive characters are at distance 1.  
>

**Method #1 : Using** **list comprehension** **+** **all()**

In this, we check for each character having common difference using all(), and
list comprehension is used to iterate strings.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equidistant consecutive characters Strings

# Using list comprehension + all()

 

# initializing list

test_list = ["abcd", "egil", "mpsv", "abd"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# ord() used to get ASCII value

res = [sub for sub in test_list if all(ord(

 sub[idx + 1]) - ord(sub[idx]) == ord(sub[1]) -
ord(sub[0]) for idx in range(0, len(sub) -
1))]

 

# printing result

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['abcd', 'egil', 'mpsv', 'abd']
    Filtered Strings : ['abcd', 'mpsv']
    

**Method #2 : Using** **filter()** **+** **lambda** **+** **ord()** **\+
all()**

In this, we perform task of filtering using filter() and lambda function. The
task of ord() is to get ASCII equivalent of each character.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Equidistant consecutive characters Strings

# Using list comprehension + all()

 

# initializing list

test_list = ["abcd", "egil", "mpsv", "abd"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# ord() used to get ASCII value 

res = [sub for sub in test_list if all(ord(sub[idx +
1]) - ord(sub[idx]) == ord(sub[1]) -
ord(sub[0]) for idx in range(0, len(sub) -1
))]

 

# printing result 

print("Filtered Strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['abcd', 'egil', 'mpsv', 'abd']
    Filtered Strings : ['abcd', 'mpsv']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

