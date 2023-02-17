from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import shutil
import cv2



app = Flask(__name__)
CORS(app)

originalSavePath = './static/img/original.png'
preporcessingSavePath = './static/img/preprocessing.png'
preprocessingMethod = "전처리 기법을 선택해 주세요"
slideDisplay = "display:none"


@app.route('/')
def index():
    return render_template('index.html', preprocessingMethod=preprocessingMethod, slideDisplay=slideDisplay)


@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        # img = Image.open(f)
        f.save(originalSavePath)
        shutil.copy(originalSavePath, preporcessingSavePath)
        
    return render_template('index.html', preprocessingMethod=preprocessingMethod, originalImagePath=originalSavePath,
                           slideDisplay=slideDisplay)


@app.route('/color_to_gray', methods=['GET', 'POST'])
def color_to_gray():
    slideDisplay = "display:none"
    if request.method == 'POST':
        preprocessingMethod = "흑백 이미지 만들기"
        img = cv2.imread(originalSavePath, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(preporcessingSavePath, img)
        
    return render_template('index.html', preprocessingMethod=preprocessingMethod, originalImagePath=originalSavePath,
                           preprocessingImagePath=preporcessingSavePath, slideDisplay=slideDisplay)


@app.route('/make_binary', methods=['GET', 'POST'])
def make_binary():
    defaultSlideValue = 127
    if request.method == 'POST':
        preprocessingMethod = "바이너리로 만들기"
        img = cv2.imread(originalSavePath, cv2.IMREAD_GRAYSCALE)
        _, img = cv2.threshold(img, defaultSlideValue, 255, cv2.THRESH_BINARY)
        cv2.imwrite(preporcessingSavePath, img)
        
    return render_template('index.html', preprocessingMethod=preprocessingMethod, originalImagePath=originalSavePath, 
                           preprocessingImagePath=preporcessingSavePath, slideValue=defaultSlideValue)   


@app.route('/slide_binary', methods=['POST'])
def slide_binary():
    slideValue = int(request.form['value'])
    img = cv2.imread(originalSavePath, cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, slideValue, 255, cv2.THRESH_BINARY)
    cv2.imwrite(preporcessingSavePath, img)
    return ""

    
    
if __name__ == '__main__':
    # default port=5000
    app.run(debug=True, port=5000)