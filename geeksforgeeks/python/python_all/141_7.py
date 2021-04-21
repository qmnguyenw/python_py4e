Python | URL shortener using tinyurl API



There are multiple APIs (e.g-bitly API, etc.) available for URL shortening
service but in this article, we will be using Tinyurl API to shorten URLs.

Though _tinyURL_ has not officially released its API but we are going to use
it unofficially. Here, we can put as input any number of URLs at a time and
get the shortened URLs at a time.

For Example, if in command line we write

    
    
    $ python filename URL1 URL2 URL3 

then output will be:

    
    
     ['shortened url1', 'shortened url2', 'shortened url3'] 

**Step #1:**

  

  

  * First we have to import 7 libraries.
  * We could have used just one library to work, but in order to make good url shortener we have to use 7 libraries.

The code snippet is as follows:

 __

 __  
 __

 __

 __  
 __  
 __

from __future__ import with_statement 

 

import contextlib

 

try:

 from urllib.parse import urlencode 

 

except ImportError:

 from urllib import urlencode

 

try:

 from urllib.request import urlopen

 

except ImportError:

 from urllib2 import urlopen

 

import sys  
  
---  
  
 __

 __

 **Step 2:**

Here encoding of url and appending it to API is done and then we open
request_url using urlopen. Then we convert the response to UTF-8, since
urlopen() returns a stream of bytes rather than a string.

The code snippet is as follows:

 __

 __  
 __

 __

 __  
 __  
 __

def make_tiny(url):

 request_url = ('http://tinyurl.com/api-create.php?' +
urlencode({'url':url})) 

 with contextlib.closing(urlopen(request_url)) as response: 

 return response.read().decode('utf-8 ')   
  
---  
  
__

__

**Step 3:**  
In the last step we are calling main() and we are getting user input by
using sys.argv  
We have not limited ourself to only one url as input, instead, we are saying
that give us as many urls as you want, we will make them tiny. map() is a
simple way of looping over a list and passing it to a function one by one.

The code snippet is as follows:

 __

 __  
 __

 __

 __  
 __  
 __

def main(): 

 for tinyurl in map(make_tiny, sys.argv[1:]): 

 print(tinyurl)

 

if __name__ == '__main__':

 main()

 

   
  
---  
  
__

__

**Finally, the complete code is below:**

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr/bin/env python 3

from __future__ import with_statement 

 

import contextlib

 

try:

 from urllib.parse import urlencode 

 

except ImportError:

 from urllib import urlencode

try:

 from urllib.request import urlopen

 

except ImportError:

 from urllib2 import urlopen

 

import sys

 

 

def make_tiny(url):

 request_url = ('http://tinyurl.com/api-create.php?' +
urlencode({'url':url})) 

 with contextlib.closing(urlopen(request_url)) as response: 

 return response.read().decode('utf-8 ') 

 

def main(): 

 for tinyurl in map(make_tiny, sys.argv[1:]): 

 print(tinyurl)

 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

