import torch
import torch.nn as nn

class GHDOModel(nn.Module):

    def __init__(self):
        super(GHDOModel, self).__init__()
        self.encoder = nn.Linear(128,64)
        self.decoder = nn.Linear(64,128)

    def forward(self, x):
        z = self.encoder(x)
        output = self.decoder(z)
        return output

    def train_step(self):
        dummy_input = torch.randn(32,128)
        output = self.forward(dummy_input)
        loss = torch.mean((output - dummy_input)**2)
        return loss
