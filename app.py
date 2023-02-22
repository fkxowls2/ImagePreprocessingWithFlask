from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from werkzeug.utils import secure_filename
import shutil
import cv2
from utils import function_binary, function_normalize, function_adthreshold



app = Flask(__name__)
CORS(app)

originalSavePath = './static/img/original.png'
preporcessingInitSavePath = './static/img/init_preprocessing.png'
preporcessingSavePath = './static/img/preprocessing.png'
binaryValue = 127
normalizeValue = 1
adThresholdValue = 15


@app.route('/')
def index():
    global binaryValue, normalizeValue, adThresholdValue
    binaryValue, normalizeValue, adThresholdValue = 127, 1, 15
    return render_template('index.html')

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        # img = Image.open(f)
        f.save(originalSavePath)
        shutil.copy(originalSavePath, preporcessingInitSavePath)
        shutil.copy(originalSavePath, preporcessingSavePath)
        
    return render_template('upload.html', originalImagePath=originalSavePath)

@app.route('/load_original', methods=['POST'])
def load_original():
    _ = str(request.form['value'])
    shutil.copy(originalSavePath, preporcessingInitSavePath)
    shutil.copy(originalSavePath, preporcessingSavePath)
    return ""

@app.route('/color_to_gray', methods=['GET', 'POST'])
def color_to_gray():
    if request.method == 'POST':
        shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        img = cv2.imread(preporcessingInitSavePath, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(preporcessingSavePath, img)
        
    return render_template('gray.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)

@app.route('/make_binary', methods=['GET', 'POST'])
def make_binary():
    if request.method == 'POST':
        shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        function_binary(preporcessingInitSavePath, binaryValue, preporcessingSavePath)
        
    return render_template('binary.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath,
                           binaryValue=binaryValue)   

@app.route('/slide_binary', methods=['POST'])
def slide_binary():
    global binaryValue
    binaryValue = int(request.form['value'])
    function_binary(preporcessingInitSavePath, binaryValue, preporcessingSavePath)
    return ""

@app.route('/make_normalize', methods=['GET', 'POST'])
def make_normalize():
    if request.method == 'POST':
        shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        function_normalize(preporcessingInitSavePath, preporcessingSavePath)

    return render_template('normalize.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)

@app.route('/make_adthreshold', methods=['GET', 'POST'])
def make_adthreshold():
    if request.method == 'POST':
        shutil.copy(preporcessingSavePath, preporcessingInitSavePath)
        function_adthreshold(preporcessingInitSavePath, adThresholdValue, preporcessingSavePath)

    return render_template('adthreshold.html', originalImagePath=preporcessingInitSavePath, preprocessingImagePath=preporcessingSavePath)    
    
    
    
    
if __name__ == '__main__':
    # default port=5000
    app.run(debug=True, port=5000)