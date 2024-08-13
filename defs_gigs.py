#importing requiried assets to create model
import datetime

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
from defs_users import logged_in_user

Base = declarative_base()

class Gig(Base):
    """creates structure of db, add params for gigs. Some params are mandatory, some not."""
    __tablename__ = 'gigs'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable = False)
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

Session = sessionmaker(bind=engine)
session = Session()

def add_gigs():
    """function that adds new events to db"""
    if not logged_in_user:
        print("Please login first.")
        return
    else:
        artist = input("Enter artis/band name: ")
        date = datetime.datetime(input("Enter date (DD-MM-YYYY): "), '%d-%m-%Y').date()
        venue = input("Enter venue: ")
        city = input("Enter city: ")
        country = input("Enter country: ")
        festival = input("Is it a festival? (yes/no): ").lower() == 'yes'
        festival_name = input("Enter festival name (or leave blank if it was stand-alone event") if festival else None
        personal_rating = int(input("Enter personal rating (from 1 to 10): "))
        ticket_price = float(input("Enter ticket price in EUR: "))
        comments = input("Any comments about that event?")

        new_gig = Gig(
            artist = artist,
            user = logged_in_user,
            date = date,
            venue = venue,
            city = city,
            country = country,
            festival = festival,
            festival_name = festival_name,
            personal_rating = personal_rating,
            ticket_price = ticket_price,
            comments = comments,
        )
        session.add(new_gig)
        session.commit()
        print("Your base was successfully updated.")

