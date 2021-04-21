Dictionary and counter in Python to find winner of election



Given an array of names of candidates in an election. A candidate name in the
array represents a vote cast to the candidate. Print the name of candidates
received Max vote. If there is tie, print a lexicographically smaller name.

Examples:

    
    
    Input :  votes[] = {"john", "johnny", "jackie", 
                        "johnny", "john", "jackie", 
                        "jamie", "jamie", "john",
                        "johnny", "jamie", "johnny", 
                        "john"};
    Output : John
    We have four Candidates with name as 'John', 
    'Johnny', 'jamie', 'jackie'. The candidates
    John and Johny get maximum votes. Since John
    is alphabetically smaller, we print it.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find winner of an
election where votes are represented as candidate names link. We can solve
this problem quickly in python using Dictionary data structure.  
 **Method 1:**  
Approach is very simple,

  1. Convert given list of votes into dictionary using Counter(iterator) method. We will have a dictionary having candidate names as **Key** and their frequency ( counts ) as **Value**.
  2. Since more than 1 candidate may get same number of votes and in this situation we need to print lexicographicaly smaller name, so now we will create another dictionary by traversing previously created dictionary, counts of votes will be **Key** and candidate names will be **Value**.
  3. Now find value of maximum vote casted for a candidate and get list of candidates mapped on that count value.
  4. Sort list of candidates having same number of maximum votes and print first element of sorted list in order to print lexicographicaly smaller name.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find winner of an election where votes

# are represented as candidate names 

from collections import Counter 

 

def winner(input): 

 

 # convert list of candidates into dictionary 

 # output will be likes candidates = {'A':2, 'B':4} 

 votes = Counter(input) 

 

 # create another dictionary and it's key will 

 # be count of votes values will be name of 

 # candidates 

 dict = {} 

 

 for value in votes.values(): 

 

 # initialize empty list to each key to 

 # insert candidate names having same 

 # number of votes 

 dict[value] = [] 

 

 for (key,value) in votes.items(): 

 dict[value].append(key) 

 

 # sort keys in descending order to get maximum 

 # value of votes 

 maxVote = sorted(dict.keys(),reverse=True)[0] 

 

 # check if more than 1 candidates have same 

 # number of votes. If yes, then sort the list 

 # first and print first element 

 if len(dict[maxVote])>1: 

 print (sorted(dict[maxVote])[0])

 else: 

 print (dict[maxVote][0]) 

 

# Driver program 

if __name__ == "__main__": 

 input =['john','johnny','jackie','johnny',

 'john','jackie','jamie','jamie',

 'john','johnny','jamie','johnny',

 'john'] 

 winner(input)   
  
---  
  
__

__

**Output:**

  

  

    
    
    john
    

**Method 2:**  
This is a shorter method.  
1\. Count the number of votes for each person and stores in a dictionary.  
2\. Find the maximum number of votes.  
3\. Find corresponding person(s) having votes equal to maximum votes.  
4\. As we want output according to lexicographical order, so sort the list and
print first element.

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter 

 

votes
=['john','johnny','jackie','johnny','john','jackie',


'jamie','jamie','john','johnny','jamie','johnny','john']


 

#Count the votes for persons and stores in the dictionary

vote_count=Counter(votes)

 

#Find the maximum number of votes

max_votes=max(vote_count.values())

 

#Search for people having maximum votes and store in a list

lst=[i for i in vote_count.keys() if
vote_count[i]==max_votes]

 

#Sort the list and print lexicographical smallest name

print(sorted(lst)[0])  
  
---  
  
 __

 __

Output:

    
    
    john
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

