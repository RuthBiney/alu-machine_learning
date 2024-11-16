import gym
import tensorflow.keras as K
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory

# Set up the Breakout environment
env = gym.make('Breakout-v0')
nb_actions = env.action_space.n
input_shape = env.observation_space.shape

# Define the model (same as training)
model = Sequential()
model.add(Flatten(input_shape=(1,) + input_shape))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))

# Define replay memory
memory = SequentialMemory(limit=50000, window_length=1)

# Use a greedy policy for evaluation
policy = GreedyQPolicy()

# Set up the DQN agent
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(optimizer='adam', metrics=['mae'])

# Load the trained policy
dqn.load_weights('policy.h5')

# Evaluate the agent
dqn.test(env, nb_episodes=5, visualize=True)
