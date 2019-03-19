#!flask/bin/python
import os
import configparser
import pydicom
from flask import Flask, request
from werkzeug import secure_filename
from pynetdicom import AE, VerificationPresentationContexts

# ae = AE(ae_title=b'MY_ECHO_SCP')
#
# ae.supported_contexts = VerificationPresentationContexts
#
# ae.start_server(('127.0.0.1', 11112), block=True)

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

        repo_filename = os.path.join(config['DEFAULT']['REPO_FOLDER'], filename)
        file.save(repo_filename)

        ds = pydicom.dcmread(repo_filename)
        return str(ds.PatientName)

if __name__ == '__main__':
    app.run(debug=True)