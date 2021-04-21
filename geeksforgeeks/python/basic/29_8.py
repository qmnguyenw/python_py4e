A Game of Anagrams in Python



 **Project idea:**

The aim of this project is to create a game in python in which the user is
presented with an anagram of a word and has to guess the right word within a
limited number of attempts.

 **Features of Project:**

  1. The user is given a fixed number of attempts to guess the correct word. The number of attempts is dependent on the length of the word.
  2. After each incorrect attempt the user is provided with a hint of the correct word.
  3. If the user is not able to guess the right word within the fixed number of attempt the correct word is displayed and the game moves on to the next word.
  4. Ctrl+C or Ctrl+D exits the game.

 **Implementation:**

This tutorial is valid only for Linux based systems. This tutorial is written
on a Linux Mint 17.1 system. For implementing on other Linux systems
(Redhat,Arch) see special note at the end of this tutorial.

  

  

In almost all the Linux based systems there is a file located at directory
location “/usr/share/dict/” under different names like “cracklib-small”(Ubuntu
based systems),”words”(Redhat,Arch) which contains words from dictionary and
are often used by many applications to implement features such as “spell-
check”.

In this project, I will be using the same file to create a game of anagrams.

Reading the file can provide us with all the words required for the game. The
words in the file are separated with a new-line so while reading the file we
need to split the words based on the new-line character to get individual
words. The code for the same would look like:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

loc='/usr/share/dict/cracklib-small'

with open(loc) as f:

content=f.read().split('\n')

f.close()  
  
---  
  
 __

 __

The file also contains words like “zoo’s” but we do not want such words in our
game so we can omit them. To avoid making the game too simple I decided to
also ommit words of length less than 5 but this step is optional and can be
skipped. The code for the same looks like:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

l=len(content)

words=[]

for i in range(0,l):

 if '\'' in content[i] or len(content[i])<5:

 continue

words.append(content[i])  
  
---  
  
 __

 __

The file also contains words like “2nd,3rd” at the start of the file. To
prevent them from appearing in our game we omit them by:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

words=words[1:]

d=len(words)

words=words[:d]  
  
---  
  
 __

 __

