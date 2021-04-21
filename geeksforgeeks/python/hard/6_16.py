Asynchronous Advantage Actor Critic (A3C) algorithm



The **Asynchronous Advantage Actor Critic (A3C)** algorithm is one of the
newest algorithms to be developed under the field of Deep Reinforcement
Learning Algorithms. This algorithm was developed by Google’s DeepMind which
is the Artificial Intelligence division of Google. This algorithm was first
mentioned in 2016 in a research paper appropriately named Asynchronous Methods
for Deep Learning.

Decoding the **different parts** of the algorithm’s name:-

  *  **Asynchronous:** Unlike other popular Deep Reinforcement Learning algorithms like Deep Q-Learning which uses a single agent and a single environment, This algorithm uses multiple agents with each agent having its own network parameters and a copy of the environment. This agents interact with their respective environments **Asynchronously** , learning with each interaction. Each agent is controlled by a global network. As each agent gains more knowledge, it contributes to the total knowledge of the global network. The presence of a global network allows each agent to have more diversified training data. This setup mimics the real-life environment in which humans live as each human gains knowledge from the experiences of some other human thus allowing the whole “global network” to be better.
  *  **Actor-Critic:** Unlike some simpler techniques which are based on either Value-Iteration methods or Policy-Gradient methods, the A3C algorithm combines the best parts of both the methods ie the algorithm predicts both the value function V(s) as well as the optimal policy function ![\\pi \(s\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-01935f8b1503d76a864a84aaf9e45539_l3.png). The learning agent uses the value of the Value function (Critic) to update the optimal policy function (Actor). Note that here the policy function means the **probabilistic distribution of the action space**. To be exact, the learning agent determines the conditional probability P(a|s ;![\\theta](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a372b7ef1ffaec3b4ad80e0141550990_l3.png)) ie the parametrized probability that the agent chooses the action a when in state s.

 **Advantage:** Typically in the implementation of **Policy Gradient** , the
value of Discounted Returns(![\\gamma r](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-d39982a8b95c52c6befe83ac98382be8_l3.png)) to
tell the agent which of it’s actions were rewarding and which ones were
penalized. By using the value of Advantage instead, the agent also learns how
much better the rewards were than it’s expectation. This gives a new-found
insight to the agent into the environment and thus the learning process is
better. The advantage metric is given by the following expression:-

 **Advantage: A = Q(s, a) – V(s)**

The following pseudo-code is referred from the research paper linked above.

  

  

    
    
    **Define global shared parameter vectors![\\theta](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a372b7ef1ffaec3b4ad80e0141550990_l3.png) and ![\\theta _{v}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-5307f273390941db709603f8dfa5f459_l3.png)
    Define global shared counter T = 0
    Define thread specific parameter vectors ![\\theta '](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d4006e0df11c0657b6c9f10f95b68320_l3.png) and ![\\theta _{v}'](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c20b14a76b908e7ccb9f79a47f7b5d1d_l3.png)
    Define thread step counter t = 1
    while(![T<T_{max}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-0efecee7509289172c4b21da5539bbea_l3.png))
    {
        ![d\\theta = 0](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e9b8235e8f0eb518f7b6b4adb01b6392_l3.png)
        ![d\\theta _{v} = 0](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-1cd398241180754101de2db600fc5a2f_l3.png)
        ![\\theta ' = \\theta](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-fb37722b043596a5875fff0eba61105d_l3.png)
        ![\\theta '_{v} = \\theta _{v}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-badfc92e719c3fbff79d563eb18689a5_l3.png)
        ![t_{start} = t](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b86d8d3c454bdfd5920aa933b1f411d7_l3.png)
        ![s = s_{t}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-2ca54e3ad04c08b23e7cb84eedcab968_l3.png)
        while(![s_{t}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-785c7cb9532a3f8908de08ca978fdcaa_l3.png) is not terminal ![t-t_{start} < t_{max}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-2f5ec03d4fb9ac61f3cfb23834697c8a_l3.png))
        {
            Simulate action ![a_{t}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-dde4d7086739f757e666e89406201b2f_l3.png) according to ![\\pi \(a_{t}|s;\\theta \)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-0b03e915202bfcca67eedfc4806d20f5_l3.png)
            Receive reward ![r_{t}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-953bd432cbc178d01cb1b55149bf3f42_l3.png) and next state ![s_{t+1}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3f20d27cb7812a844adc22591d12fa6c_l3.png)
            t++
            T++ 
        }
        if(![s_{t}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-785c7cb9532a3f8908de08ca978fdcaa_l3.png) is terminal)
        {
            R = 0
        }
        else
        {
            R = ![V\(s_{t}, \\theta _{v}'\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-62c6424be498bba0ee3c3f7812206d64_l3.png)
        }
        for(i=t-1;i>=![t_{start}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8ffeac3377ddc123055ca9e230620b38_l3.png);i--)
        {
            R = ![r_{i} + \\gamma R](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3e9c4870b664956fe1de90ac0b064901_l3.png)
    
            ![d\\theta = d\\theta + \\Delta _{\\theta '}log\(\\pi \(a_{i}|s{i};\\theta '\)\(R-V\(s_{i};\\theta _{v}'\)\)\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f80ff37278769de83169d6316c070209_l3.png)
            
            ![d\\theta _{v}= d\\theta _{v} + \\frac{\\partial \(\(R-V\(s_{i};\\theta _{v}'\)\)^{2}\)}{\\partial \\theta _{v}'}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e00dbc4e95d3a0be8e903aed089ce7f7_l3.png)
        }
        ![\\theta = \\theta + d\\theta](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-52259ba9a72318499eb31e450f390d84_l3.png)
        ![\\theta _{v}= \\theta + d\\theta _{v}](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-865028953e114e12b0cafc5bb43a72ae_l3.png)
    }
    **
    

**Where,**

![T_{max}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-567e0dac327e8ab3d38a4f38896341b0_l3.png) – Maximum number
of iterations

![d\\theta](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-212274d28dc226a5d041f36a204f5031_l3.png) – change in
global parameter vector

![R](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-40e110f8a63635f3c8e9ab42993d2049_l3.png) – Total Reward

![\\pi](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8874a17fc40c8e51a122ea351eb44182_l3.png) – Policy
function

![V](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-885e2f541303990c14e80785818a8674_l3.png) – Value function

![\\gamma](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-137dac33e00867a8b0c38e7734db8b8a_l3.png) – discount
factor

 **Advantages:**

  * This algorithm is faster and more robust than the standard Reinforcement Learning Algorithms.
  * It performs better than the other Reinforcement learning techniques because of the diversification of knowledge as explained above.
  * It can be used on discrete as well as continuous action spaces.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

