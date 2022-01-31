import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASS']}@{os.environ['MYSQL_URL']}/{os.environ['MYSQL_DB']}"  # NOQA
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()
