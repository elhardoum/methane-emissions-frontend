from flask import Flask, request, send_from_directory, jsonify
from os import environ
import config
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import json
import imageio

app = Flask(__name__,
    static_url_path='/',
    static_folder='www')
app.secret_key = environ.get('FLASK_SECRET', config.FLASK_SECRET)

def predict_and_show_filename(model, input):
    img = imageio.imread(input)
    img = tf.cast(img, tf.float32) / 255.
    img = tf.image.resize(img, size=[217, 217])
    img = tf.slice(img, [0, 0, 0], [-1, -1, 3]) # extract first 3 channels
    pred = model.predict(img[tf.newaxis, ...])
    # plt.imshow(img)
    return json.loads(str(pred).strip())

def get_model():
    json_file = open(config.MODEL_SETTINGS_LOCATION, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(config.MODEL_LOCATION)
    return loaded_model

model = get_model()

@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def index(path):
    return send_from_directory('www', path)

@app.route('/api/post-image', methods=['POST'])
def upload():
    file = request.files.get('File') if request.files and 'File' in request.files.keys() else None

    if not file:
        return jsonify(None, 400)

    global model

    data = predict_and_show_filename(model, file)

    print('@data', data, '@data-end')

    return jsonify({'success': True, 'dataset': data})

if __name__ == '__main__':
    app.run(host=environ.get('HTTP_HOST', '0.0.0.0'), port=environ.get('HTTP_PORT', 3000))
