# Backend

The backend is meant to be a simple Flask server that would serve the frontend and interact with tensorflow to do the predictions.

## Learn more

* [Save and load Keras models](https://www.tensorflow.org/guide/keras/save_and_serialize)

## Configure & Deploy

After cloning the repository, create a virtual environment and install the required dependencies:

```sh
# create a virtual environment
virtualenv -p python3 env

# activtate the env
source env/bin/activate

# install dependencies
pip install -r requirements.txt
```

Open `config.py` and customize the settings.

## Backend Server

Start the app server:

```sh
FLASK_APP=server.py FLASK_ENV=development flask run --port 3000
```
