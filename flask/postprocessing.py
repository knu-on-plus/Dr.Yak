import re

def remove_missing_value(results):
    texts = []
    for i in range(len(results[0])):
        text = results[0][i][1][0]
        texts.append(text)
    filtered_words = [word for word in texts if re.fullmatch(r'[가-힣]{3,4}', word)]
    # 리스트를 하나의 문자열로 변환
    filtered_words = set(filtered_words)
    combined_string = ' '.join(filtered_words)
    return combined_string