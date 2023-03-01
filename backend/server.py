from flask import Flask, request, send_from_directory, jsonify
from os import environ, path
import config
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import json
import imageio
import csv
import re

app = Flask(__name__,
    static_url_path='/',
    static_folder='www')
app.secret_key = environ.get('FLASK_SECRET', config.FLASK_SECRET)

def predict_and_show_filename(model, file):
    img = imageio.imread(file)
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

def get_csv_map(filename):
    with open(config.IMAGES_MAP_CSV_FILE, 'r') as csv_file:
        reader = csv.reader(csv_file)

        headers, source_col, lat_col, lng_col = None, None, None, None

        for row in reader:
            if not headers:
                headers = row

                for i,col in enumerate(headers):
                    if str(col).strip().lower() == 'source_id':
                        source_col = i
                    elif str(col).strip().lower() == 'source_lat':
                        lat_col = i
                    elif str(col).strip().lower() == 'source_lon':
                        lng_col = i
                continue

            if None == source_col:
                return {}

            if str(row[source_col]).strip().lower() != str(filename).strip().lower():
                continue

            return {
                'lat': row[lat_col] if len(row) > lat_col else None,
                'lng': row[lng_col] if len(row) > lng_col else None,
            }


model = get_model()

@app.route('/<path:path>')
def index(path):
    return send_from_directory('www', path)

@app.route('/')
def root():
    return index('index.html')

@app.route('/api/post-image', methods=['POST'])
def upload():
    file = request.files.get('File') if request.files and 'File' in request.files.keys() else None

    if not file:
        return jsonify(None, 400)

    global model


    data = predict_and_show_filename(model, file)

    try:
        filename = str(path.basename(file.filename)).replace('.png', '')
        coords = get_csv_map(filename) or {}
    except:
        coords = {}

    return jsonify({'success': True, 'dataset': data, **coords})

if __name__ == '__main__':
    app.run(host=environ.get('HTTP_HOST', '0.0.0.0'), port=environ.get('HTTP_PORT', 3000))
