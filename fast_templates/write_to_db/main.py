

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session 
from pydantic import BaseModel

# Define SQLAlchemy models
Base = declarative_base()

class MLModel(Base):
    __tablename__ = "ml_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    version = Column(Integer)


# Database connection
DATABASE_URL = "postgresql://localuser:root@localhost/readOne"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()


# Endpoint to create a new ML model
@app.post("/models/")
def create_model(data: dict):
    db_model = MLModel(**data)
    db = SessionLocal()
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


# FastAPI endpoint to get all ML models
@app.get("/models/")
def get_models():
    db = SessionLocal()
    models = db.query(MLModel).all()
    return models
