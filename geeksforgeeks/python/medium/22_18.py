Chain Code for 2D Line



Chain code is a lossless compression technique used for representing an object
in images. The co-ordinates of any continuous boundary of an object can be
represented as a string of numbers where each number represents a particular
direction in which the next point on the connected line is present. One point
is taken as the reference/starting point and on plotting the points generated
from the chain, the original figure can be re-drawn.

This article describes how to generate a 8-neighbourhood chain code of a 2-D
straight line. In a rectangular grid, a point can have at most 8 surrounding
points as shown below. The next point on the line has to be one of these 8
surrounding points. Each direction is assigned a code. Using this code we can
find out which of the surrounding point should be plotted next.

![8-Neighbourhood connected system](https://media.geeksforgeeks.org/wp-
content/uploads/2DChain_code_8-neighbourhood-1.png)

The chain codes could be generated by using conditional statements for each
direction but it becomes very tedious to describe for systems having large
number of directions(3-D grids can have up to 26 directions). Instead we use a
hash function. The difference in X(![dx](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-32fdd5096fd96eaedec6a11ef6b1f976_l3.png)) and
Y(![dy](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-67c8a539777d69b64694c156286d3039_l3.png)) co-ordinates of
two successive points are calculated and hashed to generate the key for the
chain code between the two points.

Chain code list: ![\[5, 6, 7, 4, -1, 0, 3, 2,
1\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5014d67d01a9649337f72bf143831407_l3.png)

  

  

Hash function: ![ C\(dx, dy\) = 3dy + dx +
4](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-90d0386b1dff3baeda9cae58409fa8b8_l3.png)

Hash table:-![dx](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-32fdd5096fd96eaedec6a11ef6b1f976_l3.png)|
![dy](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-67c8a539777d69b64694c156286d3039_l3.png)| ![C\(dx,
dy\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a04698bdbaafed67f8ec1b5179e068fa_l3.png)|
![chainCode\[C\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-cc00a09c9b54d4f2e057353b54b9d44a_l3.png)| 1| 0| 5| 0| 1|
1| 8| 1| 0| 1| 7| 2| -1| 1| 6| 3| -1| 0| 3| 4| -1| -1| 0| 5| 0| -1| 1| 6| 1|
-1| 2| 7  
---|---|---|---  
  
The function does not generate the value 4 so a dummy value is stored there.

Examples:

    
    
    Input : (2, -3), (-4, 2)
    Output : Chain code for the straight line from (2, -3) to (-4, 2) is 333433
    ![Line plotted from \(2, -3\) to \(-4, 2\)](https://media.geeksforgeeks.org/wp-content/uploads/2DChain_code_example_1-1.png)
    
    Input : (-7, -4), (9, 3)
    Output : Chain code for the straight line from (-7, -4) to (9, 3) is 0101010100101010
    ![Line plotted from \(-7, -4\) to \(9, 3\)](https://media.geeksforgeeks.org/wp-content/uploads/2DChain_code_example_2-1.png)
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code for generating 8-neighbourhood chain

# code for a 2-D line

 

codeList = [5, 6, 7, 4, -1, 0, 3, 2,
1]

 

# This function generates the chaincode 

# for transition between two neighbour points

def getChainCode(x1, y1, x2, y2):

 dx = x2 - x1

 dy = y2 - y1

 hashKey = 3 * dy + dx + 4

 return codeList[hashKey]

 

'''This function generates the list of 

chaincodes for given list of points'''

def generateChainCode(ListOfPoints):

 chainCode = []

 for i in range(len(ListOfPoints) - 1):

 a = ListOfPoints[i]

 b = ListOfPoints[i + 1]

 chainCode.append(getChainCode(a[0], a[1], b[0], b[1]))

 return chainCode

 

 

'''This function generates the list of points for 

a staright line using Bresenham's Algorithm'''

def Bresenham2D(x1, y1, x2, y2):

 ListOfPoints = []

 ListOfPoints.append([x1, y1])

 xdif = x2 - x1

 ydif = y2 - y1

 dx = abs(xdif)

 dy = abs(ydif)

 if(xdif > 0):

 xs = 1

 else:

 xs = -1

 if (ydif > 0):

 ys = 1

 else:

 ys = -1

 if (dx > dy):

 

 # Driving axis is the X-axis

 p = 2 * dy - dx

 while (x1 != x2):

 x1 += xs

 if (p >= 0):

 y1 += ys

 p -= 2 * dx

 p += 2 * dy

 ListOfPoints.append([x1, y1])

 else:

 

 # Driving axis is the Y-axis

 p = 2 * dx-dy

 while(y1 != y2):

 y1 += ys

 if (p >= 0):

 x1 += xs

 p -= 2 * dy

 p += 2 * dx

 ListOfPoints.append([x1, y1])

 return ListOfPoints

 

def DriverFunction():

 (x1, y1) = (-9, -3)

 (x2, y2) = (10, 1)

 ListOfPoints = Bresenham2D(x1, y1, x2, y2)

 chainCode = generateChainCode(ListOfPoints)

 chainCodeString = "".join(str(e) for e in chainCode)

 print ('Chain code for the straight line from', (x1, y1), 

 'to', (x2, y2), 'is', chainCodeString)

 

DriverFunction()  
  
---  
  
 __

 __

 **Output:**

    
    
    Chain code for the straight line from (-9, -3) to (10, 1) is 0010000100010000100
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

