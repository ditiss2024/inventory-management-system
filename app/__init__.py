from flask import Flask
from app.routes import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)

