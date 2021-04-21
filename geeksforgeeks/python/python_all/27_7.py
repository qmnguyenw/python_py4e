Python Program that Extract words starting with Vowel From A list



Given a list with string elements, the following program extracts those
elements which start with vowels(a, e, i, o, u).

>  **Input** : test_list = [“all”, “love”, “get”, “educated”, “by”, “gfg”]  
> **Output** : [‘all’, ‘educated’]  
> **Explanation** : a, e are vowels, hence words extracted.  
>  **Input** : test_list = [“all”, “love”, “get”, “educated”, “by”, “agfg”]  
> **Output** : [‘all’, ‘educated’, ‘agfg’]  
> **Explanation** : a, e, a are vowels, hence words extracted.

**Method 1 :** _Using_ _startswith()_ _and_ _loop_

In this, we check for each word, and check if it starts with a vowel using
startswith() on the first alphabet of every word. The iteration part is done
using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["all", "love", "and", "get", "educated",
"by", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

vow = "aeiou"

for sub in test_list:

 flag = False

 

 # checking for begin char

 for ele in vow:

 if sub.startswith(ele):

 flag = True

 break

 if flag:

 res.append(sub)

 

# printing result 

print("The extracted words : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [‘all’, ‘love’, ‘and’, ‘get’, ‘educated’, ‘by’,
> ‘gfg’]  
> The extracted words : [‘all’, ‘and’, ‘educated’]

 **Method 2 :** _Using_ _any()_ _,_ _startswith()_ _and_ _loop_

In this, we check for vowels using any(), and rest all the functionality is
similar to the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["all", "love", "and", "get", "educated",
"by", "gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

vow = "aeiou"

for sub in test_list:

 

 # check for vowel beginning

 flag = any(sub.startswith(ele) for ele in vow)

 

 if flag:

 res.append(sub)

 

# printing result 

print("The extracted words : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘all’, ‘love’, ‘and’, ‘get’, ‘educated’, ‘by’,
> ‘gfg’]  
> The extracted words : [‘all’, ‘and’, ‘educated’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

