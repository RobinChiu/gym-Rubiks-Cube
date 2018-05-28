from gym.envs.registration import register

register(
    id='RubiksCube-v0',
    entry_point='gym_Rubiks_Cube.envs:RubiksCubeEnv',
)
