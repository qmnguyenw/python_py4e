Proto Van Emde Boas Tree | Set 2 | Construction



Van Emde Boas Tree supports search, minimum, maximum, successor, predecessor,
insert and delete operations in O(lglgN) time which is faster than any of
related data structures like priority queue, binary search tree, etc. Proto
Van Emde Boas tree is similar prototype type data structure but it fails to
achieve the complexity of O(lglgN), We will learn Proto Van Emde Boas tree
first to get a basic understanding of working of Van Emde Boas tree. Here N is
the size of the universe over which tree is defined.

 **Note:** Proto Van Emde Boas Data Structure’s keys must be defined over a
range of 0 to n(n is positive integer of the form 22k) and it works when
duplicate keys are not allowed.

 **Abbreviations:**

  1. Proto-VEB is an abbreviation of Proto-Van Emde Boas tree.
  2. Proto-VEB(![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png)) is an abbreviation for Proto-VEB containing u number of keys.

 **Basic Understanding of the structure of Proto-VEB Tree:**  
Proto Van Emde boas tree are recursively defined data structure and it shrinks
to sqrt size as we go up in the tree. Please refer this article to understand
the basics of it.

In Proto-VEB we use a bit array to represents whether a key is present or not,
we put 1 if it is present and 0 else.

  

  

Here, the summary of a particular cluster contains whether there is any key
present in a cluster if at least one key present then the summary is 1 or 0
elsewhere. Clusters are segments of a bit array. A summary is also a bit
array. See the image below:

![van emde boas tree basic structure](https://media.geeksforgeeks.org/wp-
content/uploads/20190722125627/akp.png)

 **Construction of Proto VEB Tree:**

Below image represents the basic Proto-VEB structure:

![Van Emde Boas Tree](https://media.geeksforgeeks.org/wp-
content/uploads/20190722115554/aa7.png)

The recursively defined structure has two main part:

  1.  **summary** : it is a pointer to Proto-VEB structure which has ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png) size.
  2.  **cluster:** it is an array of pointers to Proto-VEB structures with ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png) size.

First of all, we have to understand some function and keywords:

  1.  **universe size (u)** : Number of keys in Proto-VEB structure.
  2.  **High(x):** From the first image, we can see that if we want to reach at the cluster of the key then we can divide it with ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png).  
  
 _For example_ , We want to know the cluster of the key 12 then can divide it
with ![\\sqrt{16}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-77dc2b04d4e7733af22a663daa10bd93_l3.png) which is 3, so
key 12 is in 3rd cluster.

    
        High(x) = floor( x / ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png))

  3.  **low(x):** From the first image, we can see that if we want the position of the key in the cluster we can apply modulus operation x % ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png).  
  
 _For example_ , If you want to find a position of 7 in the cluster you can
apply 7 % ![\\sqrt{16}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-77dc2b04d4e7733af22a663daa10bd93_l3.png) = 3 which is a
position of 7 in 2nd cluster.

    
        low(x) = x % ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png))

 **Recursive Procedure of construction:**

  1. Base case : If universe size is 2 then it is a base size so there will be nomore summary array, means it is null and we will store only bit array for 2 keys.
  2. We will recursively assign summary as ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png) sized Proto-VEB tree and ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png)-sized Proto-VEB to all ![\\sqrt{u}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-051d62530e74ca945e59a24327076a8b_l3.png) clusters.

See u=4 Proto-VEB structure in the image below:  
![VEB](https://media.geeksforgeeks.org/wp-
content/uploads/20190723004621/ch3.png)  
Here is the code representing the Algorithm:

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

class Proto_Van_Emde_Boas {

public:

 // Total number of keys

 int universe_size;

 

 // Summary

 Proto_Van_Emde_Boas* summary;

 

 // Clusters array of Proto-VEB pointers

 vector<Proto_Van_Emde_Boas*> clusters;

 

 int root(int u)

 {

 return int(sqrt(u));

 }

 

 // Function to return cluster numbers

 // in which key is present

 int high(int x)

 {

 return x / root(universe_size);

 }

 

 // Function to return the position

 // of x in cluster

 int low(int x)

 {

 return x % root(universe_size);

 }

 

 // Function to return index form

 // cluster number and position

 int generate_index(int cluster, int position)

 {

 return cluster * root(universe_size) + position;

 }

 

 // Constructor

 Proto_Van_Emde_Boas(int size)

 {

 universe_size = size;

 

 // Base case

 if (size <= 2) {

 

 // Set summary to nullptr as there is no

 // more summary for size 2

 summary = nullptr;

 

 // Vector of two pointers

 // nullptr in starting

 clusters = vector<Proto_Van_Emde_Boas*>(size, nullptr);

 }

 else {

 

 // Assiging Proto-VEB(sqrt(u)) to summary

 summary = new Proto_Van_Emde_Boas(root(size));

 

 // Creating array of Proto-VEB Tree pointers of size sqrt(u)

 // first all nullptrs are going to assign

 clusters = vector<Proto_Van_Emde_Boas*>(root(size), nullptr);

 

 // Assigning Proto-VEB(sqrt(u)) to all its clusters

 for (int i = 0; i < root(size); i++) {

 clusters[i] = new Proto_Van_Emde_Boas(root(size));

 }

 }

 }

};

 

// Driver code

int main()

{

 Proto_Van_Emde_Boas pveb(4);

}  
  
---  
  
 __

 __

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

