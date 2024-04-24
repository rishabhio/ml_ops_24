import tensorflow as tf 

class IrisPredictor:

    def __init__(self, model_path ):
        self.model_path = model_path 
        self.model = self._load_model() 

    def _load_model( self ):
        return tf.keras.models.load_model( self.model_path ) 

    def predict(self, input_args ):
        return self.model.predict( input_args ).argmax()
        