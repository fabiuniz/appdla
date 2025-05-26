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

# Day 03: Operações Básicas
@app.post('/day03/sum', response_model=BasicOpOutput)
def calculate_sum(input: BasicOpInput):
    return {'result': input.val1 + input.val2}
