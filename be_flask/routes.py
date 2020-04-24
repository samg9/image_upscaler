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
        original,output =esrgan_load_generate(destination, filename)
        images = {
            'Original': original,
            'SRGAN': output,
        }
        print("type of original: ", type(original))
        print("type of output: ",type(output))
        # l = "orginal:::::::::, {}".format(base64.b64encode(original))
        # ll = "outoput:::::::::, {}".format(base64.b64encode(output))
        # print("l and ll" , l, " : ", ll)
        # Plot the images. Note: rescaling and using squeeze since we are getting batches of size 1
        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        for i, (title, img) in enumerate(images.items()):
            axes[i].imshow(img)
            axes[i].set_title("{} - {}".format(title, img.shape))
            axes[i].axis('off')

        i = io.BytesIO()
        plt.savefig(i, format='png', bbox_inches='tight')
        encode64 = base64.b64encode(i.getvalue())
        return "data:image/png;base64, {}".format(encode64.decode('utf-8'))
    except Exception as e:
        print("error: ",e)
        return "Unable to upload", 404

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    app.run(debug=True, threaded=True, port=5000 ,use_reloader=False)