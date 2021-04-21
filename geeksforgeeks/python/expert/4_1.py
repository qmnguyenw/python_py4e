Difference between Pygame VS Arcade Libaray in Python



Game programming is very rewarding nowadays and it can also be used in
advertising or as a teaching tool. Game development encompasses mathematics,
logic, physics, AI, and much more and it can be amazingly fun. In Python, up
until now, Pygame library was employed for the same, but after many
improvements and dealing with problems possessed by Pygame a new module,
Arcade Library came into the picture. Here we will discuss how they differ
from each other, but first, let’s understand what exactly they are.

 **Pygame:** It is a Python module used for designing video games, by allowing
computer graphics and sound libraries in order to develop high quality and
user interactive games. Pygame was developed by Pete Shinners. Till 2000, it
was a community project, later on, it was released under open source free
software General Public License. Pygame is portable and its code is compatible
with all operating systems. It is also possible to create open-source, free,
freeware, shareware, and commercial games with it. Pygame code is written in C
language and the module comes with installers for Windows and macOS. It can be
easily used on handheld devices too. Even after all this, the module lacked
some facilities needed improvements which will be discussed later in the flow
of the article.

 **Arcade:** **** It is again a Python module but works for Python 3.6 and
above only. It tries to cover most of the functionalities that were not
supported by Pygame. This also uses computer graphics and sound libraries in
order to develop high quality and user interactive games. Arcade was developed
by Paul Vincent Craven. Arcade needs support for OpenGL 3.3+. It is built on
top of OpenGL and Pyglet and is compatible with Windows, Linux, and macOS X.
It is also possible to create open-source, free, freeware, shareware, and
commercial games with it. It also supports the standard coordinate system and
is extremely easy to use and code.

## Table of Difference between Arcade and PyGame

### Arcade

|

### PyGame

|  Arcade is based on Open GL| PyGame was infrequently updated and it is based
on an old SDL 1 library| It has new features of Python 3, like decorators and
type-hinting| No new features of Python 3 | Arcade draws stationary sprites
much faster than Pygame| PyGame draws stationary sprites much slower than
Arcade| Gives liberty of rotating Ellipses, arcs, and other shapes| No such
liberty | Arcade supports standard coordinate system | Pygame doesn’t support
standard coordinate system | Supports animated sprites| Doesn’t support
animated sprites| API documentation for the commands is better| The API
documentation is not that much elaborated.| Command names are consistent i.e
to add to a sprite list append() is used| Commands aren’t consistent, it uses
add()| Less boiler-plate code than Pygame and also much easier to write and to
understand.| No such facility| Encourages separation of logic and display
code| Tends to put both into the same game loop.|  Runs on top of OpenGL 3+
and Pyglet| Runs on the old SDL1 library.| Arcade uses SoLoud which Supports
panning and volume.| Pygame uses old and unsupported Avbin library  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

