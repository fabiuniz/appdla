# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Inicializa a aplicação FastAPI
app = FastAPI()

# Modelos Pydantic para Day 03
class BasicOpInput(BaseModel):
    val1: float
    val2: float

class BasicOpOutput(BaseModel):
    result: float
