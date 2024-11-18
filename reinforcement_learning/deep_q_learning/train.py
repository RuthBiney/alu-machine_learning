import gym
import gymnasium as gym
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy
import numpy as np

# Set up the Breakout environment with preprocessing
from gym.wrappers import AtariPreprocessing, FrameStack
env = gym.make('Breakout-v0')
env = AtariPreprocessing(env, frame_skip=4, grayscale_obs=True, scale_obs=True)
# Stack the last 4 frames for temporal context
env = FrameStack(env, num_stack=4)

# Define action space and input shape
nb_actions = env.action_space.n
input_shape = env.observation_space.shape

# Build the CNN model
model = Sequential()
model.add(Conv2D(32, (8, 8), strides=(4, 4),
          activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (4, 4), strides=(2, 2), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
# Output layer for action values
model.add(Dense(nb_actions, activation='linear'))

# Define replay memory and exploration policy
memory = SequentialMemory(limit=200000, window_length=1)
policy = LinearAnnealedPolicy(
    EpsGreedyQPolicy(),
    attr='eps',
    value_max=1.0,  # Start with full exploration
    value_min=0.1,  # End with 10% exploration
    nb_steps=1000000,  # Gradual decay over 1M steps
)

# Configure the DQN agent
dqn = DQNAgent(
    model=model,
    nb_actions=nb_actions,
    memory=memory,
    nb_steps_warmup=5000,
    target_model_update=1e-3,  # Smooth target model updates
    policy=policy,
    enable_double_dqn=True,  # Enable Double DQN
    gamma=0.99,  # Discount factor for future rewards
)
dqn.compile(optimizer='adam', metrics=['mae'])

# Train the agent
dqn.fit(env, nb_steps=1000000, visualize=False, verbose=2)

# Save the trained policy
dqn.save_weights('policy.h5', overwrite=True)
print("Training completed! Model saved to 'policy.h5'.")
