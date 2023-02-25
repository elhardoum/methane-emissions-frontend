from os import path

FLASK_SECRET=b'EHoPoGX2DLKIqEhMxZlpFkritOyZTeMVpp'
MODEL_LOCATION=path.join(path.dirname(path.realpath(__file__)), './model_1.h5')
MODEL_SETTINGS_LOCATION=path.join(path.dirname(path.realpath(__file__)), './model_1.json')
REACT_BUILD_DIR=path.join(path.dirname(path.realpath(__file__)), './../build')
IMAGES_MAP_CSV_FILE=path.join(path.dirname(path.realpath(__file__)), './permian_source_list_2019.csv')
