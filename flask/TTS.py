# cede by jake
from gtts import gTTS
import database
import playsound as ps

# pip install gTTS
# pip install playsound
# pip install pyobjc

# 타이레놀 = 0 , 래피콜 = 1, 제로민 = 2

# move to json DB later on
# text_0 = "타이레놀 설명 타이레놀 설명 타이레놀 설명"
# text_1 = "래피콜 설명 래피콜 설명 래피콜 설명"
# text_2 = "제로민 설명 제로민 설명 제로민 설명"

file_name = 'static/temp_description.mp3'

def make_text(idx, result_type, result_name):
    result_name, result_type = database.result(idx)
    text = f"{result_type}, {result_name}의 복용방법과 주의사항을 알려드릴게요." +"   "+ database.dic[idx][2]
    return text

def save_tts(text):
    # text = make_text(idx)
    tts_ko = gTTS(text=text,
                  lang='ko',    # 언어
                  slow=True,   # 속도조절
                  )
    
    tts_ko.save(file_name)
    return 'temp_description.mp3'

def play_desc(text):
    sound = save_tts(text)
    ps.playsound(sound)

# if __name__ == "__main__":
#     text = text_0
#     play_desc(text)
