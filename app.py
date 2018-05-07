from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return "<title>Olá Mundo!</title>", 200

app.run()
