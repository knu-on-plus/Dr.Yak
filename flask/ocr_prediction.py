import pandas as pd
from konlpy.tag import Okt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle
from joblib import dump, load

okt = Okt()
clf = load('ocr_clf.joblib')


def predict_emotion(model, input_text):
    # 입력 텍스트 형태소 분석 및 토큰화
    tokenized_input = okt.morphs(input_text)
    
    # 입력 텍스트 단어 벡터화
    input_vector = vectorizer.transform([' '.join(tokenized_input)])
    
    # 모델을 사용하여 감정 예측
    prediction = model.predict(input_vector)
    
    return prediction[0]


label_mapping = {
    0: '레피콜', 
    1: '타이레놀', 
    2: '제로민'
        }

# 예제 입력
if __name__ == "__main__":
    input_string = "불면증의 엄시적 일시적 새르자 제로민의 어린이"
    predicted_emotion = predict_emotion(clf, input_string)
    print(f'입력 텍스트: {input_string}')
    print(f'예측된 감정 클래스: {label_mapping[predicted_emotion]}')