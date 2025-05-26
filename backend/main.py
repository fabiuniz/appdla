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

# Day 04: Condicionais
class CNHInput(BaseModel):
    idade: int
    primeiraHabilitacao: bool

@app.post('/day04/cnh_renewal')
def cnh_renewal(input: CNHInput):
    vencimento = ''
    if input.primeiraHabilitacao:
        vencimento = '1 ano'
    return {'prazo_renovacao': vencimento}

# Day 10: Pilha Simples
product_stack = []
@app.post('/day10/stack/push_product')
def push_product():
    return {'message': 'Produto empilhado'}

# Day 16 & 18: Playlist
playlist_state = {'musicas': []}
@app.post('/day16_18/playlist/add_song')
def add_song_to_playlist():
    return {'message': 'Música adicionada'}
