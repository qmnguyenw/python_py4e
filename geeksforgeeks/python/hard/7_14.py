Python | Parse a website with regex and urllib



Let’s discuss the concept of parsing using python. In python we have lot of
modules but for parsing we only need **urllib** and **re** i.e regular
expression. By using both of these libraries we can fetch the data on web
pages.

Note that parsing of websites means that fetch the whole source code and that
we want to search using a given url link, it will give you the output as the
bulk of HTML content that you can’t understand. Let’s see the demonstration
with an explanation to let you understand more about parsing.

 **Code #1:** Libraries needed

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import urllib.request

import urllib.parse

import re  
  
---  
  
 __

 __

 **Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

url= 'https://www.geeksforgeeks.org/'

values = {'s':'python programming',

 'submit':'search'}  
  
---  
  
 __

 __

We have defined a url and some related values that we want to search. Remember
that we define values as a dictionary and in this key value pair we define
**python programming** to **search** on the defined url.

  

  

 **Code #3:**

 __

 __  
 __

 __

 __  
 __  
 __

data= urllib.parse.urlencode(values) 

data = data.encode('utf-8') 

req = urllib.request.Request(url, data) 

resp = urllib.request.urlopen(req) 

 

respData = resp.read()   
  
---  
  
__

__

In the first line we encode the values that we have defined earlier, then
(line 2) we encode the same data that is understand by machine.  
In 3rd line of code we request for values in the defined url, then use the
module urlopen() to open the web document that HTML.  
In the last line read() will help read the document line by line and assign
it to _respData_ named variable.

 **Code #4:**

 __

 __  
 __

 __

 __  
 __  
 __

paragraphs= re.findall(r'<p>(.*?)</p>', str(respData))

 

for eachP in paragraphs:

 print(eachP)  
  
---  
  
 __

 __

In order to extract the relevant data we apply regular expression. Second
argument must be type string and if we want to print the data we apply simple
print function.  
  
Below are few examples:

 **Example #1:**

 __

 __  
 __

 __

 __  
 __  
 __

import urllib.request

import urllib.parse

import re

 

url = 'https://www.geeksforgeeks.org/'

values = {'s':'python programming',

 'submit':'search'}

 

data = urllib.parse.urlencode(values)

data = data.encode('utf-8')

req = urllib.request.Request(url, data)

resp = urllib.request.urlopen(req)

respData = resp.read()

 

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

 

for eachP in paragraphs:

 print(eachP)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/parse1-1.png)  

**Example #2:**

 __

 __  
 __

 __

 __  
 __  
 __

import urllib.request

import urllib.parse

import re

 

url = 'https://www.geeksforgeeks.org/'

values = {'s':'pandas',

 'submit':'search'}

 

data = urllib.parse.urlencode(values)

data = data.encode('utf-8')

req = urllib.request.Request(url, data)

resp = urllib.request.urlopen(req)

respData = resp.read()

 

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

 

for eachP in paragraphs:

 print(eachP)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/parse2-1.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

