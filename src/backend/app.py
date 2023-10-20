from apis import api
from config.config import Config
from extensions import db, mgi
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)


with app.app_context():
    db.init_app(app)
    mgi.init_app(app, db)
    api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
