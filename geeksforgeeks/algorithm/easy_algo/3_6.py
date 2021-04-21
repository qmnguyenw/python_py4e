Difference Between Flood-fill and Boundary-fill Algorithm



 **Flood-fill Algorithm:**  
Flood fill algorithm is also known as a seed fill algorithm. It determines the
area which is connected to a given node in a multi-dimensional array. This
algorithm works by filling or recolouring a selected area containing different
colours at the inside portion and therefore the boundary of the image. It is
often illustrated by a picture having a neighbourhood bordered by various
distinct colour regions. To paint such regions we will replace a specific
interior colour instead of discovering a boundary colour value. This is the
rationale the approach is understood because of the flood-fill algorithm.  
Now, there are two methods which will be used for creating endless boundary by
connecting pixels – 4-connected and 8-connected approach. In the 4-connected
method, the pixel can have at maximum four neighbours that are positioned at
the proper, left, above and below the present pixel. On the contrary, in the
8-connected method, it can have eight, and the neighbouring positions are
checked against the four diagonal pixels. So, any of the 2 methods are often
wont to repaint the inside points.

 **Boundary-fill algorithm** :  
It follows an approach where the region filling begins from some extent
residing inside the region and paint the inside towards the boundary. In case
the boundary contains single colour the fill algorithm continues within the
outward direction pixel by pixel until the boundary colour is encountered. The
boundary-fill algorithm is often mainly implemented within the interactive
painting packages, where the inside points are easily chosen.  
The functioning of the boundary-fill starts by accepting the coordinates of an
indoor point (x, y), a boundary colour and fill colour becomes the input.
Beginning from the (x, y) the method checks neighbouring locations to spot
whether or not they are a part of the boundary colour. If they’re not from the
boundary colour, then they’re painted with the fill colour, and their adjacent
pixels are tested against the condition. The process ends when all the pixels
up until the boundary colour for the world are checked.

Difference Between Flood-fill and Boundary-fill Algorithm:Flood-fill
Algorithm| Boundary-fill Algorithm| It can process the image containing more
than one boundary colours.| It can only process the image containing single
boundary colour.| Flood-fill algorithm is comparatively slower than the
Boundary-fill algorithm.| Boundary-fill algorithm is faster than the Flood-
fill algorithm.| In Flood-fill algorithm a random colour can be used to paint
the interior portion then the old one is replaced with a new one.| In
Boundary-fill algorithm Interior points are painted by continuously searching
for the boundary colour.| It requires huge amount of memory.| Memory
consumption is relatively low in Boundary-fill algorithm.| Flood-fill
algorithms are simple and efficient.| The complexity of Bounndary-fill
algorithm is high.  
---|---  
  
Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

