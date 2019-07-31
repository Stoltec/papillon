import torch.nn as nn

class ArgumentsCNN(nn.Module):
    def __init__(self, word_dim, out_classes):
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
        # constrains values to [0.0, 1.0]?
        # Use nn.BCEWithLogitsLoss
        self.third = nn.Sequential(
                nn.Linear(((kernel_size + 1) ** 2) * 32, out_classes))

    def forward(self, data):
        out = self.first(data)
        out = self.second(out)
        out = self.third(out)
        return out
