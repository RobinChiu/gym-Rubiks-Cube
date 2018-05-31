import gym
import gym_Rubiks_Cube

from baselines import deepq
import argparse
import sys
from baselines.common.tf_util import load_state, save_state

args = None

def main():
    env = gym.make("RubiksCube-v0")
    # env.setScramble(5, 5)
    act = deepq.load(args.load)

    # model = deepq.models.mlp([128, 128])
    # act = deepq.learn(
    #     env,
    #     q_func=model,
    #     lr=1e-4,
    #     max_timesteps=0,
    #     buffer_size=50000,
    #     exploration_fraction=0.2,
    #     exploration_final_eps=0.01,
    #     print_freq=100,
    #     train_freq=4,
    #     learning_starts=10000,
    #     target_network_update_freq=1000,
    #     gamma=0.99,
    #     prioritized_replay=bool(args.prioritized),
    #     prioritized_replay_alpha=args.prioritized_replay_alpha,
    #     checkpoint_freq=args.checkpoint_freq,
    #     checkpoint_path=args.checkpoint_path
    # )

    # while True:
    total_reward = []
    for i in range(100):
        obs, done = env.reset(), False
        env.render("human")
        episode_rew = 0
        while not done:
            # env.render()
            obs, rew, done, _ = env.step(act(obs[None], update_eps=0)[0])
            episode_rew += rew
        total_reward.append(episode_rew)
        # env.render()
        print("Episode reward", episode_rew)
        print("scramble, action_history:", env.getlog())
        print("-----------------------")
    print("total:", len(total_reward), ", Solved: ", total_reward.count(1), ", Unsolved: ", total_reward.count(0))
    print(total_reward)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', type=str, default="rubikscube_model.pkl", 
        help='load the model file')

    parser.add_argument('--env', help='environment ID', default='BreakoutNoFrameskip-v4')
    parser.add_argument('--seed', help='RNG seed', type=int, default=0)
    parser.add_argument('--prioritized', type=int, default=1)
    parser.add_argument('--prioritized-replay-alpha', type=float, default=0.6)
    parser.add_argument('--dueling', type=int, default=1)
    parser.add_argument('--num-timesteps', type=int, default=int(10e6))
    parser.add_argument('--checkpoint-freq', type=int, default=10000)
    parser.add_argument('--checkpoint-path', type=str, default="./rubikscube/")

    args = parser.parse_args()
    return parser.parse_args(argv)

if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])
    main()
