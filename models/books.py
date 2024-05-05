from . import Base
from sqlalchemy import String, Integer, Column
import uuid
class Books(Base):
    __tablename__ = 'books'
    id =  Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    isbn = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
