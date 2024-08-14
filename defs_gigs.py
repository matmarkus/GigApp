# importing requiried assets to create model
import csv
import datetime

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

import config

Base = declarative_base()


class Gig(Base):
    """
     Represents a music gig entry in the database.

     This class defines the structure for storing gig details in the database.
     It includes both mandatory and optional parameters to capture relevant
     information about a gig.

     Attributes:
         id (int): A unique identifier for the gig (Primary Key).
         user (str): The user associated with the gig entry (Mandatory).
         artist (str): The name of the artist performing (Mandatory).
         date (date): The date of the gig (Optional).
         venue (str): The venue where the gig will take place (Optional).
         city (str): The city in which the gig will be held (Mandatory).
         country (str): The country where the gig will be held (Mandatory).
         festival (bool): Indicates whether the gig is part of a festival (Defaults to False).
         festival_name (str): The name of the festival if applicable (Optional).
         personal_rating (int): The user's personal rating for the gig (Optional).
         ticket_price (float): The price of tickets for the gig (Optional).
         comments (str): Any additional comments regarding the gig (Optional).
     """
    __tablename__ = 'gigs'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    date = Column(Date, nullable=True)
    venue = Column(String, nullable=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    festival = Column(Boolean, default=False)
    festival_name = Column(String, nullable=True)
    personal_rating = Column(Integer, nullable=True)
    ticket_price = Column(Float, nullable=True)
    comments = Column(Text, nullable=True)


# creating db
engine = create_engine('sqlite:///gigs.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_gig():
    """Adds a new gig to the database.

    This function checks if the user is logged in. If not, it prompts the user to log in.
    Once logged in, it collects information about the gig from the user, including:
    - artist or band name
    - date of the gig
    - venue of the gig
    - city
    - country
    - whether the gig was part of a festival (with an optional festival name)
    - personal rating of the gig (on a scale from 1 to 10)
    - ticket price in euros
    - any additional comments about the gig

    After gathering all the information, it creates a new Gig object, representing the gig,
    and then adds it to the database and commits the changes.
    """
    # Check if the user is logged in
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
        festival_name = input(
            "Enter festival name (or leave blank if it was stand-alone event): ") if festival else None
        personal_rating = int(input("Enter personal rating (from 1 to 10): "))
        ticket_price = float(input("Enter ticket price in EUR: "))
        comments = input("Any comments about that event?")

        # conversion to string - check if it does something....
        user = str(config.logged_in_user)

        new_gig = Gig(
            artist=artist,
            user=user,
            date=date,
            venue=venue,
            city=city,
            country=country,
            festival=festival,
            festival_name=festival_name,
            personal_rating=personal_rating,
            ticket_price=ticket_price,
            comments=comments,
        )
        session.add(new_gig)
        session.commit()
        print("Your base was successfully updated.")


def view_gigs():
    """
       Displays all gigs for the currently logged-in user with an option to filter results.

       This function checks if a user is logged in and retrieves all gig entries
       from the database associated with that user. The user has the option to filter
       the results based on several criteria, including artist name, date range,
       city, country, and whether the gig is part of a festival.

       If the logged-in user has no gigs or if they choose not to filter,
       the function will show all their gigs or inform them if no gigs exist.

       Workflow:
       1. Checks if the user is logged in.
       2. Prompts the user to choose if they want to apply filters.
       3. If the user opts to filter, collects filter criteria from user input.
       4. Applies the filter criteria to the query.
       5. Executes the query and retrieves the gig entries.
       6. Prints out the details of each gig found, or a message if no gigs exist.

       Returns:
           None: The function prints the results directly to the console and does not return a value.

       Note:
           Dates should be entered in 'DD-MM-YYYY' format.
           If no filters are set, all gigs for the user will be displayed.
       """
    if not config.logged_in_user:
        print("Please login first.")
        return

    print("Do you want to filter gigs? (yes/no)")
    filter_choice = input("Choose what you want to do: ").lower()

    # preparing gigs of currently logged in user
    query = session.query(Gig).filter_by(user=config.logged_in_user)

    # adding filters
    if filter_choice == 'yes':
        print("You can filter by the following parameters. Leave blank to ignore a parameter.")

        artist = input("Filter by artist: ")
        if artist:
            query = query.filter(Gig.artist.ilike(f'%{artist}%'))

        date_from = input("Filter by date from (DD-MM-YYYY): ")
        if date_from:
            date_from = datetime.datetime.strptime(date_from, '%d-%m-%Y').date()
            query = query.filter(Gig.date >= date_from)

        date_to = input("Filter by date to (DD-MM-YYYY): ")
        if date_to:
            date_to = datetime.datetime.strptime(date_to, '%d-%m-%Y').date()
            query = query.filter(Gig.date <= date_to)

        city = input("Filter by city: ")
        if city:
            query = query.filter(Gig.city.ilike(f'%{city}%'))

        country = input("Filter by country: ")
        if country:
            query = query.filter(Gig.country.ilike(f'%{country}%'))

        festival = input("Filter by festival (yes/no): ").lower()
        if festival == 'yes':
            query = query.filter(Gig.festival == True)
        elif festival == 'no':
            query = query.filter(Gig.festival == False)

    # preparing output
    user_gigs = query.all()

    if not user_gigs:
        print("No gigs found for you. Add at least one first.")

    # showing results
    for gig in user_gigs:
        print(
            f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}, Festival: {gig.festival}, Rating: {gig.personal_rating}, Price: {gig.ticket_price}, Comments: {gig.comments}")


def edit_gig():
    """
        Edits an existing gig entry for the currently logged-in user.

        This function allows a user to modify details of a gig that they have previously added.
        The user must be logged in, and they can choose which gig to edit from a list
        of their existing gigs. The user can update various parameters, including artist name,
        date, venue, city, country, festival status, festival name, personal rating,
        ticket price, and comments.

        Workflow:
        1. Check if the user is logged in.
        2. Retrieve and display all gigs associated with the logged-in user.
        3. Prompt the user to enter the ID of the gig they wish to edit.
        4. Verify that the gig ID is valid and belongs to the logged-in user.
        5. Present a list of editable parameters for the user to choose from.
        6. Update the selected parameter based on user input.
        7. Save the changes to the database.

        Returns:
            None: The function prints the success message after updating the gig details.

        Note:
            - Dates should be entered in 'DD-MM-YYYY' format.
            - The personal rating should be an integer between 1 and 10.
            - If updating the festival name, it should only be done if the gig is marked as a festival.
        """
    if not config.logged_in_user:
        print("Please login first.")
        return

    user_gigs = session.query(Gig).filter_by(user=config.logged_in_user).all()

    for gig in user_gigs:
        print(
            f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}")

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
    """
        Deletes a selected gig entry for the currently logged-in user.

        This function allows a user to delete a specific gig that they have previously added.
        The user must be logged in to perform this action, and they can select which gig to delete
        from a list of their existing gigs. The function requires user confirmation before
        proceeding with the deletion.

        Workflow:
        1. Check if the user is logged in.
        2. Retrieve and display all gig entries associated with the logged-in user.
        3. Prompt the user to enter the ID of the gig they wish to delete.
        4. Verify that the gig ID is valid and that the gig belongs to the logged-in user.
        5. Confirm with the user whether they want to proceed with the deletion.
        6. If confirmed, delete the gig from the database and commit the changes.

        Returns:
            None: The function prints a success or cancellation message
            and does not return a value.

        Note:
            - The user must enter a valid gig ID corresponding to one of their entries.
            - Deletion is irreversible, so the user must confirm their action.
        """
    if not config.logged_in_user:
        print("Please login first.")
        return

    user_gigs = session.query(Gig).filter_by(user=config.logged_in_user).all()

    for gig in user_gigs:
        print(
            f"ID: {gig.id}, Artist: {gig.artist}, Date: {gig.date}, Venue: {gig.venue}, City: {gig.city}, Country: {gig.country}")

    gig_id = int(input("Enter the ID of the gig you want to delete: "))
    gig_to_delete = session.query(Gig).filter_by(id=gig_id, user=config.logged_in_user).first()

    if not gig_to_delete:
        print("Gig not found or you don't have permission to delete it.")
        return

    conf = input(
        f"Are you sure you want to delete the gig {gig_to_delete.artist} on {gig_to_delete.date}? (yes/no): ").lower()
    if conf == 'yes':
        session.delete(gig_to_delete)
        session.commit()
        print("Gig was deleted")
    else:
        print("Gig deletion stopped.")


def import_gigs_from_csv(file_path):
    """
        Imports gigs from a specified CSV file and adds them to the database.

        This function allows a logged-in user to import gig data from a CSV file scrapped from Last.fm using
        https://mainstream.ghan.nl/export.html (option: Events: full)

        The CSV file is expected to contain specific columns: artist, date, venue, place (for city),
        country, type (to determine if it's a festival), title (for the festival name)
         and href, which is a link to last.fm event, (for comments).

        **Important Note**: This functionality requires a properly formatted CSV file.
        If the CSV does not meet the expected structure (e.g., missing columns), the function will raise an error.

        **CSV Creation Instructions**:
        1. Go to the website [https://mainstream.ghan.nl/export.html](https://mainstream.ghan.nl/export.html).
        2. Enter your username from Last.fm.
        3. Choose "Events (full)" from the options.
        4. Select CSV format and export the data.
        5. Ensure that the exported CSV file contains the following headers:
           - artist
           - date (format: YYYY-MM-DD)
           - venue
           - place (for city)
           - country
           - type (should be "festival" or not)
           - title (name of the festival, if applicable)
           - href (for comments)

        Workflow:
        1. Check if the user is logged in.
        2. Prompt the user for the CSV file path.
        3. Open the CSV file and read its contents.
        4. Validate the required columns are present.
        5. For each row, extract information and create a new gig entry.
        6. Add the gig to the session and commit the changes.

        Args:
            file_path (str): The path to the CSV file containing gig information. Taken from def add_gigs_menu():

        Returns:
            None: The function prints a success message once gigs are imported or error messages if issues arise.
        """
    if not config.logged_in_user:
        print("Please login first.")
        return

    # opening csv with utf-8 coding and sets up mapping
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Validate required columns
            required_columns = ['artist', 'date', 'venue', 'place', 'country', 'type', 'title', 'href']
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                print(
                    f"Error: The following required columns are missing from the CSV file: {', '.join(missing_columns)}")
                return

            for row in reader:
                try:
                    artist = row['artist']
                    date = datetime.datetime.strptime(row['date'], '%Y-%m-%d').date()
                    venue = row['venue']
                    city = row['place']
                    country = row['country']
                    festival = True if row['type'].lower() == 'festival' else False
                    comments = row['href']

                    # Creating gig
                    new_gig = Gig(
                        user=config.logged_in_user,
                        artist=artist,
                        date=date,
                        venue=venue,
                        city=city,
                        country=country,
                        festival=festival,
                        festival_name=row['title'] if festival else None,
                        personal_rating=None,  # CSV doesn't provide this data.
                        ticket_price=None,  # CSV doesn't provide this data.
                        comments=comments
                    )
                    # Adding and saving gig
                    session.add(new_gig)

                except Exception as e:
                    print(f"Error processing row {row}: {e}")

        session.commit()
        print(f"Imported gigs from {file_path}")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
