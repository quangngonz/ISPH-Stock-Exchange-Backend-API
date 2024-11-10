from flask import Flask, redirect
from flask_restx import Api
from routes import api

app = Flask(__name__)

@app.route('/')
def redirect_to_docs():
    return redirect('/docs', code=302)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
