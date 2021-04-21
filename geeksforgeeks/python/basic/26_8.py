Write your own len() in Python



The method len() returns the number of elements in the list or length of the
string depending upon the argument you are passing.

 **How to implement without using len():**

    
    
    1. Take input and pass the string/list into
       a function which return its length.
    2. Initialize a count variable to 0, this count 
       variable count character in the string.
    3. Run a loop till length if the string and increment 
       count by 1.
    4. When loop is completed return count.
    

**Python implementation:**

 __

 __  
 __

 __

 __  
 __  
 __

# Function which return length of string

def findLength(string):

 

 # Initialize count to zero

 count = 0

 

 # Counting character in a string

 for i in string:

 count+= 1

 # Returning count

 return count

 

# Driver code

string = "geeksforgeeks"

print(findLength(string))  
  
---  
  
 __

 __

Output:

    
    
    13
    

This article is contributed by **Sahil Rajput**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

  

  

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

