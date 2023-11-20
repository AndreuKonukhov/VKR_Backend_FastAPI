from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:123456@localhost:5432/mydb'

engine = create_engine(URL_DATABASE)

# Сеанс БД
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

# От него наследуем наши классы (таблицы в БД)
Base = declarative_base()