from flask import Flask
from helpers.api import api
from helpers.database import db, migrate
from helpers.cors import cors
from config import Config
import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

cors.init_app(app)

api.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()
    print('Tabelas criadas')

create_tables()

if __name__ == '__main__':
    app.run(debug=True)
