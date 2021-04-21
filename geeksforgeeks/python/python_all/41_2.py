Python – Remove similar index elements in Strings



Given two strings, removed all elements from both, which are same at similar
index.

>  **Input** : test_str1 = ‘geels’, test_str2 = ‘beaks’  
>  **Output** : gel, bak  
>  **Explanation** : e and s are removed as occur in same indices.
>
>  **Input** : test_str1 = ‘geeks’, test_str2 = ‘geeks’  
>  **Output** : ”, ”  
>  **Explanation** : Same strings, all same index, hence removed.

 **Method #1 : Using loop + zip() + join()**

In this, we pair elements with its index using join(), and check for
inequality to filter only dissimilar elements in both strings, join() is used
to convert result in strings.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove similar index elements in Strings

# Using join() + zip() + loop

 

# initializing strings

test_str1 = 'geeks'

test_str2 = 'beaks'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# conversion to list for zipping

list1 = list(test_str1)

list2 = list(test_str2)

res1 = []

res2 = []

for ch1, ch2 in zip(list1, list2):

 

 # check inequalities

 if ch1 != ch2:

 res1.append(ch1)

 res2.append(ch2)

 

# conversion to string 

res1 = "".join(res1)

res2 = "".join(res2)

 

# printing result 

print("Modified String 1 : " + str(res1)) 

print("Modified String 2 : " + str(res2))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeks
    The original string 2 is : beaks
    Modified String 1 : ge
    Modified String 2 : ba
    

**Method #2 : Using list comprehension**

Performs task using similar method as above, just one-liner to perform task in
compact form.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove similar index elements in Strings

# Using list comprehension

 

# initializing strings

test_str1 = 'geeks'

test_str2 = 'beaks'

 

# printing original strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# one-liner to solve problem

res = ["".join(mastr) for mastr

 in zip(*[(a, b) for a, b in zip(test_str1, test_str2)
if a != b])]

 

# printing result 

print("Modified String 1 : " + str(res[0])) 

print("Modified String 2 : " + str(res[1]))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : geeks
    The original string 2 is : beaks
    Modified String 1 : ge
    Modified String 2 : ba
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

