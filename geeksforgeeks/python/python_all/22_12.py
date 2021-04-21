Python Program that prints the count of either peaks or valleys from a list



Given a List, the following article shows ways to count elements which are
either peak(x > y < z) or valley(x < y > z).

>  **Input** : test_list = [1, 2, 4, 2, 6, 7, 8, 3]  
> **Output** : 3  
> **Explanation** : (2, 4, 2), (4, 2, 6), (7, 8, 3) are peaks and valleys.  
> **Input** : test_list = [1, 2, 4, 5, 3, 2]  
> **Output** : 1  
> **Explanation** : (4, 5, 3) is peak.

**Method 1 :** _Using_ _loop_

In this, we iterate for each element and check if its next and previous
element is either smaller or larger than the current element. If found, the
counter is incremented.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [1, 2, 4, 2, 6, 7, 8, 3]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = 0

for idx in range(1, len(test_list) - 1):

 if test_list[idx + 1] > test_list[idx] < test_list[idx - 1]
or test_list[idx + 1] < test_list[idx] > test_list[idx - 1]:

 res += 1

 

# printing result

print("Peaks and Valleys count : " + str(res))  
  
---  
  
 __

 __

