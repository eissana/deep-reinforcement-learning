from tensorboardX import SummaryWriter
import numpy as np


if __name__ == "__main__":
    # to monitor, navigate to the current directory and run:
    # tensorboard --logdir runs --host localhost
    writer = SummaryWriter()

    funcs = {
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan
    }
    full_circle_degree = 360

    for angle in range(-full_circle_degree, full_circle_degree):
        angle_rad = 2. * angle * np.pi / full_circle_degree
        for name, func in funcs.items():
            val = func(angle_rad)
            writer.add_scalar(name, val, angle_rad)
    writer.close()
