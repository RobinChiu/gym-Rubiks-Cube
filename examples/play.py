import gym
import gym_Rubiks_Cube

env = gym.make("RubiksCube-v0")

print(env.reset()) # scramble status

env.render("human")

env.step(0) # action 0~11

env.render("human")
