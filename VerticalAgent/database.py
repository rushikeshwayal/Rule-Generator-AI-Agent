import sqlalchemy as bd
from sqlalchemy.orm import sessionmaker

# Database configuration
database="vect",
user="postgres",
password="newpassword",
host="127.0.0.1",
port=5432

# Create the SQLAlchemy engine
DATABASE_URL = f'postgresql://postgres:{password}@{host}:{port}/{database}'
engine = bd.create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("Database connection successful!")