Print anagrams together in Python using List and Dictionary



Given an array of words, print all anagrams together ?

Examples:

    
    
    Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
    Output : 'cat tac act dog god'
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Anagrams and Given a sequence
of words, print all anagrams together links. We will solve this problem in
python using List and Dictionary data structures. Approach is very simple :

  * Traverse list of strings.
  * Sort each string in ascending order and consider this sorted value as **Key** and original value as **Value** of corresponding key. Check if key is not present in dictionary that means it is occurring first time,  
so map a empty list to **Key** and append value in it, if key is already
present then simple append the value.

  * Now each key will contain list of strings which are anagram together.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to return all anagrams together

def allAnagram(input): 

 

 # empty dictionary which holds subsets 

 # of all anagrams together 

 dict = {} 

 

 # traverse list of strings 

 for strVal in input: 

 

 # sorted(iterable) method accepts any 

 # iterable and rerturns list of items 

 # in ascending order 

 key = ''.join(sorted(strVal)) 

 

 # now check if key exist in dictionary 

 # or not. If yes then simply append the 

 # strVal into the list of it's corresponding 

 # key. If not then map empty list onto 

 # key and then start appending values 

 if key in dict.keys(): 

 dict[key].append(strVal) 

 else: 

 dict[key] = [] 

 dict[key].append(strVal) 

 

 # traverse dictionary and concatenate values 

 # of keys together 

 output = "" 

 for key,value in dict.items(): 

 output = output + ' '.join(value) + ' '

 

 return output 

 

# Driver function 

if __name__ == "__main__": 

 input=['cat', 'dog', 'tac', 'god', 'act'] 

 print (allAnagram(input))   
  
---  
  
__

__

Output:

  

  

    
    
    'cat tac act dog god'
    

This article is contributed by **Shashank Mishra (Gullu)**. If you like
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

