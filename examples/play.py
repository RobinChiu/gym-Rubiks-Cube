import gym.spaces
import gym_Rubiks_Cube

env = gym.make("RubiksCube-v0")


env.setScramble(1, 10, False)
print(env.reset()) # print status
env.render()


env.setScramble(1, 10, True)
print(env.reset()) # scramble status
env.render()
env.step(0) # action 0~11
env.step(1) # action 0~11
env.render()
scramble, action = env.getlog()
print("Scramble: ", scramble)
print("Action: ", action)


