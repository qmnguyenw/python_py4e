Python – Substring Suffix Frequency



Given a String and substring, count all the substitutes from string which can
be used to complete the substring.

>  **Input** : test_str = “Gfg is good . Gfg is good . Gfg is better . Gfg is
> good .”, substr = “Gfg is”  
>  **Output** : {‘good’: 3, ‘better’: 1}  
>  **Explanation** : good occurs 3 times as suffix after substring in string
> hence 3. and so on.
>
>  **Input** : test_str = “Gfg is good . Gfg is good . Gfg is good . Gfg is
> good .”, substr = “Gfg is”  
>  **Output** : {‘good’: 4}  
>  **Explanation** : good occurs 4 times as suffix after substring in string
> hence 4. and so on.

 **Method #1 : Using regex() + defaultdict() + loop**

This is one of the ways in which this task can be performed. In this we
construct regex for getting all the matching elements for substring. Then
check all possible with occurrences in String, frequency count using
defaultdict().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring substitutes frequency

# Using regex() + defaultdict() + loop

from collections import defaultdict

import re

 

# initializing string

test_str = "Gfg is good . Gfg is best . Gfg is better . Gfg is good ."

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

substr = "Gfg is"

 

# initializing regex

temp = re.findall(substr + " (\w+)", test_str, flags =
re.IGNORECASE)

 

# adding values to form frequencies

res = defaultdict(int)

for idx in temp:

 res[idx] += 1

 

# printing result

print("Frequency of replacements : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : Gfg is good . Gfg is best . Gfg is better . Gfg is good .
    Frequency of replacements : {'good': 2, 'best': 1, 'better': 1}
    
    

**Method #2 : Using Counter() + regex()**

This is yet another way in which this task can be performed. In this, we
compute elements frequency using Counter().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring substitutes frequency

# Using Counter() + regex()

import re

from collections import Counter

 

# initializing string

test_str = "Gfg is good . Gfg is best . Gfg is better . Gfg is good ."

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing substring

substr = "Gfg is"

 

# initializing regex

temp = re.findall(substr + " (\w+)", test_str, flags =
re.IGNORECASE)

 

# adding values to form frequencies

res = dict(Counter(temp))

 

# printing result

print("Frequency of replacements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : Gfg is good . Gfg is best . Gfg is better . Gfg is good .
    Frequency of replacements : {'good': 2, 'best': 1, 'better': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

