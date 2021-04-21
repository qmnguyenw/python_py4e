Python – Extract hashtags from text



A **hashtag** is a keyword or phrase preceded by the hash symbol (#), written
within a post or comment to highlight it and facilitate a search for it. Some
examples are: #like, #gfg, #selfie

We are provided with a string containing hashtags, we have to extract these
hashtags into a list and print them.

 **Examples :**

    
    
    **Input :** GeeksforGeeks is a wonderful #website for #ComputerScience
    **Output :** website , ComputerScience
    
    **Input :** This day is beautiful! #instagood #photooftheday #cute
    **Output :** instagood, photooftheday, cute
    

**Method 1:**

  * Split the text into words using the split() method.
  * For every word check if the first character is a hash symbol(#) or not.
  * If yes then add the word to the list of hashtags without the hash symbol.
  * Print the list of hashtags.

 __

 __  
 __

 __

 __  
 __  
 __

# function to print all the hashtags in a text

def extract_hashtags(text):

 

 # initializing hashtag_list variable

 hashtag_list = []

 

 # splitting the text into words

 for word in text.split():

 

 # checking the first charcter of every word

 if word[0] == '#':

 

 # adding the word to the hashtag_list

 hashtag_list.append(word[1:])

 

 # printing the hashtag_list

 print("The hashtags in \"" + text + "\" are :")

 for hashtag in hashtag_list:

 print(hashtag)

 

if __name__=="__main__":

 text1 = "GeeksforGeeks is a wonderful # website for #
ComputerScience"

 text2 = "This day is beautiful ! # instagood # photooftheday # cute"

 extract_hashtags(text1)

 extract_hashtags(text2)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The hashtags in "GeeksforGeeks is a wonderful #website for #ComputerScience" are :
    website
    ComputerScience
    The hashtags in "This day is beautiful! #instagood #photooftheday #cute" are :
    instagood
    photooftheday
    cute
    

**Method 2 :** Using regular expressions.

 __

 __  
 __

 __

 __  
 __  
 __

# import the regex module

import re

 

# function to print all the hashtags in a text

def extract_hashtags(text):

 

 # the regular expression

 regex = "#(\w+)"

 

 # extracting the hashtags

 hashtag_list = re.findall(regex, text)

 

 # printing the hashtag_list

 print("The hashtags in \"" + text + "\" are :")

 for hashtag in hashtag_list:

 print(hashtag)

 

if __name__=="__main__":

 text1 = "GeeksforGeeks is a wonderful # website for #
ComputerScience"

 text2 = "This day is beautiful ! # instagood # photooftheday # cute"

 extract_hashtags(text1)

 extract_hashtags(text2)  
  
---  
  
 __

 __

 **Output :**

    
    
    The hashtags in "GeeksforGeeks is a wonderful #website for #ComputerScience" are :
    website
    ComputerScience
    The hashtags in "This day is beautiful! #instagood #photooftheday #cute" are :
    instagood
    photooftheday
    cute
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

