Python | Word Stretch



Write a program to get all possibilities (in sorted order) for stretching a
word to the given size. If the list of required indices is passed, then only
those combinations present at those indices should be returned. If the
required indices are null, then all the combinations have to be returned.

 **Examples:**

    
    
    **Input:**
    str = "1234"  
    n = 6 
    indices = null 
    
    **Output:** 
    ["111234", "112234", "112334", "112344", "122234",
     "122334", "122344", "123334", "123344", "123444"] 
    
    The above string  “1234”, with stretch length can be stretched for different possibilities
    like "111234", "112334", "112344" etc. The output represents a list of 
    different stretches in a sorted manner. Since the indices are given as
    null we print the entire list of possibilities 
    
    **Input:**
    str = "1234"
    n = 6 
    indices = 1, 5, 9 
    **Output:** 
    ["112234", "122334", "123444"]
     
    Here only stretched strings of given indices are printed. 
    
    **Input:**
    str = "merit"  
    n = 6 
    indices = null 
    **Output:**
    ["meerit", "meriit", "meritt", "merrit", "mmerit"] 
    
    **Input:**
    str = "java" 

