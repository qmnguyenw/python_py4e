Python String | ljust(), rjust(), center()



String alignment is frequently used in many day-day applications. Python in
its language offers several functions that helps to align string. Also, offers
a way to add user specified padding instead of blank space.

These functions are :

    
    
    str. **ljust** (s, width[, fillchar])
    str. **rjust** (s, width[, fillchar])
    str. **center** (s, width[, fillchar])
    

These functions respectively left-justify, right-justify and center a string
in a field of given width. They return a string that is at least width
characters wide, created by padding the string _s_ with the character
_fillchar_ (default is a space) until the given width on the right, left or
both sides. The string is never truncated.

