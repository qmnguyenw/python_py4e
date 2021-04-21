Python – Replace delimiter



Given List of Strings and replacing delimiter, replace current delimiter in
each string.

>  **Input** : test_list = [“a, t”, “g, f, g”, “w, e”, “d, o”], repl_delim = ‘
> ‘  
>  **Output** : [“a t”, “g f g”, “w e”, “d o”]  
>  **Explanation** : comma is replaced by empty spaces at each string.
>
>  **Input** : test_list = [“g#f#g”], repl_delim = ‘, ‘  
>  **Output** : [“g, f, g”]  
>  **Explanation** : hash is replaced by comma at each string.

 **Method #1 : Usingreplace() \+ loop**  
The combination of above functions provide a brute force method to solve this
problem. In this, a loop is used to iterate through each string and perform
replacement using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace delimiter

# Using loop + replace()

 

# initializing list

test_list = ["a, t", "g, f, g", "w, e", "d, o"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing replace delimiter

repl_delim = '#'

 

# Replace delimiter

res = []

for ele in test_list:

 

 # adding each string after replacement using replace()

 res.append(ele.replace(", ", repl_delim))

 

# printing result 

print("Replaced List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : ['a, t', 'g, f, g', 'w, e', 'd, o']
    Replaced List : ['a#t', 'g#f#g', 'w#e', 'd#o']
    

