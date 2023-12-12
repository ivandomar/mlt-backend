from typing import List


def format_prediction_response(result: bool):
    return {
        'outcome': result,
    }