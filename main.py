from flask import Flask, render_template, send_file, request
from generate import pngtopdf
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder where files will be saved
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size 16MB

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
  if 'file' not in request.files:
      return 'No file part', 400
  file = request.files['file']
  if file.filename == '':
      return 'No selected file', 400
  if file:
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(filepath)
      return 'File successfully uploaded to ' + filepath, 200
  return render_template('result.html')
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001) # change to ip and port for non-debug