Creating a Basic hardcoded ChatBot using Python-NLTK



Creating a basic chatbot using Python in Jupyter Notebook. This chatbot
interacts with the user using the hardcoded inputs and outputs which are fed
into the Python code.

 **Requirements:**  
You need to install the NLTK (Natural Language Toolkit), it provides libraries
and programs for symbolic and statistical natural language processing for
English written in the Python programming language. To install this module
type the below command in the terminal.

    
    
    pip install nltk

Below is the implementation

 __

 __  
 __

 __

 __  
 __  
 __

from nltk.chat.util import Chat, reflections

 

pairs =[

 ['my name is (.*)', ['Hello ! % 1']],

 ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !',
'Hey !']],

 ['(.*) your name ?', ['My name is Geeky']],

 ['(.*) do you do ?', ['We provide a platform for tech enthusiasts, a
wide range of options !']],

 ['(.*) created you ?', ['Geeksforgeeks created me using python and
NLTK']]

]

 

chat = Chat(pairs, reflections)

chat.converse()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200520023255/Screenshot-2020-05-20-at-02.32.31.png)

 **Explanation of the above code:**  
In the first line of code we have imported the Chat class and Reflections
dictionary from the Natural Language Toolkit’s chatbot utilities. Chat class
which will process the conversation between the user and your chatbot.
Reflections is a dictionary that when a value in a regular expression group
matches a key in the dictionary it will output the value in the response. So
for the first item of list pairs if we input my name is geeky where geeky
corresponds to the regex “(.*)” it will output “Hello ! Geeky”, that is it
replaces the regex in response to “%1” that was referred to as “(.*)” with
“Geeky”. Now we initialize the chatbot using pairs and reflections dictionary.
Then after initialization we call the converse method of Chat class that
automates the chatbot.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

