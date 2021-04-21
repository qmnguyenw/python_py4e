Python | Find most frequent element in a list



Given a list, find the most frequent element in it. If there are multiple
elements that appear maximum number of times, print any one of them.

 **Examples:**

    
    
    **Input :** [2, 1, 2, 2, 1, 3]
    **Output :** 2
    
    **Input :** ['Dog', 'Cat', 'Dog']
    **Output :** Dog
    

**Approach #1 :** Naive Appraoch

This is a brute force approach in which we make use of for loop to count the
frequency of each element. If the current frequency is greater than the
previous frequency, update the counter and store the element.

 __

 __  
 __

 __

 __  
 __  
 __

# Program to find most frequent

# element in a list

 

def most_frequent(List):

 counter = 0

 num = List[0]

 

 for i in List:

 curr_frequency = List.count(i)

 if(curr_frequency> counter):

 counter = curr_frequency

 num = i

 

 return num

 

List = [2, 1, 2, 2, 1, 3]

print(most_frequent(List))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2
    

