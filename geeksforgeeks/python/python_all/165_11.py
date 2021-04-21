Python | Get key with maximum value in Dictionary



Given a dictionary, the task is to find the key having the maximum value.

 **Examples :**

    
    
    **Input :** {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
    **Output :** Jaguar
    
    **Input:** {'Geeks':1900, 'for':1292, 'geek' : 88}
    **Output:** Geeks

**Method #1:** Using max() function

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find key with Maximum value in Dictionary

 

# Dictionary Initialization

Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC'
: 88}

 

Keymax = max(Tv, key=Tv.get)

print(Keymax)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    GameOfThrones
    

