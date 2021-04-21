FuzzyWuzzy Python library



There are many methods of comparing string in python. Some of the main methods
are:

  1. Using regex
  2. Simple compare
  3. Using difflib

But one of the very easy method is by using **fuzzywuzzy** library where we
can have a score out of 100, that denotes two string are equal by giving
similarity index. This article talks about how we start using fuzzywuzzy
library.

FuzzyWuzzy is a library of Python which is used for string matching. Fuzzy
string matching is the process of finding strings that match a given pattern.
Basically it uses Levenshtein Distance to calculate the differences between
sequences.  
FuzzyWuzzy has been developed and open-sourced by SeatGeek, a service to find
sport and concert tickets. Their original use case, as discussed in their
blog.

 **Requirements of fuzzywuzzy**

* Python 2.4 or higher
* python-Levenshtein

