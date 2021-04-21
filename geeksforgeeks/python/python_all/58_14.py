Python – Maximum length consecutive positive elements



Sometimes, while working with Python lists, we can have a problem in which we
monitor a sequence and we need to find what was the maximum length when just
positive elements occur. This kind of problem can have application in data
domains. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [4, 5, 4, 1, 7, 2, 5, 6, -2, -9, -10]  
>  **Output** : 8
>
>  **Input** : test_list = [4, -5, -4, -1, -7, 2, 5, -6, -2, -9, -10]  
>  **Output** : 2

 **Method #1 : Using loop**  
This is one of the way in which we perform this task. In this brute force way,
we iterate for all the elements and keep on updating max, whenever the
positive elements chain is broken.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum length consecutive positive elements

# Using loop

 

# initializing list

test_list = [4, 5, -4, -1, -7, 2, 5,
6, -2, -9, -10]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Maximum length consecutive positive elements

# Using loop

counter = 0

max_score = 1

for ele in test_list:

 if ele > 0:

 counter += 1

 else:

 if(counter > 0):

 max_score = max(max_score, counter)

 counter = 0

if(counter > 0):

 max_score = max(max_score, counter)

 

# printing result 

print("Maximum elements run length : " + str(max_score))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [4, 5, -4, -1, -7, 2, 5, 6, -2, -9, -10]
    Maximum elements run length : 3
    

