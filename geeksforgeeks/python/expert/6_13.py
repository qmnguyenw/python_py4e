Using Matplotlib for Animations



Matplotlib library of Python is a plotting tool used to plot graphs of
functions or figures. It can also be used as an animation tool too. The
plotted graphs when added with animations gives a more powerful visualization
and helps the presenter to catch a larger number of audience. Matplotlib can
also easily connect with Pandas to create even more sophisticated animations.

Animations in Matplotlib can be made by using the Animation class in two
ways:

  *  **By calling a function over and over:** It uses a predefined function which when ran again and again creates an animation.
  *  **By using fixed objects:** Some animated artistic objects when combined with others yield an animation scene.

It is important to note that we must at all points keep a reference to the
animated object or else the animation will stop. This is because the
Animation class holds a single pointer reference to the animation object and
as the time advances to run the animation this pointer reference must be kept
otherwise it will be collected as a garbage value.

Though there are two ways, the first way is more common and convenient and
here, we will make use of that only. However, you can read the documentation
of the other as well, here .

Let’s dive into Matplotlib animations.

  

  

>  **Installations required:**
>
> 1\. Numpy and Matplotlib  
> 2\. ffmpeg
>
>  _Download ffmpeg for Python fromhere._

Let’s check an example. Here we will try and make a continuous sine wave using
animations and plotting tools. We will make use of numpy and pyplot from
matplotlib for this. As already said, we will be using the function method
as opposed to the artistic objects.

 **Note:** To save an animation to your computer, use
**anim.save(filename)** or **Animation.to_html5_video**.

 __

 __  
 __

 __

 __  
 __  
 __

from matplotlib import pyplot as plt

import numpy as np

from matplotlib.animation import FuncAnimation 

 

# initializing a figure in 

# which the graph will be plotted

fig = plt.figure() 

 

# marking the x-axis and y-axis

axis = plt.axes(xlim =(0, 4), 

 ylim =(-2, 2)) 

 

# initializing a line variable

line, = axis.plot([], [], lw = 3) 

 

# data which the line will 

# contain (x, y)

def init(): 

 line.set_data([], [])

 return line,

 

def animate(i):

 x = np.linspace(0, 4, 1000)

 

 # plots a sine graph

 y = np.sin(2 * np.pi * (x - 0.01 * i))

 line.set_data(x, y)

 

 return line,

 

anim = FuncAnimation(fig, animate, init_func = init,

 frames = 200, interval = 20, blit = True)

 

 

anim.save('continuousSineWave.mp4', 

 writer = 'ffmpeg', fps = 30))  
  
---  
  
 __

 __

At first, after importing the necessities, we set a blank figure or a blank
window on which the entire animation will be drawn. Next we initialize a
variableline which will contain the x and y co-ordinates of the plot. These
are kept empty at first as the data in it will continuously keep changing
because of the animation. Finally, we state the animation function
animate(i) which takes an argument **i** , where **i** is called the frame
number and using this we create the sine wave(or any other figure) which will
continuously vary depending upon the value of **i**. In the last line anim =
FuncAnimation(fig, animate, init_func=init, frames=200, interval=20,
blit=True) we use the FuncAnimation function to create an animation which
will display 200 frames per second and in an interval of 20 micro secs.

 **Output :**  

https://media.geeksforgeeks.org/wp-content/uploads/20200113213401/sine.mp4

Now that’s a very powerful visualization. One thing to note is that when we
view our saved gif, it will be a continuous clip unlike the video in our
output which gets terminated in a few seconds. Let’s look at one more example.
Try to guess the output as we code the program as it will clear our concept.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.animation as animation 

import matplotlib.pyplot as plt 

import numpy as np 

 

 

# creating a blank window

# for the animation 

fig = plt.figure() 

axis = plt.axes(xlim =(-50, 50),

 ylim =(-50, 50)) 

 

line, = axis.plot([], [], lw = 2) 

 

# what will our line dataset

# contain?

def init(): 

 line.set_data([], []) 

 return line, 

 

# initializing empty values

# for x and y co-ordinates

xdata, ydata = [], [] 

 

# animation function 

def animate(i): 

 # t is a parameter which varies

 # with the frame number

 t = 0.1 * i 

 

 # x, y values to be plotted 

 x = t * np.sin(t) 

 y = t * np.cos(t) 

 

 # appending values to the previously 

 # empty x and y data holders 

 xdata.append(x) 

 ydata.append(y) 

 line.set_data(xdata, ydata) 

 

 return line,

 

# calling the animation function 

anim = animation.FuncAnimation(fig, animate, init_func = init, 

 frames = 500, interval = 20, blit = True) 

 

# saves the animation in our desktop

anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)  
  
---  
  
 __

 __

As we might already have guessed and as obvious as the saved file name
suggests, it’s an animation of a continuously growing coil. Just as before, we
first import all the modules. But this time, we import
thematplotlib.animation library completely

    
    
    import matplotlib.animation as animation

however, in the previous example, we imported just the FuncAnimation
function from it

    
    
    from matplotlib.animation import FuncAnimation

However, this does not really make any changes and one can choose any way of
importing. Then we create a figure on which the animation will be placed. The
animate function varies with the frame number **i**. One thing to know is
that a coil is nothing but a composite function of sine and cos. We take the
sine function in x-axis and cos in y-axis and the resultant figure gives a
coil.

 **Output:**

https://media.geeksforgeeks.org/wp-
content/uploads/20200113213446/growingCoil.mp4

Hence, we conclude that many interesting animations can be made by using some
basic knowledge of matplotlib. This really comes in handy when one needs to
present some visualizations with additional power of animation without using
higher level animation tools such as Blender.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

