Python program to count upper and lower case characters without using inbuilt
functions



Given a string that contains both upper and lower case characters in it. The
task is to count number of upper and lower case characters in it without using
in-built functions.

Counting the upper and lower case characters of a string can be easily done
using isupper() and islower() functions, refer this. But doing the same
without help of any inbuilt function is quite exciting. Let’s see how this can
be done :

Examples :

    
    
    Input : Introduction to Python
    Output : Lower Case characters : 18 Upper case characters : 2
    
    Input :  Welcome to GeeksforGeeks
    Output : Lower Case characters : 19  Upper case characters: 3
    

  
Below is the implementation of above idea :

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to count upper and

# lower case characters without using

# inbuilt functions

def upperlower(string):

 

 upper = 0

 lower = 0

 

 for i in range(len(string)):

 

 # For lower letters

 if (ord(string[i]) >= 97 and

 ord(string[i]) <= 122):

 lower += 1

 

 # For upper letters

 elif (ord(string[i]) >= 65 and

 ord(string[i]) <= 90):

 upper += 1

 

 print('Lower case characters = %s' %lower,

 'Upper case characters = %s' %upper)

 

# Driver Code

string = 'GeeksforGeeks is a portal for Geeks'

upperlower(string)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Lower case characters = 27 Upper case characters = 3
    

