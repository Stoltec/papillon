import torch.nn as nn

class ArgumentMLP(nn.Module):
    def __init__(self, embedding_length, num_words):
        super(self).__init__()
        self.first = nn.Sequential(
                nn.Linear(embedding_length, 1024), 
                nn.SELU())
        self.second = nn.Sequential(
                nn.Linear(1024, 512), 
                nn.SELU())
        self.third = nn.Sequential(
                nn.Linear(512, 512), 
                nn.SELU())
        self.fourth = nn.Sequential(
                nn.Linear(512, 256), 
                nn.SELU())
        self.fifth = nn.Sequential(
                nn.Linear(256, 512), 
                nn.SELU())
        # constrains values to [0.0, 1.0]?
        # Use nn.BCEWithLogitsLoss
        self.sixth = nn.Sequential(
                nn.Linear(512, num_words))

    def forward(self, data):
        out = self.first(data)
        out = self.second(out)
        out = self.third(out)
        out = self.fourth(out)
        out = self.fifth(out)
        out = self.sixth(out)
        return out
