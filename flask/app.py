from flask import Flask, request, render_template, url_for, redirect
import os, uuid
import preprocessing, sentimental, ocr, yolo_classifier, database, ensemble #postprocessing,
import TTS



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
    print("classification_result : ", classification_result)
    # OCR 모델에 대한 sentimental 모델 결과
    sentimental_result = sentimental.sentimental(ocr_result)
    
    # OCR 모델에 대한 sentimental 모델 결과와 약 이미지 분류기 앙상블 (voting) 결과 idx 
    idx = ensemble.soft_voting(sentimental_result, classification_result)
    # idx = int(max(classification_result[0])) #yolo만

    # Database에서 해당 약에 대한 정보 불러오기
    result_name, result_type = database.result(idx)

    #오디오파일 생성 및 저장
    text = TTS.make_text(idx, result_type, result_name)
    filename = TTS.save_tts(text)
    return render_template("result.html", result_name = result_name, result_type = result_type, filename = f"uploads/{uploaded_uuid}.png")
    
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
    app.run(debug=True, host='172.20.10.3', port=5000)
    # app.run(debug = True, port = 5004, threaded=True)
