from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///cards_flask.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# создали класс Card и наследовали его от класса Base (который нам создала алхимия)
class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    en_meaning = Column(String(500), unique=True)
    ru_meaning = Column(String(500))
    example = Column(String(500))
    extra_info = Column(String(500))
    score = Column(Integer)
    is_active = Column(Boolean)

    # метод, который вызывается автоматически, когда мы создаем новый объект класса Card
    def __init__(self, en_meaning=None, ru_meaning=None, example=None, extra_info=None, score=None, is_active=None): 
        self.en_meaning = en_meaning
        self.ru_meaning = ru_meaning
        self.example = example
        self.extra_info = extra_info
        self.score = score
        self.is_active = is_active

    def __repr__(self):
        return '<Card {} {} {} {} {}>'.format(self.en_meaning,
                                              self.ru_meaning,
                                              self.example,
                                              self.extra_info,
                                              self.score,
                                              self.is_active)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
