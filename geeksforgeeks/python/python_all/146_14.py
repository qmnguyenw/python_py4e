Python | Scramble words from a text file



Given some data in a text file, the task is to scramble the text and output in
a separate text file. So, we need to write a Python program that reads a text
file, scrambles the words in the file and writes the output to a new text
file.

 **Rules to be followed:**

  * Words less than or equal to 3 characters need not be scrambled.
  * Don’t scramble first and last char, so _Scrambling_ can become _Srbmnacilg_ or _Srbmnailcg_ or _Snmbracilg_ , i.e. letters except first and last can be scrambled in any order.
  * Punctuation at the end of the word to be maintained as is i.e. “Surprising, ” could become “Spsirnirug, ” but not “Spsirn, irug”.
  * Following punctuation marks are to be supported – Comma Question mark, Full stop, Semicolon, Exclamation.
  * Do this for a file and maintain sequences of lines.

On executing the program, it should prompt the user to enter input file name
and generate an output file with scrambled text. The output file should be
named by appending the word “Scrambled” to the input file name.

 **Example:**

    
    
    **Input :**  MyFile.txt ->
      
    Scrambling words is very  
    interesting. Because even  
    if they are scrambled, it   
    doesn't impact our   
    reading. Because we don't 
    read letter by letter, we 
    read the word as a whole.   
    
    **Output :** MyFileScrambled.txt ->
      
    Srbmnacilg wrods is vrey   
    itrensientg. Bscauee even  
    if tehy are srelabcmd, it  
    dosn'et ipcmat our 
    raidneg. Bacusee we dn'ot 
    raed lteetr by letetr, we 
    raed the wrod as a wolhe.
    

Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

punct = (".", ";", "!", "?", ",")

count = 0

new_word = ""

 

inputfile = input("Enter input file name:")

 

with open(inputfile, 'r') as fin:

 for line in fin.readlines(): # Read line by line in txt file

 

 for word in line.split(): # Read word by word in each line

 

 if len(word) > 3: # If word length >3

 

 '''If word ends with punctuation

 Remove firstletter, lastletter and punctuation

 Shuffle the words

 Add the removed letters (first letter)

 Add the removed letters (last letter)

 Add the removed letters (punctuation mark)'''

 

 if word.endswith(punct):

 word1 = word[1:-2]

 word1 = random.sample(word1, len(word1))

 word1.insert(0, word[0])

 word1.append(word[-2])

 word1.append(word[-1])

 

 '''If there is no punctuation mark 

 Remove first letter and last letter

 Shuffle the word

 Add the removed letters (first letter)

 Add the removed letters (last letter)

 Append the word and " " to the previous words'''

 

 else:

 word1 = word[1:-1]

 word1 = random.sample(word1, len(word1))

 word1.insert(0, word[0])

 word1.append(word[-1])

 new_word = new_word + ''.join(word1) + " "

 

 '''If word length <3

 just append the word and " " to the previous words'''

 

 else:

 new_word = new_word + word + " "

 

 # "Append to <filename>Scrambled.txt"

 

with open((inputfile[:-4] + "Scrambled.txt"), 'a+') as
fout:

 fout.write(new_word + "\n")

 

new_word = ""  
  
---  
  
 __

 __

 **Output:**

    
    
    Smcinrablg wodrs very Bauscee eevn tehy dnoes't
    icpamt Bcuesae d'not read lteter raed wrod whole. 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

