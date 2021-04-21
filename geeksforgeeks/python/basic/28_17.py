Tips and Tricks for Competitive Programmers | Set 2 (Language to be used for
Competitive Programming)



This is a question asked quite often as in which language should be preferred
to be efficient in competitive programming. It is something one should not
worry about as what matters is the logic not the language. Most of the
languages are more or less same ,but till now the most proffered language is
C++ and here are the reasons.

 **Python**

  *  **Simple and Easy:** Python is simple, easy to write (we need to type less), and has a huge collection of modules with almost all the functions you can imagine.
  *  **Data Types:** Python is generally preferred as it does not have any upper limit on the memory of integers. Also, one does not need to specify which data type it is and things like this make it easier to code but at the same time makes it difficult to compile (in reference to time taken for compilation).
  *  **Slow in Execution:** Python programs are generally slower compared to Java (See this). Python is pretty much ruled out in the starting itself due to it’s high time of execution.

  

  

Now we are mostly left with Java, C, C++, now here it becomes difficult to
compare and is mostly dependent on the user but let’s discuss the good and the
bad points of each of the them.

 **Java**

  *  **STL vs containers:** STL in C++ is really well designed whereas some people love Java Containers more than anything. There are few situations where STL doesn’t have a direct solution. For example priority_queue in STL doesn’t support decrease key operation which is required for implementations of Dijkstra’s shortest Path Algorithm and Prim’s algorithm
  *  **Exception Handling in Java is incomparable:** Java code provides a stronger exception handling versus C++. For instance it’s easier to trace an ArrayIndexOutOfBound exceptions or a segmentation faultin Java. C++/C might give you wrong answers but Java is surely reliable in this context.
  *  **Time Limit Exceeds** : You might get TLE due to Java being slightly slower on the time limit side (Specially in SPOJ), Codeforces.
  *  **Big integer and Regular Expressions:** Java has some few advantages with respect to programming contests. Biginteger, Regular Expressions and geometry library are some of them.

Now let us proceed to C++.

 **C++ and C**

  *  **C++ speed is comparable to C:** Many C programs are valid C++ programs as well – and such C programs run at identical speed when compiled
  *  **C++ does not force object oriented programming:** The C++ language contains some language extensions that facilitate object oriented programming and C++ does not force object oriented design anywhere – it merely allows it.
  *  **Parametrized types** The template keyword allows the programmer to write generic (type-agnostic) implementations of algorithms. Where in C, one could write a generic list implementation with an element like:
    
            struct element_t 
        {
           struct element_t *next, *prev;
           void *element;
        };

C++ allows one to write something like:

  

  

    
        template <typename T>
    struct element_t 
    {
        element_t<T> *next, *prev;
        T element;
    };

  *  **A bigger standard library:** C++ allows the full use of the C standard library as well as C++ includes its own libraries including Standard Template Library. The STL contains a number of useful templates, like the sort routine above. It includes useful common data structures such as lists, maps, sets, etc. Like the sort routine, the other STL routines and data structures are “tailored” to the specific needs the programmer has – all the programmer has to do is fill in the types.  
For example, if we need to implement Binary Search for a problem, we will have
to write our own function whereas in C++ Binary Search STL routine is defined
as

    
         binary_search(startaddress, endaddress, valuetofind)
    

**C++ vs Java**

  *  **Java Codes are longer** A programmer needs to write more when programming in Java

  *  **Java is verbose** : In C++, Input Output is simpler by just writing scanf/printf. In Java, you need the BufferedReader class, which again is tedious.
  *  **C++ STL vs Java Containers:** Most of the programmers find it easier to use STLs.
  *  **C++ is more Popular:** Be it the origin year or the comfort of use, but C++ outstands Java in terms of number of users that use the language.
  *  **C++ saves time :** It’s well-known fact that Java is slower than C++. We generally need to compile and run programs many times to test them. It takes relatively much less time in C++. Therefore, in limited time contests, our time can be saved.

Wrapping it up, C++ is till date most preferred language followed by Java when
it comes to programming contests but you should always choose a language you
are comfortable with. Being CONFIDENT in any language is most important. Never
choose a language which you have “just learnt” as it will be difficult to
express yourself in that language.

For topics, start with cakewalk questions and then move to ad-hoc questions,
then cover standard algorithms and data structure. Finally learn to optimize
your code. All this time emphasis at learning maths, for mathematical algos
are important part of excelling Competitive programming.

 **Happy Coding!!**

Reference: http://unthought.net/c++/c_vs_c++.html

This article is exclusively drafted by contributions of our Campus Geeks-
**Rahul Agarwal, Aditya Chatterjee, Shubham Singh Rajput, Vineet Sethia,
Saiteja Reddy, Shaily Seth, Mudit Maheshwari, Ajay Jain and Ruchir Garg.**

If you like GeeksforGeeks and would like to contribute, you can also write an
article and mail your article to contribute@geeksforgeeks.org. See your
article appearing on the GeeksforGeeks main page and help other Geeks.

Tips and Tricks for Competitive Programmers | Set 1 (For Beginners)

If you are new to competitive programming, this article may help you to write
your first code.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

