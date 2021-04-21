Reloading modules in Python



 **reload()** reloads a previously imported module. This is useful if you have
edited the module source file using an external editor and want to try out the
new version without leaving the Python interpreter. The return value is the
module object.

 **Note** : The argument should be a module which has been successfully
imported.

 **Usage** :

For Python2.x

    
    
    reload( _module_ )
    

For above 2.x and <=Python3.3

  

  

    
    
    import imp
    imp.reload( _module_ )
    

For >=Python3.4

    
    
    import importlib
    importlib.reload( _module_ )
    

For more information, check out reload().

This article is contributed by **Sri Sanketh Uppalapati**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

