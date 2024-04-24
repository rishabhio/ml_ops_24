from sklearn.preprocessing import StandardScaler 
import joblib 



class FeatureScaler:

    def __init__(self, model_path ):
        self.model_path = model_path 
        self.scaler = self._load_scaler()

    def _load_scaler( self ):
        return joblib.load( self.model_path )

    def scale_features(self, data):
        '''
            This functions  takes a list of 
            input args and scales them using 
            StandardScaler. 
            [sepal_length, sepal_width, petal_length, petal_width]
        '''
        return self.scaler.transform( data )

