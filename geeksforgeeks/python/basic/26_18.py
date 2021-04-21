Amazing hacks of Python



Python is indeed one of the smart and most trending language. Here are some
cool hacks that makes a python superb among all other languages.

  1.  **List comprehensions:** List comprehension is best and efficient technique to get rid of writing unnecessary lines of code. Read Article to know more.
  2.  **Printing a list:** List are not printed according the user requirement. They are always printed in unwanted square brackets and single quotes. But there is trivial solution to print the list efficiently by using the string’s join method.  
 _The join method turns the list into a string by casting each item into a
string and connecting them with the string that join was called on_.

 __

 __  
 __

 __

 __  
 __  
 __

# Declaring the list geek

geek = ['Geeks', 'Programming', 'Algorithm', 'Article']

 

# Directly printing the list

print ("Simple List:", geek)

 

# Printing the list by join method

print ('List by using join method: %s' % ', ' .join(geek))

 

# Direct use of join method

print ('Direct apply the join method:',(", " .join(geek)))  
  
---  
  
 __

 __

    
        **Output:** 
    Simple List: ['Geeks', 'Programming', 'Algorithm', 'Article']
    List by using join method: Geeks, Programming, Algorithm, Article
    Direct apply the join method: Geeks, Programming, Algorithm, Article
    

**Cool Zip tricks**

  3.  **Transpose a matrix:** You can Read Here about this.
  4.  **Partition a list into N groups:** We used iter() as an iterator over a sequence.

 __

 __  
 __

 __

 __  
 __  
 __



# Declaring the list geek

geek = ['Sun', 'Flowers', 'Peoples', 'Animals',
'Day', 'Night']

 

partition = list(zip (*[iter(geek)] * 2))

print (partition)  
  
---  
  
 __

 __

    
        **Output:** 
    [('Sun', 'Flowers'), ('Peoples', 'Animals'), ('Day', 'Night')]
    

**Explanation** : [iter(geek)] * 2 produces a list containing 2 items of
geek[] list, i.e. a list of length 2. *arg unpacks a sequence into arguments
for a function call. Therefore we are passing the same iterator 2 times to
zip().

  5.  **Printing more than one list’s items simultaneously**

 __

 __  
 __

 __

 __  
 __  
 __

list1= [1, 3, 5, 7]

list2 = [2, 4, 6, 8]

 

# Here zip() function takes two equal length list and merges them

# together in pairs

for a, b in zip(list1,list2):

 print (a, b)  
  
---  
  
 __

 __

    
        **Output:** 
    1 2
    3 4
    5 6
    7 8
    

  6. **Take the string as input and convert it into list:**

 __

 __  
 __

 __

 __  
 __  
 __

# Reads a string from input and type case them to int

# after splitting to white-spaces

 

formatted_list = list(map(int, input().split()))

print(formatted_list)  
  
---  
  
 __

 __

    
        **Input:**
    2 4 5 6
    **Output:**
    [2, 4, 5, 6] 
    
    

  7. **Convert list of list into single list**

 __

 __  
 __

 __

 __  
 __  
 __

# import the itertools

import itertools 

 

# Declaring the list geek 

geek = [[1, 2], [3, 4], [5, 6]] 

 

# chain.from_iterable() function returns the

# elements of nested list 

# and iterate from first list 

# of iterable till the last 

# end of the list 

 

lst = list(itertools.chain.from_iterable(geek)) 

print(lst)  
  
---  
  
 __

 __

    
        **Output:** 
    [1, 2, 3, 4, 5, 6]
    

  8. **Printing the repeated characters:** Task is to print the pattern like this Geeeeekkkkss. So we can easily print this pattern without using for loop.

 __

 __  
 __

 __

 __  
 __  
 __

# + used for string concatenation

# To repeat the character n times, just multiply n 

# with that character 

print ("G" + "e"*5 + "k"*4 + "s"*2)  
  
---  
  
 __

 __

    
        **Output:**
    Geeeeekkkkss
    

**Read More:** 10 interesting facts about Python  
 **Reference:** https://www.quora.com/What-are-some-cool-Python-tricks

This article is contributed by Shubham Bansal. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

  

  

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

