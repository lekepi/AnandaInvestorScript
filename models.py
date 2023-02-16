from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, \
    Date, Float, Boolean, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import ConfigDefault
from datetime import datetime
import sys

config_class = ConfigDefault  # get the config file from config.py classes

try:
    my_URI = config_class.SQLALCHEMY_DATABASE_URI
except:
    print("The config file is incorrect")
    sys.exit(1)

Base = declarative_base()
engine = create_engine(my_URI)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), unique=True, nullable=False)
    last_name = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)


class UserRoles(Base):
    __tablename__ = 'user_roles'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id', ondelete='CASCADE'))
    role_id = Column(Integer(), ForeignKey('role.id', ondelete='CASCADE'))


class AuthEmails(Base):
    __tablename__ = 'auth_emails'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)


class LogDb(Base):
    __tablename__ = 'log_db'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False, default=datetime.now)
    project = Column(String(45), nullable=False)
    task = Column(String(45), nullable=False)
    issue = Column(String(45), nullable=False)
    msg_type = Column(String(45), nullable=False)
    description = Column(String(400), nullable=False)


class UserActivity(Base):
    __tablename__ = 'user_activity'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    user = relationship("User")
    date_time = Column(DateTime, nullable=False, default=datetime.now)


class NameValue(Base):
    __tablename__ = 'name_value'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    my_value = Column(String(45))
