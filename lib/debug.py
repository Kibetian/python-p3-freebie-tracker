 #!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Try to retrieve the Dev instance with the name "Dev X"
dev = session.query(Dev).filter_by(name="Dev X").first()

if dev:
    # If the Dev instance was found, print its freebies
    print(f"Freebies collected by {dev.name}:")
    for freebie in dev.freebies:
        print(freebie.print_details())
else:
    # If the Dev instance was not found, display a message
    print("Dev X not found in the database.")
