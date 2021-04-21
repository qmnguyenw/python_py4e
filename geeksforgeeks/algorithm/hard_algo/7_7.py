Print all paths from top left to bottom right in a matrix with four moves
allowed



The problem is to print all the possible paths from top left to bottom right
of an mXn matrix with the constraints that from each cell you can either move
up, right, left or down.

 **Examples:**

    
    
    **Input :**  
    1 2 3 
    4 5 6 
    **Output :**  
    1 2 3 6 
    1 2 5 6  
    1 4 5 6  
    4 5 2 3 6 
    
    **Input :**
    1 2 3
    4 5 6
    7 8 9
    **Output :**
    1 2 3 6 9 
    1 2 3 6 5 8 9 
    1 2 3 6 5 4 7 8 9 
    1 2 5 6 9 
    1 2 5 8 9 
    1 2 5 4 7 8 9 
    1 4 5 6 9 
    1 4 5 8 9 
    1 4 5 2 3 6 9 
    1 4 7 8 9 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem is mainly an extension of Count all paths from top left to bottom
right in a matrix with two moves allowed

The algorithm is a simple recursive algorithm, from each cell first print all
paths by going down and then print all paths by going right then print all
paths by going up then print all paths by going left. Do this recursively for
each cell encountered. There we will use Hash matrix for it will not repeat
the same path which already traversed.

Following is C++ implementation of the above algorithm.

 __

 __  
 __

 __

 __  
 __  
 __

// Print All path from top left to bottom right

#include <iostream>

#include <vector>

using namespace std;

 

// Function to print all path

void printAllPath(vector<vector<int> > vec, 

 vector<vector<int> > hash,

 int i, int j, vector<int> res = {})

{

 // check Condition

 if (i < 0 || j < 0 || i >= vec.size() || 

 j >= vec[0].size() || hash[i][j] == 1)

 return;

 

 // once it get the position (bottom right) 

 // than print the path

 if (i == vec.size() - 1 && j == vec[0].size() - 1) {

 

 // push the last element

 res.push_back(vec[i][j]);

 int k;

 

 // print the path

 for (k = 0; k < res.size(); k++)

 cout << res[k] << " ";

 

 cout << "\n";

 

 return;

 }

 

 // if the path is traverse already then

 // it will not go again the same path

 hash[i][j] = 1;

 

 // store the path

 res.push_back(vec[i][j]);

 

 // go to the right

 printAllPath(vec, hash, i, j + 1, res);

 

 // go to the down

 printAllPath(vec, hash, i + 1, j, res);

 

 // go to the up

 printAllPath(vec, hash, i - 1, j, res);

 

 // go to the left

 printAllPath(vec, hash, i, j - 1, res);

 

 // pop the last element

 res.pop_back();

 

 // hash position 0 for traverse another path

 hash[i][j] = 0;

}

 

// Driver code

int main()

{

 // Given matrix

 vector<vector<int> > vec = { { 1, 2, 3 },

 { 4, 5, 6 } };

 

 // mxn(2x3) 2d hash matrix

 vector<vector<int> > hash(2, vector<int>(3, 0));

 

 // print All Path of matrix

 printAllPath(vec, hash, 0, 0);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 3 6 
    1 2 5 6 
    1 4 5 6 
    1 4 5 2 3 6
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

