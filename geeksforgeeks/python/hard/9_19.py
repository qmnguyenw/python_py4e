Creating a Proxy Webserver in Python | Set 1



Socket programming in python is very user friendly as compared to c. The
programmer need not worry about minute details regarding sockets. In python,
the user has more chance of focusing on the application layer rather than the
network layer. In this tutorial we would be developing a simple multi-threaded
proxy server capable of handling HTTP traffic. It would be mostly based on the
basic socket programming ideas. If you are not sure about the basics then i
would recommend that you brush them up before going through this tutorial.

This is a naive implementation of a proxy server. We would be gradually
developing it into a quite useful server in the upcoming tutorials.

 **To begin with, we would achieve the process in 3 easy steps**

 **1\. Creating an incoming socket**  
We create a socket serverSocket in the __init__ method of the Server Class.
This creates a socket for the incoming connections. We then bind the socket
and then wait for the clients to connect.

    
    
    def __init__(self, config):
        # Shutdown on Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown) 
    
        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        # bind the socket to a public host, and a port   
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))
        
        self.serverSocket.listen(10) # become a server socket
        self.__clients = {}
    

**2\. Accept client and process**  
This is the easiest yet the most important of all the steps. We wait for the
client’s connection request and once a successful connection is made, we
dispatch the request in a separate thread, making ourselves available for the
next request. This allows us to handle multiple requests simultaneously which
boosts the performance of the server multifold times.

  

  

    
    
    while True:
    
        # Establish the connection
        (clientSocket, client_address) = self.serverSocket.accept() 
        
        d = threading.Thread(name=self._getClientName(client_address), 
        target = self.proxy_thread, args=(clientSocket, client_address))
        d.setDaemon(True)
        d.start()
    

**3\. Redirecting the traffic**  
The main feature of a proxy server is to act as an intermediate between source
and destination. Here, we would be fetching data from source and then pass it
to the client.

  * First, we extract the URL from the received request data.

    
    
    # get the request from browser
    request = conn.recv(config['MAX_REQUEST_LEN']) 
    
    # parse the first line
    first_line = request.split('\n')[0]
    
    # get url
    url = first_line.split(' ')[1]

  * Then, we find the destination address of the request. Address is a tuple of **(destination_ip_address, destination_port_no)**. We will be receiving data from this address.

    
    
    http_pos = url.find("://") # find pos of ://
    if (http_pos==-1):
        temp = url
    else:
        temp = url[(http_pos+3):] # get the rest of url
    
    port_pos = temp.find(":") # find the port pos (if any)
    
    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)
    
    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos): 
    
        # default port 
        port = 80 
        webserver = temp[:webserver_pos] 
    
    else: # specific port 
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos] 
    

  * Now, we setup a new connection to the destination server (or remote server), and then send a copy of the original request to the server. The server will then respond with a response. All the response messages use the generic message format of **RFC 822**.

    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(config['CONNECTION_TIMEOUT'])
    s.connect((webserver, port))
    s.sendall(request)
    

  * We then redirect the server’s response to the client. conn is the original connection to the client. The response may be bigger then MAX_REQUEST_LEN that we are receiving in one call, so, a null response marks the end of the response.

    
    
    while 1:
        # receive data from web server
        data = s.recv(config['MAX_REQUEST_LEN'])
    
        if (len(data) > 0):
            conn.send(data) # send to browser/client
        else:
            break
    

We then close the server connections appropriately and do the error handling
to make sure the server works as expected.

 **How to test the server?**  
1\. Run the server on a terminal. Keep it running and switch to your favorite
browser.  
2\. Go to your browser’s proxy settings and change the proxy server to
‘localhost’ and port to ‘12345’.  
3\. Now open any HTTP website (not HTTPS), for eg. geeksforgeeks.org and volla
!! you should be able to access the content on the browser.

Once the server is running, we can monitor the requests coming to the client.
We can use that data to monitor the content that is going or we can develop
statistics based on the content.  
We can even restrict access to a website or blacklist an IP address. We would
be dealing with more such features in the upcoming tutorials.  
What next?  
We would be adding the following features in our proxy server in the upcoming
tutorials.  
– Blacklisting Domains  
– Content monitoring  
– Logging  
– HTTP WebServer + ProxyServer

The whole working source code of this tutorial is available here

Creating a Proxy Webserver in Python | Set 2

If you have any questions/comments then feel free to post them in the comments
section.

About the Author:

 **Pinkesh Badjatiya** hails from IIIT Hyderabad .He is a geek at heart with
ample projects worth looking for. His project work can be seen here.

If you also wish to showcase your blog here, please see GBlog for guest blog
writing on GeeksforGeeks.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

