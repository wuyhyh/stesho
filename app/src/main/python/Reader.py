import cv2
import torch

def getPicture(file_path):
    img = torch.from_numpy(cv2.resize(cv2.imread(file_path), (224, 224)) / 255).permute(2,1,0).float()
    return img