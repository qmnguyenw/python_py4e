Rail Fence Cipher – Encryption and Decryption



Given a plain-text message and a numeric key, cipher/de-cipher the given text
using Rail Fence algorithm.  
The rail fence cipher (also called a zigzag cipher) is a form of transposition
cipher. It derives its name from the way in which it is encoded.  
 **Examples:**

    
    
    **Encryption**
    Input :  "GeeksforGeeks "
    Key = 3
    Output : GsGsekfrek eoe
    **Decryption**
    Input : GsGsekfrek eoe
    Key = 3
    Output :  "GeeksforGeeks "
    
    **Encryption**
    Input :  "defend the east wall"
    Key = 3
    Output : dnhaweedtees alf  tl
    **Decryption**
    Input : dnhaweedtees alf  tl
    Key = 3
    Output : defend the east wall
    
    **Encryption**
    Input : "attack at once"
    Key = 2 
    Output : atc toctaka ne 
    **Decryption**
    Input : "atc toctaka ne"
    Key = 2
    Output : attack at once
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Encryption**

In a transposition cipher, the order of the alphabets is re-arranged to obtain
the cipher-text.

  * In the rail fence cipher, the plain-text is written downwards and diagonally on successive rails of an imaginary fence.
  * When we reach the bottom rail, we traverse upwards moving diagonally, after reaching the top rail, the direction is changed again. Thus the alphabets of the message are written in a zig-zag manner.
  * After each alphabet has been written, the individual rows are combined to obtain the cipher-text.

For example, if the message is “GeeksforGeeks” and the number of rails = 3
then cipher is prepared as:  
![Rail Fence Algorithm](https://media.geeksforgeeks.org/wp-
content/uploads/Untitled1.jpg)

  

  

 **Decryption**

As we’ve seen earlier, the number of columns in rail fence cipher remains
equal to the length of plain-text message. And the key corresponds to the
number of rails.

  * Hence, rail matrix can be constructed accordingly. Once we’ve got the matrix we can figure-out the spots where texts should be placed (using the same way of moving diagonally up and down alternatively ).
  * Then, we fill the cipher-text row wise. After filling it, we traverse the matrix in zig-zag manner to obtain the original text.

Implementation:  
Let cipher-text = “GsGsekfrek eoe” , and Key = 3

  * Number of columns in matrix = len(cipher-text) = 12
  * Number of rows = key = 3

Hence original matrix will be of 3*12 , now marking places with text as ‘*’ we
get

    
    
    * _ _ _ * _ _ _ * _ _ _ *
    _ * _ * _ * _ * _ * _ * 
    _ _ * _ _ _ *  _ _ _ * _ 
    

Below is a program to encrypt/decrypt the message using the above algorithm.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to illustrate Rail Fence Cipher

// Encryption and Decryption

#include <bits/stdc++.h>

using namespace std;

 

// function to encrypt a message

string encryptRailFence(string text, int key)

{

 // create the matrix to cipher plain text

 // key = rows , length(text) = columns

 char rail[key][(text.length())];

 

 // filling the rail matrix to distinguish filled

 // spaces from blank ones

 for (int i=0; i < key; i++)

 for (int j = 0; j < text.length(); j++)

 rail[i][j] = '\n';

 

 // to find the direction

 bool dir_down = false;

 int row = 0, col = 0;

 

 for (int i=0; i < text.length(); i++)

 {

 // check the direction of flow

 // reverse the direction if we've just

 // filled the top or bottom rail

 if (row == 0 || row == key-1)

 dir_down = !dir_down;

 

 // fill the corresponding alphabet

 rail[row][col++] = text[i];

 

 // find the next row using direction flag

 dir_down?row++ : row--;

 }

 

 //now we can construct the cipher using the rail matrix

 string result;

 for (int i=0; i < key; i++)

 for (int j=0; j < text.length(); j++)

 if (rail[i][j]!='\n')

 result.push_back(rail[i][j]);

 

 return result;

}

 

// This function receives cipher-text and key

// and returns the original text after decryption

string decryptRailFence(string cipher, int key)

{

 // create the matrix to cipher plain text

 // key = rows , length(text) = columns

 char rail[key][cipher.length()];

 

 // filling the rail matrix to distinguish filled

 // spaces from blank ones

 for (int i=0; i < key; i++)

 for (int j=0; j < cipher.length(); j++)

 rail[i][j] = '\n';

 

 // to find the direction

 bool dir_down;

 

 int row = 0, col = 0;

 

 // mark the places with '*'

 for (int i=0; i < cipher.length(); i++)

 {

 // check the direction of flow

 if (row == 0)

 dir_down = true;

 if (row == key-1)

 dir_down = false;

 

 // place the marker

 rail[row][col++] = '*';

 

 // find the next row using direction flag

 dir_down?row++ : row--;

 }

 

 // now we can construct the fill the rail matrix

 int index = 0;

 for (int i=0; i<key; i++)

 for (int j=0; j<cipher.length(); j++)

 if (rail[i][j] == '*' && index<cipher.length())

 rail[i][j] = cipher[index++];

 

 

 // now read the matrix in zig-zag manner to construct

 // the resultant text

 string result;

 

 row = 0, col = 0;

 for (int i=0; i< cipher.length(); i++)

 {

 // check the direction of flow

 if (row == 0)

 dir_down = true;

 if (row == key-1)

 dir_down = false;

 

 // place the marker

 if (rail[row][col] != '*')

 result.push_back(rail[row][col++]);

 

 // find the next row using direction flag

 dir_down?row++: row--;

 }

 return result;

}

 

//driver program to check the above functions

int main()

{

 cout << encryptRailFence("attack at once", 2) << endl;

 cout << encryptRailFence("GeeksforGeeks ", 3) << endl;

 cout << encryptRailFence("defend the east wall", 3) << endl;

 

 //Now decryption of the same cipher-text

 cout << decryptRailFence("GsGsekfrek eoe",3) << endl;

 cout << decryptRailFence("atc toctaka ne",2) << endl;

 cout << decryptRailFence("dnhaweedtees alf tl",3) << endl;

 

 return 0;

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

# Python3 program to illustrate

# Rail Fence Cipher Encryption

# and Decryption

 

# function to encrypt a message

def encryptRailFence(text, key):

 

 # create the matrix to cipher 

 # plain text key = rows , 

 # length(text) = columns

 # filling the rail matrix 

 # to distinguish filled 

 # spaces from blank ones

 rail = [['\n' for i in range(len(text))]

 for j in range(key)]

 

 # to find the direction

 dir_down = False

 row, col = 0, 0

 

 for i in range(len(text)):

 

 # check the direction of flow

 # reverse the direction if we've just

 # filled the top or bottom rail

 if (row == 0) or (row == key - 1):

 dir_down = not dir_down

 

 # fill the corresponding alphabet

 rail[row][col] = text[i]

 col += 1

 

 # find the next row using

 # direction flag

 if dir_down:

 row += 1

 else:

 row -= 1

 # now we can construct the cipher 

 # using the rail matrix

 result = []

 for i in range(key):

 for j in range(len(text)):

 if rail[i][j] != '\n':

 result.append(rail[i][j])

 return("" . join(result))

 

# This function receives cipher-text 

# and key and returns the original 

# text after decryption

def decryptRailFence(cipher, key):

 

 # create the matrix to cipher 

 # plain text key = rows , 

 # length(text) = columns

 # filling the rail matrix to 

 # distinguish filled spaces

 # from blank ones

 rail = [['\n' for i in range(len(cipher))] 

 for j in range(key)]

 

 # to find the direction

 dir_down = None

 row, col = 0, 0

 

 # mark the places with '*'

 for i in range(len(cipher)):

 if row == 0:

 dir_down = True

 if row == key - 1:

 dir_down = False

 

 # place the marker

 rail[row][col] = '*'

 col += 1

 

 # find the next row 

 # using direction flag

 if dir_down:

 row += 1

 else:

 row -= 1

 

 # now we can construct the 

 # fill the rail matrix

 index = 0

 for i in range(key):

 for j in range(len(cipher)):

 if ((rail[i][j] == '*') and

 (index < len(cipher))):

 rail[i][j] = cipher[index]

 index += 1

 

 # now read the matrix in 

 # zig-zag manner to construct

 # the resultant text

 result = []

 row, col = 0, 0

 for i in range(len(cipher)):

 

 # check the direction of flow

 if row == 0:

 dir_down = True

 if row == key-1:

 dir_down = False

 

 # place the marker

 if (rail[row][col] != '*'):

 result.append(rail[row][col])

 col += 1

 

 # find the next row using

 # direction flag

 if dir_down:

 row += 1

 else:

 row -= 1

 return("".join(result))

 

# Driver code

if __name__ == "__main__":

 print(encryptRailFence("attack at once", 2))

 print(encryptRailFence("GeeksforGeeks ", 3))

 print(encryptRailFence("defend the east wall", 3))

 

 # Now decryption of the

 # same cipher-text

 print(decryptRailFence("GsGsekfrek eoe", 3))

 print(decryptRailFence("atc toctaka ne", 2))

 print(decryptRailFence("dnhaweedtees alf tl", 3))

 

# This code is contributed 

# by Pratik Somwanshi  
  
---  
  
 __

 __

 **Output:**

    
    
    atc toctaka ne
    GsGsekfrek eoe
    dnhaweedtees alf  tl
    GeeksforGeeks 
    attack at once
    delendfthe east wal
    

**  
References:**  
https://en.wikipedia.org/wiki/Rail_fence_cipher

This article is contributed by **Ashutosh Kumar** If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

