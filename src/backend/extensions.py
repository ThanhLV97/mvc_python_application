from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

api = Api(prefix="/api")
db = SQLAlchemy()
mgi = Migrate()
