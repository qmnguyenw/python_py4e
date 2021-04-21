Python String Methods | Set 3 (strip, lstrip, rstrip, min, max, maketrans,
translate, replace & expandtabs())



Some of the string methods are covered in below sets.

String Methods Part- 1  
String Methods Part- 2

More methods are discussed in this article

 **1\. strip()** :- This method is used to **delete all the leading and
trailing** characters mentioned in its argument.

 **2\. lstrip()** :- This method is used to **delete all the leading**
characters mentioned in its argument.

  

  

 **3\. rstrip()** :- This method is used to **delete all the trailing**
characters mentioned in its argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# strip(), lstrip() and rstrip()

str = "---geeksforgeeks---"

 

# using strip() to delete all '-'

print ( " String after stripping all '-' is : ", end="")

print ( str.strip('-') )

 

# using lstrip() to delete all trailing '-'

print ( " String after stripping all leading '-' is : ", end="")

print ( str.lstrip('-') )

 

# using rstrip() to delete all leading '-'

print ( " String after stripping all trailing '-' is : ", end="")

print ( str.rstrip('-') )  
  
---  
  
 __

 __

Output:

    
    
     String after stripping all '-' is : geeksforgeeks
     String after stripping all leading '-' is : geeksforgeeks---
     String after stripping all trailing '-' is : ---geeksforgeeks
    

**4\. min(“string”)** :- This function returns the **minimum value alphabet**
from string.

 **5\. max(“string”)** :- This function returns the **maximum value alphabet**
from string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# min() and max()

str = "geeksforgeeks"

 

# using min() to print the smallest character

# prints 'e'

print ("The minimum value character is : " + min(str))

 

# using max() to print the largest character

# prints 's'

print ("The maximum value character is : " + max(str))  
  
---  
  
 __

 __

Output:

    
    
    The minimum value character is : e
    The maximum value character is : s
    

**6\. maketrans()** :- It is used to **map the contents of string 1 with
string 2** with respective indices to be translated later using translate().

 **7\. translate()** :- This is used to **swap the string elements mapped**
with the help of maketrans().

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# maketrans() and translate()

from string import maketrans # for maketrans()

 

str = "geeksforgeeks"

 

str1 = "gfo"

str2 = "abc"

 

# using maktrans() to map elements of str2 with str1

mapped = maketrans( str1, str2 )

 

# using translate() to translate using the mapping

print "The string after translation using mapped elements is : "

print str.translate(mapped)   
  
---  
  
__

__

Output:

  

  

    
    
    The string after translation using mapped elements is : 
    aeeksbcraeeks
    

In the above code, ‘g’ is replaced by a, ‘f’ is replaced by b and ‘o’ is
replaced by ‘c’ in the string using translate function.  

 **8.replace()** :- This function is used to **replace the substring with a
new substring** in the string. This function has 3 arguments. **The string to
replace, new string which would replace and max value denoting the limit to
replace action ( by default unlimited ).**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# replace()

 

str = "nerdsfornerds is for nerds"

 

str1 = "nerds"

str2 = "geeks"

 

# using replace() to replace str2 with str1 in str

# only changes 2 occurrences 

print ("The string after replacing strings is : ", end="")

print (str.replace( str1, str2, 2))   
  
---  
  
__

__

Output:

    
    
    The string after replacing strings is : geeksforgeeks is for nerds
    

This method is contributed by Chinmoy Lenka  
 **9\. expandtabs()** :- It is used to **replace all tab characters(“\t”) with
whitespace** or simply spaces using the given tab size, which is optional to
supply.  
Syntax: string.tabsize(tabsize)  
Parameters: Specifying the number of characters to be replaced for one tab
character. By default, the function takes tab size as 8.  
Return Value: A string in which all the tab characters are replaced with
spaces.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate expandtabs()

string = 'GEEKS\tFOR\tGEEKS'

 

# No parameters, by default size is 8

print (string.expandtabs())

 

# tab size taken as 2

print(string.expandtabs(2))

 

# tab size taken as 5

print(string.expandtabs(5))  
  
---  
  
 __

 __

Output:

    
    
    GEEKS   FOR     GEEKS
    GEEKS FOR GEEKS
    GEEKS     FOR  GEEKS
    

This article is contributed by **Manjeet Singh** .If you like GeeksforGeeks
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

