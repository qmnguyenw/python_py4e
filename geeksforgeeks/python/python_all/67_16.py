SpongeBob Mocking Text Generator – Python



SpongeBob mocking text (spongemock) is a style of writing in which the
alphabets are randomly written in upper and lower case. It is used in internet
communities to mock something. The text originated as a meme from the
SpongeBob cartoon series.

 **Examples :**

    
    
    **Input :** The quick brown fox jumps over the lazy dog.
    **Output :** tHE QuiCK BrOWN fOX juMps over tHe lAzY dOG.
    
    **Input :** This sentence is to test the function.
    **Output :** This seNtENce is TO TeST THE funcTiON.
    

**Algorithm :**

  1. Process the input string by character.
  2. Check if the character is an alphabet by using isalpha() method.
  3. Use random.random() method to generate a random number between 0 and 1.
  4. If the number generated is greater than 0.5 then change the character to upper case using upper() method.
  5. If the number generated is less than or equal to 0.5 then change the character to lower case using lower() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import the random library

import random

 

# Function to convert into spongemock

def spongemock(input_text):

 

 # variable declaration for the output text

 output_text = ""

 

 # check the cases for every individual character

 for char in input_text:

 

 # check if the character is an alphabet

 if char.isalpha():

 

 # convert to upper case

 if random.random() > 0.5:

 output_text += char.upper()

 

 # convert to lower case

 else:

 output_text += char.lower()

 

 # if character is not and alphabet

 # add it as it is

 else:

 output_text += char

 

 # return the output_text

 return output_text

 

# Driver code

if __name__=="__main__":

 input_text1 = "The quick brown fox jumps over the lazy dog."

 input_text2 = "This sentence is to test the function."

 print(spongemock(input_text1))

 print(spongemock(input_text2))  
  
---  
  
 __

 __

 **Output :**

    
    
    tHe qUICk BrOWn fox jUMPs oVEr thE lAZy dOG.
    THIS seNTEncE IS tO TesT tHe FuNcTIOn.
    

The above code generates the text with equal amount if lower and upper case
characters. If we want to skew the balance to favour one side we can switch
the random.random() method with random.triangular() method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the random library

import random

 

def skewupper():

 low = 0

 high = 100

 mode = 80

 return random.triangular(low, high, mode)

 

def skewlower():

 low = 0

 high = 100

 mode = 20

 return random.triangular(low, high, mode)

 

# Function to convert into spongemock

# with more upper case charcters

def spongemockupper(input_text):

 output_text = ""

 for char in input_text:

 if char.isalpha():

 if skewupper() > 50:

 output_text += char.upper()

 else:

 output_text += char.lower()

 else:

 output_text += char

 return output_text

 

# Function to convert into spongemock

# with more lower case charcters

def spongemocklower(input_text):

 output_text = ""

 for char in input_text:

 if char.isalpha():

 if skewlower() > 50:

 output_text += char.upper()

 else:

 output_text += char.lower()

 else:

 output_text += char

 return output_text

 

# Driver code

if __name__=="__main__":

 input_text1 = "The quick brown fox jumps over the lazy dog."

 print("Spongemock text with more upper case characters :\n" +

 spongemockupper(input_text1))

 

 print("\nSpongemock text with more lower case characters :\n" +

 spongemocklower(input_text1))  
  
---  
  
 __

 __

 **Output :**

    
    
    Spongemock text with more upper case characters :
    ThE qUICK BROwN FOX jUMPs OVeR THE lazy DoG.
    
    Spongemock text with more lower case characters :
    The qUick BrOwn fOX JuMPs oveR the LaZy DOg.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

