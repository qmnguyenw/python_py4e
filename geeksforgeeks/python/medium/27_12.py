Understanding Code Reuse and Modularity in Python 3



 **What is Object Oriented Programming(OOP)?**

OOP is a programming paradigm based on the concept of “objects”, which may
contain data, in the form of fields, often known as attributes; and code, in
the form of procedures, often known as methods.Learn more here, or just Google
“OOP”.

Objects have characteristics and features, known as attributes, and can do
various things, through their methods. The biggest feature of OOP is how well
objects can be interacted with, and even molded in the future, which makes
them very friendly to developers, scale, change over time, testing, and much
more.

 **What is Modularity?**

  

  

Modularity refers to the concept of making multiple modules first and then
linking and combining them to form a complete system (i.e, the extent to which
a software/Web application may be divided into smaller modules is called
modularity). Modularity enables re-usability and will minimize duplication.

 **Flow of the Article**

 **Aim:** To learn object oriented programming – Modularity. How can we turn
some portions of our code into a library so that it can be used by anyone for
future reference. Making the code modular will enable re-usability and
minimizes duplication.

 **Dependencies:** pygame

 **Summary:** We are going to make a small game(not really a game) but just an
environment and some objects in it. We will try to make the environment static
and the objects( blobs in our case) modular. We will make use of PyGame, since
it gives us a simple way to actually visualize what we’re doing and building,
so we can see our objects in action. What we’re going to do is build Blob
World, which is a world that consists of actors, known as blobs. Different
blobs have different properties, and the blobs need to otherwise function
within their Blob World environment. With this example, we’ll be able to
illustrate modularity.  
We are dividing our learning process into two phases.

  1. Creating the Environment and the Blobs
  2. Understanding Modularity

Repository(Github):

