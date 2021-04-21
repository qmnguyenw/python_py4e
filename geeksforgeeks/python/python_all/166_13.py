Python program to convert seconds into hours, minutes and seconds



Given an integer _n_ (in seconds), convert it into hours, minutes and seconds.

 **Examples:**

    
    
    **Input :** 12345
    **Output :** 3:25:45
    
    **Input :** 3600
    **Output :** 1:00:00
    

**Approach #1 :** Naive

This approach is simply a naive approach to get the hours, minutes and seconds
by simple mathematical calculations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to Convert seconds

# into hours, minutes and seconds

 

def convert(seconds):

 seconds = seconds % (24 * 3600)

 hour = seconds // 3600

 seconds %= 3600

 minutes = seconds // 60

 seconds %= 60

 

 return "%d:%02d:%02d" % (hour, minutes, seconds)

 

# Driver program

n = 12345

print(convert(n))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3:25:45
    

