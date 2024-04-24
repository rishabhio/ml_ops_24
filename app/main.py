


# create a file with name: main.py
# Writing your first handler

from fastapi import FastAPI, HTTPException
from steps.preprocess import FeatureScaler
from predictors.iris_predictor import IrisPredictor
import sys
import os

# Define FastAPI app
app = FastAPI()

# Get the root of the project
# Get the root directory of your project
root_dir = os.path.dirname(os.path.abspath(__file__))

# Add the root directory to the Python path
sys.path.append(root_dir)


# Define route to handle requests 
@app.get('/hello')
async def say_hello():
    return {'result': 'Hello from API'}
            

# define a route to make predictions 

@app.post('/predict')
async def predict(data: dict):
    # dummy data in list format 
    CLASSES = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }
    features = [
        data.get('sepal_length'),
        data.get('sepal_width'),
        data.get('petal_length'),
        data.get('petal_width')
    ]
    # scale features 
    scaler = FeatureScaler('steps/scaler.pkl') 
    scaled_features = scaler.scale_features([features])
    # make predictions 
    predictor = IrisPredictor('predictors/model.keras')
    prediction = predictor.predict(scaled_features)
    # post process predictions 
    # Find the highest probability prediction 
    # and return the corresponding class
    result = {
        'class': CLASSES.get(prediction),
        'message': f'Predicted class is {CLASSES.get(prediction)}'
    }
    return result 