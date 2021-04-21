Exposing ML/DL Models as REST APIs



In this article, we will learn how to expose ML/DL model as flask APIs.

 **Frameworks we’ll be using:**  
 **Keras** is a Deep Learning library, built on top of backends such as
Tensorflow, Theano or CNTK. It provides abstraction and allows rapid
development of ML/DL models.

 **Flask** is a micro web framework in Python, which is used to quickly spin
up servers to serve pages. Refer Introduction to Flask.

Since the focus of the article is to **serve a ML/DL model using an API** , we
wouldn’t get deeper into the making of the Convolutional model. We will be
using the **ResNet50** Convolutional Neural Network.

 **Install Tensorflow and Keras**

  

  
 **Step**|  **Linux/Mac**|  **Windows**|  Update pip| pip install -U pip|
python -m pip install -U pip| Install virtualenv| sudo pip install virtualenv|
pip install virtualenv| Create a new folder ml-api| mkdir ml-api && cd ml-api|
mkdir ml-api && cd ml-api| Create a virtual environment(Good practice) and
activate it| virtualenv –system-site-packages -p python3 ./venv| virtualenv
–system-site-packages -p python3 ./venv| Activate the virtual environment|
source ./venv/bin/activate  
---|---|---|---|---|---|---|---  
  
.\venv\Scripts\activate| Install TensorFlow| pip install –upgrade tensorflow|
pip install –upgrade tensorflow| Install Keras| pip install keras| pip install
keras| Install other dependencies| pip install flask gevent requests pillow|
pip install flask gevent requests pillow

