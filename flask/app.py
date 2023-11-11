from flask import Flask, request, render_template, send_from_directory, url_for, redirect
# chatGPT 라이브러리가 실제로 존재하지 않으므로 대체되었습니다. 적절한 라이브러리를 사용해주세요.
# import chatGPT
import tempfile
import os
import torch
import time

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')


@app.route('/', methods=['GET', "POST"])
def form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    print(uploaded_file)
    uploaded_file.save('static/uploads/uploaded_image.png')
    
    # appear loading div
    #  model's result will set heres
    time.sleep(5) # let's say this is the model's inference
    # disappear loading div
    result_name, result_type  = "타이레놀", "각성제"
    # return redirect(url_for('result', result_name = result_name, result_type = result_type))
    return render_template("result.html", result_name = result_name, result_type = result_type)


# @app.route('/result', methods = ['GET', 'POST'])
# def result():
#     result_name = request.args.get('result_name')
#     result_type = request.args.get('result_type')
#     print(result_type, result_name)
#     return render_template("result.html", result_name = result_name, result_type = result_type)
    



if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    # app.run(debug=True, host='172.16.2.75', port=5000)
    app.run(debug = True, port = 5004, threaded=True)
