import pytest 
import numpy as np 
from modular.apis.iris.predictors.iris_predictor import IrisPredictor
import tensorflow as tf


@pytest.fixture
def predictor():
    return IrisPredictor('apis/iris/predictors/model.keras')

# Test cases for Predictor class
def test_predictor_initialization(predictor):
    assert isinstance(predictor.model, tf.keras.Model)

def test_predictor_prediction(predictor):
    X_test = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = predictor.predict(X_test)
    # print( predictions ) 
    assert prediction == 2 
    # assert np.all(predictions >= 0) and np.all(predictions <= 1)






