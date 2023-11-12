import os
import albumentations as A
import cv2
import numpy as np
from PIL import Image

def transform_img(img_path, save_path, filename):
    
    transform = A.Compose([
    #A.Resize(height = 512, width = 512),
    A.RandomResizedCrop(p=1, height= 820 ,width= 820, scale=(0.4, 0.75),ratio=(0.40, 1.10)),
    A.RandomBrightnessContrast(always_apply=True, p=1.0, brightness_limit=(0, 0.3), contrast_limit=(-0.2, 0.3), brightness_by_max=False),
    A.SafeRotate(always_apply=False, p=0.5, limit=(-10, 30), interpolation=1, border_mode=0, value=None, mask_value=None),
    A.CLAHE(always_apply=False, p=0.5, clip_limit=(1, 15), tile_grid_size=(8, 8)),
    A.CenterCrop(always_apply=True, p=1, height=512, width=512)
    ])
    
    im_bgr = cv2.imread(img_path)
    
    # BGR -> RGB
    img = im_bgr[:, :, ::-1]
    preprocessed_img = transform(image=img)["image"]
    
    # 전처리한 이미지 저장
    file_name = f"{filename}_preprocessed.jpg"
    saved_path =os.path.join(save_path,file_name)
    
    img_array = Image.fromarray(preprocessed_img.astype(np.uint8))
    img_array.save(saved_path)
    
    return saved_path