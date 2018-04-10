from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# třídy Event a Garage
# dědí SQLAlchemy metody
# třídy Base
class Event(Base):
    ...
    # odkaz na příslušnou garáž
    garage_id = Column(Integer, ForeignKey(
        'Garage.id'), nullable=False)

class Garage(Base): 
    ...
    # definice 1:N vztahu mezi garáží a událostí
    events = relationship('Event', backref='Garage')