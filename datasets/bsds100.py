
import imageio
import numpy as np
import os
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
from PIL import Image
from pathlib import Path
from torchvision.transforms import transforms

class BSDSDataset(Dataset):
    dataset_dir = "bsds100"
    dataset_url = "https://www.kaggle.com/datasets/msahebi/super-resolution"
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    def __init__(self, data_dir:str='data', transform=transform):
        super().__init__()
        self.paths = list(Path(data_dir).rglob("*.png"))
        self.transform = transform

    def load_image(self, index:int)->Image.Image:
        image_path = self.paths[index]
        return Image.open(image_path)
    
    def __len__(self):
        return len(self.paths)
    
    def __getitem__(self, index:int):
        target = []
        img = self.load_image(index)
        img = np.array(img)

        if self.transform != None:
            return self.transform(img).permute(1, 2, 0)
        
        target = tuple(target) if len(target) > 1 else target[0]
        return img.permute(1, 2, 0), target
    
if __name__ == '__main__':

    dataset = BSDSDataset("/mnt/apple/k66/ptrang/DDNM/exp/datasets/sr/BSDS100/")
    

    print(len(dataset))

    img = dataset[0]
    
    print(img.shape)

    plt.imshow(img)
    plt.show()