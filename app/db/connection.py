from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
Base = declarative_base()
