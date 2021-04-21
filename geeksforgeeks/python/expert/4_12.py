Output of Python Program – Dictionary (set 25)



Prerequisite: Dictionaries in Python  
These question sets will make you conversant with Dictionary Concepts in
Python programming language.

 **Question 1** : Which of the following is true about Python dictionaries?

A. Items are accessed by their position in a dictionary.

B. All the keys in a dictionary must be of the same type.

  

  

C. Dictionaries are mutable.

D. A dictionary can contain any object type except another dictionary.

 **Answer:** B

 **Explanation:** It means that you can change their content without changing
their identity.

* * *

 **Question 2:** Suppose we have a dictionary defined as :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

Python= {'Geeks': 100, 'For': 200, 'Geeks': 300}

Python ['For':'Geeks']  
  
---  
  
 __

 __

What is the result of this statement:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

Python ['For':'Geeks']  
  
---  
  
 __

 __

A. [200, 300]

  

  

B. (200, 300)

C. It raises an exception.

D. 200 300

 **Answer:** C

 **Explanation:** Dictionaries are accessed by key, not by the position of the
items. It doesn’t make sense to slice a dictionary.

* * *

 **Question 3:** Which of the following could **not** be a valid dictionary
key:

A. len

B. (5+7j)

C. (‘Geeks’,’For’)

D. [‘Geeks’,’For’]

 **Answer:** D

 **Explanation:** A list is a mutable data structure so it cannot be used as a
key as it raises the risk of modification and thus, aren’t hashable.

* * *

 **Question 4.** Suppose you have the following dictionary defined as-

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

Python= {'Geeks': 100, 'For': 200, 'Geeks': 300}  
  
---  
  
 __

 __

What method call will delete the entry whose value is 100?

A. push()

B. pop()

C. append()

D. extend()

 **Answer:** B

 **Explanation:** The pop() is an inbuilt function in Python that removes the
item from the dictionary provided the key as a parameter.

* * *

 **Question 5.** Suppose you have a dictionary d1. Which of the following
effectively creates a variable d2 which contains a copy of d1?

A. d2 = dict(d1.keys())

B. d2 = dict(d1.values())

C. d2 = d1

D. d2 = dict(d1.items())

 **Answer:** D

 **Explanation:** The d1 dictionary can be passed directly as an argument to
dict() to create a new dictionary.

* * *

 **Question 6.** What will be the output of the following code snippet?

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

y={16:"Geeks",25:"For",32:"Geeks"}

 

for i,j in y.items():

 print(i,j,end=" ")  
  
---  
  
 __

 __

A. Geeks For Geeks

B. 16 Geeks 25 For 32 Geeks

C. 16 25 32

D. 16 :”Geeks” 25:”For” 32:”Geeks”

 **Answer:** B

 **Explanation:** Python’s print() function comes with a parameter called
‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line
character. You can end a print statement with any character/string using this
parameter.

* * *

 **Question 7.** What is the correct command to shuffle the following list?

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

d= {"Albert":70, "Suzan":85}

d["Albert"]  
  
---  
  
 __

 __

A. 85

B. “Albert”

C. 70

D. “Suzan”

 **Answer:** C

 **Explanation:** A key can be used to access the value in a dictionary.

* * *

 **Question 8.** Which statement defined below can create a dictionary?

A. d = {“Computer”:100, “Programming”:95}

B. d = {100:” Computer”, 95:”Programming”}

C. d = { }

D. All the above.

 **Answer:** D

 **Explanation:** Since there are multiple methods to define dictionary ,all
of which are defined above.

* * *

 **Question 9.** Which of the following statements can be used for declaration
of the dictionary?

A. {23: ‘Geeks’, 26: ‘ForGeeks’}

B. dict([[23,”Geeks”],[26,”ForGeeks”]])

C. {23,”Geeks”,26”ForGeeks”}

D. All the above

 **Answer:** A

 **Explanation:** Because a dictionary has a key and a value which should be
defined as {key: value}

* * *

 **Question10.** Let us assume d = {“Nobita”:70, “Doremon”:65} . Which command
you will use to delete the entry for “Nobita”:

A. d.delete(“Nobita”:70)

B. d.delete(“Nobita”)

C. del d[“Nobita”]

D. del d(“Nobita”:70)

 **Answer:** C

 **Explanation:** The del keyword is used to delete objects. In Python
everything is an object, so the del keyword can also be used to delete
variables, lists, or parts of a list etc.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

