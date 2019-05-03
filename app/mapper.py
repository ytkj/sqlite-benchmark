from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class ItemMapper(db.Model):

    __tablename__: str = 'item'

    id = sa.Column(sa.Integer, primary_key=True)
    text1 = sa.Column(sa.String, nullable=False)
    text2 = sa.Column(sa.String, nullable=False)
    number1 = sa.Column(sa.Float, nullable=False)
    number2 = sa.Column(sa.Float, nullable=False)
