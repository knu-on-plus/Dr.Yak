import albumentations as A
import cv2
import platform
import numpy as np
import pandas as pd
import os
from PIL import ImageFont, ImageDraw, Image
from paddleocr import PaddleOCR, draw_ocr
from paddleocr.paddleocr import MODEL_URLS

ocr = PaddleOCR(lang="korean")

# Declare an augmentation pipeline
transform = A.Compose([
    A.Resize(height = 812, width = 375),
    A.RandomBrightnessContrast(always_apply=True, p=1.0, brightness_limit=(-0.1, 0.2), contrast_limit=(0.7, 0.9), brightness_by_max=False),
    A.CenterCrop(always_apply=True, p=1, height=375, width=375)
])
transform_o = A.Compose([
    A.Resize(height = 400, width = 256)
])


meds = ['zeromin', 'lepical', 'tylenol']
save_path = './Data/preprocessed_img_2/'
os.makedirs(save_path, exist_ok=True)



for med in meds:
    img_path = './test_data/'+med+'.png'
    im_bgr = cv2.imread(img_path)
    img = im_bgr[:, :, ::-1]
    transformed_img = transform(image=img)["image"]
    img_array = Image.fromarray(transformed_img.astype(np.uint8))
    file_name = f"{med}_preprocessed.jpg"
    img_array.save(os.path.join(save_path,file_name))
    img_path = os.path.join(save_path,file_name)
    result = ocr.ocr(img_path, cls=False)
    texts = []
    for i in range(len(result[0])):
        text = result[0][i][1][0]

        texts.append(text)
    print(texts)

    # 숫자가 포함된 문자열과 2자 이하인 문자열 제거
    filtered_words = [word for word in texts if not any(char.isdigit() for char in word) and 2 < len(word) < 5 ]

    print(set(filtered_words))
    # 리스트를 하나의 문자열로 변환
    filtered_words = set(filtered_words)
    combined_string = ' '.join(filtered_words)
    print(combined_string)

