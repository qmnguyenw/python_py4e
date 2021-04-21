Get similar words suggestion using Enchant in Python



For the given user input, get similar words through Enchant module.

Enchant is a module in python which is used to check the spelling of a word,
gives suggestions to correct words. Also, gives antonym and synonym of words.
It checks whether a word exists in dictionary or not. Other dictionaries can
also be added, as, (“en_UK”), (“en_CA”), (“en_GB”) etc.

To install enchant :

    
    
    pip install pyenchant

 **Examples :**

    
    
    Input : Helo
    Output : Hello, Help, Hero, Helot, Hole
    
    Input : Trth
    Output : Truth, Trash, Troth, Trench
    

  
Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print the similar

# words using Enchant module

 

# Importing the Enchant module

import enchant

 

# Using 'en_US' dictionary

d = enchant.Dict("en_US")

 

# Taking input from user

word = input("Enter word: ")

 

d.check(word)

 

# Will suggest similar words

# form given dictionary

print(d.suggest(word))  
  
---  
  
 __

 __

 **Output :**

    
    
    Enter word: **aple**
    
    ['pale', 'ale', 'ape', 'maple', 'ample', 'apple', 'plea', 'able', 'apse']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

