from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SYNTAX_ERROR
from controllers.home import index
from controllers.classification import predict
from schemas.responses import ElementResponseSchema, ErrorResponseSchema


home_tag = Tag(name="Main routes", description="Main routes for MLT")

main_blueprint = APIBlueprint("main", __name__)

main_blueprint.get("/docs", tags=[home_tag], summary="Renders Swagger API docs")(index)

main_blueprint.get(
    '/prediction',
    tags=[home_tag],
    summary='Calculates classification prediction using embedded SVM model',
    responses={
        str(OK): ElementResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(predict)
