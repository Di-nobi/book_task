from models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from models.books import Books

class storage:
    def __init__(self) -> None:
        """Initialzies the database"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_book(self, **kwargs):
        """Adds a book to the database"""
        add_book = Books(**kwargs)
        self._session.add(add_book)
        self._session.commit()

    def get_a_book_by_id(self, id):
        book_id = self._session.query(Books).filter(Books.id==id).first()
        if not book_id:
            return None
        return book_id
    
    def remove(self, obj):
        return self._session.delete(obj)
    
    def all(self):
        get_books = self._session.query(Books).all()
        if not get_books:
            return None
        return get_books
    