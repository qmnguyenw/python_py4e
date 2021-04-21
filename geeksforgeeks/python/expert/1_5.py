Python Selenium – Find element by text



The technique to verify if the requirements given by the user meet with the
actual software product developed is known as **Software Testing**. Moreover,
it also checks if the final software product developed is error-free or not.
Software testing can either be performed manually or with the help of software
testing tools. The testing which is done automatically through the inbuilt
tools is known as **Automation Testing.** An incredible library in Python,
Selenium helps you in automated testing of the software. While doing
automation testing, are you not able to find an element by text in the
required web page? Then, you are at an appropriate place. In this article, we
will be discussing the appropriate steps along with an example to do the same.

>  **Syntax:** driver.find_element_by_xpath(“//tag [contains( text(),
> ‘word’)]”)
>
>  **Parameters:**
>
>   *  **tag:** Here, tag stands for the tag name which contains the
> particular word.
>   *  **word:** Here, word stands for the text which has to be found in a
> particular string. We don’t need to write a complete sentence which we want
> to find, but we can write a few words which are unique in the web page.
>

 **Example:** For instance, consider this simple page source:

## HTML

  

  

 __

 __  
 __

 __

 __  
 __  
 __

<!DOCTYPE html>

<html> 

<body> 

<button type= “button” >Geeks For Geeks</button> 

</body> 

<html>  
  
---  
  
 __

 __

