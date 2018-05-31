# gym-Rubiks-Cube
The Rubik's Cube is a popular game. If you still didn't know it, you can go to check it on Wiki.  
[Wiki: Rubik's Cube](https://en.wikipedia.org/wiki/Rubik%27s_Cube "Wiki: Rubik's Cube")  
This is the open gym environment for the Rubik's Cube. You can check it here.  
https://gym.openai.com/

---
# Installation

You can use the command to install the Rubik's Cube gym module.

    pip install -e .
    
It will create a Rubiks Cube of gym environment. The cube will be scrambled in the reset function. You can change the scramble low/high step in it by call the setScramble function. You can look the play.py to learn how to use it. 

    python examples/play.py
    
![image](https://github.com/RobinChiu/gym-Rubiks-Cube/blob/master/image/play.png)

---
# Training
The traning program is copied from deepq of the OpenAI baseline. You need to install it first. 
https://github.com/openai/baselines
Then you can run the command to train it. 

    cd examples
    python train_rubikscube.py

I put my training check point file and model in the examples directory also. If you don't want to use it, you should delete it before your training. 

    rm -rf examples/rubikscube
    rm examples/rubikscube_model.pkl
    
---
# Run it
After the training you can test your model by runing the command. It will run 100 episodes(100 scrambled Rubik's Cube), and try to use your model to solve it.
    
    python enjoy_rubikscube.py
    
![image](https://github.com/RobinChiu/gym-Rubiks-Cube/blob/master/image/enjoy.png)

