import gym
import gym_Rubiks_Cube

# from baselines import deepq
# import baselines.common.tf_util as U
# import zipfile
# import cloudpickle
# import tensorflow as tf

# import os
# import tempfile
# from baselines import logger
# from baselines import bench

from baselines import deepq
from baselines.common import set_global_seeds
from baselines import bench
import argparse
from baselines import logger

def callback(lcl, glb):
    # stop training if reward exceeds 199
    is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 0.95
    if is_solved :
        return True

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--env', help='environment ID', default='BreakoutNoFrameskip-v4')
    parser.add_argument('--seed', help='RNG seed', type=int, default=0)
    parser.add_argument('--prioritized', type=int, default=1)
    parser.add_argument('--prioritized-replay-alpha', type=float, default=0.6)
    parser.add_argument('--dueling', type=int, default=1)
    parser.add_argument('--num-timesteps', type=int, default=int(10e6))
    parser.add_argument('--checkpoint-freq', type=int, default=10000)
    parser.add_argument('--checkpoint-path', type=str, default="./rubikscube/")

    args = parser.parse_args()
    logger.configure()
    set_global_seeds(args.seed)
    env = gym.make("RubiksCube-v0")
    # change the scramble step low and high
    # i = 6
    # env.setScramble(i, i)

    print("logger.get_dir():", logger.get_dir())
    model = deepq.models.mlp([128, 128])

    act = deepq.learn(
        env,
        q_func=model,
        lr=1e-4,
        max_timesteps=args.num_timesteps,
        buffer_size=50000,
        exploration_fraction=0.3,
        exploration_final_eps=0.01,
        print_freq=100,
        train_freq=4,
        learning_starts=10000,
        target_network_update_freq=1000,
        gamma=0.99,
        prioritized_replay=bool(args.prioritized),
        prioritized_replay_alpha=args.prioritized_replay_alpha,
        checkpoint_freq=args.checkpoint_freq,
        checkpoint_path=args.checkpoint_path,
        callback=callback
    )

    print("Saving model to rubikscube_model.pkl")
    act.save("rubikscube_model.pkl")


if __name__ == '__main__':
    main()    
