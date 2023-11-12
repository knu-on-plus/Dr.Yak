
import os
import uuid

import preprocessing, postprocessing
from paddleocr import PaddleOCR

# 난수, 경로 파라미터
unique_filename = str(uuid.uuid4())
img_path = ''
save_path = ''
max_text_length= 2
drop_score = 0.9


saved_path = preprocessing.transform_img(img_path, save_path, unique_filename)
# PaddleOCR 객체 모델 선언
ocr = PaddleOCR(lang='korean', max_text_length=max_text_length, drop_score=drop_score) 

results = ocr.ocr(saved_path, cls=False)

