Finding Mean, Median, Mode in Python without libraries



In this article, we will learn how to calculate **Mean, Median, and Mode with
Python** without using external libraries.

  1.  **Mean :** The mean is the average of all numbers and is sometimes called the arithmetic mean. This code calculates Mean or Average of a list containing numbers:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# mean of elements

 

# list of elements to calculate mean

n_num = [1, 2, 3, 4, 5]

n = len(n_num)

 

get_sum = sum(n_num)

mean = get_sum / n

 

print("Mean / Average is: " + str(mean))  
  
---  
  
 __

 __

 **Output:**

    
    
    Mean / Average is: 3.0
    

We define a list of numbers and calculate the length of the list. We then use
sum() function to get sum of all the elements in a list. We finally divide the
total sum by the number of elements in the list and we print the result to get
the mean/average of a list.

  2.  **Median :** The median is the middle number in a group of numbers. This code calculates Median of a list containing numbers:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# median of elements

 

# list of elements to calculate median

n_num = [1, 2, 3, 4, 5]

n = len(n_num)

n_num.sort()

 

if n % 2 == 0:

 median1 = n_num[n//2]

 median2 = n_num[n//2 - 1]

 median = (median1 + median2)/2

else:

 median = n_num[n//2]

print("Median is: " + str(median))  
  
---  
  
 __

 __

 **Output:**

    
    
    Median is: 3
    

We define a list of numbers and calculate the length of the list. To find a
median, we first sort the list in Ascending order using sort() function.  
Now we check if the number is even or odd by checking their remainders. If the
number is even, we find 2 middle elements in a list and get their average to
print it out. But if the number is odd, we find the middle element in a list
and print it out.

  3.  **Mode :** The mode is the number that occurs most often within a set of numbers. This code calculates Mode of a list containing numbers:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# mode of elements

from collections import Counter

 

# list of elements to calculate mode

n_num = [1, 2, 3, 4, 5, 5]

n = len(n_num)

 

data = Counter(n_num)

get_mode = dict(data)

mode = [k for k, v in get_mode.items() if v ==
max(list(data.values()))]

 

if len(mode) == n:

 get_mode = "No mode found"

else:

 get_mode = "Mode is / are: " + ', '.join(map(str,
mode))

 

print(get_mode)  
  
---  
  
 __

 __

 **Output:**

    
    
    Mode is / are: 5
    

We will import Counter from collections library which is a built-in module in
Python 2 and 3. This module will help us count duplicate elements in a list.  
We define a list of numbers and calculate the length of the list. We then call
Counter (a dict subclass) which helps to count hashable objects, and we then
convert it to dict object. We then initialize a list with a For Loop to
compare all the dict values (Number of elements) to the max of all dict values
(count of most occurring element) and it returns all the elements equal to max
count. If the elements returned are equal to the number of total elements in a
list then we print out ‘No mode’, else we print out the modes returned.

  

  

 **Another simple approach to find mode with simple coding**

 __

 __  
 __

 __

 __  
 __  
 __

# The list for which you need to find

# the Mode

y= [11, 8, 8, 3, 4, 4, 5, 6, 6,
6, 7, 8]

 

# First you sort it

# You will get numbers arranged from 3 to 

# 11 in asc order

y.sort() 

 

# Now open an empty list.

# What you are going to do is to count

# the occurrence of each number and append

# (or to add your findings to) L1

L1=[]

 

# You can iterate through the sorted list

# of numbers in y,

# counting the occurrence of each number,

# using the following code

 

i = 0

while i < len(y) :

 L1.append(y.count(y[i]))

 i += 1

 

# your L1 will be [1, 2, 2, 1, 3, 3, 3, 1, 3, 3, 3, 1], 

# the occurrences for each number in sorted y

 

# now you can create a custom dictionary d1 for k : V

# where k = your values in sorted y 

# and v = the occurrences of each value in y

 

# the Code is as follows

 

d1 = dict(zip(y, L1))

 

# your d1 will be {3: 1, 4: 2, 5: 1, 6: 3, 7: 1, 8: 3, 11: 1}

# now what you need to do is to filter 

# the k values with the highest v values.

# do this with the following code

 

d2={k for (k,v) in d1.items() if v == max(L1) }

 

print("Mode(s) is/are :" + str(d2))  
  
---  
  
 __

 __

 **Output:**

    
        Mode(s) is/are :{8, 6}

 **Conclusion**  
We have successfully calculated mean, median, and mode of a dataset but you
might be thinking ‘Will I be using these algorithms every time I want to get
mean, median and mode of a dataset?’  
The answer is you can but you certainly won’t. This was just to show you how
the algorithm works behind the scenes when finding out any of these.  
For any projects, this can be achieved by simply importing an inbuilt library
‘statistics’ in Python 3, and using the inbuilt functions mean(), median() and
mode(). Also, there are other external libraries that can help you achieve the
same results in just 1 line of code as the code is pre-written in those
libraries.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

