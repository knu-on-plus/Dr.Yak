
from paddleocr import PaddleOCR
import re

max_text_length= 2
drop_score = 0.9

def remove_missing_value(result):
    texts = []
    print(result[0])
    
    for i in range(len(result[0])):
        text = result[0][i][1][0]
        texts.append(text)
    filtered_words = [word for word in texts if re.fullmatch(r'[가-힣]{3,4}', word)]
    # 리스트를 하나의 문자열로 변환
    filtered_words = set(filtered_words)
    combined_string = ' '.join(filtered_words)
    return combined_string

def paddle_ocr(saved_path):
    # PaddleOCR 객체 모델 선언
    ocr = PaddleOCR(lang='korean', max_text_length=max_text_length, drop_score=drop_score) 
    result = ocr.ocr(saved_path, cls=False)
    return remove_missing_value(result)

