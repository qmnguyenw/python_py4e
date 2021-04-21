Python | Sort JSON by value



Let’s see the different ways to sort the JSON data using Python.

 **What is JSON ?**  
JSON (JavaScript Object Notation) is a lightweight, text-based, language-
independent data exchange format that is easy for humans and machines to read
and write. JSON can represent two structured types: objects and arrays. An
object is an unordered collection of zero or more name/value pairs. An array
is an ordered sequence of zero or more values. The values can be strings,
numbers, booleans, null, and these two structured types.

The task is to sort the JSON first by _code_ , then by _grade_ and then by
_enrollment_no_.

 **Code #1:** Sorting in Desc order

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate sorting in JSON.

import json

 

data='''{ 

 "Student":[ 

 { 

 "enrollment_no":"9915103000",

 "name":"JIIT",

 "subject":[ 

 { 

 "code":"DBMS",

 "grade":"C"

 }

 ]

 },

 { 

 "enrollment_no":"8815103057",

 "name":"JSS",

 "subject":[ 

 { 

 "code":"COA",

 "grade":"A"

 },

 { 

 "code":"CN",

 "grade":"A+"

 }

 ]

 }

 ]

}'''

 

# Parsing Json object

json_parse = json.loads(data)

 

# iterating 

for it in json_parse['Student']:

 for y in it['subject']:


print(y['code'],y['grade'],it['enrollment_no'],it['name'])  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    DBMS C 9915103000 JIIT
    COA A 8815103057 JSS
    CN A+ 8815103057 JSS

  
**Code #2 :** By using External library such as Pandas (Sorting in Ascending
order).

 __

 __  
 __

 __

 __  
 __  
 __

from pandas.io.json import json_normalize

 

df = json_normalize(json_parse['Student'],

 'subject', 

 ['enrollment_no', 'name'])

 

df.sort_values(['code', 'grade',
'enrollment_no']).reset_index(drop=True)  
  
---  
  
 __

 __

 **Output:**

    
    
      code grade  enrollment_no      name
    0  CN     A+  8815103057         JSS
    1  COA    A  8815103057         JSS
    2  DBMS   C  9915103000        JIIT

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

