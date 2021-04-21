Python – Dictionary values combination of size K



Sometimes while working with Python dictionaries, we can have a problem in
which we need to extract combination of cetain key’s value of size K. This is
usually when values are in form of strings. This can have application in day-
day programming. Let’s discuss a way in which this task can be performed.

>  **Input** : test_dict = {‘a’ : ‘a’, ‘b’ : ‘b’, ‘c’ : ‘c’, ‘d’ : ‘d’}  
>  **Output** : [‘aaa’, ‘bbb’, ‘ccc’, ‘ddd’]
>
>  **Input** : test_dict = {‘a’ : ‘abcd’, ‘b’ : ”, ‘c’ : ”, ‘d’ : ”}  
>  **Output** : [‘aaa’, ‘aab’, ‘aac’, ‘aad’]

 **Method : Using recursion + generator function + yield**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of combinations all possible using recursion. The
generator function is used to dynamically create values and return to calling
function using yield.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary values combination of size K

# Using yield + generator function + recursion

 

def gen_strs(chr_key, test_dict, K):

 def hlpr(s):

 if len(s) == K:

 yield s

 elif len(s) < K:

 for ltr in test_dict[s[-1]]:

 yield from hlpr(s + ltr)

 for ltr in chr_key:

 yield from hlpr(ltr)

 

# initializing dictionary

test_dict = {'a' : 'abc', 'b' : 'bd', 'c' : 'c',
'd' : 'ab'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 3

 

# initializing character keys 

chr_key = 'abcd'

 

# Dictionary values combination of size K

# Using yield + generator function + recursion

res = []

for ele in gen_strs(chr_key, test_dict, K):

 res.append(ele)

 

# printing result 

print("The extracted combinations : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘b’: ‘bd’, ‘a’: ‘abc’, ‘d’: ‘ab’, ‘c’: ‘c’}  
> The extracted combinations : [‘aaa’, ‘aab’, ‘aac’, ‘abb’, ‘abd’, ‘acc’,
> ‘bbb’, ‘bbd’, ‘bda’, ‘bdb’, ‘ccc’, ‘daa’, ‘dab’, ‘dac’, ‘dbb’, ‘dbd’]

