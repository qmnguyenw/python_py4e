Counting the frequencies in a list using dictionary in Python



Given an unsorted list of some elements(may or may not be integers), Find the
frequency of each distinct element in the list using a dictionary.

 **Example:**

    
    
    Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                      4, 4, 4, 2, 2, 2, 2]
    Output : 1 : 5
             2 : 4
             3 : 3
             4 : 3
             5 : 2
    Explanation : Here 1 occurs 5 times, 2 
                  occurs 4 times and so on...
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The problem can be solved in many ways. A simple approach would be to iterate
over the list and use each distinct element of the list as a key of the
dictionary and store the corresponding count of that key as values. Below is
the Python code for this approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count the frequency of

# elements in a list using a dictionary

 

def CountFrequency(my_list):

 

 # Creating an empty dictionary 

 freq = {}

 for item in my_list:

 if (item in freq):

 freq[item] += 1

 else:

 freq[item] = 1

 

 for key, value in freq.items():

 print ("% d : % d"%(key, value))

 

# Driver function

if __name__ == "__main__": 

 my_list =[1, 1, 1, 5, 5, 3, 1, 3,
3, 1, 4, 4, 4, 2, 2, 2, 2]

 

 CountFrequency(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
     1 :  5
     2 :  4
     3 :  3
     4 :  3
     5 :  2
    

**Time Complexity:** O(N), where N is the length of the list.

  

  

 **Alternative way:** An alternative approach can be to use the list.count()
method. This makes the program much more compact without affecting the run
time. Below is the Python code for this:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count the frequency of

# elements in a list using a dictionary

 

def CountFrequency(my_list):

 

 # Creating an empty dictionary 

 freq = {}

 for items in my_list:

 freq[items] = my_list.count(items)

 

 for key, value in freq.items():

 print ("% d : % d"%(key, value))

 

# Driver function

if __name__ == "__main__": 

 my_list =[1, 1, 1, 5, 5, 3, 1, 3,
3, 1, 4, 4, 4, 2, 2, 2, 2]

 CountFrequency(my_list)  
  
---  
  
 __

 __

 **Output:**

    
    
     1 :  5
     2 :  4
     3 :  3
     4 :  3
     5 :  2
    

**Time Complexity:** O(N), where N is the length of the list.

 **Alternative way:** An alternative approach can be to use the dict.get()
method. This makes the program much more shorter and makes understand how get
method is useful instead of if…else.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count the frequency of

# elements in a list using a dictionary

 

def CountFrequency(my_list):

 

 # Creating an empty dictionary 

 count = {}

 for i in [1, 1, 1, 5, 5, 3, 1, 3,
3, 1 ,4, 4, 4, 2, 2, 2, 2]:

 count[i] = count.get(i, 0) + 1

 return count

 

# Driver function

if __name__ == "__main__": 

 my_list =[1, 1, 1, 5, 5, 3, 1, 3,
3, 1, 4, 4, 4, 2, 2, 2, 2]

 print(CountFrequency(my_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    {1: 5, 5: 2, 3: 3, 4: 3, 2: 4}
    

**Related Article :**  
Count frequencies of all elements in array in Python using collections module

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

