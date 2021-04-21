Bigram formation from a given Python list



When we are dealing with text classification, sometimes we need to do certain
kind of natural language processing and hence sometimes require to form
bigrams of words for processing. In case of absence of appropriate library,
its difficult and having to do the same is always quite useful. Let’s discuss
certain ways in which this can be achieved.

 **Method #1 : Using list comprehension +enumerate() + split()**  
The combination of above three functions can be used to achieve this
particular task. The enumerate function performs the possible iteration, split
function is used to make pairs and list comprehension is used to combine the
logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Bigram formation

# using list comprehension + enumerate() + split()

 

# initializing list 

test_list = ['geeksforgeeks is best', 'I love it']

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension + enumerate() + split()

# for Bigram formation

res = [(x, i.split()[j + 1]) for i in test_list 

 for j, x in enumerate(i.split()) if j < len(i.split())
- 1]

 

# printing result

print ("The formed bigrams are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘geeksforgeeks is best’, ‘I love it’]  
> The formed bigrams are : [(‘geeksforgeeks’, ‘is’), (‘is’, ‘best’), (‘I’,
> ‘love’), (‘love’, ‘it’)]

  
**Method #2 : Usingzip() + split() + list comprehension**  
The task that enumerate performed in the above method can also be performed by
the zip function by using the iterator and hence in a faster way. Let’s
discuss certain ways in which this can be done.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Bigram formation

# using zip() + split() + list comprehension

 

# initializing list 

test_list = ['geeksforgeeks is best', 'I love it']

 

# printing the original list 

print ("The original list is : " + str(test_list))

 

# using zip() + split() + list comprehension

# for Bigram formation

res = [i for j in test_list 

 for i in zip(j.split(" ")[:-1], j.split("
")[1:])]

 

# printing result

print ("The formed bigrams are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘geeksforgeeks is best’, ‘I love it’]  
> The formed bigrams are : [(‘geeksforgeeks’, ‘is’), (‘is’, ‘best’), (‘I’,
> ‘love’), (‘love’, ‘it’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

