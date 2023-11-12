import os
import albumentations as A
import cv2
import numpy as np
from PIL import Image

def transform_img(img_path, preprocessed_path, filename):
    
    transform = A.Compose([
    A.Resize(height = 820, width = 820),
    A.RandomBrightnessContrast(always_apply=True, p=1.0, brightness_limit=(-0.1, 0.2), contrast_limit=(0.7, 0.9), brightness_by_max=False),
    A.CenterCrop(always_apply=True, p=1, height=512, width=512)
    ])
    
    im_bgr = cv2.imread(img_path)
    
    # BGR -> RGB
    img = im_bgr[:, :, ::-1]
    preprocessed_img = transform(image=img)["image"]
    
    # 전처리한 이미지 저장
    file_name = f"{filename}.jpg"
    saved_path =os.path.join(preprocessed_path,file_name)
    
    img_array = Image.fromarray(preprocessed_img.astype(np.uint8))
    img_array.save(saved_path)
    
    return saved_path