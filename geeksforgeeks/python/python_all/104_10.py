Python program to modify the content of a Binary File



Given a binary file that contains some sentences (space separated words),
let’s write a Python program to modify or alter any particular word of the
sentence.

 **Approach:**  
 **Step 1:** Searching for the word in the binary file.  
**Step 2:** While searching in the file, the variable “pos” stores the
position of file pointer record then traverse(continue) reading of the record.  
**Step 3:** If the word to be searched exists then place the write pointer (to
ending of the previous record) i.e. at pos.  
**Step 4:** Call write() function to take the new record.  
**Step 5:** Write the new object at the position “pos” and hence the record is
updated and print “record successfully updated”.  
**Step 6:** If the word does not exists then print “record not found”.

 **Implementation**  
Let’s suppose the content of the binary file is:

![python-binary-file-input](https://media.geeksforgeeks.org/wp-
content/uploads/20200110122056/python-binary-file-input.png)

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to modify the

# content of binary file

# Function to update the

# content of binary file

def update_binary(word, new)

 # string variable to store

 # each word after reading

 # from the file

 string = b""

 # Flag variable to check

 # if the record is found or

 # not

 Flag = 0

 # Open the file in r + b mode which means

 # opening a binary file for reding and

 # writing

 with open('file.txt', 'r + b') as file:

 pos = 0

 # Reading the content of the

 # file character by character

 data = string = file.read(1)

 # Looping till the end of

 # file is reached

 while data:

 data = file.read(1)

 # Checking if the space is reached

 if data == b" ":

 # checking the word read with

 # the word entered by user

 if string == word:

 # Mpving the file pointer

 # at the end of the previously

 # read record

 file.seek(pos)

 # Updating the content of the file

 file.write(new)

 Flag = 1

 break

 else:

 # storing the position of

 # current file pointer i.e. at

 # the end of previously read record

 pos = file.tell()

 data = string = file.read(1)

 else:

 # Storing the data of the file

 # in the string variable

 string += data

 continue

 if Flag:

 print("Record successfully updated")

 else:

 print("Record not found")

 

 

# Driver code

# Input the word to be found

# and the new word

word = input("Enter the word to be replaced: ").encode()

new = input("\nEnter the new word: ").encode()

update_binary(word, new)  
  
---  
  
 __

 __

 **Output:**  

![python-binary-file-output-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200110122359/python-binary-file-output-1.png)

**Text file:**  

![python-binary-file-output-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200110122509/python-binary-file-output-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

