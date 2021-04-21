Python – Sort String list by K character frequency



Given String list, perform sort operation on basis of frequency of particular
character.

>  **Input** : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”],
> K = ‘s’  
>  **Output** : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’]  
>  **Explanation** : bessst has 3 occurrance, geeksforgeekss has 3, and so on.
>
>  **Input** : test_list = [“geekforgeekss”, “is”, “bessst”], K = ‘e’  
>  **Output** : [“geekforgeekss”, “bessst”, “is”]  
>  **Explanation** : Ordered decreasing order of ‘e’ count.

 **Method #1 : Using sorted() + count() + lambda**

In this, sorted() is used to perform task of sort, count() is as function upon
which sorting is to be performed. using additional key param, and function
encapsulation used is lambda.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort String list by K character frequency

# Using sorted() + count() + lambda

 

# initializing list

test_list = ["geekforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 'e'

 

# "-" sign used to reverse sort

res = sorted(test_list, key = lambda ele: -ele.count(K))

 

# printing results

print("Sorted String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geekforgeeks', 'is', 'best', 'for', 'geeks']
    Sorted String : ['geekforgeeks', 'geeks', 'best', 'is', 'for']
    

**Method #2 : Using sort() + count() + lambda**

In this, we perform task of sort using sort(), this is similar to above, only
difference being that sorting is done inplace.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort String list by K character frequency

# Using sort() + count() + lambda

 

# initializing list

test_list = ["geekforgeeks", "is", "best", "for",
"geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 'e'

 

# "-" sign used to reverse sort

# inplace sort

test_list.sort(key = lambda ele: -ele.count(K))

 

# printing results

print("Sorted String : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geekforgeeks', 'is', 'best', 'for', 'geeks']
    Sorted String : ['geekforgeeks', 'geeks', 'best', 'is', 'for']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

