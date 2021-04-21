Python – First K unique elements



Sometimes, while working with Python Lists, we can have a problem in which we
need to extract first K unique elements. This means we need to extract
duplicate if they occur in first K elements as well. This can essentially make
count of first K unique elements more than K. This kind of problem can have
application in day-day programming. Let’s discuss certain ways in which this
task can be performed.

>  **Input** : test_list = [6, 7, 6, 7], K = 2  
>  **Output** : [6, 7]
>
>  **Input** : test_list = [3, 4, 5, 7], K = 3  
>  **Output** : [3, 4, 5]

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
perform task of getting elements by keeping counter and store list to compare
previous occurrences.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# First K unique elements

# Using loop

 

# initializing list

test_list = [6, 7, 6, 7, 8, 3, 9, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 4

 

# First K unique elements

# Using loop

store = []

res = []

cnt = 0

for ele in test_list:

 if ele not in store:

 cnt = cnt + 1

 store.append(ele)

 res.append(ele)

 if cnt >= K :

 break

 

# printing result 

print("The extracted elements : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [6, 7, 6, 7, 8, 3, 9, 11]
    The extracted elements : [6, 7, 6, 7, 8, 3]
    

