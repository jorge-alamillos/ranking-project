from src.app import app
import src.controllers.gen_api
from config import PORT

app.run("0.0.0.0", PORT, debug=True)
