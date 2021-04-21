Find alphabet in a Matrix which has maximum number of stars around it



Given a matrix **mat** consisting of ***** and lowercase English alphabets,
the task is to find the character which has the maximum number of ***** around
it (including diagonal elements too). If two characters have same maximum
count, print lexicographically smallest character.  
 **Source** :D-E Shaw Interview Experience  
 **Examples:**  

    
    
    **Input:** 
    mat[][] = {{'b', '*', '*', '*'}, 
               {'*', '*', 'c', '*'}, 
               {'*', 'a', '*', '*'}, 
               {'*', '*', '*', 'd'}}
    **Output:** a
    'a', 'b', 'c' and 'd' are surrounded by 
    '7', '3', '7' and '3' stars respectively.
    'a' and 'c' are surrounded by maximum stars 
    but 'a' is lexicographically smaller than 'c'.
    
    **Input:** 
    mat[][] = {{'*', 'r', '*', '*'}, 
               {'m', 'a', 'z', '*'}, 
               {'l', '*', 'f', 'k'}, 
               {'*', '*', '*', 'd'} }
    **Output:** f

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** The idea is to traverse the matrix and if a character is found
then calculate the count of stars around it. Check at all 8 positions around
it and count the number of starts.  
Use a map to keep track of the character and the number of stars surrounding
it. Then traverse the map and find the character which is surrounded by
maximum stars and is lexicographically smallest.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find alphabet in a Matrix

// which has maximum number of stars

// surrounding it

#include <bits/stdc++.h>

using namespace std;

// Function to return the count of stars

// around a particular index

int countStars(int mat[][4], int i, int j, int n)

{

 int count = 0;

 int rowNum[] = { -1, -1, -1, 0, 0, 1, 1, 1 };

 int colNum[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

 // consider all 8 neighbours

 for (int k = 0; k < 8; k++) {

 int x = i + rowNum[k];

 int y = j + colNum[k];

 if (x >= 0 && x < n && y >= 0 && y < n

 && mat[x][y] == '*')

 count++;

 }

 return count;

}

// Function to return the character in a Matrix

// which has maximum number of stars around it

char alphabetWithMaxStars(int mat[][4], int n)

{

 unordered_map<char, int> umap;

 for (int i = 0; i < n; i++) {

 for (int j = 0; j < n; j++) {

 // If current element is a character

 if ((mat[i][j] - 97) >= 0

 && (mat[i][j] - 97) < 26) {

 // Count of start surrounding it

 int stars = countStars(mat, i, j, n);

 umap[mat[i][j]] = stars;

 }

 }

 }

 int max = -1;

 char result = 'z' + 1;

 // Traverse the map

 for (auto x : umap) {

 if (x.second > max || (x.second == max

 && x.first < result)) {

 max = x.second;

 result = x.first;

 }

 }

 return result;

}

// Driver code

int main()

{

 int mat[][4] = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 int n = 4;

 cout << alphabetWithMaxStars(mat, n);

 return 0;

}  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program to find alphabet in a Matrix

// which has maximum number of stars

// surrounding it

import java.util.*;

class GFG

{

// Function to return the count of stars

// around a particular index

static int countStars(int mat[][], int i, int j, int n)

{

 int count = 0;

 int rowNum[] = { -1, -1, -1, 0, 0, 1, 1,
1 };

 int colNum[] = { -1, 0, 1, -1, 1, -1, 0,
1 };

 // consider all 8 neighbours

 for (int k = 0; k < 8; k++)

 {

 int x = i + rowNum[k];

 int y = j + colNum[k];

 if (x >= 0 && x < n && y >= 0 && y < n

 && mat[x][y] == '*')

 count++;

 }

 return count;

}

// Function to return the character in a Matrix

// which has maximum number of stars around it

static char alphabetWithMaxStars(int mat[][], int n)

{

 HashMap<Character,Integer> umap =

 new HashMap<Character,Integer>();

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // If current element is a character

 if ((mat[i][j] - 97) >= 0

 && (mat[i][j] - 97) < 26)

 {

 

 // Count of start surrounding it

 int stars = countStars(mat, i, j, n);

 umap.put((char)mat[i][j], stars);

 }

 }

 }

 int max = -1;

 char result = 'z' + 1;

 // Traverse the map

 for (Map.Entry<Character,Integer> x : umap.entrySet())

 {

 if (x.getValue() > max || (x.getValue() == max

 && x.getKey() < result))

 {

 max = x.getValue();

 result = x.getKey();

 }

 }

 return result;

}

// Driver code

public static void main(String[] args)

{

 int mat[][] = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 int n = 4;

 System.out.print(alphabetWithMaxStars(mat, n));

}

}

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find alphabet in a

# Matrix which has maximum number of stars

# surrounding it

import math as mt

# Function to return the count of stars

# around a particular index

def countStars(mat, i, j, n):

 count = 0

 rowNum = [-1, -1, -1, 0, 0, 1, 1,
1 ]

 colNum = [-1, 0, 1, -1, 1, -1, 0,
1 ]

 # consider all 8 neighbours

 for k in range(8):

 x = i + rowNum[k]

 y = j + colNum[k]

 if (x >= 0 and x < n and y >= 0 and

 y < n and mat[x][y] == '*'):

 count += 1

 

 return count

# Function to return the character in a Matrix

# which has maximum number of stars around it

def alphabetWithMaxStars(mat, n):

 umap = dict()

 for i in range(n):

 for j in range(n):

 # If current element is a character

 if ((ord(mat[i][j]) - 97) >= 0 and

 (ord(mat[i][j]) - 97) < 26):

 # Count of start surrounding it

 stars = countStars(mat, i, j, n)

 umap[mat[i][j]] = stars

 

 Max = -1

 result = chr(ord('z') + 1)

 # Traverse the map

 for x in umap:

 if (umap[x] > Max or

 (umap[x] == Max and x < result)):

 Max = umap[x]

 result = x

 

 return result

# Driver code

mat = [[ 'b', '*', '*', '*' ],

 [ '*', '*', 'c', '*' ],

 [ '*', 'a', '*', '*' ],

 [ '*', '*', '*', 'd' ]]

n = 4

print(alphabetWithMaxStars(mat, n))

# This code is contributed by

# Mohit kumar 29  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# program to find alphabet in a Matrix

// which has maximum number of stars

// surrounding it

using System;

using System.Collections.Generic;

class GFG

{

// Function to return the count of stars

// around a particular index

static int countStars(int [,]mat, int i, int j, int n)

{

 int count = 0;

 int []rowNum = { -1, -1, -1, 0, 0, 1, 1, 1 };

 int []colNum = { -1, 0, 1, -1, 1, -1, 0, 1 };

 // consider all 8 neighbours

 for (int k = 0; k < 8; k++)

 {

 int x = i + rowNum[k];

 int y = j + colNum[k];

 if (x >= 0 && x < n && y >= 0 && y < n

 && mat[x, y] == '*')

 count++;

 }

 return count;

}

// Function to return the character in a Matrix

// which has maximum number of stars around it

static char alphabetWithMaxStars(int [,]mat, int n)

{

 Dictionary<char,int> umap =

 new Dictionary<char,int>();

 for (int i = 0; i < n; i++)

 {

 for (int j = 0; j < n; j++)

 {

 // If current element is a character

 if ((mat[i, j] - 97) >= 0

 && (mat[i, j] - 97) < 26)

 {

 

 // Count of start surrounding it

 int stars = countStars(mat, i, j, n);

 if(umap.ContainsKey((char)mat[i,j]))

 umap[(char)mat[i,j]] = stars;

 else

 umap.Add((char)mat[i,j], stars);

 }

 }

 }

 int max = -1;

 char result = (char)('z' + 1);

 // Traverse the map

 foreach(KeyValuePair<char, int> x in umap)

 {

 if (x.Value > max || (x.Value == max

 && x.Key < result))

 {

 max = x.Value;

 result = x.Key;

 }

 }

 return result;

}

// Driver code

public static void Main(String[] args)

{

 int [,]mat = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 int n = 4;

 Console.Write(alphabetWithMaxStars(mat, n));

}

}

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    a

**Another approach:**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find alphabet in a Matrix

// which has maximum number of stars

// surrounding it

#include <bits/stdc++.h>

using namespace std;

/**

 * Counts the number of stars around the letter at position i,j

 * start at position max(i-1,0),max(j-1,0) and iterate the 3*3 mini matrix

 * while watching out the boundaries of

 * our main matrix. 

 * @param i

 * @param j

 * @param mat

 * @return

 */

int countStars(int i, int j, vector<vector<char>> mat)

{

 int initialRow = i != 0 ? i - 1 : i;

 int initialCol = j != 0 ? j - 1 : j;

 int stars = 0;

 for (int row=initialRow;(row <= i + 1) &&

 row < mat.size() ; row++)

 {

 for (int col=initialCol;(col <= j + 1) &&

 col < mat.size() ; col++)

 {

 if (mat[row][col] == '*')

 {

 stars++;

 }

 }

 }

 return stars;

}

// Function to return the character in a Matrix

// which has maximum number of stars around it

char getStarredLetter (vector<vector<char>> mat)

{

 char currentSuperStar = 'a';

 int currentFans = 0;

 for (int i = 0 ; i < mat.size() ; i++)

 {

 vector<char> row = mat[i];

 for (int j = 0 ; j < row.size(); j++)

 {

 char currentChar = row[j];

 if (currentChar != '*')

 {

 // Count of start surrounding it

 int fans = countStars(i, j, mat);

 if (fans > currentFans)

 {

 currentSuperStar = currentChar;

 currentFans = fans;

 }

 else if(fans == currentFans &&

 currentChar < currentSuperStar)

 {

 currentSuperStar = currentChar;

 }

 }

 }

 }

 return currentSuperStar;

}

// Driver Code

int main()

{

 vector<vector<char>> mat = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 cout << getStarredLetter(mat);

 return 0;

}

// This code is contributed by rag2127.  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program to find alphabet in a Matrix

// which has maximum number of stars

// surrounding it

public class SuperStarLetter {

 

 // Function to return the character in a Matrix

 // which has maximum number of stars around it

 private static char getStarredLetter (char[][] mat) {

 char currentSuperStar = 'a';

 int currentFans = 0;

 for (int i=0 ; i < mat.length ; i++) {

 char[] row = mat[i];

 for (int j = 0 ; j < row.length; j++) {

 char currentChar = row[j];

 if (currentChar != '*') {

 

 // Count of start surrounding it

 int fans = countStars(i, j, mat);

 if (fans > currentFans) {

 currentSuperStar = currentChar;

 currentFans = fans;

 } else if (fans == currentFans &&

 currentChar < currentSuperStar) {

 currentSuperStar = currentChar;

 }

 }

 }

 }

 return currentSuperStar;

 }

 /**

 * Counts the number of stars around the letter at position i,j

 * start at position max(i-1,0),max(j-1,0) and iterate the 3*3 mini matrix

 * while watching out the boundaries of

 * our main matrix.

 * @param i

 * @param j

 * @param mat

 * @return

 */

 private static int countStars(int i, int j, char[][]
mat) {

 int initialRow = i != 0 ? i-1 : i;

 int initialCol = j != 0 ? j-1 : j;

 int stars= 0;

 for (int row=initialRow;(row <= i+1) && row < mat.length ;
row++) {

 for (int col=initialCol;(col <= j+1) && col < mat.length ;
col++) {

 if (mat[row][col] == '*') {

 stars++;

 }

 }

 }

 return stars;

 }

 //Driver Code

 public static void main(String[] args) {

 char[][] mat = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 System.out.println(getStarredLetter(mat));

 

 }

}  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find alphabet

# in a Matrix which has maximum

# number of stars surrounding it

# Function to return the character

# in a Matrix which has maximum

# number of stars around it

def getStarredLetter (mat) :

 currentSuperStar = 'a'

 currentFans = 0

 for i in range(len(mat)) :

 row = mat[i]

 

 for j in range(len(row)) :

 

 currentChar = row[j]

 if (currentChar != '*') :

 

 # Count of start surrounding it

 fans = countStars(i, j, mat)

 if (fans > currentFans) :

 currentSuperStar = currentChar

 currentFans = fans

 

 elif (fans == currentFans and

 currentChar < currentSuperStar) :

 currentSuperStar = currentChar;

 

 return currentSuperStar;

 

"""

 * Counts the number of stars around the

 * letter at position i,j start at position

 * max(i-1,0),max(j-1,0) and iterate the 3*3

 * mini matrix while watching out the boundaries

 * of our main matrix.

 * @param i

 * @param j

 * @param mat

 * @return

"""

def countStars(i, j, mat) :

 

 if i != 0 :

 initialRow = i - 1

 else :

 initialRow = i

 

 

 if j != 0 :

 initialCol = j - 1

 else :

 initialCol = j

 

 stars = 0

 

 row = initialRow

 

 while ((row <= i + 1) and (row < len(mat))):

 col = initialCol

 while ((col <= j + 1) and (col < len(mat))):

 if (mat[row][col] == '*') :

 

 stars += 1

 

 col += 1

 

 row += 1

 

 return stars

 

# Driver Code

if __name__ == "__main__" :

 

 mat = [ [ 'b', '*', '*', '*' ],

 [ '*', '*', 'c', '*' ],

 [ '*', 'a', '*', '*' ],

 [ '*', '*', '*', 'd' ] ]

 

 print(getStarredLetter(mat))

 

# This code is contributed by Ryugaa  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# program to find row with

// max sum in a matrix

using System;

public class SuperStarLetter

{

 

 // Function to return the character in a Matrix

 // which has maximum number of stars around it

 private static char getStarredLetter (char[,] mat)

 {

 char currentSuperStar = 'a';

 int currentFans = 0;

 for (int i = 0 ; i < mat.GetLength(0) ; i++)

 {

 char[] row = GetRow(mat, i);

 for (int j = 0 ; j < row.Length; j++)

 {

 char currentChar = row[j];

 if (currentChar != '*')

 {

 

 // Count of start surrounding it

 int fans = countStars(i, j, mat);

 if (fans > currentFans)

 {

 currentSuperStar = currentChar;

 currentFans = fans;

 }

 else if (fans == currentFans &&

 currentChar < currentSuperStar)

 {

 currentSuperStar = currentChar;

 }

 }

 }

 }

 return currentSuperStar;

 }

 

public static char[] GetRow(char[,] matrix, int row)

{

 var rowLength = matrix.GetLength(1);

 var rowVector = new char[rowLength];

 for (var i = 0; i < rowLength; i++)

 rowVector[i] = matrix[row, i];

 return rowVector;

}

 /**

 * Counts the number of stars around the letter at position i,j

 * start at position max(i-1,0),max(j-1,0) and iterate the 3*3 mini matrix

 * while watching out the boundaries of

 * our main matrix.

 * @param i

 * @param j

 * @param mat

 * @return

 */

 private static int countStars(int i, int j, char[,]
mat)

 {

 int initialRow = i != 0 ? i-1 : i;

 int initialCol = j != 0 ? j-1 : j;

 int stars= 0;

 for (int row = initialRow;(row <= i+1) && row < mat.GetLength(0) ;
row++)

 {

 for (int col=initialCol;(col <= j+1) && col < mat.GetLength(1);
col++)

 {

 if (mat[row,col] == '*')

 {

 stars++;

 }

 }

 }

 return stars;

 }

 

 // Driver Code

 public static void Main(String[] args)

 {

 char[,] mat = { { 'b', '*', '*', '*' },

 { '*', '*', 'c', '*' },

 { '*', 'a', '*', '*' },

 { '*', '*', '*', 'd' } };

 Console.WriteLine(getStarredLetter(mat));

 

 }

}

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    a

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

