English dictionary application using Python



 **Dictionary** ****in Python is an unordered collection of data values, used
to store data values like a map, which unlike other Data Types that hold only
single value as an element, Dictionary holdskey:value pair. Key value is
provided in the dictionary to make it more optimized. Each key-value pair in a
Dictionary is separated by a colon :, whereas each key is separated by a
‘comma’.

A Dictionary in Python works similar to the Dictionary in a real world. Keys
of a Dictionary must be unique and of immutable data type such as Strings,
Integers, and tuples, but the key-values can be repeated and be of any type.

 **Note** – To know more about dictionary click here.

#### Modules needed:

  *  **json:** It comes built-in with python, so there is no need to install it externally. To know more about JSON click here.
  *  **difflib:** This module provides classes and functions for comparing sequences. It also comes built-in with python so there is no need to install it externally.

 **Steps:**

  1. Download a JSON file containing English dictionary words in a python dictionaries data type format, or arrange the file content in that way.
  2. Create a folder and add the downloaded .json file and python script in that folder.
  3. In python editor, import the required modules.

Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import the modules required

import json

from difflib import get_close_matches

 

# Loading data from json file

# in python dictionary

data = json.load(open("dictionary.json"))

 

def translate(w):

 # converts to lower case

 w = w.lower()

 

 if w in data:

 return data[w]

 # for getting close matches of word

 elif len(get_close_matches(w, data.keys())) > 0: 

 yn = input("Did you mean % s instead? Enter Y if yes, or N if no:
" % get_close_matches(w, data.keys())[0])

 yn = yn.lower()

 if yn == "y":

 return data[get_close_matches(w, data.keys())[0]]

 elif yn == "n":

 return "The word doesn't exist. Please double check it."

 else:

 return "We didn't understand your entry."

 else:

 return "The word doesn't exist. Please double check it."

 

# Driver code

word = input("Enter word: ")

output = translate(word)

 

if type(output) == list:

 for item in output:

 print(item)

else:

 print(output)

input('Press ENTER to exit')   
  
---  
  
__

__

Important, the output should not vary with different cases such as upper case
and lower case input of same text should be same i.e rain or Rain or RaIn
should produce same output. Also if user mistakes with spelling of word it
should return the close words related to the word input or print a user
friendly message that word does not exist.

 **Input:**

    
    
    rain

 **Output:**  
![dictionary-python-script](https://media.geeksforgeeks.org/wp-
content/uploads/20191030114206/rain1.png)

For mixed cases –  
 **Input:**

    
    
    RaIn

 **Output:**  
![dictionary-python-script](https://media.geeksforgeeks.org/wp-
content/uploads/20191030114635/rain2.png)

If spelling is wrong it gives the word holding closest meaning with word typed
by the user as shown. Suppose if the input is “rane” and the user wanter to
search “range”, then the output will be as follows.  
 **Input:**

    
    
    rane

 **Output:**  
![dictionary-python-script](https://media.geeksforgeeks.org/wp-
content/uploads/20191030115306/range.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

