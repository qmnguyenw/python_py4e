Python – Sort Dictionary List by Key’s ith Index value



Given List of dictionaries, sort dictionaries on basis of Key’s ith index
value

>  **Input** : [{“Gfg” : “Best”, “for” : “Geeks”}, {“Gfg” : “Good”, “for” :
> “Me”}, {“Gfg” : “Better”, “for” : “All”}], K = “Gfg”, i = 1  
>  **Output** : [{‘Gfg’: ‘Best’, ‘for’: ‘Geeks’}, {‘Gfg’: ‘Better’, ‘for’:
> ‘All’}, {‘Gfg’: ‘Good’, ‘for’: ‘Me’}]  
>  **Explanation** : Sort in order of e = e < o, as 1st index element of
> "Gfg"'s value.
>
>  **Input** : [{“Gfg” : “Best”, “for” : “Geeks”}, {“Gfg” : “Good”, “for” :
> “Me”}, {“Gfg” : “Better”, “for” : “All”}], K = “Gfg”, i = 0  
>  **Output** : [{‘Gfg’: ‘Best’, ‘for’: ‘Geeks’}, {‘Gfg’: ‘Better’, ‘for’:
> ‘All’}, {‘Gfg’: ‘Good’, ‘for’: ‘Me’}]  
>  **Explanation** : Sort in order of B = B < G, as 1st index element of
> "Gfg"'s value.

 **Method #1 : Using sort() + lambda**

The combination of above functions can be used to solve this problem. In this,
we perform task of sorting using sort() and lambda function in “key” parameter
drives condition.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary List by Key's ith Index value

# Using sort() + lambda

 

# initializing lists

test_list = [{"Gfg" : "Best", "for" : "Geeks"},

 {"Gfg" : "Good", "for" : "Me"},

 {"Gfg" : "Better", "for" : "All"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing i 

i = 2

 

# using sort to perform sort(), lambda

# function drives conditions

res = sorted(test_list, key = lambda sub: sub[K][i])

 

# printing result 

print("List after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: ‘Best’, ‘for’: ‘Geeks’}, {‘Gfg’: ‘Good’, ‘for’:
> ‘Me’}, {‘Gfg’: ‘Better’, ‘for’: ‘All’}]  
> List after sorting : [{‘Gfg’: ‘Good’, ‘for’: ‘Me’}, {‘Gfg’: ‘Best’, ‘for’:
> ‘Geeks’}, {‘Gfg’: ‘Better’, ‘for’: ‘All’}]

 **Method #2 : Using sort() + lambda + get()**

The combination of above functions can also solve this problem. This is just a
slight variation to above method. In this, we use get() to avoid chances of
key not present in particular record.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary List by Key's ith Index value

# Using sort() + lambda + get()

 

# initializing lists

test_list = [{"Gfg" : "Best", "for" : "Geeks"},

 {"Gfg" : "Good", "for" : "Me"},

 {"Gfg" : "Better", "for" : "All"}]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = "Gfg"

 

# initializing i 

i = 2

 

# using sort to perform sort(), lambda

# function drives conditions, get() used to 

# avoid missing key error

res = sorted(test_list, key = lambda sub: sub.get(K)[i])

 

# printing result 

print("List after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [{‘Gfg’: ‘Best’, ‘for’: ‘Geeks’}, {‘Gfg’: ‘Good’, ‘for’:
> ‘Me’}, {‘Gfg’: ‘Better’, ‘for’: ‘All’}]  
> List after sorting : [{‘Gfg’: ‘Good’, ‘for’: ‘Me’}, {‘Gfg’: ‘Best’, ‘for’:
> ‘Geeks’}, {‘Gfg’: ‘Better’, ‘for’: ‘All’}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

