How to split a string in C/C++, Python and Java?



Splitting a string by some delimiter is a very common task. For example, we
have a comma-separated list of items from a file and we want individual items
in an array.  
Almost all programming languages, provide a function split a string by some
delimiter.

### **In C:**

    
    
    // Splits str[] according to given delimiters.
    // and returns next token. It needs to be called
    // in a loop to get all tokens. It returns NULL
    // when there are no more tokens.
    char * strtok(char str[], const char *delims);

## C

 __

 __  
 __

 __

 __  
 __  
 __

// A C/C++ program for splitting a string

// using strtok()

#include <stdio.h>

#include <string.h>

int main()

{

 char str[] = "Geeks-for-Geeks";

 // Returns first token

 char *token = strtok(str, "-");

 

 // Keep printing tokens while one of the

 // delimiters present in str[].

 while (token != NULL)

 {

 printf("%s\n", token);

 token = strtok(NULL, "-");

 }

 return 0;

}  
  
---  
  
 __

 __

    
    
    Output: Geeks
        for
        Geeks

###  **In C++**

    
    
    Note:  The main disadvantage of strtok() is that it only works for C style strings.
           Therefore we need to explicitly convert C++ string into a char array.
           Many programmers are unaware that C++ has two additional APIs which are more elegant
           and works with C++ string. 

#### **Method 1:** Using stringstream API of C++

 **Prerequisite** : stringstream API

Stringstream object can be initialized using a string object, it automatically
**_tokenizes strings on space char._** Just like “cin” stream stringstream
allows you to read a string as a stream of words.

    
    
     _Some of the Most Common used functions of StringStream._
    clear() — flushes the stream 
    str() —  converts a stream of words into a C++ string object.
    operator << — pushes a string object into the stream.
    operator >> — extracts a word from the stream.

The code below demonstrates it.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

// A quick way to split strings separated via spaces.

void simple_tokenizer(string s)

{

 stringstream ss(s);

 string word;

 while (ss >> word) {

 cout << word << endl;

 }

}

int main(int argc, char const* argv[])

{

 string a = "How do you do!";

 // Takes only space seperated C++ strings.

 simple_tokenizer(a);

 cout << endl;

 return 0;

}  
  
---  
  
 __

 __

    
    
    Output : How 
         do 
         you
         do!

####  **Method 2: Using C++ find() and substr() APIs.**

 **Prerequisite:** **find function** **and** **substr()** **.**

  

  

This method is **_more robust and can parse a string with any delimiter_** ,
not just spaces(though the default behavior is to separate on spaces.) The
logic is pretty simple to understand from the code below.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

void tokenize(string s, string del = " ")

{

 int start = 0;

 int end = s.find(del);

 while (end != -1) {

 cout << s.substr(start, end - start) << endl;

 start = end + del.size();

 end = s.find(del, start);

 }

 cout << s.substr(start, end - start);

}

int main(int argc, char const* argv[])

{

 // Takes C++ string with any separator

 string a = "Hi$%do$%you$%do$%!";

 tokenize(a, "$%");

 cout << endl;

 return 0;

}  
  
---  
  
 __

 __

    
    
    Output: How 
        do 
        you
        do
        !

 **In Java :**  
In Java, split() is a method in String class.

    
    
    // **expregexp** is the delimiting regular expression; 
    // **limit** is the number of returned strings
    public String[] **split** (String regexp, int limit);
    
    // We can call split() without limit also
    public String[] **split** (String regexp)

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// A Java program for splitting a string

// using split()

import java.io.*;

public class Test

{

 public static void main(String args[])

 {

 String Str = new String("Geeks-for-Geeks");

 // Split above string in at-most two strings 

 for (String val: Str.split("-", 2))

 System.out.println(val);

 System.out.println("");

 

 // Splits Str into all possible tokens

 for (String val: Str.split("-"))

 System.out.println(val);

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks
    for-Geeks
    
    Geeks
    for
    Geeks

 **In Python:**  
The split() method in Python returns a list of strings after breaking the
given string by the specified separator.

    
    
     
      // **regexp** is the delimiting regular expression; 
      // **limit** is limit the number of splits to be made 
      str. **split** (regexp = "", limit = string.count(str))  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

line= "Geek1 \nGeek2 \nGeek3";

print line.split()

print line.split(' ', 1)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geek1', 'Geek2', 'Geek3']
    ['Geek1', '\nGeek2 \nGeek3'] 

This article is contributed by **Aditya Chatterjee.** If you like
GeeksforGeeks and would like to contribute, you can also write an article and
mail your article to contribute@geeksforgeeks.org. See your article appearing
on the GeeksforGeeks main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

