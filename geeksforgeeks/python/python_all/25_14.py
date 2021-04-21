Python program to Sort Strings by Punctuation count



Given the Strings list, sort by punctuations count.

>  **Input** : test_list = [“gfg@%^”, “is”, “Best!”]  
> **Output** : [‘is’, ‘Best!’, ‘gfg@%^’]  
> **Explanation** : 0 < 1 < 3, sorted by punctuation count.
>
>  **Input** : test_list = [“gfg@%^”, “Best!”]  
> **Output** : [ ‘Best!’, ‘gfg@%^’]  
> **Explanation** : 1 < 3, sorted by punctuation count.

**Method #1 : Using** **string.punctuation** **+** **sort()**

In this, sorting is done using sort() and punctuations are extracted from
punctuation pool from string library. Performs inplace sort.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Punctuation count

# Using string.punctuation + sort()

from string import punctuation

 

def get_pnc_count(strng):

 

 # getting punctuation count

 return len([ele for ele in strng if ele in
punctuation])

 

# initializing list

test_list = ["gfg@%^", "is", "Best!", "fo@#r",
"@#$ge24eks!"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing inplace sort 

test_list.sort(key = get_pnc_count)

 

# printing result 

print("Sorted Strings list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg@%^’, ‘is’, ‘Best!’, ‘fo@#r’, ‘@#$ge24eks!’]  
> Sorted Strings list : [‘is’, ‘Best!’, ‘fo@#r’, ‘gfg@%^’, ‘@#$ge24eks!’]

 **Method #2 : Using** **sorted()** **\+ punctuation +** **lambda**

In this, we perform sort using sorted() using lambda to avoid external
function to perform task of filtering punctuations extracted using
punctuation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings by Punctuation count

# Using sorted() + punctuation + lambda

from string import punctuation

 

# initializing list

test_list = ["gfg@%^", "is", "Best!", "fo@#r",
"@#$ge24eks!"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort using sorted() with lambda

# function for filtering

res = sorted(test_list, key=lambda strng: len(

 [ele for ele in strng if ele in punctuation]))

 

# printing result

print("Sorted Strings list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg@%^’, ‘is’, ‘Best!’, ‘fo@#r’, ‘@#$ge24eks!’]  
> Sorted Strings list : [‘is’, ‘Best!’, ‘fo@#r’, ‘gfg@%^’, ‘@#$ge24eks!’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

