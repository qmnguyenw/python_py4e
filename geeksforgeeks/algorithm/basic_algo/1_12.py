Array of Vectors in C++ STL



 **Prerequisite:** Arrays in C++, Vector in C++ STL

An **array** is a collection of items stored at contiguous memory locations.
It is to store multiple items of the same type together. This makes it easier
to get access to the elements stored in it by the position of each element.

 **Vectors** are known as dynamic arrays with the ability to resize itself
automatically when an element is inserted or deleted, with their storage being
handled automatically by the container automatically.

Therefore, **array of vectors** is two dimensional array with fixed number of
rows where each row is vector of variable length. Each index of array stores a
vector which can be traversed and accessed using iterators.

 **Syntax:**

  

  

    
    
    vector <data_type> V[size];
    

**Example:**

    
    
    vector <int> A[5];
    where A is the array of vectors of int of size 5
    

_**Insertion:**_ Insertion in array of vectors is done using **push_back()**
function.

 **For Example:**

    
    
    for i in [0, n) {
      A[i].push_back(35)
    }
    

Above pseudo-code inserts element 35 at every index of **vector <int> A[n]**.

 _ **Traversal:**_ Traversal in an array of vectors is perform using
iterators.

 **For Example:**

    
    
    for i in [0, n) {
       for(iterator it = A[i].begin(); 
           it!=A[i].end(); it++) {
          print(*it)
        }
    }
    

Above pseudo-code traverses **vector <int> A[n]** at each index using starting
iterators **A[i].begin()** and ending iterator **A[i].end()**. For accessing
the element it uses **(*it)** as iterators are pointers pointing to elements
in **vector <int> A[n]**.

Below is the program to illustrate the insertion in the array of vectors.

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to illustrate

// array of vectors

 

#include <iostream>

#include <vector>

using namespace std;

 

// Declaring array of vectors

// globally

vector<int> v[5];

 

// Function for inserting elements

// in array of vectors

void insertionInArrayOfVectors()

{

 

 for (int i = 0; i < 5; i++) {

 

 // Inserting elements at every

 // row i using push_back()

 // function in vector

 for (int j = i + 1; j < 5; j++) {

 v[i].push_back(j);

 }

 }

}

 

// Function to print elements in array

// of vectors

void printElements()

{

 

 // Traversing of vectors v to print

 // elements stored in it

 for (int i = 0; i < 5; i++) {

 

 cout << "Elements at index "

 << i << ": ";

 

 // Displaying element at each column,

 // begin() is the starting iterator,

 // end() is the ending iterator

 for (auto it = v[i].begin();

 it != v[i].end(); it++) {

 

 // (*it) is used to get the

 // value at iterator is

 // pointing

 cout << *it << ' ';

 }

 cout << endl;

 }

}

 

// Function to illustrate array

// of vectors

void arrayOfVectors()

{

 // Inserting elements in array

 // of vectors

 insertionInArrayOfVectors();

 

 // Print elements stored in array

 // of vectors

 printElements();

}

 

// Driver code

int main()

{

 arrayOfVectors();

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Elements at index 0: 1 2 3 4 
    Elements at index 1: 2 3 4 
    Elements at index 2: 3 4 
    Elements at index 3: 4 
    Elements at index 4:
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

