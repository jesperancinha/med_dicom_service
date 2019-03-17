#!flask/bin/python
import os
import configparser
from flask import Flask, request
from werkzeug import secure_filename

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

@app.route('/')
def index():
    return "This is a start of a great Med application!"

@app.route('/upload', methods=['POST'])
def getfile():
        file = request.files['dicom']
        filename = secure_filename(file.filename)

        file.save(os.path.join(config['DEFAULT']['REPO_FOLDER'], filename))

        return 'OK'

if __name__ == '__main__':
    app.run(debug=True)