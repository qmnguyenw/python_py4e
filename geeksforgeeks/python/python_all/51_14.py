Python – Sort dictionaries list by Key’s Value list index



Given list of dictionaries, sort dictionaries on basis of Key’s index value.

>  **Input** : [{“Gfg” : [6, 7, 8], “is” : 9, “best” : 10},  
> {“Gfg” : [2, 0, 3], “is” : 11, “best” : 19},  
> {“Gfg” : [4, 6, 9], “is” : 16, “best” : 1}], K = “Gfg”, idx = 0  
>  **Output** : [{‘Gfg’: [2, 0, 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’: [4, 6, 9],
> ‘is’: 16, ‘best’: 1}, {‘Gfg’: [6, 7, 8], ‘is’: 9, ‘best’: 10}]  
>  **Explanation** : 2<4<6, hence dictionary ordered in that way by 0th index
> of Key.
>
>  **Input** : [{“Gfg” : [6, 7, 8], “is” : 9, “best” : 10},  
> {“Gfg” : [2, 0, 3], “is” : 11, “best” : 19},  
> {“Gfg” : [4, 6, 9], “is” : 16, “best” : 1}], K = “Gfg”, idx = 1  
>  **Output** : [{‘Gfg’: [2, 0, 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’: [4, 6, 9],
> ‘is’: 16, ‘best’: 1}, {‘Gfg’: [6, 7, 8], ‘is’: 9, ‘best’: 10}]  
>  **Explanation** : 0<6<7, hence dictionary ordered in that way by 1st index.

 **Method #1 : Using sorted() + lambda**

The combination of above functions can be used to solve this problem. In this,
we perform sort using sorted and logic based on list index is provided in
lambda function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionaries list by Key's Value list index

# Using sorted() + lambda

 

# initializing lists

test_list = [{"Gfg" : [6, 7, 8], "is" : 9,
"best" : 10}, 

 {"Gfg" : [2, 0, 3], "is" : 11, "best" :
19},

 {"Gfg" : [4, 6, 9], "is" : 16, "best" :
1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing idx 

idx = 2

 

# using sorted() to perform sort in basis of 1 parameter key and 

# index

res = sorted(test_list, key = lambda ele: ele[K][idx])

 

# printing result 

print("The required sort order : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: [6, 7, 8], ‘is’: 9, ‘best’: 10}, {‘Gfg’: [2, 0,
> 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’: [4, 6, 9], ‘is’: 16, ‘best’: 1}]  
> The required sort order : [{‘Gfg’: [2, 0, 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’:
> [6, 7, 8], ‘is’: 9, ‘best’: 10}, {‘Gfg’: [4, 6, 9], ‘is’: 16, ‘best’: 1}]

 **Method #2 : Using sorted() + lambda (Additional parameter in case of tie)**

This is modification in sorting of values, adding another parameter in case of
tie of values among list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionaries list by Key's Value list index

# Using sorted() + lambda (Additional parameter in case of tie)

 

# initializing lists

test_list = [{"Gfg" : [6, 7, 9], "is" : 9,
"best" : 10}, 

 {"Gfg" : [2, 0, 3], "is" : 11, "best" :
19},

 {"Gfg" : [4, 6, 9], "is" : 16, "best" :
1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing idx 

idx = 2

 

# initializing K2 

K2 = "best"

 

# using sorted() to perform sort in basis of 2 parameter key

# inner is evaluated after the outer key in lambda order

res = sorted(sorted(test_list, key = lambda ele: ele[K2]),
key = lambda ele: ele[K][idx])

 

# printing result 

print("The required sort order : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: [6, 7, 9], ‘is’: 9, ‘best’: 10}, {‘Gfg’: [2, 0,
> 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’: [4, 6, 9], ‘is’: 16, ‘best’: 1}]  
> The required sort order : [{‘Gfg’: [2, 0, 3], ‘is’: 11, ‘best’: 19}, {‘Gfg’:
> [4, 6, 9], ‘is’: 16, ‘best’: 1}, {‘Gfg’: [6, 7, 9], ‘is’: 9, ‘best’: 10}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

