Python – Words Frequency in String Shorthands



Sometimes while working with Python strings, we can have problem in which we
need to extract frequency of all the words in string. This problem has been
solved earlier. This discusses the shorthands to solve this problem as this
has application in many domains ranging from web development and competitive
programming. Let’s discuss certain ways in which this problem can be solved.

>  **Input** : test_str = ‘Gfg is best’  
>  **Output** : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
>
>  **Input** : test_str = ‘Gfg Gfg Gfg’  
>  **Output** : {‘Gfg’: 3}

 **Method #1 : Using dictionary comprehension +count() + split()**  
The combination of above functions can be used to solve this problem. In this,
we first split all the words and then perform count of them using count().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Words Frequency in String Shorthands

# Using dictionary comprehension + count() + split()

 

# initializing string

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Words Frequency in String Shorthands

# Using dictionary comprehension + count() + split()

res = {key: test_str.count(key) for key in test_str.split()}

 

# printing result 

print("The words frequency : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original string is : Gfg is best . Geeks are good and Geeks like Gfg  
> The words frequency : {‘Gfg’: 2, ‘is’: 1, ‘best’: 1, ‘.’: 1, ‘Geeks’: 2,
> ‘are’: 1, ‘good’: 1, ‘and’: 1, ‘like’: 1}

