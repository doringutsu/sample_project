from sqlalchemy import Column, Integer, String

from .base import Base


class Sample(Base):
    __tablename__ = 'sample_table'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
