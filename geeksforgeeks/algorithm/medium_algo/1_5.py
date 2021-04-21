Flood Fill Algorithm



Given a 2D screen **arr[][]** where each **arr[i][j]** is an integer
representing the colour of that pixel, also given the location of a pixel
**(X, Y)** and a colour **C** , the task is to replace the colour of the given
pixel and all the adjacent same-coloured pixels with the given colour.

 **Example:**

>  **Input:** arr[][] = {  
> {1, 1, 1, 1, 1, 1, 1, 1},  
> {1, 1, 1, 1, 1, 1, 0, 0},  
> {1, 0, 0, 1, 1, 0, 1, 1},  
> {1, **2, 2, 2, 2,** 0, 1, 0},  
> {1, 1, 1, **2, 2,** 0, 1, 0},  
> {1, 1, 1, **2, 2, 2, 2,** 0},  
> {1, 1, 1, 1, 1, **2,** 1, 1},  
> {1, 1, 1, 1, 1, **2, 2,** 1}}  
> X = 4, Y = 4, C = 3  
>  **Output:**  
>  1 1 1 1 1 1 1 1  
> 1 1 1 1 1 1 0 0  
> 1 0 0 1 1 0 1 1  
> 1 **3 3 3 3** 0 1 0  
> 1 1 1 **3 3** 0 1 0  
> 1 1 1 **3 3 3 3** 0  
> 1 1 1 1 1 **3** 1 1  
> 1 1 1 1 1 **3 3** 1  
>  **Explanation:**  
>  The values in the given 2D screen indicate colours of the pixels. X and Y
> are coordinates of the brush, C is the colour that should replace the
> previous colour on screen[X][Y] and all surrounding pixels with the same
> colour. Hence all the 2 are replaced with 3.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **BFS Approach:** The idea is to use BFS traversal to replace the colour with
the new colour.

  * Create an empty queue lets say _Q_.
  * Push the starting location of the pixel as given in the input and apply replacement colour to it.
  * Iterate until **Q** is not empty and pop the front node (pixel position).
  * Check the pixels adjacent to the current pixel and push into the queue if valid (had not been coloured with replacement colour and have the same colour as the old colour).

Below is the implementation of the above approach:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 implementation of the approach

 

# Function that returns true if 

# the given pixel is valid

def isValid(screen, m, n, x, y, prevC, newC):

 if x<0 or x>= m\

 or y<0 or y>= n or\

 screen[x][y]!= prevC\

 or screen[x][y]== newC:

 return False

 return True

 

 

# FloodFill function

def floodFill(screen, 

 m, n, x, 

 y, prevC, newC):

 queue = []

 

 # Append the position of starting 

 # pixel of the component

 queue.append([x, y])

 

 # Color the pixel with the new color

 screen[x][y] = newC

 

 # While the queue is not empty i.e. the 

 # whole component having prevC color 

 # is not colored with newC color

 while queue:

 

 # Dequeue the front node

 currPixel = queue.pop()

 

 posX = currPixel[0]

 posY = currPixel[1]

 

 # Check if the adjacent

 # pixels are valid

 if isValid(screen, m, n, 

 posX + 1, posY, 

 prevC, newC):

 

 # Color with newC

 # if valid and enqueue

 screen[posX + 1][posY] = newC

 queue.append([posX + 1, posY])

 

 if isValid(screen, m, n, 

 posX-1, posY, 

 prevC, newC):

 screen[posX-1][posY]= newC

 queue.append([posX-1, posY])

 

 if isValid(screen, m, n, 

 posX, posY + 1, 

 prevC, newC):

 screen[posX][posY + 1]= newC

 queue.append([posX, posY + 1])

 

 if isValid(screen, m, n, 

 posX, posY-1, 

 prevC, newC):

 screen[posX][posY-1]= newC

 queue.append([posX, posY-1])

 

 

 

# Driver code

screen =[

[1, 1, 1, 1, 1, 1, 1, 1], 

[1, 1, 1, 1, 1, 1, 0, 0], 

[1, 0, 0, 1, 1, 0, 1, 1], 

[1, 2, 2, 2, 2, 0, 1, 0], 

[1, 1, 1, 2, 2, 0, 1, 0], 

[1, 1, 1, 2, 2, 2, 2, 0], 

[1, 1, 1, 1, 1, 2, 1, 1], 

[1, 1, 1, 1, 1, 2, 2, 1], 

 ]

 

# Row of the display

m = len(screen)

 

# Column of the display

n = len(screen[0])

 

# Co-ordinate provided by the user

x = 4

y = 4

 

# Current colour at that co-ordinate

prevC = screen[x][y]

 

# New colour that has to be filled

newC = 3

 

floodFill(screen, m, n, x, y, prevC, newC)

 

 

# Priting the updated screen

for i in range(m):

 for j in range(n):

 print(screen[i][j], end =' ')

 print()  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 0 0 
    1 0 0 1 1 0 1 1 
    1 3 3 3 3 0 1 0 
    1 1 1 3 3 0 1 0 
    1 1 1 3 3 3 3 0 
    1 1 1 1 1 3 1 1 
    1 1 1 1 1 3 3 1
    

**DFS Approach:** Similarly DFS approach can be used to implement the Flood
Fill algorithm as well.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

