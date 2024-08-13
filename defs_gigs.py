#importing requiried assets to create model
import datetime

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
import config
import defs_gigs


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

def add_gig():
    """function that adds new events to db"""
    if not config.logged_in_user:
        print("Please login first.")
        return
    else:
        artist = input("Enter artis/band name: ")
        date = datetime.datetime.strptime(input("Enter date (DD-MM-YYYY): "), '%d-%m-%Y').date()
        venue = input("Enter venue: ")
        city = input("Enter city: ")
        country = input("Enter country: ")
        festival = input("Is it a festival? (yes/no): ").lower() == 'yes'
        festival_name = input("Enter festival name (or leave blank if it was stand-alone event): ") if festival else None
        personal_rating = int(input("Enter personal rating (from 1 to 10): "))
        ticket_price = float(input("Enter ticket price in EUR: "))
        comments = input("Any comments about that event?")

        #conversion to string - check if it does something....
        user = str(config.logged_in_user)

        new_gig = Gig(
            artist = artist,
            user = user,
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

def view_gigs():
    "Shows all gigs of currently logged in user"
    if not config.logged_in_user:
        print("Please login first.")
        return

    user_gigs = session.query(Gig).filter_by(user=config.logged_in_user).all()
    if not user_gigs:
        print("No gigs found for you. Add at least one first.")
    for gig in user_gigs:
        print(f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}, Festival: {gig.festival}, Rating: {gig.personal_rating}, Price: {gig.ticket_price}, Comments: {gig.comments}")

def edit_gig():
    """Edits chosen gig."""
    if not config.logged_in_user:
        print("Please login first.")
        return

    user_gigs = session.query(Gig).filter_by(user=config.logged_in_user).all()

    for gig in user_gigs:
        print(f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}")

    gig_id = int(input("Enter the ID of the gig you want to edit: "))
    gig_to_edit = session.query(Gig).filter_by(id=gig_id, user=config.logged_in_user).first()

    if not gig_to_edit:
        print("Gig not found or you don't have permission to choose it.")
        return

    print("Which parameter would you like to edit?")
    print("1. Artist")
    print("2. Date")
    print("3. Venue")
    print("4. City")
    print("5. Country")
    print("6. Festival")
    print("7. Festival Name")
    print("8. Personal Rating")
    print("9. Ticket Price")
    print("10. Comments")

    choice = input("Enter the number of the parameter you want to edit: ")

    if choice == '1':
        gig_to_edit.artist = input("Enter new artist name: ")
    elif choice == '2':
        gig_to_edit.date = datetime.datetime.strptime(input("Enter new date (DD-MM-YYYY): "), '%d-%m-%Y').date()
    elif choice == '3':
        gig_to_edit.venue = input("Enter new venue: ")
    elif choice == '4':
        gig_to_edit.city = input("Enter new city: ")
    elif choice == '5':
        gig_to_edit.country = input("Enter new country: ")
    elif choice == '6':
        gig_to_edit.festival = input("Is it a festival? (yes/no): ").lower() == 'yes'
    elif choice == '7':
        gig_to_edit.festival_name = input("Enter new festival name: ") if gig_to_edit.festival else None
    elif choice == '8':
        gig_to_edit.personal_rating = int(input("Enter new personal rating (from 1 to 10): "))
    elif choice == '9':
        gig_to_edit.ticket_price = float(input("Enter new ticket price in EUR: "))
    elif choice == '10':
        gig_to_edit.comments = input("Enter new comments: ")
    else:
        print("Invalid choice.")

    session.commit()
    print("Updated successfully!")

def delete_gig():
    """Deletes gig"""
    if not config.logged_in_user:
        print("Please login first.")
        return

    user_gigs = session.query(Gig).filter_by(user=config.logged_in_user).all()

    for gig in user_gigs:
        print(
            f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}")

    gig_id = int(input("Enter the ID of the gig you want to delete: "))
    gig_to_delete = session.query(Gig).filter_by(id=gig_id, user=config.logged_in_user).first()

    if not gig_to_edit:
        print("Gig not found or you don't have permission to delete it.")
        return

    conf = input(f"Are you sure you want to delete the gig {gig_to_delete.artist} on {gig_to_delete.date}? (yes/no): ").lower()
    if conf == 'yes':
        session.delete(gig_to_delete)
        session.commit()
        print("Gig was deleted")
    else:
        print("Gig deletion stopped.")