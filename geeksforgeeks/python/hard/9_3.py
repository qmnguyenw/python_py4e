Prime or not in Python



Every programmer comes across the problem of checking whether a number is
prime and indeed it’s one of the basic level program in any language. I also
tried it in many different languages, but the best language that I found to
implement it is Python. It’s just one single line and the program does it all.
Its so simple and smooth than other languages.

The concept of Any and All has really reduced this problem to a single line
and yes it is fast too.  
The logic used in this program is based on school method to check prime.

 __

 __  
 __

 __

 __  
 __  
 __

# Returns true if n is prime else false

def prime(n):

 return all([(n % j) for j in range(2,
int(n**0.5)+1)]) and n>1

 

# Driver code

n = 41

if prime(n):

 print("Yes")

else:

 print("No")  
  
---  
  
 __

 __

    
    
    Yes

This article is contributed by **Chinmoy Lenka**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
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

