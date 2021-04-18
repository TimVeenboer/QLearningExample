import numpy as np
from game import Game
import matplotlib.pyplot as plt

STATE_SIZE = 24
ACTION_SIZE = 4
WIDTH, HEIGHT = 4, 6
RIGHT, LEFT, DOWN, UP = 1, -1, 1, -1

class Agent:
    def __init__(self, epsilon=1):
        # initialize Q-Table
        self.Q = {}
        for h in range(HEIGHT):
            for w in range(WIDTH):
                self.Q[(h, w)] = np.zeros(ACTION_SIZE)
        self.epsilon = epsilon

    def choose_action(self, position):
        """This function lets the agent take an action in the game."""
        randnum = np.random.uniform(0, 1)

        if randnum >= self.epsilon:
            # choose max Q
            return np.argmax(self.Q[(position[0], position[1])])
        else:
            # explore, choose a random action
            return np.random.choice([0, 1, 2, 3])

def mse(y):
    return (y - 92)**2

game = Game()
agent = Agent()
episodes = 100
alpha = 0.3
gamma = 0.9
decay = 0.2
min_epsilon = 0
max_epsilon = 1
rewards = []

for i in range(episodes):
    rewards_episode = 0
    while not game.done:
        # get current state
        state = game.player_position.copy()
        # get next action
        action = agent.choose_action(game.player_position)
        # observe the reward and next state
        reward = game.move(action)
        state_prime = game.player_position.copy()
        # update state-value
        agent.Q[(state[0], state[1])][action] = (1 - alpha) * \
            agent.Q[(state[0], state[1])][action] + \
            alpha*(reward + gamma*np.max(agent.Q[(state_prime[0], state_prime[1])]))
        # handle epsilon decay
        agent.epsilon = min_epsilon + (max_epsilon - min_epsilon) \
            * np.exp(-decay*i)
        rewards_episode += reward

    rewards.append(rewards_episode)
    # restart game
    game.__init__()

plt.plot(rewards)
plt.title('Rewards per episode')
plt.show()