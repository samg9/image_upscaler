from flask import Flask, request, Response, jsonify
from flask import Flask, request, Response, jsonify, redirect, url_for, session
from flask_cors import CORS, cross_origin
from flask import Flask, make_response
from scraper.scraper import get_profile, scrape
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/samurai/code/couleur/be_flask/'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "70l0"

# file upload 
@app.route('/api/upload', methods=['POST'])
@cross_origin()
def fileUpload():
    try:
        target=os.path.join(UPLOAD_FOLDER,'test_docs')
        if not os.path.isdir(target):
            os.mkdir(target)
        file = request.files['file']
        filename = secure_filename(file.filename)
        destination="/".join([target, filename])
        file.save(destination)
        session['uploadFilePath']=destination
        return "successfully Uploaded", 202
    except Exception as e:
        print("error: ",e)
        return "Unable to upload", 404

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    app.run(debug=True, threaded=True, port=5000 ,use_reloader=False)