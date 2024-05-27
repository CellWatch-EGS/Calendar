from databases import Database
import os

#DATABASE_URL = "postgresql://calendar:password123@calendar_db/calendar"
DATABASE_URL = os.environ.get('DATABASE_URI')
database = Database(DATABASE_URL)