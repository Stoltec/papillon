import torch.nn as nn

class ActionCNN(nn.Module):
    def __init__(self, word_dim, out_nodes):
        super(ConvNet, self).__init__()
        self.first = nn.Sequential(
                nn.Conv2d(1, 16, kernel_size = word_dim, stride = 1,
                        padding = int(word_dim / 2)),
                nn.BatchNorm2d(16),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size = 2, stride = 2))
        self.second = nn.Sequential(
                nn.Conv2d(16, 32, kernel_size = word_dim, stride = 1,
                        padding = int(word_dim / 2)),
                nn.BatchNorm2d(32),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size = 2, stride = 2))
        # constrains values to [0.0, 1.0]
        self.third = nn.Sequential(
                nn.Linear(((kernel_size + 1) ** 2) * 32, out_nodes),
                nn.ReLU())

    def forward(self, data):
        out = self.first(data)
        out = self.second(out)
        out = self.third(out)
        return out
