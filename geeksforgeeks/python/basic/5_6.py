Python – Append content of one text file to another



Having two file names entered from users, the task is to append the content of
the second file to the content of the first file.

 **Example**

    
    
    **Input :**
    file1.txt
    file2.txt
    
    **Ouput :**
    Content of first file (before appending) - geeksfor
    Content of second file (before appending) - geeks
    Content of first file (after appending) - geeksforgeeks
    Content of second file (after appending) - geeks
    

**Algorithm :**

  1. Enter the names of the files.
  2. Open both the files in read only mode using the open() function.
  3. Print the contents of the files before appending using the read() function.
  4. Close both the files using the close() function.
  5. Open the first file in append mode and the second file in read mode.
  6. Append the contents of the second file to the first file using the write() function.
  7. Reposition the cursor of the files at the beginning using the seek() function.
  8. Print the contents of the appended files.
  9. Close both the files.

Suppose the text files file1.txt and file2.txt contain the following data.

 **file1.txt**  
![file1.txt](https://media.geeksforgeeks.org/wp-
content/uploads/20200711111201/jupyter32.png)  
 **file2.txt**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200711111345/jupyter33.png)

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# entering the file names

firstfile = input("Enter the name of first file ")

secondfile = input("Enter the name of second file ")

 

# opening both files in read only mode to read initial contents

f1 = open(firstfile, 'r')

f2 = open(secondfile, 'r')

 

# printing the contens of the file before appending

print('content of first file before appending -', f1.read())

print('content of second file before appending -', f2.read())

 

# closing the files

f1.close()

f2.close()

 

# opening first file in append mode and second file in read mode

f1 = open(firstfile, 'a+')

f2 = open(secondfile, 'r')

 

# appending the contents of the second file to the first file

f1.write(f2.read())

 

# relocating the cursor of the files at the beginning

f1.seek(0)

f2.seek(0)

 

# printing the contents of the files after appendng

print('content of first file after appending -', f1.read())

print('content of second file after appending -', f2.read())

 

# closing the files

f1.close()

f2.close()  
  
---  
  
 __

 __

 **Output :**  
![Python - Append content of one text file to
another](https://media.geeksforgeeks.org/wp-
content/uploads/20200708125236/Outputfileappend-300x119.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

