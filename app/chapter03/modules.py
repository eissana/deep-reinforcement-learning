import torch
import torch.nn as nn


class ModuleExample(nn.Module):
    def __init__(self, num_inputs, num_classes, dropout_prob=0.3):
        super(ModuleExample, self).__init__()

        self.pipe = nn.Sequential(
            nn.Linear(num_inputs, 5),
            nn.ReLU(),
            nn.Linear(5, 20),
            nn.ReLU(),
            nn.Linear(20, num_classes),
            nn.Dropout(p=dropout_prob),
            nn.Softmax(dim=0)
        )

    def forward(self, x):
        return self.pipe(x)


if __name__ == "__main__":
    net = ModuleExample(num_inputs=2, num_classes=3)
    input = torch.FloatTensor([2, 3])
    output = net(input)

    print(output)