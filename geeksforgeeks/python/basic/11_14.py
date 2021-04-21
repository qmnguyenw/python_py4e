Python | Number to Words using num2words



num2words module in Python, which converts number (like 34) to words (like
thirty-four). Also, this library has support for multiple languages. In this
article, we will see how to convert number to words using num2words module.

 **Installation**  
One can easily install num2words using pip.

    
    
    pip install num2words
    

Consider the following two excerpts from different files taken from 20
Newsgroups, a popular NLP database. Pre-processing 20 Newsgroups effectively
has remained to be a matter of interest.

> In article, Martin Preston writes: Why not use the PD C library for
> reading/writing TIFF files? It took me a good **20** minutes to start using
> them in your own app.  
> ISCIS VIII is the eighth of a series of meetings which have brought together
> computer scientists and engineers from about **twenty** countries. This
> year’s conference will be held in the beautiful Mediterranean resort city of
> Antalya, in a region rich in natural as well as historical sites.

In the above two excerpts, one can observe that the number ’20’ appears in
both numeric and alphabetical forms. Simply following the pre-processing
steps, that involve tokenization, lemmatization and so on would not be able to
map ’20’ and ‘twenty’ to the same stem, which is of contextual importance.
Luckily, we have the in-built library, num2words which solves this problem
in a single line.

  

  

Below is the sample usage of the tool.

 __

 __  
 __

 __

 __  
 __  
 __

from num2words import num2words

 

# Most common usage.

print(num2words(36))

 

# Other variants, according to the type of article.

print(num2words(36, to = 'ordinal'))

print(num2words(36, to = 'ordinal_num'))

print(num2words(36, to = 'year'))

print(num2words(36, to = 'currency'))

 

# Language Support.

print(num2words(36, lang ='es'))  
  
---  
  
 __

 __

 **Output:**

    
    
    thirty-six
    thirty-sixth
    36th
    zero euro, thirty-six cents
    treinta y seis
    

Therefore, in the pre-processing step, one could convert ALL numeric values to
words for better accuracy in the further stages.

 **References:** https://pypi.org/project/num2words/  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

