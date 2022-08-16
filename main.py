from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model import ToyModel
from transformer import Cost_Transformer

app = Flask(__name__)
api = Api(app)

# load trained classifier
model_path = 'models/model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

def get_prediction(score):
    '''
    score float: model proba
    return str: negative or positive
    '''
    return 'Positive' if score >=0.5 else 'Negative'

class PredictToy(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        predict_proba = model.predict(user_query)

        # Output either 'Negative' or 'Positive' along with the score
        prediction = get_prediction(predict_proba[0])

        # create JSON object
        output = {'prediction': prediction, 'ModelScore': round(predict_proba[0], 3)}
        
        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictToy, '/')


if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port= int(os.environ.get("PORT", 8080)))