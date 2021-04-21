Text transliteration from English to Indian languages – Using indic-
transliteration



 **Transliteration** is the process of transferring a word from the alphabet
of one language to another. Transliteration helps people pronounce words and
names in foreign languages. It is also useful for non-Latin script language
speakers to use in their own language, as typing in Latin is more convenient.

 **Examples :**

    
    
    **Input :** namaskaara
    **Output :**![](https://media.geeksforgeeks.org/wp-content/uploads/20200529092731/Capture507.png)
    Transliterating from English(Latin) to Hindi(Devanagari)
    
    **Input :** namaskaara
    **Output :**![](https://media.geeksforgeeks.org/wp-content/uploads/20200529092911/Capture1138.png)
    Transliterating from English(Latin) to Telugu(Telugu)
    

To implement transliteration of Latin to Indian scripts we will use the
**indic-transliteration** module.

 **Installation :**

    
    
    pip install indic-transliteration

We will use the **transliterate()** method of the **sanscript** class of
the indic-transliteration module.

  

  

## transliterate()

>  **Syntax :** transliterate(text, romanization_style, script)
>
>  **Parameters :**  
>  **test :** The text totransliterated  
>  **romanization_style :** The following romanization styles are available :
>
>   * HK = ‘hk’
>   * IAST = ‘iast’
>   * ITRANS = ‘itrans’
>   * OPTITRANS = ‘optitrans’
>   * KOLKATA = ‘kolkata’
>   * SLP1 = ‘slp1’
>   * VELTHUIS = ‘velthuis’
>   * WX = ‘wx’
>

>
>  **script :** The script to be transliterated into. The following scripts
> are available :
>
>   * Bengali
>   * Devanagari
>   * Gujarati
>   * Kannada
>   * Malayalam
>   * Telugu
>   * Tamil
>   * Oriya
>   * Gurmukhi/ Punjabi/ Panjabi
>

>
>  **Returns :** A string of the transliterated text.

 **Example 1:** Transliterating from Latin to Devanagari.

 __

 __  
 __

 __

 __  
 __  
 __

# import the module

from indic_transliteration import sanscript

from indic_transliteration.sanscript import transliterate

 

# the text to be transliterated

text = "Apa sabhii kaa yahaan svaagat hai."

 

# printing the transliterated text

print(transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200529093132/Capture3104.png)

 **Example 2:** Transliterating from Latin to Gujarati.

 __

 __  
 __

 __

 __  
 __  
 __

# import the module

from indic_transliteration import sanscript

from indic_transliteration.sanscript import transliterate

 

# the text to be transliterated

text = "Suprabhaata"

 

# printing the transliterated text

print(transliterate(text, sanscript.IAST, sanscript.GUJARATI))  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200529093203/Capture2113.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

