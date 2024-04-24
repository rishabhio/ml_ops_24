


import sys 
import os 
import sys
sys.path.append('/Users/fourofour/Professional/Jio-2024/WarmHole/ml_ops_24')
 
from fastapi import FastAPI
from apis.iris.endpoints.health import router as health_router



app = FastAPI()
app.include_router(health_router, tags=['health'], prefix='/health')
