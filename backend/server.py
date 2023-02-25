from flask import (Flask, render_template)
from os import environ
import config
import tensorflow as tf


app = Flask(__name__, static_url_path='', static_folder='public', template_folder='templates')
app.secret_key = environ.get('FLASK_SECRET', config.FLASK_SECRET)

new_model = tf.keras.models.load_model( config.MODEL_LOCATION )
print( new_model )

@app.route('/', methods=['GET'])
def index(locale=''):
    # print( get_model() )

    return render_template('index.html',
        title='Methane Emissions Predictions App')

if __name__ == '__main__':
    app.run(host=environ.get('HTTP_HOST', '0.0.0.0'), port=environ.get('HTTP_PORT', 3000))
