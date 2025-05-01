import torch
import torch.nn as nn
# import torch

class DQN(nn.Module):
    def __init__(self, input_size=42, output_size=7):
        super(DQN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_size)
        )

    def forward(self, x):
        return self.fc(x)
