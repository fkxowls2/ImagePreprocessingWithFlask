from flask import Flask, render_template, request, redirect, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import shutil
import cv2
from utils import function_binary, function_normalize, function_adthreshold, function_blob, function_blur



app = Flask(__name__)
CORS(app)

originalSavePath = './static/img/original.png'
preporcessingInitSavePath = './static/img/init_preprocessing.png'
preporcessingSavePath = './static/img/preprocessing.png'
isUpload = False

binaryValue = 127
normalizeValue = 1
adThresholdValue = 15
blobValue = 0
blurWidthValue, blurHeightValue, blurSigmaValue = 0, 0, 1



@app.route('/')
def index():
    global binaryValue, normalizeValue, adThresholdValue, blobValue
    binaryValue, normalizeValue, adThresholdValue, blobValue = 127, 1, 15, 10
    global blurWidthValue, blurHeightValue, blurSigmaValue
    blurWidthValue, blurHeightValue, blurSigmaValue = 0, 0, 1
    
    return render_template('index.html')


@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        # img = Image.open(f)
        f.save(originalSavePath)
        shutil.copy(originalSavePath, preporcessingInitSavePath)
        shutil.copy(originalSavePath, preporcessingSavePath)
        global isUpload; isUpload = True
            
    return render_template('upload.html', originalImagePath=originalSavePath)


@app.route('/load_original', methods=['POST'])
def load_original():
    _ = str(request.form['value'])
    shutil.copy(originalSavePath, preporcessingInitSavePath)
    shutil.copy(originalSavePath, preporcessingSavePath)
    return ""


@app.route('/color_to_gray', methods=['GET', 'POST'])
def color_to_gray():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
            img = cv2.imread(preporcessingInitSavePath, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(preporcessingSavePath, img) 
        return render_template('gray.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)
    else:
        return "이미지를 먼저 업로드 해주세요"


@app.route('/make_binary', methods=['GET', 'POST'])
def make_binary():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
            function_binary(preporcessingInitSavePath, binaryValue, preporcessingSavePath) 
        return render_template('binary.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath,
                               slideValue=binaryValue)   
    else:
        return "이미지를 먼저 업로드 해주세요"

@app.route('/slide_binary', methods=['POST'])
def slide_binary():
    global binaryValue
    binaryValue = int(request.form['value'])
    function_binary(preporcessingInitSavePath, binaryValue, preporcessingSavePath)
    return ""


@app.route('/make_normalize', methods=['GET', 'POST'])
def make_normalize():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
            function_normalize(preporcessingInitSavePath, preporcessingSavePath)
        return render_template('normalize.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)
    else:
        return "이미지를 먼저 업로드 해주세요"


@app.route('/make_adthreshold', methods=['GET', 'POST'])
def make_adthreshold():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
            function_adthreshold(preporcessingInitSavePath, adThresholdValue, preporcessingSavePath)
        return render_template('adthreshold.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath,
                               slideValue=adThresholdValue)    
    else:
        return "이미지를 먼저 업로드 해주세요"
    
@app.route('/slide_adthreshold', methods=['POST'])
def slide_adthreshold():
    global adThresholdValue
    adThresholdValue = int(request.form['value'])
    function_adthreshold(preporcessingInitSavePath, adThresholdValue, preporcessingSavePath)
    return ""


@app.route('/make_blob', methods=['GET', 'POST'])
def make_blob():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        return render_template('blob.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)    
    else:
        return "이미지를 먼저 업로드 해주세요"
    
@app.route('/action_blob', methods=['POST'])
def action_blob():
    global blobValue
    blobValue = int(request.form['value'])
    function_blob(preporcessingInitSavePath, blobValue, preporcessingSavePath)
    return ""

    
@app.route('/make_blur', methods=['GET', 'POST'])
def make_blur():
    if isUpload:
        if request.method == 'POST':
            shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        return render_template('blur.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)    
    else:
        return "이미지를 먼저 업로드 해주세요"
    
@app.route('/action_blur', methods=['POST'])
def action_blur():
    global blurWidthValue, blurHeightValue, blurSigmaValue
    jsonData = request.get_json()
    blurWidthValue, blurHeightValue, blurSigmaValue = int(jsonData['widthValue']), int(jsonData['heightValue']), int(jsonData['sigmaValue'])
    function_blur(preporcessingInitSavePath, blurWidthValue, blurHeightValue, blurSigmaValue, preporcessingSavePath)
    return ""
    
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # default port=5000