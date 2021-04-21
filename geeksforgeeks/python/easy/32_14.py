Get() method for dictionaries in Python



In python dictionaries, following is a conventional method to access a value
for a key.

 __

 __  
 __

 __

 __  
 __  
 __

dic= {"A":1, "B":2}

print(dic["A"])

print(dic["C"])  
  
---  
  
 __

 __

The problem that arises here is that the 3rd line of the code returns a key
error :

    
    
    Traceback (most recent call last):
      File ".\dic.py", line 3, in 
        print (dic["C"])
    KeyError: 'C'
    

The **get()** method is used to avoid such situations. This method returns the
value for the given key, if present in the dictionary. If not, then it will
return None (if get() is used with only one argument).

 **Syntax :**

Dict.get(key, default=None)

  

  

 **Example:  
**

 __

 __  
 __

 __

 __  
 __  
 __

dic= {"A":1, "B":2}

print(dic.get("A"))

print(dic.get("C"))

print(dic.get("C","Not Found ! "))  
  
---  
  
 __

 __

Output:

    
    
    1
    None
    Not Found !
    

This article is contributed by **Mayank Rawat** .If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

