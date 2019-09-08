from flask import Flask
from app.controller.kanji_controller import kanji

app = Flask(__name__)
app.debug = True
app.register_blueprint(kanji)