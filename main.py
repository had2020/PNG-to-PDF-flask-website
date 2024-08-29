from flask import Flask, render_template, send_file, request
from flask_cors import CORS
from generate import generate_pdf
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
  file = request.form['file']
  pdf = str(generate_pdf(file))
  result = "Button clicked!"
  return send_file(pdf), render_template('result.html', result=result)
  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001) # change to ip and port for non-debug