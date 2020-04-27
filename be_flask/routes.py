from flask import Flask, request, Response, make_response, jsonify, redirect, url_for, session
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from esrgan.esrgan import esrgan_load_generate
import json
import os
import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/samurai/Documents/image_upscaler/be_flask/'
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
        orig,output =esrgan_load_generate(destination, filename)
        img = Image.fromarray(output.astype("uint8")) 
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        buffered.seek(0)
        img_byte = buffered.getvalue()
        img_str = "data:image/png;base64," + base64.b64encode(img_byte).decode()
        return img_str
    except Exception as e:
        print("error: ",e)
        return "Unable to upload", 404

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    app.run(debug=True, threaded=True, port=5000 ,use_reloader=False)