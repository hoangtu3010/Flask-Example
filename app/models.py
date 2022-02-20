from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class User(db.Model):
#     __tablename__ = "user"

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Text, unique=True, nullable=False)
#     password = db.Column(db.Text, nullable=False)

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id"))
    category = db.relationship("Category", backref="category")
