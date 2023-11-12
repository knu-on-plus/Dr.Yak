from flask import Flask, request, render_template, url_for, redirect
import os, uuid
import preprocessing, postprocessing, sentimental, ocr, yolo_classifier, database, ensemble
#import TTS



app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')


@app.route('/', methods=['GET', "POST"])
def form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_uuid = str(uuid.uuid4())
    uploaded_file_path = f'static/uploads/{uploaded_uuid}.png'
    
    # 업로드 파일 저장
    uploaded_file = request.files['image']
    uploaded_file.save(uploaded_file_path)

    # 이미지 전처리
    preprocessed_path =  f'static/preprocessed_img'
    img_path = preprocessing.transform_img(uploaded_file_path, preprocessed_path, uploaded_uuid)
    
    # OCR 모델 결과
    ocr_result = ocr.paddle_ocr(img_path)

    # 약 이미지 분류기
    classification_result =yolo_classifier.classifier(img_path)

    # OCR 모델에 대한 sentimental 모델 결과
    sentimental_result = sentimental(ocr_result)
    
    # OCR 모델에 대한 sentimental 모델 결과와 약 이미지 분류기 앙상블 (voting) 결과 idx 
    idx = ensemble(sentimental_result, classification_result)
    
    # Text To Speech 음성 파일 실행
    #tts_filename = TTS.save_tts(idx)

    # Database에서 해당 약에 대한 정보 불러오기
    result_name, result_type = database.result(idx)

    return render_template("result.html", result_name = result_name, result_type = result_type, filename = tts_filename)
    
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
