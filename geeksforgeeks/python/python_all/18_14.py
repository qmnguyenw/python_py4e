Python – Sort Matrix by Palindrome count



Given a String Matrix, sort each row by palindromic strings count.

>  **Input** : test_list = [[“nitin”, “meem”, “geeks”], [“peep”], [“gfg”,
> “is”, “best”], [“sees”, “level”, “mom”, “noon”]]  
> **Output** : [[‘peep’], [‘gfg’, ‘is’, ‘best’], [‘nitin’, ‘meem’, ‘geeks’],
> [‘sees’, ‘level’, ‘mom’, ‘noon’]]  
> **Explanation** : 1 = 1 < 2 < 4 is palindromic count order.
>
>  **Input** : test_list = [[“nitin”, “meem”, “geeks”], [“peep”], [“sees”,
> “level”, “mom”, “noon”]]  
> **Output** : [[‘peep’], [‘nitin’, ‘meem’, ‘geeks’], [‘sees’, ‘level’, ‘mom’,
> ‘noon’]]  
> **Explanation** : 1 < 2 < 4 is palindromic count order.

**Method #1 : Using** **reversed()** **+** **len()** **\+ sort()**

In this, we perform inplace sort using sort(), the computation of length and
check for Palindrome is done using reversed().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Palindrome count

# Using reversed() + len() + sort()

 

# get palin

def get_palin_freq(row):

 

 # returning length

 return len([sub for sub in row if
''.join(list(reversed(sub))) == sub])

 

 

# initializing list

test_list = [["nitin", "meem", "geeks"], ["peep"],

 ["gfg", "is", "best"], 

 ["sees", "level", "mom", "noon"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort

test_list.sort(key=get_palin_freq)

 

# printing result

print("Sorted rows : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘nitin’, ‘meem’, ‘geeks’], [‘peep’], [‘gfg’, ‘is’,
> ‘best’], [‘sees’, ‘level’, ‘mom’, ‘noon’]]  
> Sorted rows : [[‘peep’], [‘gfg’, ‘is’, ‘best’], [‘nitin’, ‘meem’, ‘geeks’],
> [‘sees’, ‘level’, ‘mom’, ‘noon’]]

 **Method #2 : Using sorted() + len() + reversed()**

Similar to the above method, the difference being sorted() used along with
lambda function to perform task in one-liner without the external function
call.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by Palindrome count

# Using sorted() + len() + reversed()

 

# initializing list

test_list = [["nitin", "meem", "geeks"], ["peep"],

 ["gfg", "is", "best"], ["sees", "level", "mom",
"noon"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort

# sorted() and lambda used to get 1 sentence approach

res = sorted(test_list, key=lambda row: len(

 [sub for sub in row if ''.join(list(reversed(sub)))
== sub]))

 

# printing result

print("Sorted rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘nitin’, ‘meem’, ‘geeks’], [‘peep’], [‘gfg’, ‘is’,
> ‘best’], [‘sees’, ‘level’, ‘mom’, ‘noon’]] Sorted rows : [[‘peep’], [‘gfg’,
> ‘is’, ‘best’], [‘nitin’, ‘meem’, ‘geeks’], [‘sees’, ‘level’, ‘mom’, ‘noon’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

