Scan-line Polygon filling using OPENGL in C



Figures on a computer screen can be drawn using polygons. To fill those
figures with color, we need to develop some algorithm.There are two famous
algorithms for this purpose: Boundary fill and Scanline fill algorithms.

Boundary filling requires a lot of processing and thus encounters few problems
in real time. Thus the viable alternative is scanline filling as it is very
robust in nature. This article discusses how to use Scanline filling algorithm
to fill colors in an image.

 **Scanline Polygon filling Algorithm**

Scanline filling is basically filling up of polygons using horizontal lines or
scanlines. The purpose of the SLPF algorithm is to fill (color) the interior
pixels of a polygon given only the vertices of the figure. To understand
Scanline, think of the image being drawn by a single pen starting from bottom
left, continuing to the right, plotting only points where there is a point
present in the image, and when the line is complete, start from the next line
and continue.  
This algorithm works by intersecting scanline with polygon edges and fills the
polygon between pairs of intersections.  
![](https://media.geeksforgeeks.org/wp-content/uploads/scanlinefilling.png)

 **Special cases of polygon vertices:**

  

  

  1. If both lines intersecting at the vertex are on the same side of the scanline, consider it as two points.
  2. If lines intersecting at the vertex are at opposite sides of the scanline, consider it as only one point.

 **Components of Polygon fill:**

  1.  **Edge Buckets:** It contains an edge’s information. The entries of edge bucket vary according to data structure you have used.In the example we are taking below, there are three edge buckets namely: ymax, xofymin,  
slopeinverse.

  2.  **Edge Table:** It consistsof several edge lists -> holds all of the edges that compose the figure. When creating edges, the vertices of the edge need to be ordered from left to right and thee edges are maintained in increasing yMin order. Filling is complete once all of the edges are removed from the ET
  3.  **Active List:** IT maintains the current edges being used to fill in the polygon.Edges aree pushed into the AL from the Edge Table when an edge’s yMin is equal to the current scan line being processed.  
The Active List will be re-sorted after every pass.

 **Data Structure:**  
![Scan line polygon filling1](https://media.geeksforgeeks.org/wp-
content/uploads/scanlinefillingds.png)

