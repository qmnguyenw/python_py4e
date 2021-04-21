Secure coding – What is it all about?



So you think you can code? Well that’s great to know… The world definitely
needs more geeks and nerds like you and me… But, **are your programs secure?**
This is what this whole article is all about.

As a programmer, it is not only your job but also moral responsibility to
ensure that your codes don’t have any margin which can be later on exploited
by any other Black Hat Hacker. This is what **_secure coding_** is all about.
If you do a quick search on Google about Secure Coding, the first link that
will attract your attention will be our own Wiki.

 _Secure coding is the practice of developing computer software in a way that
guards against the accidental introduction of security vulnerabilities.
Defects, bugs and logic flaws are consistently the primary cause of commonly
exploited software vulnerabilities._

Okay! That’s enough of jargon… What does that really mean? Let me give you an
example. Now, since, I am a snake charmer, I will use Python 2.7x…

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#test_run.py

pswd ="MY PASSWORD"

not_secret ="Geeks rock!"

 

inputVal = input("Please enter number of geeks") #A VERY BAD
IDEA

print "There are", inputVal,"geeks here, chanting", not_secret  
  
---  
  
 __

 __

Now, go ahead and give it a try… It compiles successfully and you know what,
it gives the desired output! So, here is what I got when I tried different
inputs…

 **Run – 1**

Please enter number of geeks **5**

    
    
     **** There are **5** geeks here, chanting **Geeks rock!**

 **Run – 2**

 **** Please enter number of geeks **dir()**

    
    
    There are **[‘pswd’, ‘not_secret’, ‘__builtins__’, ‘__doc__’, ‘__file__’,
    ‘__name__’, ‘__package__’]** geeks here, chanting **Geeks rock!**

 **Run – 3**

 **** Please enter number of geeks **pswd**

    
    
     **** There are **MY PASSWORD** geeks here, chanting **Geeks rock!**

If you didn’t realise it till now, let me state it… The program worked
perfectly! But, not in the way we wanted it to… It printed out our secret
data… Now, you can’t blame the language for this, and neither can you blame
the programmer… He/she did what he was asked to do… This is where **Secure
Coding** comes into play. Now, this example was just a small example, a very
small one. There are endless number of possibilities of exploiting a program.
All you need is a smart mind and an experience of exploiting the
vulnerabilities. And if you are a **network security** guy/gal, then hiring a
coder with no or very little knowledge about secure coding standards can prove
to be the biggest mistake you can make. Thus, to have a safe professional
future, it becomes a necessity to have complete knowledge about secure coding
standards.

  

  

Now, who can decide what safe way of coding is? It is not something that a
single programmer can do. Thankfully, we don’t need to bother about it. Go and
check out the **SEI CERT Coding Standards**. It has a very nice collection of
recommended steps to take to ensure that your program is secure and that also
sorted according to the programming languages – C, C++, Java, Perl, and
Android. But, sadly, for the easiest language (in my opinion) there are no
such standards given. Does that mean that a Python program is always secure?
NO!! Fortunately, some Python enthusiasts set forward to make a list of
similar recommendations for Python and resulted in the birth of what is known
today as **PEP 0008**. Known as the **Style Guide for Python Code** , it was
created in 2001.

 _With an exhaustive list of “safe” and “unsafe” programs, it serves as a must
use for any Python programmer._

Now, enough of theory! Let’s get back to some coding stuff! I am now going to
use a Hi-Fi term that you can further use to impress someone 😉 and that term
is **Cross Site Scripting (XSS)**. In the present scenario when every site has
a comment section where they allow the visitors to share their experiences,
XSS has come up to become a frequently used method by hackers (not a good
term!) to steal data/ launch Distributed Denial Of Service (DDOS) attacks/
installing viruses and malwares into the system of client and many other ‘not
– so – good’ acts.

Most of the comment sections allow the users to write in HTML code to provide
an opportunity of formatting. This means that the comment is first processed
and then the result is printed on the site. So, suppose instead of a comment,
I write a JavaScript code like this:

    
    
    window.alert(“Your comment has been received! – Geeks4Geeks”);

Now, going by what I discussed just now, the code will be processed and the
client will receive a pop – up mentioning, “ _Your comment has been received!
– Geeks4Geeks_ ”. That doesn’t sound bad… But, just imagine the possibilities.
One can write a simple script which will download a malware/virus in the
system of client, or show an advertisement with content that will attract
him/her to click on it which will be present in an IFrame which can steal
cookies (this is called **Clickjacking** ) which further leads to what is
known as **Session Hijacking** ; options are not limited! So, what should we
do? Again, the solution lies in Secure Coding! Just to give you an example, of
how you can avoid XSS, and Clickjacking using Django:

    
    
    # **Clickjacking**
    
    response = render_to_response(“webpage.html”, {},
    context_instance=RequestContext(request))
    response[‘X-Frame-Options’] = ‘DENY’ #Frame Killing
    reponse[‘Content-Security-Policy’] = “frame-ancestors ‘none’”
    return response
    

# **XSS**

#Django by default escapes HTML, so most programs will be safe from #XSS
attacks

**{{ contents }}** #is safe

**{{ contents|safe }}** #Overriding escape, **not a good idea**

So, basically the summary is that if you want to be successful in the field of
coding, then you should **make it a habit to follow Secure Coding Standards**.
Why? Because only those programs are safe that are not accessible to public…
As soon as they are available to everyone, there is a whole lot of people out
there trying to break your code… You better take care of that!

With this I take my leave!

 **Auf Wiedersehen!** **!** (See you again in German)

 **About the author:**

 **Vishwesh Shrimali** is an Undergraduate Mechanical Engineering student at
BITS Pilani. He fulfils![vish](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/vish-100x100.png) about all the requirements not taught in his branch-
white hat hacker, network security operator, and an ex – Competitive
Programmer. As a firm believer in power of Python, his majority work has been
in the same language. Whenever he get some time apart from programming,
attending classes, watching CSI Cyber, he go for a long walk and play guitar
in silence. His motto of life is – “Enjoy your life, ‘cause it’s worth
enjoying!”

 **If you also wish to showcase your blog here, please seeGBlog for guest blog
writing on GeeksforGeeks.**

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

