import os
import random
import torch
import logging
import numpy as np

color2idx = {
    (0, 0, 0): 0,
    (255, 255, 0): 1,
    (150, 80, 0): 2,
    (100, 100, 100): 3,
    (0, 0, 150): 4,
    (0, 255, 0): 5,
    (0, 125, 0): 6,
    (150, 150, 250): 7,
    (255, 255, 255): 8
}

idx2color = { v: k for k, v in color2idx.items() }

def init_logger():
    logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=logging.INFO,
        )

def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def rgb_to_cat(rgb_arr):
    arr = np.ndarray(shape=rgb_arr.shape[:2], dtype=np.uint8)
    arr[:,:] = 8
    for rgb, idx in color2idx.items():
        arr[(rgb_arr==rgb).all(2)] = idx
        
    return arr

def cat_to_rgb(cat_arr):
    arr = np.zeros((*cat_arr.shape[:2], 3), dtype=np.uint8)
    arr[:,:] = (255, 255, 255)
    for idx, rgb in idx2color.items():
        arr[(cat_arr==idx)] = rgb
    
    return arr