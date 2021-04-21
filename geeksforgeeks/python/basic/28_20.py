How to input multiple values from user in one line in Python?



For instance, in C we can do something like this:

 __

 __  
 __

 __

 __  
 __  
 __

// Reads two values in one line

scanf("%d %d", &x;, &y;)   
  
---  
  
__

__

One solution is to use raw_input() two times.

 __

 __  
 __

 __

 __  
 __  
 __

x, y= input(), input()  
  
---  
  
 __

 __

Another solution is to usesplit()

 __

 __  
 __

 __

 __  
 __  
 __

x, y= input().split()  
  
---  
  
 __

 __

Note that we don’t have to explicitly specify split(‘ ‘) because split() uses
any whitespace characters as a delimiter as default.

One thing to note in the above Python code is, both x and y would be of
string. We can convert them to int using another line

  

  

    
    
    x, y = [int(x), int(y)]
    
    # We can also use  list comprehension
    x, y = [int(x) for x in [x, y]]
    

Below is complete one line code to read two integer variables from standard
input using split and list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Reads two numbers from input and typecasts them to int using

# list comprehension

x, y = [int(x) for x in input().split()]   
  
---  
  
__

__

__

__  
__

__

__  
__  
__

# Reads two numbers from input and typecasts them to int using

# map function

x, y = map(int, input().split())  
  
---  
  
 __

 __

This article is contributed by **Abhishek Shukla**. Please write comments if
you find anything incorrect, or you want to share more information about the
topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

