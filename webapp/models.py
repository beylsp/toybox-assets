from sqlalchemy import Column, Integer, String

from webapp.app import db


class Token(db.Model):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)

    def __repr__(self):
        return f"<Token {self.name}>"