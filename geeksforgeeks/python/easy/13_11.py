Python NLTK | nltk.TweetTokenizer()



With the help of **NLTK nltk.TweetTokenizer()** method, we are able to
convert the stream of words into small small tokens so that we can analyse the
audio stream with the help of nltk.TweetTokenizer() method.

>  **Syntax :** nltk.TweetTokenizer()  
>  **Return :** **Return the stream of token**

 **Example #1 :**  
In this example when we pass audio stream in the form of string it will
converted to small tokens from a long string with the help of
nltk.TweetTokenizer() method.

 __

 __  
 __

 __

 __  
 __  
 __

# import TweetTokenizer() method from nltk

from nltk.tokenize import TweetTokenizer

 

# Create a reference variable for Class TweetTokenizer

tk = TweetTokenizer()

 

# Create a string input

gfg = "Geeks for Geeks"

 

# Use tokenize method

geek = tk.tokenize(gfg)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

> [‘Geeks’, ‘for’, ‘Geeks’]
>
>  
>
>
>  
>

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import TweetTokenizer() method from nltk

from nltk.tokenize import TweetTokenizer

 

# Create a reference variable for Class TweetTokenizer

tk = TweetTokenizer()

 

# Create a string input

gfg = ":-) <> () {} [] :-p"

 

# Use tokenize method

geek = tk.tokenize(gfg)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

> [‘:-)’, ”, ‘(‘, ‘)’, ‘{‘, ‘}’, ‘[‘, ‘]’, ‘:-p’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

