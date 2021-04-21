Python – Length Conditional Concatenation



Given a list of strings, perform concatenation of Strings whose length is
greater than K.

>  **Input** : test_list = [“Gfg”, ‘is’, “Best”, ‘for’, ‘CS’, ‘Everything’], K
> = 3  
>  **Output** : BestEverything  
>  **Explanation** : All elements with Length > 3 are concatenated.
>
>  **Input** : test_list = [“Gfg”, ‘is’, “Best”, ‘for’, ‘CS’, ‘Everything’], K
> = 1  
>  **Output** : GfgisBestforCSEverything  
>  **Explanation** : All elements with Length > 1 are concatenated.

 **Method #1 : Using loop + len()**

This offers brute way to solve this problem. In this, we iterate for each
string and perform concatenation if the string length is greater than K using
len().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Length Conditional Concatenation

# Using loop + len()

 

# initializing lists

test_list = ["Gfg", 'is', "Best", 'for', 'CS',
'Everything']

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# loop to run through all the elements

res = ''

for ele in test_list:

 

 # using len() to check for length

 if len(ele) > 2:

 res += ele

 

# printing result 

print("String after Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'for', 'CS', 'Everything']
    String after Concatenation : GfgBestforEverything
    

**Method #2 : Using join() + filter() + lambda + len()**

The combination of above functions can be used to solve this problem. In this,
we perform concatenation using join(), filter and lambda are used for
conditional check using len().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Length Conditional Concatenation

# Using join() + filter() + lambda + len()

 

# initializing lists

test_list = ["Gfg", 'is', "Best", 'for', 'CS',
'Everything']

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# join() performing Concatenation of required strings

res = ''.join(filter(lambda ele: len(ele) > K, test_list))

 

# printing result 

print("String after Concatenation : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'for', 'CS', 'Everything']
    String after Concatenation : GfgBestforEverything
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

