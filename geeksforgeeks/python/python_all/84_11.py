Python program to Reverse a single line of a text file



Given a text file. The task is to reverse a single line of user’s choice from
a given text file and update the already existing file.

 **Examples:**

    
    
    **Input:**
            Hello Geeks
            for geeks!
    
      User choice = 1
    
    **Output:**
            Hello Geeks
            geeks! for
    
    **Input:**
            This is a geek
            Welcome to GeeksforGeeks
            GeeksforGeeks is a computer science portal
    
        User choice = 0
    
    **Output:**
            geek a is This
            Welcome to GeeksforGeeks
            GeeksforGeeks is a computer science portal
    

**Implementation:**

Let’s suppose the text file looks like this –

![python-reverse-text-file](https://media.geeksforgeeks.org/wp-
content/uploads/20200318150045/python-reverse-text-file.png)

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Open file in read mode

f = open('GFG.txt', 'r')

 

# Read the content of the

# file and store it in a list

lines = f.readlines()

 

# Close file

f.close()

 

# User's choice

choice = 1

 

# Split the line into words 

line = lines[choice].split()

 

# line is reversed

Reversed = " ".join(line[::-1])

 

# Updating the content of the

# file

lines.pop(choice)

lines.insert(choice, Reversed)

 

# Open file in write mode

u = open('GFG.txt', 'w')

 

# Write the new content in file

# and note, it is overwritten 

u.writelines(lines)

u.close()  
  
---  
  
 __

 __

 **Output:**

![python-reverse-text-file1](https://media.geeksforgeeks.org/wp-
content/uploads/20200318150542/python-reverse-text-file1.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

