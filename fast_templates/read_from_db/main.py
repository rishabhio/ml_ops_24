from fastapi import FastAPI, HTTPException 

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy models
Base = declarative_base()

class MLModel(Base):
    __tablename__ = "ml_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String )
    version = Column(Integer )

# Database connection
DATABASE_URL = "postgresql://localuser:root@localhost/readOne"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI endpoint to get all users
@app.get("/available_models/")
def get_users(db = Depends(get_db)):
    all_models  = db.query(MLModel).all()
    return all_models 
