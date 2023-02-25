from flask import (Flask, render_template)
from os import environ
import config
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import json
import imageio

app = Flask(__name__, static_url_path='', static_folder='public', template_folder='templates')
app.secret_key = environ.get('FLASK_SECRET', config.FLASK_SECRET)

def predict_and_show_filename(model, filename):
    img = imageio.imread(filename)
    img = tf.cast(img, tf.float32) / 255.
    img = tf.image.resize(img, size=[217, 217])
    img = tf.slice(img, [0, 0, 0], [-1, -1, 3]) # extract first 3 channels
    pred = model.predict(img[tf.newaxis, ...])
    # plt.imshow(img)
    print("Prediction:", pred[0][0])
    return pred

def get_model():
    json_file = open(config.MODEL_SETTINGS_LOCATION, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(config.MODEL_LOCATION)
    return loaded_model

@app.route('/', methods=['GET'])
def index(locale=''):
    model = get_model()

    # print( predict_and_show_filename(model, '/tmp/17A.png') )

    return render_template('index.html',
        title='Methane Emissions Predictions App')

if __name__ == '__main__':
    app.run(host=environ.get('HTTP_HOST', '0.0.0.0'), port=environ.get('HTTP_PORT', 3000))
