multimap clear() function in C++ STL



The multimap clear() function is an inbuilt function in C++ STL which is used
to remove all elements from the multimap container (which are destroyed),
leaving the container with a size of 0.

 **Syntax :**

    
    
    mymultimap_name.clear()
    

**Parameters** : This function does not take any arguments.

 **Return Value** : This function does not returns anything. The return type
of the function is void. It just empties the whole container.

Below program illustrate the multimap::clear() function in C++:

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to illustrate the

// multimap::clear() function

 

#include <cstring>

#include <iostream>

#include <map>

 

using namespace std;

 

int main()

{

 // Creating multimap of string and int

 multimap<string, int> mymultimap;

 

 // Inserting 3 Items with their value

 // using insert function

 mymultimap.insert(pair<string, int>("Item1", 10));

 mymultimap.insert(pair<string, int>("Item2", 20));

 mymultimap.insert(pair<string, int>("Item3", 30));

 

 cout << "Size of the multimap before using "

 << "clear function : ";

 cout << mymultimap.size() << '\n';

 

 // Removing all the elements

 // present in the multimap

 mymultimap.clear();

 

 cout << "Size of the multimap after using"

 << " clear function : ";

 cout << mymultimap.size() << '\n';

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of the multimap before using clear function : 3
    Size of the multimap after using clear function : 0
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

