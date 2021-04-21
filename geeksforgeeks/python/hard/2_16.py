glob – Filename pattern matching



Glob module searches all path names looking for files matching a specified
pattern according to the rules dictated by the Unix shell. Results so obtained
are returned in arbitrary order. Some requirements need traversal through a
list of files at some location, mostly having a specific pattern. Python’s
glob module has several functions that can help in listing files that match a
given pattern under a specified folder.

Pattern matching is done using **os.scandir()** and **fnmatch.fnmatch()**
functions, and not by actually invoking a sub-shell. Unlike ****
fnmatch.fnmatch(), glob treats filenames beginning with a dot **(.)** as
special cases. For tilde and shell variable expansion,
**os.path.expanduser()** and **os.path.expandvars()** functions are used.

###  **Pattern rules**

  * Follow standard Unix path expansion rules.
  * Special characters supported : two different wild-cards- *, ? and character ranges expressed in [].
  * The pattern rules are applied to segments of the filename (stopping at the path separator, /).
  * Paths in the pattern can be relative or absolute.

### Application

  * It is useful in any situation where your program needs to look for a list of files on the file system with names matching a pattern.
  * If you need a list of filenames that have a certain extension, prefix, or any common string in the middle, use glob instead of writing code to scan the directory contents yourself.

### Functions in Glob:

  *  **glob(pathname, *, recursive=False)-** It returns list of path names that match pathname given, which must be a string containing a path specification. List can be empty too.
  *  **iglob(pathname, *, recursive=False)-** This method creates a Python generator object which is used to list files under a given directory. Also returns an iterator that yields the same values as glob() without actually storing them all simultaneously.
  *  **escape(pathname)-** It allows escaping the given character sequence. You can find it handy for locating files with certain characters in their file names and matching an arbitrary literal string that may have special characters in it.

Given below is the implementation to help you understand how this module can
be put to practice:

 **Example 1:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import glob

 

# search .py files

# in the current working directory

for py in glob.glob("*.py"):

 print(py)  
  
---  
  
 __

 __

