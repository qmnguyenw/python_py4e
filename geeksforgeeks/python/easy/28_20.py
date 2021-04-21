Output of Python programs | Set 9 (Dictionary)



 **Prerequisite:** **Dictionary**  
 **1) What is the output of the following program?**

 __

 __  
 __

 __

 __  
 __  
 __

dictionary= {'GFG' : 'geeksforgeeks.org',

 'google' : 'google.com',

 'facebook' : 'facebook.com'

 }

del dictionary['google'];

for key, values in dictionary.items():

 print(key)

dictionary.clear();

for key, values in dictionary.items():

 print(key)

del dictionary;

for key, values in dictionary.items():

 print(key)  
  
---  
  
 __

 __

a) Both b and d  
b) Runtime error  
c) GFG  
facebook  
d) facebook  
GFG

 **Ans. (a)**  
Output:

    
    
    facebook
    GFG
    

**Explanation:** The statement: **del dictionary;** removes the entire
dictionary, so iterating over a deleted dictionary throws a runtime error as
follows:

    
    
    Traceback (most recent call last):
      File "cbeac2f0e35485f19ae7c07f6b416e84.py", line 12, in 
        for key, values in dictionary.items():
    NameError: name 'dictionary' is not defined

 **2) What is the output of the following program?**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

dictionary1= {'Google' : 1,

 'Facebook' : 2,

 'Microsoft' : 3

 }

dictionary2 = {'GFG' : 1,

 'Microsoft' : 2,

 'Youtube' : 3

 }

dictionary1.update(dictionary2);

for key, values in dictionary1.items():

 print(key, values)  
  
---  
  
 __

 __

a) Compilation error  
b) Runtime error  
c) (‘Google’, 1)  
(‘Facebook’, 2)  
(‘Youtube’, 3)  
(‘Microsoft’, 2)  
(‘GFG’, 1)  
d) None of these

 **Ans. (c)**  
 **Explanation:** dictionary1.update(dictionary2) is used to update the
entries of dictionary1 with entries of dictionary2. If there are same keys in
two dictionaries, then the value in second dictionary is used.  
 **  
3) What is the output of the following program?**

 __

 __  
 __

 __

 __  
 __  
 __

dictionary1= {'GFG' : 1,

 'Google' : 2,

 'GFG' : 3

 }

print(dictionary1['GFG']);  
  
---  
  
 __

 __

a) Compilation error due to duplicate keys  
b) Runtime time error due to duplicate keys  
c) 3  
d) 1

 **Ans. (c)**  
 **Explanation:** Here, GFG is the duplicate key. Duplicate keys are not
allowed in python. If there are same keys in a dictionay, then the **value
assigned mostly recently** is assigned to the that key.

 **4) What is the output of the following program?**

 __

 __  
 __

 __

 __  
 __  
 __

temp= dict()

temp['key1'] = {'key1' : 44, 'key2' : 566}

temp['key2'] = [1, 2, 3, 4]

for (key, values) in temp.items():

 print(values, end = "")  
  
---  
  
 __

 __

a) Compilation error  
b) {‘key1’: 44, ‘key2’: 566}[1, 2, 3, 4]  
c) Runtime error  
d) None of the above

 **Ans.** (b)  
 **Explanation:** A dictionary can hold any value such as an integer, string,
list or even another dictionary holding key value pairs.  
 **Note:** This code can be executed only in python versions above 3  
 **  
5) What is the output of the following program?**

 __

 __  
 __

 __

 __  
 __  
 __

temp= {'GFG' : 1,

 'Facebook' : 2,

 'Google' : 3

 }

for (key, values) in temp.items():

 print(key, values, end = " ")  
  
---  
  
 __

 __

a) Google 3 GFG 1 Facebook 2  
b) Facebook 2 GFG 1 Google 3  
c) Facebook 2 Google 3 GFG 1  
d) Any of the above

 **Ans.** (d)  
 **Explanation:** Dictionaries are unordered. So any key value pairs can be
added at any location within a dictionary. Any of the output may come.  
 **Note:** This code can be executed only in python versions above 3.

This article is contributed by **Mayank Kumar**. If you like GeeksforGeeks and
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

