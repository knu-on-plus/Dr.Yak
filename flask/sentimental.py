import database
import pandas as pd
from konlpy.tag import Okt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
from joblib import dump, load

okt = Okt()
clf = load('ocr_clf.joblib')
vectorizer = load('vectorizer.joblib')
vectorizer._validate_vocabulary()

def predict_emotion(model, input_text):
    # 입력 텍스트 형태소 분석 및 토큰화
    tokenized_input = okt.morphs(input_text)
    
    # 입력 텍스트 단어 벡터화
    input_vector = vectorizer.transform([' '.join(tokenized_input)])
    
    # 모델을 사용하여 감정 예측
    prediction = model.predict(input_vector)
    probabilities = model.predict_proba(input_vector)
    probs = np.round(probabilities, 2)
    return probs


def sentimental(text):
    predicted_probs = predict_emotion(clf, text)
    # result_name_sent, result_type_sent = database.result(predicted_emotion)
    print(f'입력 텍스트: {text}')
    print(f'예측된 약 클래스: {[predicted_probs]}')
    print(f'예측된 약 이름: {database.result(predicted_probs)}')


    return predicted_probs








if __name__ == "__main__":
    text = '일치적 보호옹 입시적 어린이 타이레놀 임시적 보호온 불면증의 안전포'
    a = sentimental(text)
    print(a)





    


