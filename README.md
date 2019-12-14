# Deep Reinforcement Learning

This repo includes codes from Deep Reinforcement Learning Hands-On book by Maxim Lapan.

## Requirements

Some codes require FFmpeg to be installed on your machine. For example, `Monitor` feature of the `gym` environments generate videos that shows the simulation of reinforcement learning process.

To create videos, you may need `xvfb` tool, too. For example, to run on a machine with no graphical features (server side), you can run:

```sh
xvfb-run -s "-screen 0 640x480x24" python app/chapter02/cartpole_random.py
```
