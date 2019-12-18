# Deep Reinforcement Learning

This repo includes codes from Deep Reinforcement Learning Hands-On book by Maxim Lapan. The reference repo can be cloned as follows:

```sh
git clone https://github.com/PacktPublishing/Deep-Reinforcement-Learning-Hands-On.git
```

## Requirements

Some codes require FFmpeg to be installed on your machine. For example, `Monitor` feature of the `gym` environments generate videos that shows the simulation of reinforcement learning process.

To create videos, you may need `xvfb` tool, too. For example, to run on a machine with no graphical features (server side), you can run:

```sh
xvfb-run -s "-screen 0 640x480x24" python app/chapter02/cartpole_random.py
```

## TensorBoard

To use tensorboard, make sure tensorflow, tensorboard, and tensorboardX are installed in the virtual environment. Then, run tensorboard server as follows from the root directory of this project:

```sh
tensorboard --logdir=runs --host=localhost --port=6006
```

where logs will be stored in the `runs/` directory. Also, run the tensorboard example in another terminal as follows:

```sh
python app/chapter03/tensorboard.py
```

Finally, go to `http://localhost:6006` from your browser to see the details: plots of `sin`, `cos`, and `tan` in this example.
