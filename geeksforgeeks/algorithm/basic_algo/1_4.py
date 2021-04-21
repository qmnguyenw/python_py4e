Painter’s Algorithm in Computer Graphics



 **Painter’s algorithm** is the algorithm which is introduced by **Hewells**
in **1972**.

The techniques used by these algorithms are **image space** and **object
space**.

The name of this algorithm is Painter’s because it’s working is like a painter
who creating an **oil painting**. Just like an artist paints, he start his
painting with an empty canvas, the first thing the artist will do is to create
a **background layer** for the painting, after this layer he start creating
**another layers** of objects **one-by-one**. In this way he completes his
painting, by covering the previous layer partially or fully according to the
requirement of the painting.

This algorithm is basically used to paint the **polygons** in the view plane
by considering their distance from the viewer. The polygons which are at more
distance from the viewer are painted first. After that the nearer polygons are
started painted on or over more distant polygons according to the requirement.

In this algorithm the polygons or surfaces in the scene are firstly scanned or
then painted in the frame buffer in the **decreasing distance** from view
point of the viewer starting with the polygons of **maximum depth** or we can
say minimum z-value.

  

  

Firstly the **depth sort** is performed in which the polygons are listed
according to their **visibility order** or depth priority.

As this algorithm uses the concept of depth priority so it is also called as
**depth priority algorithm** or **priority algorithm**.

The frame buffer is painted with the background color. After that the polygon
which is farthest enter to the frame buffer. For this, the pixel information
will get changed i.e. information of the background which has the farthest
polygon get replaced with that of the background. This is going to be
repeatedly changed as we move from one polygon to the other and end up with
the nearest polygon.

Usually **comparisons** are performed whenever the polygons are going to
overlap each other. The most common method used for the comparison is called
as **mini-max method**. For this purpose, the rectangles are drawn around the
polygons such that the rectangles exactly fit the polygons.

Then the rectangles are going to check to see whether they overlap ecah other
or not. If the rectangles are observed as they do not overlap then we consider
that the surfaces are also not overlap. If the rectangles are overlapped then
the surfaces are also overlapped which is as shown in the following figure:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200702091247/rectangles.jpg)

To find out which rectangle is to be overlap, we need to find the minimum and
maximum x and y values to the rectangles which are going to test for
overlapping. If the minimum value of y of one of the rectangles is larger than
the maximum y value of the other rectangle then they are not going to be
overlapped and as the rectangles are not overlapped then the surfaces are also
not overlapped.

The same test is to be performed for the x-coordinates.

If the surfaces are overlapping, we do not know which surface should be
present on the top of the other. To find out which surface is to be present on
the top the **principle of** **mini-max** is used on the depth vales of both
the overlapping surfaces.

 **Example:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200702090138/imagesjpg.jpg)

### Algorithm for Painter’s method

The following are the steps of this algorithm:

  1. Sorting of the various surfaces which is on the basis of their decreasing depth or we can say the largest value of z.
  2. Now scanning to convert the various surfaces which is in the order starting with the surface which has greatest depth.
  3. Comparing is to be done on the basis of various overlapping surfaces so that the user will determine which surface is to be kept visible.
  4. In the refresh buffer enter the intensity value for the determined surface i.e. the surface which is determined to be visible.
  5. The above process is going to be repeat for all the available surfaces.
  6. However, if the overlapping is observed, then their is the need of the further tests. The following tests are required:

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

