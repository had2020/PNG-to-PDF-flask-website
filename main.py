from flask import Flask, render_template, send_file, request , jsonify
from generate import pngtopdf
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# check the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_save_path)
        
        pngtopdf(image_save_path)

        #return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
        os.remove(image_save_path)
        return send_file('pdf-with-image.pdf', as_attachment=True, mimetype='application/pdf')
    else:
        return jsonify({'error': 'File type not allowed'}), 400
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001) # change to ip and port for non-debug