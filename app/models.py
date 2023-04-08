from app.app import db
from flask_security.models import fsqla


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return self.name


class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return self.email

    def __iter__(self):
        values = vars(self)
        for attr in self.__mapper__.columns.keys():
            if attr in values:
                yield attr, values[attr]


class Offer(db.Model):
    __tablename__ = 'offer'
    __table_args__ = {'extend_existing': True}


class Category(db.Model):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}


class Order(db.Model):
    __tablename__ = 'order'
    __table_args__ = {'extend_existing': True}


class UserScore(db.Model):
    __tablename__ = 'user_score'
    __table_args__ = {'extend_existing': True}
