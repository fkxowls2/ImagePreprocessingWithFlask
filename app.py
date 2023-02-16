from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        # img = Image.open(f)
        print(f.filename)
        image_save_path = './static/img/init_image.png'
        f.save(image_save_path)
        
    return render_template('index.html', image_file=image_save_path)
   
   
    
if __name__ == '__main__':
    app.run(debug=True)