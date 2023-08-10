

import numpy as np

from src.get_data import read_params
import joblib

import json
import os

params_path = 'params.yaml'

schema_path = os.path.join('prediction_service', 'schema_in.json')


class NotInRange(Exception):
    def __init__(self,  message='Values  not in range'):
        self.message = message
        super().__init__(self.message)


class NotInCols(Exception):
    def __init__(self,  message='Not in columns'):
        self.message = message
        super().__init__(self.message)


def get_schema():
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema


def validate_input(dict_request):

    print(dict_request)
    print(type(dict_request))
    print(dict_request.items())

    def _validate_cols(col):
        schema = get_schema()

        actual_cols_list = list(schema.keys())

        if col not in actual_cols_list:
            raise NotInCols

    def _validate_values(col, val):
        schema = get_schema()
        if not (schema[col]["min"] <= float(val) <= schema[col]["max"]):
            raise NotInRange

    for col, val in list(dict_request.items()):
        _validate_cols(col)
        _validate_values(col, val)

    return True


def form_response(dict_request):

    if validate_input(dict_request):

        data = dict_request.values()

        data = [list(map(float, data))]
        pred = predict(data)
        return pred


def api_response(dict_request):
    print(dict_request)
    try:

        if validate_input(dict_request):

            # data = np.array([list(dict_request.values())])
            data = np.array([list(dict_request.values())])

            response = predict(data)
            response = {"response": response}
            return response
    except NotInRange as e:
        response = {"the_exected_range": get_schema(), "response": str(e)}
        return response

    except NotInCols as e:
        response = {"the_exected_cols": list(get_schema().keys()),
                    "response": str(e)}
        return response

    except Exception as e:
        response = {"response": str(e)}
        return response


def predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]

    try:
        if prediction > -10000:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"
