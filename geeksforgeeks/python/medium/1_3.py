How to build a Random Story Generator using Python?



In this section, we are going to make a very interesting beginner-level
project of Python. It is a random story generator. The random story generator
project aims to generate random stories every time user executes the code. A
story is made up of a collection of sentences. We will choose random phrases
to build sentences, and hence stories.

Now, the pertinent question is – How we will do so? Its answer is very simple
:

  * We will first put the elements of the story in different lists.
  * Then we will use the random module to select random parts of the story collected in different lists.
  * And then concatenate them to make a story.

We will make use of random.choice() function. Before starting, let’s see an
example of how random.choice() works.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import random

 

# list of books is stored in the list -'books'

books = ['Mother', 'Midnight Children', 'My experiments with
truth']

 

# An item from the list 'books' is selected

# by random.choice()

print(random.choice(books))  
  
---  
  
 __

 __

 **Output**

    
    
    Midnight Children

As we can see, random.choice() function basically selects an item from a list
of items.

  

  

Following are the steps involved in this Random story generator project.

 **1.** Import the random module, as it is a built-in module of python. So,
there’s no need to install it manually.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing random module

import random  
  
---  
  
 __

 __

 **2.** Define several lists of phrases. Here, we have defined eight lists. We
can define more also, it depends totally on our choice.

  * Sentence_starter – This list gives an idea about the time of the event.
  * character – This list tells about the main character of this story.
  * time – This list defines the exact day on which some incident has occurred.
  * story_plot – This list defines the plot of the story.
  * place – This list defines the place at which the incident occurred.
  * second_character – This list defines the second character of the story.
  * age – This list defines the age of the second character.
  * work – This list tells about the work the second character was doing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Defining list of phrases which will help to build a story

Sentence_starter = ['About 100 years ago', ' In the 20 BC',
'Once upon a time']

 

character = [' there lived a king.',' there was a man named
Jack.',

 ' there lived a farmer.']

 

time = [' One day', ' One full-moon night']

 

story_plot = [' he was passing by', ' he was going for a picnic to
']

 

place = [' the mountains', ' the garden']

 

second_character = [' he saw a man', ' he saw a young lady']

 

age = [' who seemed to be in late 20s', ' who seemed very old and
feeble']

 

work = [' searching something.', ' digging a well on roadside.']  
  
---  
  
 __

 __

3\. With the help of random.choice() select an item from each list and
concatenate the selected items to generate sentences for the story.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Selecting an item from each list and concatenating them.

print(random.choice(Sentence_starter)+random.choice(character)+

 random.choice(time)+random.choice(story_plot)+

 random.choice(place)+random.choice(second_character)+

 random.choice(age)+random.choice(work))  
  
---  
  
 __

 __

 **Implementation:**

Let’s try the full implementation with the help of an example.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing random module

import random

 

# Defining list of phrases which will help to build a story

 

Sentence_starter = ['About 100 years ago', ' In the 20 BC',
'Once upon a time']

character = [' there lived a king.',' there was a man named
Jack.',

 ' there lived a farmer.']

time = [' One day', ' One full-moon night']

story_plot = [' he was passing by',' he was going for a picnic to
']

place = [' the mountains', ' the garden']

second_character = [' he saw a man', ' he saw a young lady']

age = [' who seemed to be in late 20s', ' who seemed very old and
feeble']

work = [' searching something.', ' digging a well on roadside.']

 

# Selecting an item from each list and concatenating them.

print(random.choice(Sentence_starter)+random.choice(character)+

 random.choice(time)+random.choice(story_plot) +

 random.choice(place)+random.choice(second_character)+

 random.choice(age)+random.choice(work))  
  
---  
  
 __

 __

 **Output:**

> In the 20 BC there lived a king. One day he was going for a picnic to the
> mountains he saw a man who seemed to be in late 20s digging a well on
> roadside.

In this way, we can compile and run this code as many times as we want. And
different short stories will be generated.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

