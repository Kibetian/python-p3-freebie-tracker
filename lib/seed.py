#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create some companies and devs
company1 = Company(name="Company A", founding_year=2000)
company2 = Company(name="Company B", founding_year=2010)
dev1 = Dev(name="Dev X")
dev2 = Dev(name="Dev Y")

# Add them to the session and commit to the database
session.add_all([company1, company2, dev1, dev2])
session.commit()

# Create some freebies associated with companies and devs
freebie1 = Freebie(item_name="Laptop", value=1000, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Mouse", value=30, dev=dev2, company=company1)

# Add freebies to the session and commit to the database
session.add_all([freebie1, freebie2, freebie3])
session.commit()
