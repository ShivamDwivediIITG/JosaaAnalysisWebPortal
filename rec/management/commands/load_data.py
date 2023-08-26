from csv import DictReader


from django.core.management import BaseCommand
# Import the model 
from rec.models import rec







ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from rec.csv"

    def handle(self, *args, **options):
        # Show this when the data already exist in the database
        if rec.objects.exists():
            print('iit data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # Show this before loading the data into the database
        print("Loading iit data")

        #Code to load the data into database
        for row in DictReader(open('./rec.csv')):
            iit=rec(institute=row['institute'],academic=row['academic'],quota=row['quota'],seattype=row['seattype'],gender=row['gender'],openingrank=row['openingrank'],closingrank=row['closingrank'],year=row['year'],round=row['round'])
            
            iit.save()
        print("Loaded iit data")