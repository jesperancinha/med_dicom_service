#!flask/bin/python
import os
import configparser
import pydicom
from flask import Flask, request
from werkzeug import secure_filename

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)


@app.route('/all')
def list_all():
    return_string = '<table>'
    return_string += '<tr>'
    return_string += '<th>Patient Name</th>'
    return_string += '<th>Patient ID</th>'
    return_string += '<th>Photometric Interpretation</th>'
    return_string += '</tr>'
    for r, d, f in os.walk(os.path.join(config['DEFAULT']['REPO_FOLDER'])):
        for file in f:
            ds = pydicom.dcmread(os.path.join(config['DEFAULT']['REPO_FOLDER'], file))
            return_string += '<tr>'
            return_string += '<td>' + str(ds.PatientName) + '</td>'
            return_string += '<td>' + str(ds.PatientID) + '</td>'
            return_string += '<td>' + str(ds.PhotometricInterpretation) + '</td>'
        return_string += '</tr>'
    return return_string + '</table>'

@app.route('/')
def index():
    return "This is a start of a great Med application!"

@app.route('/upload', methods=['POST'])
def getfile():
        file = request.files['dicom']
        filename = secure_filename(file.filename)

        repo_filename = os.path.join(config['DEFAULT']['REPO_FOLDER'], filename)
        file.save(repo_filename)

        ds = pydicom.dcmread(repo_filename)
        return str(ds.PatientName)

if __name__ == '__main__':
    app.run(debug=True)