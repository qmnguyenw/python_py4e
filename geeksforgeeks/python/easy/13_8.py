Python NLTK | nltk.tokenize.StanfordTokenizer()



With the help of **nltk.tokenize.StanfordTokenizer()** method, we are able
to extract the tokens from string of characters or numbers by using
tokenize.StanfordTokenizer() method. It follows **stanford** standard for
generating tokens.

>  **Syntax :** tokenize.StanfordTokenizer()  
>  **Return :** **Return the tokens from a string of characters or numbers.**

 **Example #1 :**  
In this example we can see that by using tokenize.SExprTokenizer() method,
we are able to extract the tokens from stream of characters or numbers using
stanford standard.

 __

 __  
 __

 __

 __  
 __  
 __

# import StanfordTokenizer() method from nltk

from nltk.tokenize.stanford import StanfordTokenizer

 

# Create a reference variable for Class StanfordTokenizer

tk = StanfordTokenizer()

 

# Create a string input

gfg = "Geeks f o r Geeks"

 

# Use tokenize method

geek = tk.tokenize(gfg)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

> [‘Geeks’, ‘f’, ‘o’, ‘r’, ‘Geeks’]
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

# import StanfordTokenizer() method from nltk

from nltk.tokenize.stanford import StanfordTokenizer

 

# Create a reference variable for Class StanfordTokenizer

tk = StanfordTokenizer()

 

# Create a string input

gfg = "This is your great author."

 

# Use tokenize method

geek = tk.tokenize(gfg)

 

print(geek)  
  
---  
  
 __

 __

 **Output :**

> [‘This’, ‘is’, ‘your’, ‘great’, ‘author’, ‘.’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

