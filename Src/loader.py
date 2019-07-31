import torch
import torchvision.transforms 
from torchvision import datasets
import PIL

DATA_PATH_TRAIN = '../Data/dataset/train/'
DATA_PATH_VALID = '../Data/dataset/valid/'
DATA_PATH_TEST = '../Data/dataset/test/'

def data_generator(BATCH_SZ=32):
    transform = torchvision.transforms.Compose([
        torchvision.transforms.RandomResizedCrop(224),
        torchvision.transforms.ToTensor(),
        # Cutout(n_holes=1, length=16),
        torchvision.transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)), #R,G,B每层的归一化用到的均值和方差
    ])

    # # show image
    # train_set = datasets.ImageFolder(root=DATA_PATH_TRAIN, transform=transform)
    # train_set.class_to_idx
    # img = torchvision.transforms.ToPILImage()(train_set[0][0]).convert('RGB')
    # img.show() 

    train_loader = torch.utils.data.DataLoader(
        dataset=datasets.ImageFolder(root=DATA_PATH_TRAIN, transform=transform),
        batch_size=BATCH_SZ, 
        shuffle=True,               
    )

    valid_loader = torch.utils.data.DataLoader(
        dataset=datasets.ImageFolder(root=DATA_PATH_VALID, transform=transform),
        batch_size=BATCH_SZ, 
        shuffle=True,               
    )

    test_loader = torch.utils.data.DataLoader(
        dataset=datasets.ImageFolder(root=DATA_PATH_TEST, transform=transform),
        batch_size=BATCH_SZ, 
        shuffle=True,               
    )

    return train_loader, valid_loader, test_loader

if __name__ == "__main__":
    """ generate data loader """
    train_loader, valid_loader, test_loader = data_generator()
    # # display image
    # img = torchvision.transforms.ToPILImage()(train_loader.dataset[0][0]).convert('RGB')
    # img.show() 
    # # print class_to_idx
    # print(train_loader.dataset.class_to_idx)
    # # print size
    # print(len(train_loader.dataset))
    