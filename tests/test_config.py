import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service


input_data = {
    "incorrect_range":
    {
        "Feature_1": 0,
        "Feature_2": 0,
        "Feature_3": 0,
        "Feature_4": 0
    },

    "correct_range":
    {
        "Feature_1": 2,
        "Feature_2": 1,
        "Feature_3": 1,
        "Feature_4": 4
    },

    "incorrect_col":
    {
        "Feature_": 2,
        "Feature_2": 1,
        "Feature_3": 1,
        "Feature_4": 4
    }
}


prediction_range = {
    "min": -1000.0,
    "max": 1000.0
}  # For the unexpected result


def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert prediction_range["min"] <= res <= prediction_range["max"]


def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert prediction_range["min"] <= res["response"] <= prediction_range["max"]


def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        form_response(data)


def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message


def test_form_response_incorrect_col(data=input_data["incorrect_col"]):
    with pytest.raises(prediction_service.prediction.NotInCols):
        form_response(data)


def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message
