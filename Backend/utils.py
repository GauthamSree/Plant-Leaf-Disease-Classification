import torch
import numpy as np
import torch.nn as nn
from torchvision import transforms
from PIL import Image
from io import BytesIO
import os

class AdaptiveConcatPool2d(nn.Module):
    def __init__(self, size=None):
        super().__init__()
        self.size = size or 1
        self.ap = nn.AdaptiveAvgPool2d(self.size)
        self.mp = nn.AdaptiveMaxPool2d(self.size)
        
    def forward(self, x): 
        return torch.cat([self.mp(x), self.ap(x)], 1)

def init_weights(m):
    if type(m) == nn.Linear:
        if hasattr(m, 'weight'): nn.init.kaiming_normal_(m.weight)
        if hasattr(m, 'bias') and hasattr(m.bias, 'data'): m.bias.data.fill_(0.)

def create_head(nf, n_out, h1=512, d=0.25, init=nn.init.kaiming_normal_):
    layers = [AdaptiveConcatPool2d(), nn.Flatten(),
                  nn.BatchNorm1d(nf*2), nn.Dropout(d), 
                  nn.Linear(nf*2, h1), nn.ReLU(inplace=True),
                  nn.BatchNorm1d(h1), nn.Dropout(2*d), 
                  nn.Linear(h1, n_out)]
    model = nn.Sequential(*layers)
    if init is not None: model.apply(init_weights)
    return model

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image

def process_image(image_encoded):
    pil_image = read_image(image_encoded)
    test_aug = transforms.Compose([transforms.Resize((224,224)),
                                transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                ])
    image = test_aug(pil_image)
    image = image.unsqueeze(0)
    return image

def softmax_output(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

sample_images = os.listdir('test_images/')

classes = ['Apple -- Apple Scab',
    'Apple -- Black Rot',
    'Apple -- Cedar Apple Rust',
    'Apple -- Healthy',
    'Cherry -- Powdery Mildew',
    'Cherry --  Healthy',
    'Corn -- Gray Leaf Spot (Cercospora Leaf Spot)',
    'Corn -- Common Rust',
    'Corn -- Northern Leaf Blight',
    'Corn -- Healthy',
    'Grape -- Black Rot',
    'Grape -- Esca (Black Measles)',
    'Grape -- Leaf Blight (Isariopsis Leaf Spot)',
    'Grape -- Healthy',
    'Peach -- Bacterial_spot',
    'Peach -- Healthy',
    'Pepper Bell -- Bacterial Spot',
    'Pepper Bell -- Healthy',
    'Potato -- Early Blight',
    'Potato -- Late Blight',
    'Potato -- Healthy',
    'Strawberry -- Leaf Scorch',
    'Strawberry -- Healthy',
    'Tomato -- Bacterial Spot',
    'Tomato -- Early Blight',
    'Tomato -- Late Blight',
    'Tomato -- Leaf Mold',
    'Tomato -- Septoria Leaf Spot',
    'Tomato -- Two-spotted Spider Mites',
    'Tomato -- Target Spot',
    'Tomato -- Yellow Leaf Curl Virus',
    'Tomato -- Mosaic Virus',
    'Tomato -- Healthy']