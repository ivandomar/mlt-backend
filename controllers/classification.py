from constants.error_messages import GENERAL_ERROR
from constants.http_statuses import OK, SYNTAX_ERROR
from flask import request
from formatters.classification import format_prediction_response
from schemas.requests.element import GetPredictionRequestSchema
from classification.SVMClassificator import SVMClassificator


def get(params: GetPredictionRequestSchema):
    id = params.id
    
    try:
        classificator = SVMClassificator()

        classificator.load("../assets/classificator.pkl")

        result = classificator.predict([[]])
        
        return format_prediction_response(result), OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
