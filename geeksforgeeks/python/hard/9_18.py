Creating a Proxy Webserver in Python | Set 2



Prerequisite: Creating a Proxy Webserver in Python – Set1

In this tutorial, few interesting features are added to make it more useful.

  *  **Add blacklisting of domains**. For Ex. google.com, facebook.com. Create a list of BLACKLIST_DOMAINS in our configuration dict. For now, just ignore/drop the requests received for blacklisted domains. (Ideally we must respond with a forbidden response.)
    
              
    # Check if the host:port is blacklisted
    for i in range(0, len(config['BLACKLIST_DOMAINS'])):
        if config['BLACKLIST_DOMAINS'][i] in url:
            conn.close()
    return
    

  * **To add host blocking:** Say, you may need to allow connections from a particular subnet or connection for a particular person. To add this, create a list of all the allowed hosts. Since the hosts can be a subnet as well, add regex for matching the IP addresses, specifically IPV4 addresses. _“ IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1. Each part represents a group of 8 bits (octet) of the address.”_
  *  **Using regex to match correct IP addresses:**
    * Create a new method, _ishostAllowed in Server class, and use fnmatch module to match regexes. Iterate through all the regexes and allow request if it matches any of them. If a client address is not found to be a part of any regex, then send a FORBIDDEN response. Again, for now skip this response creation part.

 _Note: We would be creating a full fledged custom webserver in upcoming
tutorials, there creation of a createResponse function will be done to handle
the generic response creation._

    
    
    def _ishostAllowed(self, host):
    
        """ Check if host is allowed to access
            the content """
        for wildcard in config['HOST_ALLOWED']:
            if fnmatch.fnmatch(host, wildcard):
                return True
        return False
    

Default host match regex would be ‘*’ to match all the hosts. Though, regex of
the form ‘192.168.*’ can also be used. Server currently processes requests but
does not show any messages, so we are not aware of the state of the server.
Its messages should be logged onto console. For this purpose , use the logging
module as it is thread safe. (server is multi-threaded if you remember.)

 **Import module and setup its initial configuration.**

  

  

    
    
    logging.basicConfig(level = logging.DEBUG,
    format = '[%(CurrentTime)-10s] (%(ThreadName)-10s) %(message)s',)
    

  * **Create a separate method that logs every message** : Pass it as argument, with additional data such as thread-name and current-time to keep track of the logs. Also create a function that colorizes the logs so that the looks pretty on STDOUT.  
To achieve this, add a boolean in configuration, COLORED_LOGGING and create a
new function that colorizes every msg passed to it based on the LOG_LEVEL.

    
    
    def log(self, log_level, client, msg):
    
        """ Log the messages to appropriate place """
        LoggerDict = {
           'CurrentTime' : strftime("%a, %d %b %Y %X", localtime()),
           'ThreadName' : threading.currentThread().getName()
        }
        if client == -1: # Main Thread
            formatedMSG = msg
        else: # Child threads or Request Threads
            formatedMSG = '{0}:{1} {2}'.format(client[0], client[1], msg)
        logging.debug('%s', utils.colorizeLog(config['COLORED_LOGGING'],
        log_level, formatedMSG), extra=LoggerDict)
    

  * **Create a new module, ColorizePython.py:** It contains a pycolors class which maintains a list of color codes. Separate this into another module in order to make code modular and to follow PEP8 standards.

    
    
    # ColorizePython.py
    class pycolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # End color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

**Module:**

    
    
    import ColorizePython

 **Method:**

    
    
    def colorizeLog(shouldColorize, log_level, msg):
        ## Higher is the log_level in the log()
        ## argument, the lower is its priority.
        colorize_log = {
        "NORMAL": ColorizePython.pycolors.ENDC,
        "WARNING": ColorizePython.pycolors.WARNING,
        "SUCCESS": ColorizePython.pycolors.OKGREEN,
        "FAIL": ColorizePython.pycolors.FAIL,
        "RESET": ColorizePython.pycolors.ENDC
        }
    
        if shouldColorize.lower() == "true":
            if log_level in colorize_log:
                return colorize_log[str(log_level)] + msg + colorize_log['RESET']
            return colorize_log["NORMAL"] + msg + colorize_log["RESET"]
        return msg
    

  * Since the colorizeLog is not a function of a server class, it is created as a separate module named utils.py which stores all the utility that make code easier to understand and put this method there. _Add appropriate log messages wherever required, especially whenever the state of server changes._
  * Modify shutdown method in server to exit all the running threads before exiting the application. _threading.enumerate()_ iterates over all the running threads, so we do not need to maintain a list of them. The behavior of threading module is unexpected when we try to end the main_thread. The official documentation also states this:

 _“join() raises a RuntimeError if an attempt is made to join the current
thread as that would cause a deadlock. It is also an error to join() a thread
before it has been started and attempts to do so raises the same exception.”_

So, skip it appropriately. Here’s the code for the same.

    
    
    def shutdown(self, signum, frame):
        """ Handle the exiting server. Clean all traces """
        self.log("WARNING", -1, 'Shutting down gracefully...')
        main_thread = threading.currentThread() # Wait for all clients to exit
        for t in threading.enumerate():
            if t is main_thread:
                continue
                self.log("FAIL", -1, 'joining ' + t.getName())
            t.join()
            self.serverSocket.close()
        sys.exit(0)
    

If you have any comments/suggestions/queries then feel free to ask. 🙂

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

