Python – Construct Grades List



Given a number, construct list having all the possible Grades combination for
first N characters.

>  **Input** : num = 3  
>  **Output** : [‘A+’, ‘A’, ‘A-‘, ‘B+’, ‘B’, ‘B-‘, ‘C+’, ‘C’, ‘C-‘]  
>  **Explanation** : All grades till C rendered in list.
>
>  **Input** : num = 5  
>  **Output** : [‘A+’, ‘A’, ‘A-‘, ‘B+’, ‘B’, ‘B-‘, ‘C+’, ‘C’, ‘C-‘, ‘D+’, ‘D’,
> ‘D-‘, ‘E+’, ‘E’, ‘E-‘]  
>  **Explanation** : 5 corresponds to E, hence all combinations.

 **Method #1 : Using list comprehension +ord()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of incrementing and extracting ascii characters using
ord() and list comprehension is used in character list creation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Grades List

# Using list comprehension + ord()

 

# initializing N

num = 4

 

# Using list comprehension + ord()

# each charater paired to symbols and character incremented using idx

# conversion by chr + ord

res = [chr(ord('A') + idx) + sym for idx in
range(num) 

 for sym in ['+', '', '-']] 

 

# printing result 

print("Grades List : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    Grades List : ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
    

