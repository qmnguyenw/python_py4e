Top 12 Data Structure Algorithms to Implement in Practical Applications in
2021



 **New Year…New Beginning…!!!**

 _What’s your plan for this year??? (Being a programmer)_

Of course, if you’re a programmer then this year you will also write the code,
build the projects and you will solve a lot of coding questions.

Let’s talk about _**Data Structures and Algorithms**_ …

Heart of computer science and the programmer’s breath to live in the coding
world…

![Top-12-Data-Structure-Algorithms-to-Implement-in-Practical-Applications-
in-2021](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210101001655/Top-12-Data-Structure-Algorithms-to-Implement-in-
Practical-Applications-in-2021.png)

  

  

A lot of beginners start learning programming by picking up these two
important tools of computer science. You might have practiced a lot but have
you ever tried to know how these algorithms are helpful in the real-world
application. Surely there are some reasons to learn them. Most of the newbie
programmers learn it for the sake of a job but isn’t it interesting if we get
to know the practical implementation of these algorithms in the real world.

The new year is coming and this new year we encourage you to check out the
practical scenarios of famous algorithms instead of learning them just for the
sake of a job. In this blog, we will discuss some practical implementations of
these algorithms in the real world.

No matter if you’re a fresher or an experienced person, you will find it
interesting to read. This article will refresh the memories of experienced
programmers. ****

### 1\. **Fibonacci Sequence**

Surely you might have gone through implementing the program for the Fibonacci
series once in your life. Being a student you might have asked to implement
the program for the Fibonacci series or you might have asked this question
during your interviews in XYZ companies.

**Yes!!!** We are talking about the same series where we apply the
mathematical formula _ ****__**a n = an−2+an−1**_ to get the series in our
program. We implement the code to get the series 0, 1, 1, 2, 3, 5, 8, 13, and
21 on to infinity. In this series, we get the next highest number by adding
the consecutive series.

You write the program, you clear your exams or you clear your interviews but
have you ever tried to search that where this series is used in real-world
application? _What could be the possible_ _scenario_ _to utilize_ _this
algorithm_ _in_ _the_ _real_ _world?_

The beauty of this sequence can be used to _**calculate miles to kilometers
and vice versa**_. You will get a nearly accurate result (not accurate but
accurate enough). In a Fibonacci sequence, you can consider any number as
miles and the next number would be in kilometers.

> Consider the sequence 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
>
> In the above example, you can take two consecutive numbers 8 and 13. The
> smaller number is in miles i.e 8 and the bigger one is in kilometers i.e.
> 13.
>
>  
>
>
>  
>
>
> 8 in miles = 13 in kilometers.

### 2\. Palindrome Algorithms

This one is another popular algorithm among programmers. Palindrome number or
string reads the same in reverse order. For example…level, madam, 12021.
Implementing this algorithm is also a common question of the interview process
in many companies.

You test your logical ability while implementing the program for palindrome
numbers but can you just think about the practical scenario of this famous
algorithm? Where it can be used?

Palindromes are used in _**DNA sequence processing**_. But how it is used in
this processing?

A lot of DNA sequences are becoming available. To store the information about
these DNA sequences we use molecular biology database. The capacity of these
databases will be bigger in the future so it is important to communicate and
store the data efficiently in the database.

It is important to compress these DNA sequences for better performance. To
compress these sequences CTW (Context Tree Weighting Method) can be used. This
method compresses the DNA sequences in less than two bits per symbol.

Mainly two characteristic structures of DNA sequences are known. One is
palindrome or reverses compliments and the other one is approximate repeats.
Using the hash and dynamic programming the algorithm searches the approximate
repeat and palindrome before it encodes the next symbol. If it finds a
palindrome or approximate repeat with enough length then the algorithm
represents it with length and distance.

### 3\. Array

 _The first data structure to learn in programming…_

 _Most commonly and most widely used data structure in many applications…_

Every beginner’s programming journey starts with solving the questions of
Array. Being a programmer you might have surely used this data structure a lot
in your application. This data structure is used in every possible situation
where you need to collect the object in one place. From simple to complex
software or web application array is mostly used to store and display the data
dynamically at web pages. Let’s take one of the good examples of using an
array in a real-world application…

We all must have used the _**online ticket booking system**_ at least once. It
might be for booking tickets for train or maybe bus or flights or movies or
any other shows. If we want to book any seat, then it’s just a matter of
clicking on a square and it will be booked.

_Have you ever wondered that the seat you book online on any system it’s a
two-dimensional array?_

When you’re booking a seat it lies somewhere in a specific row and column.
This can be represented by a two-dimensional array such as a seat[4][5]. So an
array is applicable in all kinds of online booking systems. Hope you got the
point and understood the real-world application of Array.

### 4\. Stacks

As a beginner, you might have surely read about the common example of stack
data structure…a stack of plates or books in a cupboard but can you just think
about another example of a stack apart from this basic one?

 _Is there any real-world application built and works on the concept of_ a
_Stack data structure?_

 _ **Yes!!!**_ ****_There is…_

A _ **text editor such as notepad or Microsoft Word**_ uses a stack data
structure to accomplish undo tasks in their editor. Another good example of a
stack is the browser’s working in your laptop or system.

Whenever you perform an activity in a text editor, a stack is created. Using
the push operation you store the action, its metadata like the type of action,
the nature of the action, its data, etc. Using the pop action you perform an
undo operation and the last action (stored on the top of the stack) is removed
or undone from the stack.

Another good example of a stack data structure is the Browser’s working on
your laptop or system. Suppose you’re visiting www.google.com and then you
visit www.geeksforgeeks.org. After that, you visit www.youtube.com. This
information gets stored in the stack data structure using the push operation.
When you click on the back button in your browser you go to the previous page
which is the pop operation performed in the stack.

So if you’re on the page www.youtube.com and you’re pressing the back button
then you visit the previous page www.geeksforgeeks.org. Pressing the back
button again performs the pop operation and you get back to the page
www.google.com.

### 5\. Linked List

Another popular and common data structure among programmers is Linked List.
Now think about the purpose of this data structure in a real-world
application.

We all have a _**music player**_ on our phones, and we have songs on it.
Suppose you have 5-6 songs on your list. When you create a playlist for these
songs it works on the concept of the linked list. One by one these songs are
played and this is one of the best examples of the singly linked list. Songs
are connected and you can go from song three to song four but you can not go
back (behavior of singly linked list).

When you implement the functionality to play the song in both directions, it
follows the behavior of a doubly linked list. In a doubly-linked list, nodes
are connected in both directions. So in a playlist, you can move from song 3
to song 4 as well as song 3 to song 2. You will have both previous and next
buttons. So bidirectional navigation is possible.

When you play the songs in repeat mode it follows the behavior of a circular
linked list. In a circular linked list, the last node is connected with the
first node. So once the last song is completed the first song will play again
and it will play in the cyclic mode and it will never stop.

### 6\. Binary Search Algorithm

Being a programmer you might be aware of the binary search algorithm. This
algorithm is also known as half interval search, logarithmic search, or binary
chop. In this algorithm, we search for the target value within a sorted array.

This algorithm makes the searching process easier because you don’t need to
compare each element in the list of numbers. Binary search is the fast way to
search the target value in the ordered list of data. It gives you the power to
do this process efficiently. You can find a lot of examples of binary search
algorithms such as searching the meaning of the word in a dictionary, but do
you know anyone of a real-world application that uses the binary search
method?

One of the real-world scenarios of this algorithm is _**validating user
credentials in an application**_. Using the binary search you can validate the
millions of user’s credentials within a fraction of seconds.

This algorithm also used in many programming languages libraries such as Java,
.NET, C++ STL, and so on. Python’s list.sort() method uses _Timsort_ which
(AFAIK) uses binary search to locate the positions of elements. Binary search
is also used in 99% of 3D games and applications.

### 7\. Merge Sort Algorithm

Merge sort works on the concept of divide and conquer technique. We divide the
list into several sublist until the sublist doesn’t contain a single element.
After that, we merge these sublists to get the sorted list of elements. This
is a simple and short introduction to this algorithm but do you know where it
is used in real-world applications.

A lot of people love to do _**online shopping through any e-commerce
website**_. Do you know that these e-commerce websites use this algorithm?
Most of the e-commerce sites have the section “ **You might like”.** This
section maintains the array of all the user accounts and then whichever has
the least number of inversion with your array of choices, start recommending
what they have bought, or they like. (Next time this section will remind you
of the uses of binary search while doing shopping on these websites)

### 8\. Armstrong Numbers

Another popular program among programmers is checking the number if it is
Armstrong or not. In Armstrong numbers, the sum of cubes of digits of a number
is equal to the number itself. For example, 153 and 371 is an Armstrong
number. Armstrong numbers are mostly used in data security applications for
data encryption and decryption.

Visit the link of IJITEE. Armstrong number for _ **wireless sensor networks**_
are mentioned. They have used Armstrong based security algorithms where a
128-bit key is generated using the Armstrong number. It is used in the AES
algorithm for data encryption and decryption.

### 9\. Huffman Coding

Huffman coding is used in conjunction with cryptography and data compression.
It is used for lossless data compression. Based on the probability, it is
implemented in a way that you do not need to keep multiple copies of the same
thing.

Huffman coding is used in _**compression formats such as**_ _ **GZIP, PKZIP
(winzip**_ _ **,**_ _ **etc)**_ _ **,**_ _ **and BZIP2**_. All the
communication with and from the internet uses the Huffman encoding. Most of
the image files such as JPEG and PNG are Huffman encoded. Also, music files
such as MP3s are Huffman encoded.

Huffman code converts the fixed-length codes into variable-length codes. This
is further compressed using JPEG and MPEG techniques that generate the desired
compression ratio.

### 10\. Dynamic Programming

Another favorite topic for computer science students and for programmers is
dynamic programming. 0-1 Knapsack Problem, Wordbreak problems, Longest Common
Subsequence all these problems are the most popular and common problems of
dynamic programming. You solve it, you use your logical ability but where
actually in the real world this concept is used…

Dynamic programming is widely used in _**bioinformatics, mathematics, and
economics**_. In bioinformatics tasks such as _**sequence alignment, protein
folding, RNA structure prediction**_ _ **,**_ _ **and protein-DNA binding**_
uses dynamic programming.

In mathematics, DP is used in matrix multiplication which is widely used in
Rocket technology. The path of the rockets is decided by solving many
parameters. All the decision-making problems can be solved optimally using
dynamic programming.

### 11\. Graph

Whether you’re traveling somewhere, going outside or you’re trying to find the
route to your specific destination. You use your best friend in your phone
Google Map. Do you know that Google Map uses the Graph data structure?

The graph data structure is a very powerful data structure. Not only the earth
but the whole universe can be represented by the graph. From tiny subatomic
particles to the gigantic universe, you can represent each and everything with
the help of Graph.

When you’re using a Google map, all the cities and states are connected like a
graph with distance information. There are many ways to reach from one city to
the other one but to find the shortest path between the two cities you need to
use some algorithms. Dijkstra’s algorithms which is a very powerful algorithm
can be implemented to find the shortest path between the two cities.

To decide the shortest path to your destination, Dijkstra’s algorithm enables
your _**navigation system/GPS**_ in your phone. Uber uses Hungarian Algorithm
to assign each car to people looking for a ride.

_**Facebook also uses the graph data**_ _ **structure**_ _ **to implement the
news feed or followers**_. It uses Graph API to implement most of the things
in their application. Everything can be represented by the vertices or node
such as Pages, Places, Groups, Comments, Photos, Photo Albums, Stories,
Videos, Notes, etc. Every connection or relationship is an edge on Facebook.
Graph API stores the data in the form of vertices and edges.

### 12\. Trie Data Structure

This one is an advanced data structure topic for programmers. You learn it may
be for the sake of the job, you also enjoy solving questions based on it but
what’s the use of this advanced topic in the real-world application. _Where is
it implemented in our day-to-day life?_ Let’s come to that interesting answer…

You use your mobile phone every day, you also use the swipe features in it.
This swipe features in your mobile keypad and the auto-correct while writing a
document uses a Trie data structure. Trie data structure holds the character
values in your phone.

_**Network browser history**_ also uses a Trie data structure. The URLs of the
site, you have visited are organized by the Trie data structure. When a user
types the prefix of the previously used URL, browser’s complete the URL using
this powerful Data Structure.

### Final Thought

Now you’re aware of the practical use cases of the famous data structures and
algorithms. _ **Isn’t it interesting to know that how these famous algorithms
are implemented in our day-to-day life?**_

Many of us had no knowledge about the interesting use cases of these data
structures and algorithms. We were using it somewhere, but we weren’t aware of
it. _ ****_ It’s always good to know the benefits of something before you pick
up to learn anything. These were just a bunch of data structures and
algorithms we have introduced but there are several algorithms we use in our
day-to-day life.

Now, this new year thinks about the practical use cases of the other
algorithms…

Also, this new year not just learn these algorithms for the sake of learning
them, but also learn these algorithms to implement some interesting real-world
application on your own.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

