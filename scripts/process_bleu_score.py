import sys
import torchvision.datasets as dset

print(sys.argv)

# load the data with cocoAPI this time we dont need transform
cap = dset.CocoCaptions(root = '../coco-dataset/train2017',
                        annFile = '../coco-dataset/annotations/captions_train2017.json',
                        transform=centre_crop)

