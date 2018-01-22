from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
"""SQLAlchemy needs to know where to find the db, in this the db is in the root folder and is of a SQLite type. Were it MYSQL or PostGres it would be declared there"""

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
"""turns off Flask SQLAlchemy tracker but not SQLAlchemy's tracker so it may run leaner"""

app.secret_key = "pogo"
api = Api(app)

"""Alternative way to create tables using flask, runs before first request, uses models for column info"""
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)