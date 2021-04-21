Python | Alternate vowels and consonents in String



Sometimes, while working with Strings in Python, we can have a problem in
which we may need restructure a string, adding alternate vowels and consonants
in it. This is a popular school-level problem and having solution to this can
be useful. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop +join() + zip_longest()**  
The combination of above functions can be used to perform this task. In this,
we first, separate vowels and consonents in separate lists. And then join
alternatively using zip_longest() and join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate vowels and consonents in String

# using zip_longest() + join() + loop

from itertools import zip_longest

 

# initializing string 

test_str = "gaeifgsbou"

 

# printing original string 

print("The original string is : " + test_str)

 

# Alternate vowels and consonents in String

# using zip_longest() + join() + loop

vowels = ['a', 'e', 'i', 'o', 'u']

test_vow = []

test_con = []

for ele in test_str:

 if ele in vowels:

 test_vow.append(ele)

 elif ele not in vowels:

 test_con.append(ele)

res = ''.join(''.join(ele) for ele in zip_longest(test_vow, test_con,
fillvalue =''))

 

# printing result

print("Alternate consonents vowels are: " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gaeifgsbou
    Alternate consonents vowels are: agefigosub
    

**Method #2 : Using loop + map() \+ lambda**  
This task can also be performed using combination of above functionalities. It
is similar as above method, the only differences are usage of map() and lambda
functions to perform alternate joining.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate vowels and consonents in String

# using loop + map() + lambda

from itertools import zip_longest

 

# initializing string 

test_str = "gaeifgsbou"

 

# printing original string 

print("The original string is : " + test_str)

 

# Alternate vowels and consonents in String

# using loop + map() + lambda

vowels = ['a', 'e', 'i', 'o', 'u']

test_vow = []

test_con = []

for ele in test_str:

 if ele in vowels:

 test_vow.append(ele)

 elif ele not in vowels:

 test_con.append(ele)

res = ''.join(map(lambda sub: sub[0] + sub[1], 

 zip_longest(test_vow, test_con, fillvalue ='')))

 

# printing result

print("Alternate consonents vowels are: " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : gaeifgsbou
    Alternate consonents vowels are: agefigosub
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

