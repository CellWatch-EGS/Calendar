from databases import Database

DATABASE_URL = "postgresql://calendar:password123@calendar_db/calendar"
database = Database(DATABASE_URL)