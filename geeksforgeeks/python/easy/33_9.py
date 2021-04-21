Building a terminal based online dictionary with Python and bash



![vv1](https://media.geeksforgeeks.org/wp-content/cdn-uploads/vv1.png)

I was watching a movie yesterday and I didn’t understand some of the words
used. So what I did was, each time I didn’t understand any word, I’d fire up
my browser and type in ‘define [word]’ and google would turn me up with the
meaning of the word. But it’s annoying to open the browser every time (Blame
me for that ;P).

What do we geeks users love to operate on our linux systems? Yes. The
Terminal!

Since opening a terminal is as easy as Ctrl+Alt+T, I thought it would help if
there was an application to use a dictionary in there. Hence, the motivation
to build this!

So what we need now is, the database of words for the dictionary (duh!).There
is a free and an easily usable online dictionary called **Glosbe**. It offered
a pretty neat ******API**, though in beta stage. It gives the output in a
format called JSON, which is pretty standard for all API’s.

  

  

In order to use this API, it is required to give a query (HTTP GET request)
containing the word to Glosbe and it would return the meaning (+other items
like phrases, etc.) of the word.

For example, to search for the word ‘hello’, we would need to use:

http://glosbe.com/gapi/translate?from=eng&dest;=eng&format;=json&phrase;=hello&pretty;=true

It’s pretty obvious to see that the word is ‘hello’ [phrase=hello]. Glosbe can
offer to translate from one language to other as well. But right now, we need
only an English dictionary. So set the from-dest both to English. And of
course, the output format here is JSON (can be changed to XML as well). Visit
the above link to see the output format in JSON.

Now, the rest of the task is to write a script which would replace the word
‘hello’ (here) with the word the user will want to enter, receive the output,
parse it for the meaning alone and display.

 **Python** enters! We need to write python scripts to parse the returned JSON
object.

 __

 __  
 __

 __

 __  
 __  
 __

import urllib #library for fetching internet resources 

import json #library for json operations 

#import os 

#title=os.environ["word"] 

title = input("Enter word to search: ") #Input word to search
dictionary 

print ("Word: ",title )

 

#stores the json formatted output to a variable 

url =
'http://glosbe.com/gapi/translate?from=eng&dest;=eng&\


format=json&phrase;='+title+'&pretty;=true' 

 

#json representation of url is stored in variable result 

result = json.load(urllib.urlopen(url)) 

 

#get the first text in "meaning" in "tuc" from result 

print ("Meaning: ",
result["tuc"][0]["meanings"][0]["text"])   
  
---  
  
__

__

**Input  
**

    
    
    Geek

 **Output:**

  

  

    
    
    Enter word to search: Word:  geek
    Meaning:  expert in a technical field, particularly to do with computers

Surprised? Just a mere 9 lines of code will accomplish this task! Run this and
see if you have a python compiler installed.

 **How it works?**

  * Here, the variable ‘url’ stores the JSON formatted output from Glosbe.
  * load will take a python object and dump it to a string [stored in the variable ‘result]’ which is a JSON representation of that object.
  * Finally the JSON is parsed for the meaning alone using ‘result[“tuc”][0][“meanings”][0][“text”]’ and printed.

So now it works when this script is executed. In order to do this, I have to
navigate to the directory where it’s stored and then run it. Again, we can
simplify this by writing a shell script which will invoke the python script.
The point is, it will be accessible from anywhere irrespective of the
directory in which the terminal is.

So a bash script is written in order to call the python code.

    
    
    #!/bin/bash
    word="$1"
    export word
    python /home/vishaag/hacks/bash_scripts/terminal_dictionary.py "word"
    

To make a bash file globally accessible, it is required to,

  * Add the directory you wish for Linux to search, which is also where your script is located.
  * Add the directory in the file .bashrc (which is located in the home folder and hidden; press Ctrl+H to see hidden files). For example, I had to add the directory **/home/vishaag/hacks/bash_scripts** at the top of the .bashrc file (using a text editor like gedit/kate etc. ).
  * After this, linux can access your bash script from this folder.

The ‘word=”$1? and export word’ in the script is to take the arguments from
the bash to the python script.

$1 denotes the first argument ($2 the second and so on. Write $@ for n number
of arguments). For example, when you write,

    
    
     **$dict hello**

(dict is the name of the bash script) hello is stored in **$1** (and copied to
‘ **word** ‘ here)

Then this is exported to the python script.

 _Note: Remove both the comments on the above python code and remove/comment
‘title = raw_input(“Enter word to search: “)’ in order to use the arguments
from bash._

    
    
    import os
    title=os.environ["word"]
    #title = input("Enter word to search: ")
    

And its done!!

Now all you have to do is save the shell script and run it like you run any
application on your terminal.

Here’s another sample output

![vv2](https://media.geeksforgeeks.org/wp-content/cdn-uploads/vv2.png)

Cheers!

References:

  * http://www.pythonforbeginners.com/code-snippets/parse-json-objects-in-python
  * http://xmodulo.com/2013/05/how-to-parse-json-string-in-python.html
  * http://linuxcommand.org/lc3_wss0010.php

This article is contributed by **Vishaag Suriya Narayanan** . If you like
GeeksforGeeks and would like to contribute, you can also write an article and
mail your article to contribute@geeksforgeeks.org. See your article appearing
on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

