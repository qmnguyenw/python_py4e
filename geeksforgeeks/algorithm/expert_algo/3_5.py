Ad-hoc, Inclusion, Parametric & Coercion Polymorphisms



When we talk about Polymorphism in C++, we come to hear the following four
types:  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/polymorphism.png)

Discussing these in details:

  1.  **Ad-hoc Polymorphism** , also called as **Overloading**

 **Ad-hoc Polymorphism allows functions having same name to act differently
for different types.** For example:  
The + operator adds two integers and concatenates two strings.  
![](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/adhocPolymorphism.png)

Above example could be better illustrated by invoking the function “sum()” in
under-mentioned code:

 __

 __  
 __

 __

 __  
 __  
 __

#include<iostream>

using namespace std;

 

int sum(int x, int y)

{

 int c = x + y;

 return c;

}

 

string sum(const char* x, const char* y)

{

 string summation(x);

 summation += y;

 return summation;

}

 

int main()

{

 cout << sum(50, 20)

 << " :- Integer addition Output\n";

 cout << sum("Polymorphism", " achieved")

 << " :- String Concatenation Output\n";

}  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    70 :- Integer addition Output
    Polymorphism achieved :- String Concatenation Output
    

