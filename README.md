# QLearningExample

This is a simple path-finding AI that makes use of the basic Q-Learning algorithm. Most of this repository was inspired by the book Reinforcement Learning by Richard S. Sutton and Andrew G. Barto. The goal of reinforcement learning is to create an intelligent agent whose actions are based on the most optimal choice. This agent is placed in an environment where it either gets rewarded or punished for a certain action it chooses. The agent strives to maximize its reward for each episode. An episode is a period of time in which the agent gets to roam around in the environment. These episodes often have a certain starting point, and normally end when the agent dies or reaches the end-goal.

The heart of the Q-Learning algorithm is defined by the Bellman-equation: <img src="https://latex.codecogs.com/gif.latex?Q(s,a)=r+\gamma\max\limits_{a'}Q(s',a')" />, where a is action chosen, s is state the agent is in and r is the reward. The max a' is the most profitable action in the next state s' reached by choosing action a in state s, Q(s, a). It's then fairly obvious that the value of the state-action pair Q(s, a) is based on possible future rewards of future actions. This is the key idea of the Bellman-equation; rewards in the future are relevant for states in the past. 

For this specific project, an agent learned to walk a certain path in a 6 by 4 field. The original board looks like this:

![plot](https://github.com/TimVeenboer/QLearningExample/blob/main/Board.png)

The dark purple squares give a reward of -100 and end the episode for the agent. The squares with a value of -1 is the path we want the agent to take, and the left-bottom square also ends the episode and gives the agent a reward of +100. This is therefore the end-goal for the agent. 

![plot](https://github.com/TimVeenboer/QLearningExample/blob/main/Rewards.png)
![plot](https://github.com/TimVeenboer/QLearningExample/blob/main/StateEstimation.png)

In the images above it shows the rewards received for the agent after 100 episodes, and the average state values attributed to each state. It's pretty clear that after around 20 episodes the path is already learned. The problem is not that difficult to solve, and it also shows that with Q-Learning the agent easily finds the most profitable path in an instant.

# References

Sutton, R. S., Barto, A. G. (2018 ). Reinforcement Learning: An Introduction. The MIT Press.
Deeplizard - Building Collective Intelligence. (2021). Retrieved 18 April 2021, from https://deeplizard.com/
