Deep Q-Learning



 **Prerequisites:** Q-Learning

The process of Q-Learning creates an exact matrix for the working agent which
it can “refer to” to maximize its reward in the long run. Although this
approach is not wrong in itself, this is only practical for very small
environments and quickly loses it’s feasibility when the number of states and
actions in the environment increases.

The solution for the above problem comes from the realization that the values
in the matrix only have relative importance ie the values only have importance
with respect to the other values. Thus, this thinking leads us to **Deep
Q-Learning** which uses a deep neural network to approximate the values. This
approximation of values does not hurt as long as the relative importance is
preserved.

The basic working step for Deep Q-Learning is that the initial state is fed
into the neural network and it returns the Q-value of all possible actions as
on output.

The difference between Q-Learning and Deep Q-Learning can be illustrated as
follows:-

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190613102817/q-learning.png)

![](https://media.geeksforgeeks.org/wp-content/uploads/20190613104538/Deep-Q-
Learning.png)

 **Pseudo Code:**

    
    
    Initialize ![Q_{0}\(s,a\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-959e4928e2ccaf96aaf3dfb1adb39d14_l3.png) for all pairs (s,a)
    s = initial state
    k = 0
    while(convergence is not achieved)
    {
        simulate action a and reach state s'
        if(s' is a terminal state)
        {
            target = R(s,a,s')
        }
        else
        {
            target = R(s,a,s') + ![\\gamma max_{a'}Q_{k}\(s',a'\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b65dfcd26041738614cbbbc8c813048f_l3.png)
        }
        ![\\theta _{k+1} = \\theta _{k}-\\alpha \\Delta _{\\theta }E_{s'~P\(s'|s,a\)}\[\(Q_{\\theta }\(s,a\)-target\(s'\)\)^{2}\]|_{\\theta = \\theta _{k}}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-46030a20a7131435a4da1b17e8f6fd37_l3.png)
        s = s'
    }
    

Observe that in the equation **target = R(s,a,s’) +![\\gamma
max_{a'}Q_{k}\(s',a'\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b65dfcd26041738614cbbbc8c813048f_l3.png)** , the term  
![\\gamma max_{a'}Q_{k}\(s',a'\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b65dfcd26041738614cbbbc8c813048f_l3.png) is a variable
term. Therefore in this process, the target for the neural network is variable
unlike other typical Deep Learning processes where the target is stationary.

This problem is overcome by having two neural networks instead of one. One
neural network is used to adjust the parameters of the network and the other
is used for computing the target and which has the same architecture as the
first network but has frozen parameters. After an x number of iterations in
the primary network, the parameters are copied to the target network.

![](https://media.geeksforgeeks.org/wp-content/uploads/20190613112505/target-
network.png)

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

