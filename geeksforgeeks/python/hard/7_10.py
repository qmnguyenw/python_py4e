Q-Learning in Python



Pre-Requisite : Reinforcement Learning

 **Reinforcement Learning** briefly is a paradigm of Learning Process in which
a learning agent learns, overtime, to behave optimally in a certain
environment by interacting continuously in the environment. The agent during
its course of learning experience various different situations in the
environment it is in. These are called _states_. The agent while being in that
state may choose from a set of allowable actions which may fetch different
_rewards_ (or penalties). The learning agent overtime learns to maximize these
rewards so as to behave optimally at any given state it is in.

 **Q-Learning** is a basic form of Reinforcement Learning which uses Q-values
(also called action values) to iteratively improve the behavior of the
learning agent.

  1.  **Q-Values or Action-Values:** Q-values are defined for states and actions. ![Q\(S, A\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-70341d1b4aef90015547d7343303db74_l3.png) is an estimation of how good is it to take the action ![A](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png) at the state ![S](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f322ff29bb70c49d154ec39a209a61ca_l3.png). This estimation of ![Q\(S, A\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-70341d1b4aef90015547d7343303db74_l3.png) will be iteratively computed using the **TD- Update rule** which we will see in the upcoming sections.
  2.  **Rewards and Episodes:** An agent over the course of its lifetime starts from a start state, makes a number of transitions from its current state to a next state based on its choice of action and also the environment the agent is interacting in. At every step of transition, the agent from a state takes an action, observes a reward from the environment, and then transits to another state. If at any point of time the agent ends up in one of the terminating states that means there are no further transition possible. This is said to be the completion of an episode.
  3.  **Temporal Difference or TD-Update:**

The Temporal Difference or TD-Update rule can be represented as follows :

![](https://media.geeksforgeeks.org/wp-content/uploads/TD_Update-300x30.jpg)

  

  

This update rule to estimate the value of Q is applied at every time step of
the agents interaction with the environment. The terms used are explained
below. :

    * ![S](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f322ff29bb70c49d154ec39a209a61ca_l3.png) : Current State of the agent.
    * ![A](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png) : Current Action Picked according to some policy.
    * ![S'](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-9d398252bca3a2f46b96b8482c93656f_l3.png) : Next State where the agent ends up.
    * ![A'](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-cf0df7b3b78ea4f0907cf9ae15bdeffc_l3.png) : Next best action to be picked using current Q-value estimation, i.e. pick the action with the maximum Q-value in the next state.
    * ![R](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-40e110f8a63635f3c8e9ab42993d2049_l3.png) : Current Reward observed from the environment in Response of current action.
    * ![$\\gamma$](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-487a21f42487a6c5d51b125f05a441c3_l3.png)(>0 and <=1) : Discounting Factor for Future Rewards. Future rewars are less valuable than current rewards so they must be discounted. Since Q-value is an estimation of expected rewards from a state, discounting rule applies here as well.
    * ![$\\alpha$](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c865a40b5817133e18bdac041fcc84a6_l3.png) : Step length taken to update the estimation of Q(S, A).
  4.  **Choosing the Action to take using![$\\epsilon$](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-2719cec1748613b327f12c9b54e0b6c6_l3.png) -greedy policy:**

![$\\epsilon$](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-2719cec1748613b327f12c9b54e0b6c6_l3.png)-greedy policy of
is a very simple policy of choosing actions using the current Q-value
estimations. It goes as follows :

    * With probability ![\(1-$\\epsilon$\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a6ffa5e52fae6141cd3632923705c79a_l3.png) choose the action which has the highest Q-value.
    * With probability ![\($\\epsilon$\)](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b71ccb0040f7f367d69f070c5db2f957_l3.png) choose any action at random.

