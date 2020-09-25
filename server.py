from src.server.app import app
import src.controllers.gen_api
from src.server.config import PORT

app.run("0.0.0.0", PORT, debug=True)

