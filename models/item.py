from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    # ID que se agrega al crear un item es la primary_key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    # Llave foranea de Store y la relación de store model que no sea igual, para no checarlo manualmente
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")
    # Relacion many to many con los tags
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")