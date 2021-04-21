Python – Substitute digits using Dictionary



Sometimes, while working with Python Dictionary, we can have a problem in
which we need to perform substitution of digits of each element in List. This
can lead to change in numbers. This kind of problem can occur in data
preprocessing domains. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [45, 32], dig_map = {4 : 2, 3 : 8, 2 : 6, 5 : 7}  
>  **Output** : [27, 86]
>
>  **Input** : test_list = [44, 44], dig_map = {4 : 2}  
>  **Output** : [22, 22]

 **Method #1 : Using loop**  
This is brute way to solve this problem. In this, we iterate through each
element in list and recreate it using mapped value after converting number to
string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute digits using Dictionary

# Using loop 

 

# initializing list

test_list = [45, 32, 87, 34, 21, 91] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing digit mapping

dig_map = {1 : 4, 4 : 2, 3 : 8, 2 : 6,
7 : 5, 9 : 3, 8 : 9, 5 : 7}

 

# Substitute digits using Dictionary

# Using loop 

temp = []

for idx, ele in enumerate(test_list):

 sub1 = str(ele)

 if len(sub1) > 1:

 sub2 = ""

 for j in sub1:

 if int(j) in dig_map:

 sub2 += str(dig_map[int(j)])

 test_list[idx] = int(sub2)

 else:

 if ele in dig_map:

 test_list[idx] = dig_map[ele]

 

# printing result 

print("List after Digit Substitution : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [45, 32, 87, 34, 21, 91]
    List after Digit Substitution : [27, 86, 95, 82, 64, 34]
    

