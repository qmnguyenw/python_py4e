Python program to find uncommon words from two Strings



Given two sentences as strings **A** and **B**. The task is to return a list
of all **uncommon words**. A word is uncommon if it appears **exactly once**
in any one of the sentences, and does not appear in the other sentence.

 **Note:** A sentence is a string of space-separated words. Each word consists
only of lowercase letters.

 **Examples** :

    
    
    Input : A = "Geeks for Geeks" 
            B = "Learning from Geeks for Geeks"
    Output : ['Learning', 'from']
    
    Input : A = "apple banana mango" 
            B = "banana fruits mango"
    Output : ['apple', 'fruits']
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Every uncommon word occurs exactly once in any one of the
strings. So, we make a hash to count the number of occurrences of every word,
then return a list of words that occurs exactly once.

Below is the implementation of the above approach:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find a list of uncommon words

 

# Function to return all uncommon words

def UncommonWords(A, B):

 

 # count will contain all the word counts

 count = {}

 

 # insert words of string A to hash

 for word in A.split():

 count[word] = count.get(word, 0) + 1

 

 # insert words of string B to hash

 for word in B.split():

 count[word] = count.get(word, 0) + 1

 

 # return required list of words

 return [word for word in count if count[word] == 1]

 

# Driver Code

A = "Geeks for Geeks"

B = "Learning from Geeks for Geeks"

 

# Print required answer

print(UncommonWords(A, B))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['from', 'Learning']
    

**  
Another way to solve this problem:**

 __

 __  
 __

 __

 __  
 __  
 __

def uncommon(a,b):

 list_a = a.split()

 list_b = b.split()

 uc = ''

 for i in list_a:

 if i not in list_b:

 uc = uc+" "+i

 for j in list_b:

 if j not in list_a:

 uc = uc+" "+j

 

 return uc

 

# Driver code

a = "apple banana mango"

b = "banana fruits mango"

print(uncommon(a,b))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['apple','fruits']
    

**Also another way-using in-built function “symmetric_difference()”**

 __

 __  
 __

 __

 __  
 __  
 __

def uncommon(a,b):

 a=a.split()

 b=b.split()

 k=set(a).symmetric_difference(set(b))

 return k

 

#Driver code

if __name__=="__main__":

 a="apple banana mango"

 b="banana fruits mango"

 print(list(uncommon(a,b)))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['apple', 'fruits']
    

**Another way to solve this problem**

 __

 __  
 __

 __

 __  
 __  
 __

def uncommon(A, B):

 un_comm = [i for i in "".join(B).split() if i not in
"".join(A).split()]

 return un_comm

 

#Driver code

A = "Geeks for Geeks"

B = "Learning from Geeks for Geeks"

print(uncommon(A, B))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Learning', 'from']
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

