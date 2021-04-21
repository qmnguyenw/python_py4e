Python – Escape reserved characters in Strings List



Given List of Strings, escape reserved charaters in each String.

>  **Input** : test_list = [“Gf-g”, “be)s(t”]  
>  **Output** : [‘Gf\\\\-g’, ‘be\\\\)s\\\\(t’]  
>  **Explanation** : All reserved character elements escaped, by adding double
> \\\\.
>
>  **Input** : test_list = [“Gf-g”]  
>  **Output** : [‘Gf\\\\-g’]  
>  **Explanation** : All reserved character elements escaped, by adding double
> \\\\.

 **Method #1 : Using join() + list comprehension**

In this, we construct the dictionary to map each of reserved character to its
escaped version, and then perform the task of replacement in list
comprehension and join the result to form Strings.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Escape reserved characters in Strings List

# Using list comprehension + join()

 

# initializing list

test_list = ["Gf-g", "is*", "be)s(t"]

 

# printing string

print("The original list : " + str(test_list))

 

# the reserved string 

reserved_str = """? & | ! { } [ ] ( ) ^ ~ * : \ " ' + -"""

 

# the mapped escaped values

esc_dict = { chr : f"\\{chr}" for chr in reserved_str}

 

# performing transformation using join and list comprehension

res = [ ''.join(esc_dict.get(chr, chr) for chr in sub)
for sub in test_list]

 

# printing results 

print("The resultant escaped String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gf-g', 'is*', 'be)s(t']
    The resultant escaped String : ['Gf\\-g', 'is\\*', 'be\\)s\\(t']
    

**Method #2 : Using maketrans() + translate() + zip()**

In this, the escaping is made by pairing using zip() and maketrans() rather
than dictionary for mapping. The translation is done using the result of
maketrans().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Escape reserved characters in Strings List

# Using maketrans() + translate() + zip()

 

# initializing list

test_list = ["Gf-g", "is*", "be)s(t"]

 

# printing string

print("The original list : " + str(test_list))

 

# reserved_chars

reserved_chars = '''?&|!{}[]()^~*:\\"'+-'''

 

# the escaping logic 

mapper = ['\\' + ele for ele in reserved_chars]

result_mapping = str.maketrans(dict(zip(reserved_chars,
mapper)))

 

# reforming result

res = [sub.translate(result_mapping) for sub in test_list]

 

# printing results 

print("The resultant escaped String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gf-g', 'is*', 'be)s(t']
    The resultant escaped String : ['Gf\\-g', 'is\\*', 'be\\)s\\(t']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

