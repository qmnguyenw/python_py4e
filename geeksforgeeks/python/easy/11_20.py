Django Request and Response cycle – HttpRequest and HttpResponse Objects



 **Prerequisite –** Views In Django | Python

Before we jump into using convenience methods that views come with, Let’s talk
about Request and Response cycle. So when a Request happens to a Django
server, a couple of things go on. One of them is Middleware.

 **Middleware**  
Middleware is like a middle ground between a request and response. It is like
a window through which data passes. As in a window, light passes in and out of
the house. Similarly when a request is made a request when made moves through
middlewares to views and data is passed through middleware as a response.  
Here are the default middlewares installed in Django.

![middlewares-django-geeksforgeeks](https://media.geeksforgeeks.org/wp-
content/uploads/20190924122033/middlewares-django-geeksforgeeks.png)

You can add your middlewares. We will be discussing that in the next articles.

  

  

### Request and Response Objects –

Django uses request and response objects to pass state through the system.

When a page is requested, Django creates an HttpRequest object that contains
metadata about the request. Then Django loads the appropriate view, passing
the HttpRequest as the first argument to the view function. Each view is
responsible for returning an HttpResponse object.

#### HttpRequest and HttpResponse object Example

  * To explain these objects let’s create a view home as below in **views.py**

 __

 __  
 __

 __

 __  
 __  
 __

# importing HttResponse from library

from django.http import HttpResponse

 

def home(request):

 # request is handled using HttpResponse object

 return HttpResponse("Any kind of HTML Here")  
  
---  
  
 __

 __

  * To handle the request let us map a URL to this view in **urls.py**

 __

 __  
 __

 __

 __  
 __  
 __

# importing view from views.py

from .views import home

 

urlpatterns = [

 path('', home),

 

]  
  
---  
  
 __

 __

  * Now you can run the sever to see the following in browser  
![HttpRequest-and-HttpResponse-Object-
example](https://media.geeksforgeeks.org/wp-
content/uploads/20190924130326/HttpRequest-and-HttpResponse-Object-
example-1024x263.png)

#### HttpRequest Attributes – Django

You can use following attributes with HttpRequest for advanced
manipulationAttribute| Description| HttpRequest.scheme| A string representing
the scheme of the request (HTTP or HTTPs usually).| HttpRequest.body| It
returns the raw HTTP request body as a byte string.| HttpRequest.path| It
returns the full path to the requested page does not include the scheme or
domain.| HttpRequest.path_info| It shows path info portion of the path.|
HttpRequest.method| It shows the HTTP method used in the request.|
HttpRequest.encoding| It shows the current encoding used to decode form
submission data.| HttpRequest.content_type| It shows the MIME type of the
request, parsed from the CONTENT_TYPE header.| HttpRequest.content_params| It
returns a dictionary of key/value parameters included in the CONTENT_TYPE
header.| HttpRequest.GET| It returns a dictionary-like object containing all
given HTTP GET parameters.| HttpRequest.POST| It is a dictionary-like object
containing all given HTTP POST parameters.| HttpRequest.COOKIES| It returns
all cookies available.| HttpRequest.FILES| It contains all uploaded files.|
HttpRequest.META| It shows all available Http headers.|
HttpRequest.resolver_match| It contains an instance of ResolverMatch
representing the resolved URL.  
---|---  
  
#### HttpRequest Methods – Django

You can use following methods with HttpRequest for advanced
manipulationAttribute| Description| HttpRequest.get_host()| It returns the
original host of the request.| HttpRequest.get_port()| It returns the
originating port of the request.| HttpRequest.get_full_path()| It returns the
path, plus an appended query string, if applicable.|
HttpRequest.build_absolute_uri _(location)_|  It returns the absolute URI form
of location.| HttpRequest.get_signed_cookie _(key, default=RAISE_ERROR,
salt=”, max_age=None)_|  It returns a cookie value for a signed cookie, or
raises a django.core.signing.BadSignature exception if the signature is no
longer valid.| HttpRequest.is_secure()| It returns True if the request is
secure; that is, if it was made with HTTPS.| HttpRequest.is_ajax()| It returns
True if the request was made via an XMLHttpRequest.  
---|---  
  
#### HttpResponse Attributes – Django

You can use following attributes with HttpResponse for advanced
manipulationAttribute| Description| HttpResponse.content| A bytestring
representing the content, encoded from a string if necessary.|
HttpResponse.charset| It is a string denoting the charset in which the
response will be encoded.| HttpResponse.status_code| It is an **HTTP status
code** for the response.| HttpResponse.reason_phrase| The HTTP reason phrase
for the response.| HttpResponse.streaming| It is false by default.|
HttpResponse.closed| It is True if the response has been closed.  
---|---  
  
#### HttpResponse Methods – Django

You can use following methods with HttpResponse for advanced
manipulationMethod| Description| HttpResponse.__init__ _(content=”,
content_type=None, status=200, reason=None, charset=None)_|  It is used to
instantiate an HttpResponse object with the given page content and content
type.| HttpResponse.__setitem__ _(header, value)_|  It is used to set the
given header name to the given value.| HttpResponse.__delitem__ _(header)_|
It deletes the header with the given name.| HttpResponse.__getitem__
_(header)_|  It returns the value for the given header name.|
HttpResponse.has_header _(header)_|  It returns either True or False based on
a case-insensitive check for a header with the provided name.|
HttpResponse.setdefault _(header, value)_|  It is used to set default header.|
HttpResponse.write _(content)_|  It is used to create response object of file-
like object.| HttpResponse.flush()| It is used to flush the response object.|
HttpResponse.tell()| This method makes an HttpResponse instance a file-like
object.| HttpResponse.getvalue()| It is used to get the value of
HttpResponse.content.| HttpResponse.readable()| This method is used to create
stream-like object of HttpResponse class.| HttpResponse.seekable()| It is used
to make response object seekable.  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

