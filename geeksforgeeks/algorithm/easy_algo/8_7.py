Translation of objects in computer graphics



In computer graphics, we have seen how to draw some basic figures like line
and circles. In this post we will discuss on basics of an important operation
in computer graphics as well as 2-D geometry, which is **transformation**.  
In computer graphics, transformation of the coordinates consists of three
major processes:

  * Translation
  * Rotation
  * Scaling

In this post we will discuss about **translation** only.

 **What is translation?**

A translation process moves every point a constant distance in a specified
direction. It can be described as a rigid motion. A translation can also be
interpreted as the addition of a constant vector to every point, or as
shifting the origin of the coordinate system.  
Suppose, If point (X, Y) is to be translated by amount Dx and Dy to a new
location (X’, Y’) then new coordinates can be obtained by adding Dx to X and
Dy to Y as:

    
    
    X' = Dx + X
    Y' = Dy + Y
    
    or P' = T + P where
    
    P' = (X', Y'),
    T = (Dx, Dy ),
    P = (X, Y)
    

Here, P(X, Y) is the original point. T(Dx, Dy) is the **translation factor** ,
i.e. the amount by which the point will be translated. P'(X’, Y’) is the
coordinates of point P after translation.  
Examples:

  

  

    
    
    Input : P[] = {5, 6}, T = {1, 1}
    Output : P'[] = {6, 7}
    
    Input : P[] = {8, 6}, T = {-1, -1}
    Output : P'[] = {7, 5}
    

Whenever we perform translation of any object we simply translate its each and
every point. Some of basic objects along with their translation can be drawn
as:

  1.  **Point Translation P(X, Y) :** Here we only translate the x and y coordinates of given point as per given translation factor dx and dy respectively.  
Below is the C++ program to translate a point:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for translation

// of a single coordinate

#include<bits/stdc++.h>

#include<graphics.h>

 

using namespace std;

 

// function to translate point

void translatePoint ( int P[], int T[])

{

 /* init graph and putpixel are used for 

 representing coordinates through graphical 

 functions 

 */

 int gd = DETECT, gm, errorcode;

 initgraph (&gd;, &gm;, "c:\\tc\\bgi"); 

 

 cout<<"Original Coordinates :"<<P[0]<<","<<P[1];

 

 putpixel (P[0], P[1], 1);

 

 // calculating translated coordinates

 P[0] = P[0] + T[0];

 P[1] = P[1] + T[1];

 

 cout<<"\nTranslated Coordinates :"<< P[0]<<","<< P[1];

 

 // Draw new coordinatses

 putpixel (P[0], P[1], 3);

 closegraph();

}

 

// driver program

int main()

{

 int P[2] = {5, 8}; // coordinates of point

 int T[] = {2, 1}; // translation factor

 translatePoint (P, T);

 return 0;

}   
  
---  
  
__

__

Output:

    
    
    Original Coordinates : 5, 8
    Translated Coordinates : 7, 9
    

  2. **Line Translation:** The idea to translate a line is to translate both of the end points of the line by the given translation factor(dx, dy) and then draw a new line with inbuilt graphics function.  
Below is the C++ implementation of above idea:

 __

 __  
 __

 __

 __  
 __  
 __

// cpp program for translation

// of a single line

#include<bits/stdc++.h>

#include<graphics.h>

 

using namespace std;

 

// function to translate line

void translateLine ( int P[][2], int T[])

{

 /* init graph and line() are used for 

 representing line through graphical

 functions 

 */

 int gd = DETECT, gm, errorcode;

 initgraph (&gd;, &gm;, "c:\\tc\\bgi"); 

 

 // drawing original line using graphics functions

 setcolor (2);

 line(P[0][0], P[0][1], P[1][0], P[1][1]);

 

 // calculating translated coordinates

 P[0][0] = P[0][0] + T[0];

 P[0][1] = P[0][1] + T[1];

 P[1][0] = P[1][0] + T[0];

 P[1][1] = P[1][1] + T[1];

 

 // drawing translated line using graphics functions

 setcolor(3);

 line(P[0][0], P[0][1], P[1][0], P[1][1]);

 closegraph();

}

 

// driver program

int main()

{

 int P[2][2] = {5, 8, 12, 18}; // coordinates of point

 int T[] = {2, 1}; // translation factor

 translateLine (P, T);

 return 0;

}   
  
---  
  
__

__

**Output** :  
![translation 1](https://media.geeksforgeeks.org/wp-
content/uploads/translation-1.bmp)

  3.  **Rectangle Translation :** Here we translate the x and y coordinates of both given points A(top left ) and B(bottom right) as per given translation factor dx and dy respectively and then draw a rectangle with inbuilt graphics function

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for translation

// of a rectangle

#include<bits/stdc++.h>

#include<graphics.h>

using namespace std;

 

// function to translate rectangle

void translateRectangle ( int P[][2], int T[])

{

 /* init graph and rectangle() are used for 

 representing rectangle through graphical functions */

 int gd = DETECT, gm, errorcode;

 initgraph (&gd;, &gm;, "c:\\tc\\bgi"); 

 setcolor (2);

 // rectangle (Xmin, Ymin, Xmax, Ymax)

 // original rectangle

 rectangle (P[0][0], P[0][1], P[1][0], P[1][1]);

 

 // calculating translated coordinates

 P[0][0] = P[0][0] + T[0];

 P[0][1] = P[0][1] + T[1];

 P[1][0] = P[1][0] + T[0];

 P[1][1] = P[1][1] + T[1];

 

 // translated rectangle (Xmin, Ymin, Xmax, Ymax)

 // setcolor(3);

 rectangle (P[0][0], P[0][1], P[1][0], P[1][1]);

 // closegraph();

}

 

// driver program

int main()

{

 // Xmin, Ymin, Xmax, Ymax as rectangle

 // coordinates of top left and bottom right points

 int P[2][2] = {5, 8, 12, 18};

 int T[] = {2, 1}; // translation factor

 translateRectangle (P, T);

 return 0;

}   
  
---  
  
__

__

**Output** :  
![translation 2](https://media.geeksforgeeks.org/wp-
content/uploads/translation-2.bmp)

References : http://math.hws.edu/graphicsbook/.

This article is contributed by **Shivam Pradhan (anuj_charm)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

