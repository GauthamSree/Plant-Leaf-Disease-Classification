import os

import pandas as pd
import torch
import torch.nn as nn
from torch.nn import functional as F
from torchvision import transforms 
from sklearn import metrics, model_selection, preprocessing
import torch
from torchvision import datasets
from torch.utils.data import DataLoader, Dataset 

from Model import *
from callbacks import EarlyStopping
from efficientnet_pytorch import EfficientNet
from utils import *

class LeafModel(Model):
    def __init__(self, num_classes, init=nn.init.kaiming_normal_):
        super().__init__()

        self.effnet = EfficientNet.from_pretrained("efficientnet-b3")
        self.head = create_head(1536, num_classes)

    def monitor_metrics(self, outputs, targets):
        if targets is None:
            return {}
        outputs = torch.argmax(outputs, dim=1).cpu().detach().numpy()
        targets = targets.cpu().detach().numpy()
        accuracy = metrics.accuracy_score(targets, outputs)
        return {"accuracy": accuracy}

    def fetch_optimizer(self):
        opt = torch.optim.Adam(self.parameters(), lr=3e-4)
        return opt

    def fetch_scheduler(self):
        sch = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
            self.optimizer, T_0=10, T_mult=1, eta_min=1e-6, last_epoch=-1
        )
        return sch

    def forward(self, image, targets=None):
        batch_size, _, _, _ = image.shape

        x = self.effnet.extract_features(image)
        outputs = self.head(x)

        if targets is not None:
            loss = nn.CrossEntropyLoss()(outputs, targets)
            metrics = self.monitor_metrics(outputs, targets)
            return outputs, loss, metrics
        return outputs, None, None
