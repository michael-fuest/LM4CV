import os
import numpy as np
import torch
from PIL import Image

from dataset import images4LMU


def main():
    dataset = images4LMU('./data/')

if __name__ == '__main__':
    main()