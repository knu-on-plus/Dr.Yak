from main import MyPaddleOCR
import albumentations as A
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from PIL import Image
import IPython





ocr = MyPaddleOCR()
img_path = os.path.join(save_path,file_name)
ocr.run_ocr(img_path, debug=True)