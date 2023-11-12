from flask import Flask, request, render_template, send_from_directory, url_for, redirect
# chatGPT 라이브러리가 실제로 존재하지 않으므로 대체되었습니다. 적절한 라이브러리를 사용해주세요.
# import chatGPT
import tempfile
import os
import torch
import time
import TTS
from ultralytics import YOLO

dic = {0: ['레피콜', '감기약', '1일 3회 식후 30분에 2캡슐씩 복용 가능합니다.'], 
       1: ['타이레놀', '진통제', '1회 1~2정씩 1일 3~4회 필요시 복용합니다. 1일 최대 8정 복용 가능합니다.'],
       2: ['제로민', '수면제', '1일 1회 취침 전 복용합니다.']
        }

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')


@app.route('/', methods=['GET', "POST"])
def form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    ##이미지, 오디오 초기화
    # if os.path.exists('static/uploads/uploaded_image.png'):
    #     os.remove('static/uploads/uploaded_image.png')
    # if os.path.exists('static/temp_description.mp3'):
    #     os.remove('static/temp_description.mp3')
    #     print("audio deleted")

    uploaded_file = request.files['image']
    print(uploaded_file)
    uploaded_file.save('static/uploads/uploaded_image.png')
    model = YOLO("yolo_clf.pt")
    results = model('static/uploads/uploaded_image.png') 
    result_name = dic[results[0].probs.top1][0]
    result_type = dic[results[0].probs.top1][1]
    result_desc = f"{result_type}, {result_name}의 복용방법과 주의사항을 알려드릴게요." +"   "+ dic[results[0].probs.top1][2]
    print(result_name)
    print(result_type)
    print(result_desc)
    filename = TTS.save_tts(result_desc)
    return render_template("result.html", result_name = result_name, result_type = result_type, filename = filename)


# @app.route('/result', methods = ['GET', 'POST'])
# def result():
#     result_name = request.args.get('result_name')
#     result_type = request.args.get('result_type')
#     print(result_type, result_name)
#     return render_template("result.html", result_name = result_name, result_type = result_type)
    
@app.route('/goback', methods=['GET'])
def go_back():
    ##이미지, 오디오 초기화
    if os.path.exists('static/uploads/uploaded_image.png'):
        os.remove('static/uploads/uploaded_image.png')
        print("img deleted")
    if os.path.exists('static/temp_description.mp3'):
        os.remove('static/temp_description.mp3')
        print("audio deleted")
    return redirect(url_for('form'))


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    # app.run(debug=True, host='172.16.2.75', port=5000)
    app.run(debug = True, port = 5004, threaded=True)
