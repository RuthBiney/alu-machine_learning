import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

# Set up the Breakout environment
env = gym.make('Breakout-v0')
nb_actions = env.action_space.n
input_shape = env.observation_space.shape

# Define the model
model = Sequential()
# Flatten input to a single dimension
model.add(Flatten(input_shape=(1,) + input_shape))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
# Output layer for action values
model.add(Dense(nb_actions, activation='linear'))

# Define replay memory
memory = SequentialMemory(limit=50000, window_length=1)

# Define exploration policy
policy = EpsGreedyQPolicy(eps=0.1)

# Set up the DQN agent
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(optimizer='adam', metrics=['mae'])

# Train the agent
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

# Save the trained policy
dqn.save_weights('policy.h5', overwrite=True)
