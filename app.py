from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info
from urllib.parse import unquote

from routes.main import main_blueprint

info = Info(title="mlt api", version="0.0.1")
app = OpenAPI(__name__, info=info)

CORS(app)

app.register_api(main_blueprint)
