from os import path

FLASK_SECRET=b'EHoPoGX2DLKIqEhMxZlpFkritOyZTeMVpp'
MODEL_LOCATION=path.join(path.dirname(path.realpath(__file__)), './model_1.h5')
MODEL_SETTINGS_LOCATION=path.join(path.dirname(path.realpath(__file__)), './model_1.json')
REACT_BUILD_DIR=path.join(path.dirname(path.realpath(__file__)), './../build')
