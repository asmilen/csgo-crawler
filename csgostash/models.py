from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class SkinDB(DeclarativeBase):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(100))
    family = Column('family', String(100))
    collection = Column('collection', String(100))
    category = Column('category', String(100))
    quality_level = Column('quality_level', Integer)
    price_fn = Column('price_fn', Integer)
    price_mw = Column('price_mw', Integer)
    price_ft = Column('price_ft', Integer)
    price_ww = Column('price_ww', Integer)
    price_bs = Column('price_bs', Integer)
