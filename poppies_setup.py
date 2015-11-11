__author__ = 'Elmira'



from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, Float

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    name = Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(40))
    state = Column(String(40))
    zipCode = Column(String(10))
    website = Column(String(250))
    id = Column(Integer, primary_key = True)


class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String(250))
    gender = Column(String(10))
    weight = Column(Float)
    id = Column(Integer, primary_key = True)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))

    shelter = relationship(Shelter)

engine = create_engine('sqlite:///puppies')

Base.metadata.create_all(engine)