Python | Count overlapping substring in a given string



Given a string and a sub-string, the task is to get the count of overlapping
substring from the given string.

Note that in Python, the count() function returns the number of substrings
in a given string, but it does not give correct results when two occurrences
of the substring overlap. Consider this example –

 __

 __  
 __

 __

 __  
 __  
 __

string= "GeeksforGeeksforGeeksforGeeks"

 

print(string.count("GeeksforGeeks"))  
  
---  
  
 __

 __

 **Output:**

    
    
    2

The output we got here is 2, but the expected output is 3 since we also wanted
to count the occurrence of overlapped sub-string.

In order to solve this problem, we can use find() function in Python. It
returns the start position of the first occurrence of substring in the given
string, then we increment this position by 1 and continue the search from that
position till the end of the string.

  

  

Below is the implementation –

 __

 __  
 __

 __

 __  
 __  
 __

def CountOccurrences(string, substring):

 

 # Initialize count and start to 0

 count = 0

 start = 0

 

 # Search through the string till

 # we reach the end of it

 while start < len(string):

 

 # Check if a substring is present from

 # 'start' position till the end

 pos = string.find(substring, start)

 

 if pos != -1:

 # If a substring is present, move 'start' to

 # the next position from start of the substring

 start = pos + 1

 

 # Increment the count

 count += 1

 else:

 # If no further substring is present

 break

 # return the value of count

 return count

 

# Driver Code

string = "GeeksforGeeksforGeeksforGeeks"

print(CountOccurrences(string, "GeeksforGeeks"))  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

