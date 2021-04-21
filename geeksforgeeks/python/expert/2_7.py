Pulling a random word or string from a line in a text file in Python



File handling in Python is really simple and easy to implement. In order to
pull a random word or string from a text file, we will first open the file in
**read** mode and then use the methods in Python’s **random** module to pick a
random word.

There are various ways to perform this operation:

This is the text file we will read from:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201202005732/ssmyFile-660x190.jpg)

 **Method 1: Using** **random.choice()**

  

  

 **Steps:**

  1. Using **with** function, open the file in read mode. The **with** function takes care of closing the file automatically.
  2. Read all the text from the file and store in a string
  3. Split the string into words separated by space.
  4. Use **random.choice()** to pick a word or string.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to pick a random

# word from a text file

import random

 

# Open the file in read mode

with open("MyFile.txt", "r") as file:

 allText = file.read()

 words = list(map(str, allText.split()))

 

 # print random string

 print(random.choice(words))  
  
---  
  
 __

 __

Note: The **split()** function, by default, splits by white space. If you want
any other delimiter like newline character you can specify that as an
argument.

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201202005518/output1.jpg)

Output for two sample runs

The above can be achieved with just a single line of code like this :

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import required module

import random

 

# print random word

print(random.choice(open("myFile.txt","r").readline().split()))  
  
---  
  
 __

 __

 **Method 2: Using** **random.randint()** ****

**Steps:**

  1. Open the file in read mode using **with** function
  2. Store all data from the file in a string and split the string into words.
  3. Count the total number of words.
  4. Use **random.randint()** to generate a random number between 0 and the _word_count._
  5. Print the word at that position.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# using randint()

import random

 

# open file

with open("myFile.txt", "r") as file:

 data = file.read()

 words = data.split()

 

 # Generating a random number for word position

 word_pos = random.randint(0, len(words)-1)

 print("Position:", word_pos)

 print("Word at position:", words[word_pos])  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201202005634/output2.jpg)

Output for two sample runs

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

