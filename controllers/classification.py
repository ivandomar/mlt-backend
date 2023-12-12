from constants.error_messages import GENERAL_ERROR
from constants.http_statuses import OK, SYNTAX_ERROR
from flask import request
from formatters.classification import format_prediction_response
from schemas.requests.element import GetPredictionRequestSchema


def get(params: GetPredictionRequestSchema):
    id = params.id
    
    try:
        # check model existence

        # check model training

        # get prediction and return
        
        return {}, OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
