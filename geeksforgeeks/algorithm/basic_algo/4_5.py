Point Clipping Algorithm in Computer Graphics



 **Clipping:** In computer graphics our screen act as a 2-D coordinate system.
it is not necessary that each and every point can be viewed on our viewing
pane(i.e. our computer screen). We can view points, which lie in particular
range (0,0) and (Xmax, Ymax). So, clipping is a procedure that identifies
those portions of a picture that are either inside or outside of our viewing
pane.  
In case of point clipping, we only show/print points on our window which are
in range of our viewing pane, others points which are outside the range are
discarded.  
 **Example**

    
    
    Input :
     ![clip 2](https://media.geeksforgeeks.org/wp-content/uploads/clip-2.jpg)
    Output :
    ![clip 3](https://media.geeksforgeeks.org/wp-content/uploads/clip-3.jpg)
    

**Point Clipping Algorithm:**

  1. Get the minimum and maximum coordinates of both viewing pane.
  2. Get the coordinates for a point.
  3. Check whether given input lies between minimum and maximum coordinate of viewing pane.
  4. If yes display the point which lies inside the region otherwise discard it.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for point clipping Algorithm

#include <bits/stdc++.h> 

using namespace std;

 

// Function for point clipping 

void pointClip(int XY[][2], int n, int Xmin, int Ymin, 

 int Xmax, int Ymax) 

{ 

 /*************** Code for graphics view 

 // initialize graphics mode 

 detectgraph(&gm;,&gr;); 

 initgraph(&gm;,&gr;,"d:\\tc\\BGI"); 

 for (int i=0; i<n; i++) 

 { 

 if ( (XY[i][0] >= Xmin) && (XY[i][0] <= Xmax)) 

 { 

 if ( (XY[i][1] >= Ymin) && (XY[i][1] <= Ymax)) 

 putpixel(XY[i][0],XY[i][1],3); 

 } 

 } 

 **********************/

 /**** Arithmetic view ****/

 cout << "Point inside the viewing pane:" << endl; 

 for (int i = 0; i < n; i++) 

 { 

 if ((XY[i][0] >= Xmin) && (XY[i][0] <= Xmax)) 

 { 

 if ((XY[i][1] >= Ymin) && (XY[i][1] <= Ymax)) 

 cout <<"[" << XY[i][0] <<","<<XY[i][1]<<"] "; 

 } 

 } 

 

 // print point coordinate outside viewing pane 

 cout<<"\n"<< endl;

 cout << "Point outside the viewing pane:"<<endl; 

 for (int i = 0; i < n; i++) 

 { 

 if ((XY[i][0] < Xmin) || (XY[i][0] > Xmax)) 

 cout << "[" << XY[i][0] << "," << XY[i][1] << "] ";

 if ((XY[i][1] < Ymin) || (XY[i][1] > Ymax)) 

 cout << "[" << XY[i][0] << "," << XY[i][1] << "] ";

 } 

} 

 

// Driver code 

int main() 

{ 

 int XY[6][2] = {{10, 10}, {-10, 10}, {400, 100}, 

 {100, 400}, {400, 400}, {100, 40}}; 

 

 // getmaxx() & getmaxy() will return Xmax, Ymax 

 // value if graphics.h is included 

 int Xmin = 0; 

 int Xmax = 350; 

 int Ymin = 0; 

 int Ymax = 350; 

 pointClip(XY, 6, Xmin, Ymin, Xmax, Ymax); 

 return 0; 

} 

 

// This code is contributed by SHUBHAMSINGH10  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program for point clipping Algorithm

#include<stdio.h>

//#include<graphics.h>

 

// Function for point clipping

void pointClip(int XY[][2], int n, int Xmin, int Ymin,

 int Xmax, int Ymax)

{

 /*************** Code for graphics view

 // initialize graphics mode

 detectgraph(&gm;,&gr;);

 initgraph(&gm;,&gr;,"d:\\tc\\BGI");

 for (int i=0; i<n; i++)

 {

 if ( (XY[i][0] >= Xmin) && (XY[i][0] <= Xmax))

 {

 if ( (XY[i][1] >= Ymin) && (XY[i][1] <= Ymax))

 putpixel(XY[i][0],XY[i][1],3);

 }

 }

 **********************/

 /**** Arithmetic view ****/

 printf ("Point inside the viewing pane:\n");

 for (int i=0; i<n; i++)

 {

 if ((XY[i][0] >= Xmin) && (XY[i][0] <= Xmax))

 {

 if ((XY[i][1] >= Ymin) && (XY[i][1] <= Ymax))

 printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 }

 }

 

 // print point coordinate outside viewing pane

 printf ("\nPoint outside the viewing pane:\n");

 for (int i=0; i<n; i++)

 {

 if ((XY[i][0] < Xmin) || (XY[i][0] > Xmax))

 printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 if ((XY[i][1] < Ymin) || (XY[i][1] > Ymax))

 printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 }

}

 

// Driver code

int main()

{

 int XY[6][2] = {{10,10}, {-10,10}, {400,100},

 {100,400}, {400,400}, {100,40}};

 

 // getmaxx() & getmaxy() will return Xmax, Ymax

 // value if graphics.h is included

 int Xmin = 0;

 int Xmax = 350;

 int Ymin = 0;

 int Ymax = 350;

 pointClip(XY, 6, Xmin, Ymin, Xmax, Ymax);

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

// Java program for point clipping Algorithm

class GFG 

{

 

// Function for point clipping

static void pointClip(int XY[][], int n, 

 int Xmin, int Ymin,

 int Xmax, int Ymax)

{

 /*************** Code for graphics view

 // initialize graphics mode

 detectgraph(&gm;,&gr;);

 initgraph(&gm;,&gr;,"d:\\tc\\BGI");

 for (int i=0; i<n; i++)

 {

 if ( (XY[i][0] >= Xmin) && (XY[i][0] <= Xmax))

 {

 if ( (XY[i][1] >= Ymin) && (XY[i][1] <= Ymax))

 putpixel(XY[i][0],XY[i][1],3);

 }

 }

 **********************/

 /**** Arithmetic view ****/

 System.out.printf ("Point inside the viewing pane:\n");

 for (int i = 0; i < n; i++)

 {

 if ((XY[i][0] >= Xmin) && (XY[i][0] <= Xmax))

 {

 if ((XY[i][1] >= Ymin) && (XY[i][1] <= Ymax))

 System.out.printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 }

 }

 

 // print point coordinate outside viewing pane

 System.out.printf ("\nPoint outside the viewing pane:\n");

 for (int i=0; i<n; i++)

 {

 if ((XY[i][0] < Xmin) || (XY[i][0] > Xmax))

 System.out.printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 if ((XY[i][1] < Ymin) || (XY[i][1] > Ymax))

 System.out.printf ("[%d, %d] ", XY[i][0], XY[i][1]);

 }

}

 

// Driver code

public static void main(String[] args) 

{

 int XY[][] = {{10,10}, {-10,10}, {400,100},

 {100,400}, {400,400}, {100,40}};

 

 // getmaxx() & getmaxy() will return Xmax, Ymax

 // value if graphics.h is included

 int Xmin = 0;

 int Xmax = 350;

 int Ymin = 0;

 int Ymax = 350;

 pointClip(XY, 6, Xmin, Ymin, Xmax, Ymax);

}

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python3 program for poclipping Algorithm

 

# Function for poclipping 

def pointClip(XY, n, Xmin, Ymin, Xmax, Ymax):

 

 """************** Code for graphics view 

 # initialize graphics mode 

 detectgraph(&gm;, &gr;) 

 initgraph(&gm;, &gr;, "d:\\tc\\BGI") 

 for (i=0 i<n i++) 

 

 if ((XY[i][0] >= Xmin) and 

 (XY[i][0] <= Xmax)) 

 

 if ((XY[i][1] >= Ymin) and 

 (XY[i][1] <= Ymax)) 

 putpixel(XY[i][0], XY[i][1], 3) 

 

 *********************"""

 """*** Arithmetic view ***"""

 print("Point inside the viewing pane:") 

 for i in range(n):

 if ((XY[i][0] >= Xmin) and

 (XY[i][0] <= Xmax)): 

 if ((XY[i][1] >= Ymin) and

 (XY[i][1] <= Ymax)): 

 print("[", XY[i][0], ", ", XY[i][1], 

 "]", sep = "", end = " ") 

 

 # prpocoordinate outside viewing pane 

 print("\n\nPoint outside the viewing pane:") 

 for i in range(n): 

 if ((XY[i][0] < Xmin) or (XY[i][0] > Xmax)) :

 print("[", XY[i][0], ", ", XY[i][1],

 "]", sep = "", end = " ") 

 if ((XY[i][1] < Ymin) or (XY[i][1] > Ymax)) :

 print("[", XY[i][0], ", ", XY[i][1], 

 "]", sep = "", end = " ") 

 

# Driver Code

if __name__ == '__main__':

 XY = [[10, 10], [-10, 10], [400, 100], 

 [100, 400], [400, 400], [100, 40]] 

 

 # getmaxx() & getmaxy() will return Xmax, 

 # Ymax value if graphics.h is included 

 Xmin = 0

 Xmax = 350

 Ymin = 0

 Ymax = 350

 pointClip(XY, 6, Xmin, Ymin, Xmax, Ymax)

 

# This code is contributed by

# SHUBHAMSINGH10  
  
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

// C# program for point clipping Algorithm

using System;

 

class GFG 

{

 

// Function for point clipping

static void pointClip(int [,]XY, int n, 

 int Xmin, int Ymin,

 int Xmax, int Ymax)

{

 /*************** Code for graphics view

 // initialize graphics mode

 detectgraph(&gm;,&gr;);

 initgraph(&gm;,&gr;,"d:\\tc\\BGI");

 for (int i=0; i<n; i++)

 {

 if ( (XY[i,0] >= Xmin) && (XY[i,0] <= Xmax))

 {

 if ( (XY[i,1] >= Ymin) && (XY[i,1] <= Ymax))

 putpixel(XY[i,0],XY[i,1],3);

 }

 }

 **********************/

 /**** Arithmetic view ****/

 Console.Write("Point inside the viewing pane:\n");

 for (int i = 0; i < n; i++)

 {

 if ((XY[i, 0] >= Xmin) && (XY[i, 0] <= Xmax))

 {

 if ((XY[i, 1] >= Ymin) && (XY[i, 1] <= Ymax))

 Console.Write("[{0}, {1}] ", XY[i, 0], XY[i, 1]);

 }

 }

 

 // print point coordinate outside viewing pane

 Console.Write("\nPoint outside the viewing pane:\n");

 for (int i = 0; i < n; i++)

 {

 if ((XY[i, 0] < Xmin) || (XY[i, 0] > Xmax))

 Console.Write("[{0}, {1}] ", XY[i, 0], XY[i, 1]);

 if ((XY[i, 1] < Ymin) || (XY[i, 1] > Ymax))

 Console.Write("[{0}, {1}] ", XY[i, 0], XY[i, 1]);

 }

}

 

// Driver code

public static void Main(String[] args) 

{

 int [,]XY = {{10, 10}, {-10, 10}, {400, 100},

 {100, 400}, {400, 400}, {100, 40}};

 

 // getmaxx() & getmaxy() will return Xmax, Ymax

 // value if graphics.h is included

 int Xmin = 0;

 int Xmax = 350;

 int Ymin = 0;

 int Ymax = 350;

 pointClip(XY, 6, Xmin, Ymin, Xmax, Ymax);

}

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    Point inside the viewing pane:
    [10, 10] [100, 40] 
    
    Point outside the viewing pane:
    [-10, 10] [400, 100] [100, 400] [400, 400] [400, 400] 
    

**Related Post :**  
Line Clipping | Set 1 (Cohen–Sutherland Algorithm)  
Polygon Clipping | Sutherland–Hodgman Algorithm

  

  

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

