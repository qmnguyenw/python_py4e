Python – Extract words starting with K in String List



Given list of phrases, extract all the Strings with begin with character K.

>  **Input** : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I
> love G4G”], K = l  
>  **Output** : [‘learning’, ‘love’]  
>  **Explanation** : All elements with L as starting letter are extracted.
>
>  **Input** : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I
> love G4G”], K = m  
>  **Output** : []  
>  **Explanation** : No words started from “m” hence no word extracted.

 **Method #1 : Using loop + split()**

This is brute way in which this problem can be solved. In this, we convert
each phrase into list of words and then for each word, check if it’s initial
character is K.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract words starting with K in String List

# Using loop + split()

 

# initializing list

test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]


 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "g"

 

res = []

for sub in test_list:

 # splitting phrases

 temp = sub.split()

 for ele in temp:

 

 # checking for matching elements

 if ele[0].lower() == K.lower():

 res.append(ele)

 

# printing result 

print("The filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg is best', 'Gfg is for geeks', 'I love G4G']
    The filtered elements : ['Gfg', 'Gfg', 'geeks', 'G4G']
    
    

**Method #2 : Using list comprehension + split()**

This is yet another way in which this task can be performed. In this we run
double nested loops inside single list comprehension and perform required
conditional checks.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract words starting with K in String List

# Using list comprehension + split() 

 

# initializing list

test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]


 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "g"

res = [ele for temp in test_list for ele in temp.split()
if ele[0].lower() == K.lower()]

 

# printing result 

print("The filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg is best', 'Gfg is for geeks', 'I love G4G']
    The filtered elements : ['Gfg', 'Gfg', 'geeks', 'G4G']
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

