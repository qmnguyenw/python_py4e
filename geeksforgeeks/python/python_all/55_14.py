Python – Fill Strings for size K in Tuple List



Sometimes while working with Tuple lists, we can have a problem in which we
need to perform filling of strings to complete certain size in lists. This
type of ask can occur in data domains and data preprocessing. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [(‘Gfg’, ‘is’), (‘best’, ‘for’), (‘CS’, ‘Geeks’)],
> K = 6, fill_char = ‘#’  
>  **Output** : [(‘Gfg###’, ‘is####’), (‘best##’, ‘for###’), (‘CS####’,
> ‘Geeks#’)]
>
>  **Input** : test_list = [(‘Gfg’, ‘is’), (‘best’, ‘for’), (‘CS’, ‘Geeks’)],
> K = 5, fill_char = ‘!’  
>  **Output** : [(‘Gfg!!’, ‘is!!!’), (‘best!’, ‘for!!’), (‘CS!!!’, ‘Geeks’)]

 **Method #1 : Using list comprehension +len()**  
This functionality is shorthand to brute force method that can be applied to
solve this problem. In this, we perform task of checking for K size using
len(), and perform required fill by a character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Fill Strings for size K in Tuple List

# Using list comprehension + len()

 

# initializing list

test_list = [('Gfg', 'is'), ('best', 'for'), ('CS',
'Geeks')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 8

 

# initializing fill_char

fill_char = '*'

 

# Fill Strings for size K in Tuple List

# Using list comprehension + len()

res = [(a + fill_char * (K - len(a)), b + fill_char
* (K - len(b))) for a, b in test_list]

 

# printing result 

print("The modified list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 'is'), ('best', 'for'), ('CS', 'Geeks')]
    The modified list : [('Gfg*****', 'is******'), ('best****', 'for*****'), ('CS******', 'Geeks***')]
    

