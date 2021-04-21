Factory Method – Python Design Patterns



Factory Method is a Creational Design Pattern that allows an interface or a
class to create an object, but let subclasses decide which class or object to
instantiate. Using the Factory method, we have the best ways to create an
object. Here, objects are created without exposing the logic to the client and
for creating the new type of the object, the client uses the same common
interface.

### Problems we face without Factory Method:

Imagine you are having your own startup which provides ridesharing in the
different parts of the country. The initial version of the app only provides
the Two-Wheeler ridesharing but as time passes, your app becomes popular and
now you want to add Three and Four-Wheeler ridesharing also.  
It’s a piece of great news! but what about the software developers of your
startup. They have to change the whole code because now the most part of the
code is coupled with the Two-Wheeler class and developers have to make changes
into the entire codebase.  
After done with all these changes, either the developers end with the messy
code or with the resignation letter.  

![factory-pattern-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200117094810/localizer2.jpg)

Localizer app

 **Diagrammatic representation of Problems without using Factory Method**

Let’s understand the concept with one more example which is related to the
translations and localization of the different languages.  
Suppose we have created an app whose main purpose is to translate one language
into another and currently our app works with 10 languages only. Now our app
has become widely popular among people but the demand has grown suddenly to
include 5 more languages.  
It’s a piece of great news! only for the owner not for the developers. They
have to change the whole code because now the most part of the code is coupled
with the existing languages only and that’s why developers have to make
changes into the entire codebase which is really a difficult task to do.

  

  

Let’s look at the code for the problem which we may face without using the
factory method.

 **Note:** Following code is written without using the Factory method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code for Object

# Oriented Concepts without

# using Factory method 

 

class FrenchLocalizer:

 

 """ it simply returns the french version """

 

 def __init__(self):

 

 self.translations = {"car": "voiture", "bike":
"bicyclette",

 "cycle":"cyclette"}

 

 def localize(self, message):

 

 """change the message using translations"""

 return self.translations.get(msg, msg)

 

class SpanishLocalizer:

 """it simply returns the spanish version"""

 

 def __init__(self):

 

 self.translations = {"car": "coche", "bike":
"bicicleta",

 "cycle":"ciclo"}

 

 def localize(self, msg):

 

 """change the message using translations"""

 return self.translations.get(msg, msg)

 

class EnglishLocalizer:

 """Simply return the same message"""

 

 def localize(self, msg):

 return msg

 

if __name__ == "__main__":

 

 # main method to call others

 f = FrenchLocalizer()

 e = EnglishLocalizer()

 s = SpanishLocalizer()

 

 # list of strings

 message = ["car", "bike", "cycle"]

 

 for msg in message:

 print(f.localize(msg))

 print(e.localize(msg))

 print(s.localize(msg))  
  
---  
  
 __

 __

### Solution by Factory Method:

Its solution is to replace the straight forward object construction calls with
calls to the special factory method. Actually there will be no difference in
the object creation but they are being called within the **factory method**.

 **For example:** Our Two_Wheeler, Three_Wheeler, and Four_wheeler classes
should implement the **ridesharing** interface which will declare a method
called **ride**. Each class will implement this method uniquely.

![python-factory-patter-solution](https://media.geeksforgeeks.org/wp-
content/uploads/20200116152733/solution_factory-_diagram.png)

solution_factory_diagram

  
Now let us understand the factory method with the help of an example:

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code for factory method

# it comes under the creational 

# Design Pattern

 

class FrenchLocalizer:

 

 """ it simply returns the french version """

 

 def __init__(self):

 

 self.translations = {"car": "voiture", "bike":
"bicyclette",

 "cycle":"cyclette"}

 

 def localize(self, message):

 

 """change the message using translations"""

 return self.translations.get(msg, msg)

 

class SpanishLocalizer:

 """it simply returns the spanish version"""

 

 def __init__(self):

 self.translations = {"car": "coche", "bike":
"bicicleta",

 "cycle":"ciclo"}

 

 def localize(self, msg):

 

 """change the message using translations"""

 return self.translations.get(msg, msg)

 

class EnglishLocalizer:

 """Simply return the same message"""

 

 def localize(self, msg):

 return msg

 

def Factory(language ="English"):

 

 """Factory Method"""

 localizers = {

 "French": FrenchLocalizer,

 "English": EnglishLocalizer,

 "Spanish": SpanishLocalizer,

 }

 

 return localizers[language]()

 

if __name__ == "__main__":

 

 f = Factory("French")

 e = Factory("English")

 s = Factory("Spanish")

 

 message = ["car", "bike", "cycle"]

 

 for msg in message:

 print(f.localize(msg))

 print(e.localize(msg))

 print(s.localize(msg))  
  
---  
  
 __

 __

### Class Diagram for Factory Method:

Let’s look at the class diagram considering the example of ride sharing.

![factory-pattern-class](https://media.geeksforgeeks.org/wp-
content/uploads/20200116150155/Factory-pattern-class.png)

Factory_pattern_class_diagrma

### Advantages of using Factory method:

  1. We can easily add the new types of products without disturbing the existing client code.
  2. Generally, tight coupling is being avoided between the products and the creator classes and objects.

### Disadvantages of using Factory method:

  1. To create a particluar concrete product object, client might have to sub-class the creator class.
  2. You end up with huge number of small files i.e, cluttering of the files.

### Applicability :

    1. In a Graphics system, depending upon the user’s input it can draw different shapes like Rectangle, Square, Circle, etc. But for the ease of both developers as well as the client, we can use the factory method to create the instance depending upon the user’s input. Then we don’t have to change the client code for adding a new shape.
    2. In a Hotel booking site, we can book a slot for 1 room, 2 rooms, 3 rooms, etc. Here user can input the number of rooms he wants to book. Using the factory method, we can create a factory class AnyRooms which will help us to create the instance depending upon the user’s input. Again we don’t have to change the client’s code for adding the new facility.

  
**Further read:** **Factory Pattern in C++**

