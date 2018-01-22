from db import db

class ItemModel(db.Model): #db.Model is a SQLAlchemy construct
    __tablename__ = "items" #declares name of table in DB to be used

    """The following are not declaration of variables, but rather identification of columns in table and their attrbutes"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    """ stores table primary key is mapped to the item's store_id as the foreign key """

    store = db.relationship("StoreModel")
    """ SQLAlchemy assigns store using basic JOIN functionality without writing query"""


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        """
        SQLAlchemy shorthand for SELECT * FROM items WHERE name=name, second name is what is passed in.
        filter_by can be compounded like SQL query, ie WHERE name=name AND price=price
        .first() function adds LIMIT 1 to query
        """

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        """
        db.session.add() can add multiple items at once
        this function also serves to update making insert and update as separate processes unecessary
        """

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()