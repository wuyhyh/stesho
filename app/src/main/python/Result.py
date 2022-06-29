from ResNet import resnet34
from Reader import getPicture
import torch
import numpy as np


def getResult(file_path):
    result = 0
    device = torch.device('cpu')

    model = resnet34()
    model.ro(device)

    img = getPicture(file_path)
    img = img.to(device)

    result = model(img)

    output = np.argmax(result, axis=1)

    return output