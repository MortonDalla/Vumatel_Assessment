#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

DB_URI = 'sqlite:///./main.db'
Base = declarative_base()

class Note(Base):
    __tablename__ = 'Installations'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(1oo0))
    Address = Column(String(300))
    Appointment_date = Column(Date)
    Created_date = Column(Date)
    Created_date = Column(Date)
    Status = Column(String(80))
    read = Column(True)

if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

}
