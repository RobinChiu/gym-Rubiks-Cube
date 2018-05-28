import gym
from gym import spaces
import numpy as np
import random
from gym.envs.magic_cube import cube

actionList = [
        'f', 'r', 'l', 'u', 'd', 'b',
        '.f', '.r', '.l', '.u', '.d', '.b']

tileDict = {
    'R' : 1,
    'O' : 2,
    'Y' : 3,
    'G' : 4,
    'B' : 5,
    'W' : 0,
}

class RubiksCubeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # the action is 6 move x 2 direction = 12
        self.action_space = spaces.Discrete(12)
        # input is 9x6 = 54 array
        low = np.array([0.0 for i in range(54)])
        high = np.array([1.0 for i in range(54)])
        self.observation_space = spaces.Box(low, high) # flattened
        self.step_count = 0


    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        self.action_log.append(action)
        self.ncube.minimalInterpreter(actionList[action])
        self.state = self.getstate()
        self.step_count = self.step_count + 1

        reward = 0.0
        done = False
        others = {}
        if self.ncube.isSolved() :
            reward = 1.0
            done = True

        if self.step_count > 40 :
            done = True

        return self.state, reward, done, others


    def reset(self):
        orderNum = 3
        self.state = {}
        self.ncube = cube.Cube(order=orderNum)
        self.scramble()
        self.state = self.getstate()
        self.step_count = 0
        self.action_log = []
        return self.state

    def getstate(self):
        return np.array([tileDict[i]/5 for i in self.ncube.constructVectorState()])

    def render(self, mode='human', close=False):
        if close:
            return
        self.ncube.displayCube(isColor=True)

    def scramble(self):
        # set the scramber number
        scramble_num = random.randint(1, 10)

        # check if scramble
        while self.ncube.isSolved() :
            self.scramble_log = []
            for i in range (scramble_num):
                action = random.randint(0, 11)
                self.scramble_log.append(action)
                self.ncube.minimalInterpreter(actionList[action])

    def getlog(self):
        return self.scramble_log, self.action_log
                
