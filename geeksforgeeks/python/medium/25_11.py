Run Length Encoding in Python



Given an input string, write a function that returns the Run Length Encoded
string for the input string.

For example, if the input string is ‘wwwwaaadexxxxxx’, then the function
should return ‘w4a3d1e1x6’.

Examples:

    
    
    Input  :  str = 'wwwwaaadexxxxxx'
    Output : 'w4a3d1e1x6'
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Run Length Encoding link. Here
we will solve this problem quickly in python using OrderedDict. Approach is
very simple, first we create a ordered dictionary which contains characters of
input string as key and 0 as their default value, now we run a loop to count
frequency of each character and will map it to it’s corresponding key.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for run length encoding

from collections import OrderedDict

def runLengthEncoding(input):

 

 # Generate ordered dictionary of all lower

 # case alphabets, its output will be 

 # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}

 dict=OrderedDict.fromkeys(input, 0)

 

 # Now iterate through input string to calculate 

 # frequency of each character, its output will be 

 # dict = {'w':4,'a':3,'d':1,'e':1,'x':6}

 for ch in input:

 dict[ch] += 1

 

 # now iterate through dictionary to make 

 # output string from (key,value) pairs

 output = ''

 for key,value in dict.items():

 output = output + key + str(value)

 return output

 

# Driver function

if __name__ == "__main__":

 input="wwwwaaadexxxxxx"

 print (runLengthEncoding(input))  
  
---  
  
 __

 __

Output:

    
    
    'w4a3d1e1x6'
    

**  
Another code:**

 __

 __  
 __

 __

 __  
 __  
 __

def encode(message):

 encoded_message = ""

 i = 0

 

 while (i <= len(message)-1):

 count = 1

 ch = message[i]

 j = i

 while (j < len(message)-1):

 if (message[j] == message[j+1]):

 count = count+1

 j = j+1

 else:

 break

 encoded_message=encoded_message+str(count)+ch

 i = j+1

 return encoded_message

 

#Provide different values for message and test your program

encoded_message=encode("ABBBBCCCCCCCCAB")

print(encoded_message)  
  
---  
  
 __

 __

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

