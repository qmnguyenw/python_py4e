Wikipedia module in Python



The Internet is the single largest source of information, and therefore it is
important to know how to fetch data from various sources. And with Wikipedia
being one of the largest and most popular sources for information on the
Internet.

 **Wikipedia** is a multilingual online encyclopedia created and maintained as
an open collaboration project by a community of volunteer editors using a
wiki-based editing system.

In this article, we will see how to use Python’s Wikipedia module to fetch a
variety of information from the Wikipedia website.

## Installation

In order to extract data from Wikipedia, we must first install the Python
Wikipedia library, which wraps the official Wikipedia API. This can be done by
entering the command below in your command prompt or terminal:

    
    
    pip install wikipedia

## Getting Started

#### Getting the summary of any title

Summary of any tittle can be obtained by using summary method.

  

  

>  **Syntax :** wikipedia.summary(title, sentences)
>
>  **Argument :**  
>  Title of the topic  
> Optional argument: setting number of lines in result.
>
>  **Return :** Returns the summary in string format.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import wikipedia 

 

# finding result for the search

# sentences = 2 refers to numbers of line

result = wikipedia.summary("India", sentences = 2) 

 

# printing the result

print(result)   
  
---  
  
__

__

**Output :**

> India (Hindi: Bh?rat), officially the Republic of India (Hindi: Bh?rat
> Ga?ar?jya), is a country in South Asia. It is the seventh-largest country by
> area, the second-most populous country, and the most populous democracy in
> the world.

#### Searching title and suggestions

Title and suggestions can be get by using search() method.

>  **Syntax :** wikipedia.search(title, results)
>
>  
>
>
>  
>
>
>  **Argument :**  
>  Title of the topic  
> Optional argument : setting number of result.
>
>  **Return :** Returns the list of titles.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import wikipedia

 

# getting suggestions

result = wikipedia.search("Geek", results = 5)

 

# printing the result

print(result)  
  
---  
  
 __

 __

 **Output :**

    
    
    ['Geek', 'Geek!', 'Freaks and Geeks', 'The Geek', 'Geek show']
    

#### Getting Full Wikipedia Page Data

The page() method is used to get the contents, categories, coordinates,
images, links and other metadata of a Wikipedia page.

>  **Syntax :** wikipedia.page(title)
>
>  **Argument :** Title of the topic.
>
>  **Return :** Return a WikipediaPage object.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import wikipedia

 

# wikipedia page object is created

page_object = wikipedia.page("india")

 

# printing html of page_object

print(page_object.html)

 

# printing title

print(page_object.original_title)

 

# printing links on that page object

print(page_object.links[0:10])  
  
---  
  
 __

 __

 **Output :**

> “bound method WikipediaPage.html of “WikipediaPage ‘India'”>  
> India  
> [‘.in’, ’10th BRICS summit’, ’11th BRICS summit’, ’12th BRICS summit’, ’17th
> SAARC summit’, ’18th SAARC summit’, ‘1951 Asian Games’, ‘1957 Indian general
> election’, ‘1962 Indian general election’, ‘1982 Asian Games’]

#### Changing language of Wikipedia page

The language can be changed to your native language if the page exists in your
native language. Set_lang() method is used for the same.

>  **Syntax :** wikipedia.set_lang(language)
>
>  **Argument :** prefix of the language like for arabic prefix is ar and so
> on.
>
>  **Action performed :** It converted the data into that language default
> language is english.

 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import wikipedia

 

# setting language to hindi

wikipedia.set_lang("hi")

 

# printing the summary

print(wikipedia.summary("India"))  
  
---  
  
 __

 __

 **Output :**

![python-wikipedia](https://media.geeksforgeeks.org/wp-
content/uploads/20200305192006/python-wikipedia.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

