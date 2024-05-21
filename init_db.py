from sqlalchemy import create_engine, Column, String, DateTime, MetaData, Table
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://calendar:password123@calendar_db/calendar')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

schedules = Table(
    'schedules', metadata,
    Column('id', String, primary_key=True),
    Column('time', DateTime, nullable=False),
    Column('locationId', String, nullable=False),
    Column('person_name', String, nullable=False),
)

def create_tables():
    metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully.")
