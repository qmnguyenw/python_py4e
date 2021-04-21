Reading and Writing XML Files in Python



 **Extensible Markup Language** , commonly known as XML is a language designed
specifically to be easy to interpret by both humans and computers altogether.
The language defines a set of rules used to encode a document in a specific
format. In this article, methods have been described to read and write XML
files in python.

 **Note:** In general, the process of reading the data from an XML file and
analyzing its logical components is known as **Parsing**. Therefore, when we
refer to reading a xml file we are referring to **parsing the XML
document**.

In this article, we would take a look at two libraries that could be used for
the purpose of xml parsing. They are:

  * BeautifulSoup used alongside the lxml xml parser
  * Elementtree library.

## Using BeautifulSoup alongside with lxml parser

For the purpose of reading and writing the xml file we would be using a
Python library named BeautifulSoup. In order to install the library, type
the following command into the terminal.

    
    
    pip install beautifulsoup4
    

Beautiful Soup supports the HTML parser included in Python’s standard library,
but it also supports a number of third-party Python parsers. One is the lxml
parser (used for parsing XML/HTML documents). lxml could be installed by
running the following command in the command processor of your Operating
system:

  

  

    
    
    pip install lxml
    

Firstly we will learn how to read from an XML file. We would also parse data
stored in it. Later we would learn how to create an XML file and write data to
it.

### Reading Data From an XML File

Their are two steps required to parse a xml file:-

  * Finding Tags
  * Extracting from tags

 **Example:**

 **XML File used:**

![reading-and-writing-xml-python-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200428153952/reading-and-writing-xml-python-1.png)

 __

 __  
 __

 __

 __  
 __  
 __

from bs4 import BeautifulSoup

 

 

# Reading the data inside the xml

# file to a variable under the name 

# data

with open('dict.xml', 'r') as f:

 data = f.read()

 

# Passing the stored data inside

# the beautifulsoup parser, storing

# the returned object 

Bs_data = BeautifulSoup(data, "xml")

 

# Finding all instances of tag 

# unique

b_unique = Bs_data.find_all('unique')

 

print(b_unique)

 

# Using find() to extract attributes 

# of the first instance of the tag

b_name = Bs_data.find('child', {'name':'Frank'})

 

print(b_name)

 

# Extracting the data stored in a

# specific attribute of the 

# child tag

value = b_name.get('test')

 

print(value)  
  
---  
  
 __

 __

 **OUTPUT:**

![reading-xml-python-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200428154135/reading-xml-python-1.png)

### Writing an XML File

Writing a xml file is a primitive process, reason for that being the fact
that xml files aren’t encoded in a special way. Modifying sections of a
xml document requires one to parse through it at first. In the below code we
would modify some sections of the aforementioned xml document.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

from bs4 import BeautifulSoup

 

# Reading data from the xml file

with open('dict.xml', 'r') as f:

 data = f.read()

 

# Passing the data of the xml

# file to the xml parser of

# beautifulsoup

bs_data = BeautifulSoup(data, 'xml')

 

# A loop for replacing the value

# of attribute test to WHAT !!

# The tag is found by the clause

# bs_data.find_all('child', {'name':'Frank'})

for tag in bs_data.find_all('child', {'name':'Frank'}):

 tag['test'] = "WHAT !!"

 

 

# Output the contents of the 

# modified xml file

print(bs_data.prettify())  
  
---  
  
 __

 __

 **Output:**

![Writing-XML-python-1](https://media.geeksforgeeks.org/wp-
content/uploads/20200428154429/Writing-XML-python-1.png)

## Using Elementree

 **Elementree module** provides us with a plethora of tools for manipulating
XML files. The best part about it being its inclusion in the standard Python’s
built-in library. Therefore, one does not have to install any external modules
for the purpose. Due to the xmlformat being an inherently hierarchical data
format, it is a lot easier to represent it by a tree. The module provides
ElementTree provides methods to represent whole XML document as a single
tree.

In the later examples, we would take a look at discrete methods to read and
write data to and from XML files.

### Reading XML Files

To read an XML file using ElementTree, firstly, we import the ElementTree
class found inside xml library, under the name ET (common convension).
Then passed the filename of the xml file to the ElementTree.parse()
method, to enable parsing of our xml file. Then got the root (parent tag) of
our xml file using getroot(). Then displayed (printed) the root tag of our
xml file (non-explicit way). Then displayed the attributes of the sub-tag of
our parent tag using root[0].attrib. root[0] for the first tag of parent
root and attrib for getting it’s attributes. Then we displayed the text
enclosed within the 1st sub-tag of the 5th sub-tag of the tag root.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing element tree

# under the alias of ET

import xml.etree.ElementTree as ET

 

# Passing the path of the

# xml document to enable the

# parsing process

tree = ET.parse('dict.xml')

 

# getting the parent tag of

# the xml document

root = tree.getroot()

 

# printing the root (parent) tag

# of the xml document, along with

# its memory location

print(root)

 

# printing the attributes of the

# first tag from the parent 

print(root[0].attrib)

 

# printing the text contained within

# first subtag of the 5th tag from

# the parent

print(root[5][0].text)  
  
---  
  
 __

 __

 **Output:**

![Reading-XML-Python-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200428154838/Reading-XML-Python-2.png)

### Writing XML Files

Now, we would take a look at some methods which could be used to write data on
an xml document. In this example we would create a xml file from scratch.

To do the same, firstly, we create a root (parent) tag under the name of
_chess_ usnig the command ET.Element('chess'). All the tags would fall
underneath this tag, i.e. once a root tag has been defined, other sub-elements
could be created underneath it. Then we created a subtag/subelement named
_Opening_ inside the _chess_ tag using the command ET.SubElement(). Then we
created two more subtags which are underneath the tag _Opening_ named _E4_ and
_D4_. Then we added attributes to the _E4_ and _D4_ tags using set() which
is a method found inside SubElement(), which is used to define attributes to
a tag. Then we added text between the _E4_ and _D4_ tags using the attribute
text found inside the SubElement function. In the end we converted the
datatype of the contents we were creating from
'xml.etree.ElementTree.Element' to bytes object, using the command
ET.tostring() (even though the function name is tostring() in certain
implementations it converts the datatype to bytes rather then str).
Finally, we flushed the data to a file named gameofsquares.xml which is a
opened in wb mode to allow writing binary data to it. In the end, we saved
the data to our file.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import xml.etree.ElementTree as ET

 

# This is the parent (root) tag 

# onto which other tags would be

# created

data = ET.Element('chess')

 

# Adding a subtag named Opening

# inside our root tag

element1 = ET.SubElement(data, 'Opening')

 

# Adding subtags under the Opening

# subtag 

s_elem1 = ET.SubElement(element1, 'E4')

s_elem2 = ET.SubElement(element1, 'D4')

 

# Adding attributes to the tags under

# items

s_elem1.set('type', 'Accepted')

s_elem2.set('type', 'Declined')

 

# Adding text between the E4 and D5 

# subtag

s_elem1.text = "King's Gambit Accepted"

s_elem2.text = "Queen's Gambit Declined"

 

# Converting the xml data to byte object,

# for allowing flushing data to file 

# stream

b_xml = ET.tostring(data)

 

# Opening a file under the name items2.xml,

# with operation mode wb (write + binary)

with open("GFG.xml", "wb") as f:

 f.write(b_xml)  
  
---  
  
 __

 __

 **Output:**

![wrirint-xml-python-2](https://media.geeksforgeeks.org/wp-
content/uploads/20200428155239/wrirint-xml-python-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

