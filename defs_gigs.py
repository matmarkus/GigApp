#importing requiried assets to create model
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Gig(Base):
    """creates params for gigs. Some params are mandatory, some not."""
    __tablename__ = 'gigs'

    id = Column(Integer, primary_key=True)
    artist = Column(String, nullable = False)
    date = Column(Date, nullable = True)
    venue = Column(String, nullable=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    festival = Column(Boolean, default=False)
    festival_name = Column(String, nullable=True)
    personal_rating = Column(Integer, nullable=True)
    ticket_price = Column(Float, nullable=True)
    comments = Column(Text, nullable=True)

#creating db
engine = create_engine('sqlite:///gigs.db')
Base.metadata.create_all(engine)
