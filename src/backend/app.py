from config.config import Config
from extensions import api, db
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)


with app.app_context():
    db.init_app(app)
    api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
