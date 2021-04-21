Get Your System Information – Using Python Script



Getting system information for your system can easily be done by the operating
system in use, Ubuntu let’s say. But won’t it be fun to get this System
information using Python script? In this article, we will look into various
ways to derive your system information using Python.

There are two ways to get information:

  1. Using Platform module
  2. subprocess   

## 1\. Using Platform module:

Installation of the platform module can be done using the below command:  

    
    
    pip install platform
    
    

**Example:**  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import platform

my_system = platform.uname()

print(f"System: {my_system.system}")

print(f"Node Name: {my_system.node}")

print(f"Release: {my_system.release}")

print(f"Version: {my_system.version}")

print(f"Machine: {my_system.machine}")

print(f"Processor: {my_system.processor}")  
  
---  
  
 __

 __

