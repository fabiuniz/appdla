# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import math
import collections

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="Funções JavaScript Convertidas para API Python",
    description="Uma API que demonstra diversas funcionalidades JavaScript convertidas para Python, organizadas por 'dias' de estudo."
)

# Configuração do CORS para permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens. Em produção, você deve restringir isso.
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# --- Variáveis de Estado Global (para funções que mantêm estado) ---
# ATENÇÃO: Estas variáveis são em memória e serão resetadas ao reiniciar o servidor.
# Para persistência real, seria necessário integrar um banco de dados.

# Day 07: Sistema Bancário
banking_state = {
    "saldoConta1": 600.0,
    "saldoConta2": 400.0,
    "limite": 0.0,
    "jurosLimite": 0.0,
    "totalTransferidoHoje": 0.0, # Este é para o Day 21, mas o Day 07 não o usa diretamente
    "historicoTransacoes": [],
    "totalPorChave": {},
    "percentualLimite": 0.10,
    "saldoMinimoLimite": 1000.0,
    "taxaConversaoDolar": 5.23
}

# Day 08: Fila Simples
simple_queue = []

# Day 10 & 11: Pilha (Empilhamento de Produtos e Navegação)
product_stack = []
browser_history = {
    "pilhaVoltar": [],
    "pilhaAvancar": [],
    "paginaAtual": None
}
MAX_STACK_CAPACITY = 10 # Para empilharProduto

# Day 12: Fila Drive-Thru
drivethru_queue = []

# Day 13: Deque (Gerenciamento de Tarefas)
tasks_deque = collections.deque()

# Day 14: Múltiplas Filas (Caixas)
cashier_queues = {f"caixa{i}": [] for i in range(1, 11)}

# Day 15: Lista Encadeada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

linked_list_head = None

# Day 16 & 18: Playlist
playlist_state = {
    "musicas": []
}

# --- Modelos Pydantic para Entradas e Saídas da API ---

# Day 03: Basic Operations
class BasicOpInput(BaseModel):
    val1: float
    val2: float

class BasicOpOutput(BaseModel):
    result: float

class HoursInput(BaseModel):
    segunda: float
    terca: float
    quarta: float
    quinta: float
    sexta: float

class SalariesInput(BaseModel):
    salarioPessoa1: float
    salarioPessoa2: float
    salarioPessoa3: float

class AgeInput(BaseModel):
    anoNascimento: int
    anoAtual: int

class ProductInput(BaseModel):
    precoProduto: float
    quantidadeProduto: int

class AreaInput(BaseModel):
    comprimento: float
    largura: float

class SalaryCalcInput(BaseModel):
    horasTrabalhadas: float
    valorPorHora: float

class GradesInput(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nota4: float

class MetersInput(BaseModel):
    metros: float

# Day 04: Conditionals
class CNHInput(BaseModel):
    idade: int
    primeiraHabilitacao: bool

class GradeEvalInput(BaseModel):
    nota: float

class TernaryInput(BaseModel):
    nota: int # Para aprovado/reprovado

class PurchaseInput(BaseModel):
    saldo: float
    clienteInativo: bool

class GateInput(BaseModel):
    estado: str

class ProductDiscountInput(BaseModel):
    produto: str
    preco: float

# Day 05: Loops
class InvestmentInput(BaseModel):
    valorInvestido: float
    taxaJuros: float
    anosInvestimento: int

class InvestmentDoubleInput(BaseModel):
    valorInvestido: float
    taxaJuros: float

class InstallmentInput(BaseModel):
    valorProduto: float
    numeroParcelas: int

class InstallmentOutput(BaseModel):
    parcela: float
    valorRestante: float
    parcelas: List[Dict[str, float]] # Para retornar todas as parcelas

# Day 06: Functions
class IMCInput(BaseModel):
    peso: float
    altura: float

class DayOfWeekInput(BaseModel):
    dia: int

# Day 07: Banking System
class BankingStatusOutput(BaseModel):
    saldoConta1: float
    saldoConta2: float
    saldoTotal: float
    limite: float
    jurosLimite: float
    historicoTransacoes: List[Dict[str, Any]]
    totalPorChave: Dict[str, float]

class DepositInput(BaseModel):
    conta: int
    valor: float

class DebitInput(BaseModel):
    conta: int
    valor: float

class TransferInput(BaseModel):
    valor: float
    contaOrigem: int
    contaDestino: int

class ConvertToDolarOutput(BaseModel):
    saldoDolar: float

# Day 08: Queue
class EnqueueInput(BaseModel):
    nome: str

class QueueStatusOutput(BaseModel):
    queue: List[str]
    message: str

# Day 09: Array/List Operations
class ArraySearchInput(BaseModel):
    array: List[Any]
    elemento: Any

class ArraySliceInput(BaseModel):
    array: List[Any]
    inicio: Optional[int] = 0
    fim: Optional[int] = None

# Day 10 & 11: Stack (Product & Browser)
class ProductStackInput(BaseModel):
    produto: str

class BrowserNavigateInput(BaseModel):
    pagina: str

class BrowserStatusOutput(BaseModel):
    pilhaVoltar: List[str]
    pilhaAvancar: List[str]
    paginaAtual: Optional[str]

# Day 12: Drive-Thru Queue
class DriveThruEnqueueInput(BaseModel):
    placaDoCarro: str
    pedido: str

class DriveThruQueueStatusOutput(BaseModel):
    totalCarros: int
    filaAtual: List[str]

# Day 13: Deque (Task Management)
class TaskInput(BaseModel):
    tarefa: str

class DequeStatusOutput(BaseModel):
    tarefas: List[str]
    message: str

# Day 14: Multiple Queues (Cashiers)
class CashierEnqueueInput(BaseModel):
    caixa: str
    nome: str

class CashierQueuesStatusOutput(BaseModel):
    filasCaixas: Dict[str, List[str]]

# Day 15: Linked List
class LinkedListInput(BaseModel):
    elemento: Any
    posicao: Optional[int] = None

class LinkedListDeleteInput(BaseModel):
    posicao: int

class LinkedListSearchInput(BaseModel):
    posicao: int

class LinkedListIndexOfInput(BaseModel):
    elemento: Any

class LinkedListTraversalOutput(BaseModel):
    elements: List[Any]

# Day 16 & 18: Playlist
class MusicaInput(BaseModel):
    nome: str
    artista: str
    tempo: str

class PlaylistStatusOutput(BaseModel):
    musicas: List[Dict[str, Any]]
    message: str

# Day 17: Sorting Arrays
class ProductItem(BaseModel):
    nome: str
    preco: float

class ProductsListOutput(BaseModel):
    products: List[ProductItem]

# Day 19: Recursion (Invoice)
class InvoiceItem(BaseModel):
    descricao: str
    valor: float
    parcelas: Optional[List[Any]] = None # Any para permitir recursão

class InvoiceTotalOutput(BaseModel):
    totalFatura: float

# Day 20: Recursion (Search)
class BinarySearchInput(BaseModel):
    lista: List[Any]
    valor: Any

class MessageItem(BaseModel):
    nome: str
    mensagem: str
    telefone: str
    data: str

class SearchMessagesInput(BaseModel):
    mensagens: List[MessageItem]
    palavra: str

class SearchMessagesOutput(BaseModel):
    encontrados: List[Dict[str, Any]]

# Day 21: Pix Banking
class PixInput(BaseModel):
    chavePix: str
    valor: float
    mensagem: Optional[str] = ""
    data: str

class CancelPixInput(BaseModel):
    indiceTransacao: int
    dataTransacao: Optional[str] = None # Day 21 original uses dataTransacao, but JS version only uses index

# --- Funções Auxiliares para Estruturas de Dados (Backend) ---

# Linked List Aux Functions
def _get_linked_list_elements():
    elements = []
    current = linked_list_head
    while current:
        elements.append(current.data)
        current = current.next
    return elements

def _insert_first_ll(element):
    global linked_list_head
    new_node = Node(element)
    if not linked_list_head:
        linked_list_head = new_node
    else:
        new_node.next = linked_list_head
        linked_list_head = new_node
    return element

def _insert_last_ll(element):
    global linked_list_head
    new_node = Node(element)
    if not linked_list_head:
        linked_list_head = new_node
    else:
        current = linked_list_head
        while current.next:
            current = current.next
        current.next = new_node
    return element

def _insert_at_ll(element, position):
    global linked_list_head
    new_node = Node(element)

    if position == 0:
        new_node.next = linked_list_head
        linked_list_head = new_node
        return element

    current = linked_list_head
    prev = None
    count = 0

    while count < position and current:
        prev = current
        current = current.next
        count += 1

    if count == position:
        prev.next = new_node
        new_node.next = current
        return element
    else:
        raise HTTPException(status_code=400, detail="Posição inválida.")

def _delete_at_ll(position):
    global linked_list_head
    if not linked_list_head:
        raise HTTPException(status_code=400, detail="A lista está vazia.")

    if position == 0:
        removed_element = linked_list_head.data
        linked_list_head = linked_list_head.next
        return removed_element

    current = linked_list_head
    prev = None
    count = 0

    while count < position and current:
        prev = current
        current = current.next
        count += 1

    if current:
        prev.next = current.next
        return current.data
    else:
        raise HTTPException(status_code=400, detail="Posição inválida.")

def _search_at_ll(position):
    current = linked_list_head
    count = 0

    while count < position and current:
        current = current.next
        count += 1

    if current:
        return current.data
    else:
        raise HTTPException(status_code=404, detail="Posição inválida ou elemento não encontrado.")

def _index_of_ll(element):
    current = linked_list_head
    count = 0

    while current:
        if current.data == element:
            return count
        current = current.next
        count += 1

    raise HTTPException(status_code=404, detail="Elemento não encontrado.")

# Playlist Aux Functions
def _create_musica(nome, artista, tempo):
    return {
        "nome": nome,
        "artista": artista,
        "reproducoes": 0,
        "tempo": tempo
    }

# --- Endpoints da API ---

# --- Day 03: Operações Básicas ---
@app.post("/day03/sum", response_model=BasicOpOutput)
def calculate_sum(input: BasicOpInput):
    return {"result": input.val1 + input.val2}

@app.post("/day03/total_hours", response_model=BasicOpOutput)
def calculate_total_hours(input: HoursInput):
    return {"result": input.segunda + input.terca + input.quarta + input.quinta + input.sexta}

@app.post("/day03/total_salaries", response_model=BasicOpOutput)
def calculate_total_salaries(input: SalariesInput):
    return {"result": input.salarioPessoa1 + input.salarioPessoa2 + input.salarioPessoa3}

@app.post("/day03/subtract", response_model=BasicOpOutput)
def calculate_subtract(input: BasicOpInput):
    return {"result": input.val1 - input.val2}

@app.post("/day03/age", response_model=BasicOpOutput)
def calculate_age(input: AgeInput):
    return {"result": float(input.anoAtual - input.anoNascimento)}

@app.post("/day03/multiply", response_model=BasicOpOutput)
def calculate_multiply(input: BasicOpInput):
    return {"result": input.val1 * input.val2}

@app.post("/day03/total_purchases", response_model=BasicOpOutput)
def calculate_total_purchases(input: ProductInput):
    return {"result": input.precoProduto * input.quantidadeProduto}

@app.post("/day03/area", response_model=BasicOpOutput)
def calculate_area(input: AreaInput):
    return {"result": input.comprimento * input.largura}

@app.post("/day03/salary_calc", response_model=BasicOpOutput)
def calculate_salary(input: SalaryCalcInput):
    return {"result": input.horasTrabalhadas * input.valorPorHora}

@app.post("/day03/average_grade", response_model=BasicOpOutput)
def calculate_average_grade(input: GradesInput):
    return {"result": (input.nota1 + input.nota2 + input.nota3 + input.nota4) / 4}

@app.post("/day03/meters_to_km", response_model=BasicOpOutput)
def convert_meters_to_km(input: MetersInput):
    return {"result": input.metros / 1000}


# --- Day 04: Condicionais ---
@app.post("/day04/cnh_renewal")
def cnh_renewal(input: CNHInput):
    vencimento = ""
    if input.primeiraHabilitacao:
        vencimento = "1 ano"
    elif input.idade < 50:
        vencimento = "10 anos"
    elif input.idade < 70:
        vencimento = "5 anos"
    else:
        vencimento = "3 anos"
    return {"prazo_renovacao": vencimento}

@app.post("/day04/grade_evaluation")
def grade_evaluation(input: GradeEvalInput):
    resultado = ""
    if input.nota < 5:
        resultado = "Insuficiente."
    elif input.nota < 6:
        resultado = "Regular."
    elif input.nota < 7:
        resultado = "Bom."
    elif input.nota < 9:
        resultado = "Muito bom."
    else:
        resultado = "Excelente!"
    return {"status": resultado}

@app.post("/day04/ternary_status")
def ternary_status(input: TernaryInput):
    status = "aprovado" if input.nota >= 70 else "reprovado"
    return {"status": status}

@app.post("/day04/purchase_eligibility")
def purchase_eligibility(input: PurchaseInput):
    podeComprar = (not input.clienteInativo and input.saldo > 500)
    return {"pode_comprar": podeComprar}

@app.post("/day04/gate_status")
def gate_status(input: GateInput):
    message = ""
    if input.estado == "Aberta":
        message = "A cancela está aberta. Por favor, entre."
    elif input.estado == "Fechada":
        message = "A cancela está fechada. Por favor, aguarde a liberação."
    elif input.estado == "Manutenção":
        message = "A cancela está em manutenção. Por favor, use a outra entrada."
    else:
        message = "Estado desconhecido."
    return {"message": message}

@app.post("/day04/product_discount")
def product_discount(input: ProductDiscountInput):
    desconto = 0
    if input.produto == "Alimentos":
        desconto = 0.05
    elif input.produto == "Eletrônicos":
        desconto = 0.10
    elif input.produto == "Roupas":
        desconto = 0.20
    elif input.produto == "Livros":
        desconto = 0.50
    valor_final = input.preco * (1 - desconto)
    return {"valor_final": round(valor_final, 2), "desconto_aplicado": desconto}


# --- Day 05: Loops ---
@app.post("/day05/compound_interest_yearly")
def compound_interest_yearly(input: InvestmentInput):
    valor_investido = input.valorInvestido
    results = []
    for i in range(1, input.anosInvestimento + 1):
        valor_investido += valor_investido * input.taxaJuros
        results.append({"ano": i, "valor_investido": round(valor_investido, 2)})
    return {"results": results}

@app.post("/day05/countdown")
def countdown():
    messages = []
    for i in range(10, -1, -1):
        if i <= 3:
            messages.append(f"Atenção! {i}")
        else:
            messages.append(str(i))
    messages.append("Lançamento do foguete!")
    return {"countdown_messages": messages}

@app.post("/day05/compound_interest_to_double")
def compound_interest_to_double(input: InvestmentDoubleInput):
    valor_investido = input.valorInvestido
    valor_final_desejado = valor_investido * 2
    anos_investimento = 0
    while valor_investido < valor_final_desejado:
        valor_investido += valor_investido * input.taxaJuros
        anos_investimento += 1
    return {"anos_para_dobrar": anos_investimento}

@app.post("/day05/installment_payment")
def installment_payment(input: InstallmentInput):
    valor_produto = input.valorProduto
    valor_parcela = valor_produto / input.numeroParcelas
    payments = []
    for i in range(1, input.numeroParcelas + 1):
        valor_produto -= valor_parcela
        payments.append({
            "parcela_numero": i,
            "valor_parcela": round(valor_parcela, 2),
            "valor_restante": round(valor_produto, 2)
        })
    return {"payments": payments}


# --- Day 06: Funções ---
@app.post("/day06/calculate_imc")
def calculate_imc(input: IMCInput):
    imc = input.peso / (input.altura * input.altura)
    return {"imc": round(imc, 2)}

@app.post("/day06/get_day_of_week")
def get_day_of_week(input: DayOfWeekInput):
    dia_nome = ""
    if input.dia == 1: dia_nome = "Domingo"
    elif input.dia == 2: dia_nome = "Segunda-feira"
    elif input.dia == 3: dia_nome = "Terça-feira"
    elif input.dia == 4: dia_nome = "Quarta-feira"
    elif input.dia == 5: dia_nome = "Quinta-feira"
    elif input.dia == 6: dia_nome = "Sexta-feira"
    elif input.dia == 7: dia_nome = "Sábado"
    else: dia_nome = "Dia inválido!"
    return {"dia_da_semana": dia_nome}

@app.post("/day06/calculate_investment_func")
def calculate_investment_func(input: InvestmentInput):
    valor_investido = input.valorInvestido
    results = []
    for i in range(1, input.anosInvestimento + 1):
        valor_investido += valor_investido * input.taxaJuros
        results.append({"ano": i, "valor_investido": round(valor_investido, 2)})
    return {"results": results}


# --- Day 07: Sistema Bancário (Estado) ---
@app.get("/day07/banking/status", response_model=BankingStatusOutput)
def get_banking_status():
    total = banking_state["saldoConta1"] + banking_state["saldoConta2"]
    if total >= banking_state["saldoMinimoLimite"]:
        banking_state["limite"] = total * banking_state["percentualLimite"]
    else:
        banking_state["limite"] = 0.0 # Resetar limite se não atingir o mínimo
    
    return {
        "saldoConta1": round(banking_state["saldoConta1"], 2),
        "saldoConta2": round(banking_state["saldoConta2"], 2),
        "saldoTotal": round(total, 2),
        "limite": round(banking_state["limite"], 2),
        "jurosLimite": round(banking_state["jurosLimite"], 2),
        "historicoTransacoes": banking_state["historicoTransacoes"],
        "totalPorChave": banking_state["totalPorChave"] # Incluir para Day 21
    }

@app.post("/day07/banking/deposit")
def deposit(input: DepositInput):
    valor = input.valor
    if input.conta == 1:
        if banking_state["saldoConta1"] < 0:
            banking_state["jurosLimite"] += valor * 0.15
            valor *= 0.85 # Reduz o valor depositado que vai para o saldo
        banking_state["saldoConta1"] += valor
    elif input.conta == 2:
        if banking_state["saldoConta2"] < 0:
            banking_state["jurosLimite"] += valor * 0.15
            valor *= 0.85
        banking_state["saldoConta2"] += valor
    else:
        raise HTTPException(status_code=400, detail="Conta inválida.")
    return {"message": f"Depósito de R${round(input.valor, 2)} na conta {input.conta} realizado."}

@app.post("/day07/banking/debit")
def debit(input: DebitInput):
    if input.conta == 1 and input.valor <= (banking_state["saldoConta1"] + banking_state["limite"]):
        banking_state["saldoConta1"] -= input.valor
    elif input.conta == 2 and input.valor <= (banking_state["saldoConta2"] + banking_state["limite"]):
        banking_state["saldoConta2"] -= input.valor
    else:
        raise HTTPException(status_code=400, detail=f"Saldo insuficiente ou limite excedido para débito na conta {input.conta}.")
    return {"message": f"Débito de R${round(input.valor, 2)} da conta {input.conta} realizado."}

@app.post("/day07/banking/transfer")
def transfer(input: TransferInput):
    # Replicar a lógica de débito e depósito para garantir que o limite seja respeitado
    if input.contaOrigem == 1 and input.valor <= (banking_state["saldoConta1"] + banking_state["limite"]):
        banking_state["saldoConta1"] -= input.valor
        # Aplicar juros se a conta destino estiver negativa (lógica do depositar)
        valor_para_depositar = input.valor
        if input.contaDestino == 1: # Transferindo para a própria conta 1 (não faz sentido, mas replicando a lógica)
            if banking_state["saldoConta1"] < 0:
                banking_state["jurosLimite"] += valor_para_depositar * 0.15
                valor_para_depositar *= 0.85
            banking_state["saldoConta1"] += valor_para_depositar
        elif input.contaDestino == 2:
            if banking_state["saldoConta2"] < 0:
                banking_state["jurosLimite"] += valor_para_depositar * 0.15
                valor_para_depositar *= 0.85
            banking_state["saldoConta2"] += valor_para_depositar
        else:
            raise HTTPException(status_code=400, detail="Conta destino inválida.")

    elif input.contaOrigem == 2 and input.valor <= (banking_state["saldoConta2"] + banking_state["limite"]):
        banking_state["saldoConta2"] -= input.valor
        valor_para_depositar = input.valor
        if input.contaDestino == 1:
            if banking_state["saldoConta1"] < 0:
                banking_state["jurosLimite"] += valor_para_depositar * 0.15
                valor_para_depositar *= 0.85
            banking_state["saldoConta1"] += valor_para_depositar
        elif input.contaDestino == 2: # Transferindo para a própria conta 2 (não faz sentido)
            if banking_state["saldoConta2"] < 0:
                banking_state["jurosLimite"] += valor_para_depositar * 0.15
                valor_para_depositar *= 0.85
            banking_state["saldoConta2"] += valor_para_depositar
        else:
            raise HTTPException(status_code=400, detail="Conta destino inválida.")
    else:
        raise HTTPException(status_code=400, detail=f"Saldo insuficiente ou limite excedido para transferência na conta {input.contaOrigem}.")
    
    return {"message": f"Transferência de R${round(input.valor, 2)} da conta {input.contaOrigem} para {input.contaDestino} realizada."}

@app.get("/day07/banking/convert_to_usd", response_model=ConvertToDolarOutput)
def convert_to_usd(conta: int):
    if conta == 1:
        return {"saldoDolar": round(banking_state["saldoConta1"] / banking_state["taxaConversaoDolar"], 2)}
    elif conta == 2:
        return {"saldoDolar": round(banking_state["saldoConta2"] / banking_state["taxaConversaoDolar"], 2)}
    else:
        raise HTTPException(status_code=400, detail="Conta inválida.")

@app.post("/day07/banking/reset")
def reset_banking_state():
    global banking_state
    banking_state = {
        "saldoConta1": 600.0,
        "saldoConta2": 400.0,
        "limite": 0.0,
        "jurosLimite": 0.0,
        "totalTransferidoHoje": 0.0,
        "historicoTransacoes": [],
        "totalPorChave": {},
        "percentualLimite": 0.10,
        "saldoMinimoLimite": 1000.0,
        "taxaConversaoDolar": 5.23
    }
    return {"message": "Estado bancário resetado."}


# --- Day 08: Fila Simples (Estado) ---
@app.post("/day08/queue/enqueue", response_model=QueueStatusOutput)
def enqueue_simple(input: EnqueueInput):
    simple_queue.append(input.nome)
    return {"queue": simple_queue, "message": f"{input.nome} entrou na fila."}

@app.post("/day08/queue/dequeue", response_model=QueueStatusOutput)
def dequeue_simple():
    if len(simple_queue) > 0:
        cliente_atendido = simple_queue.pop(0) # Remove do início
        return {"queue": simple_queue, "message": f"{cliente_atendido} foi atendido."}
    else:
        return {"queue": simple_queue, "message": "Não há clientes na fila para atender."}

@app.get("/day08/queue/status", response_model=QueueStatusOutput)
def get_simple_queue_status():
    if len(simple_queue) > 0:
        return {"queue": simple_queue, "message": f"Clientes na fila: {', '.join(simple_queue)}"}
    else:
        return {"queue": simple_queue, "message": "A fila está vazia."}

@app.post("/day08/queue/reset")
def reset_simple_queue():
    global simple_queue
    simple_queue = []
    return {"message": "Fila simples resetada."}


# --- Day 09: Operações com Arrays/Listas (Implementações Customizadas) ---
@app.post("/day09/array/my_index_of")
def my_index_of(input: ArraySearchInput):
    try:
        index = input.array.index(input.elemento)
        return {"index": index}
    except ValueError:
        return {"index": -1}

@app.post("/day09/array/my_includes")
def my_includes(input: ArraySearchInput):
    return {"includes": input.elemento in input.array}

@app.post("/day09/array/my_last_index_of")
def my_last_index_of(input: ArraySearchInput):
    # Python's rindex() raises ValueError if not found, index() returns first
    # So, we'll implement manually for exact JS behavior
    for i in range(len(input.array) - 1, -1, -1):
        if input.array[i] == input.elemento:
            return {"index": i}
    return {"index": -1}

@app.post("/day09/array/extract_slice")
def extract_slice(input: ArraySliceInput):
    # Python slice handles negative indices and None for end automatically
    start = input.inicio if input.inicio is not None else 0
    end = input.fim if input.fim is not None else len(input.array)

    # Replicando a lógica de conversão de índice negativo do JS para Python se necessário
    if start < 0:
        start = len(input.array) + start
    if end < 0:
        end = len(input.array) + end

    # Garantir que os índices estejam dentro dos limites
    start = max(0, min(start, len(input.array)))
    end = max(0, min(end, len(input.array)))

    return {"portion": input.array[start:end]}


# --- Day 10 & 11: Pilha (Estado) ---
@app.post("/day10/stack/push_product")
def push_product(input: ProductStackInput):
    global product_stack
    if len(product_stack) < MAX_STACK_CAPACITY:
        product_stack.append(input.produto)
        return {"stack": product_stack, "message": f"Produto {input.produto} empilhado."}
    else:
        product_stack = [] # Inicia uma nova pilha
        product_stack.append(input.produto)
        return {"stack": product_stack, "message": f"Caixa cheia. Enviando para selagem e despacho. Produto {input.produto} empilhado na nova caixa."}

@app.get("/day10/stack/status")
def get_product_stack_status():
    return {"stack": product_stack, "message": f"Produtos na pilha: {len(product_stack)}"}

@app.post("/day10/stack/reset")
def reset_product_stack():
    global product_stack
    product_stack = []
    return {"message": "Pilha de produtos resetada."}

@app.post("/day11/browser/navigate_to")
def navigate_to_page(input: BrowserNavigateInput):
    if browser_history["paginaAtual"]:
        browser_history["pilhaVoltar"].append(browser_history["paginaAtual"])
        browser_history["pilhaAvancar"] = [] # Limpa pilha de avançar
    browser_history["paginaAtual"] = input.pagina
    return {"message": f"Navegando para: {browser_history['paginaAtual']}", "history": browser_history}

@app.post("/day11/browser/go_back")
def go_back():
    if not browser_history["pilhaVoltar"]:
        return {"message": "Não há páginas anteriores.", "history": browser_history}

    browser_history["pilhaAvancar"].append(browser_history["paginaAtual"])
    browser_history["paginaAtual"] = browser_history["pilhaVoltar"].pop()
    return {"message": f"Voltando para: {browser_history['paginaAtual']}", "history": browser_history}

@app.post("/day11/browser/go_forward")
def go_forward():
    if not browser_history["pilhaAvancar"]:
        return {"message": "Não há páginas à frente.", "history": browser_history}

    browser_history["pilhaVoltar"].append(browser_history["paginaAtual"])
    browser_history["paginaAtual"] = browser_history["pilhaAvancar"].pop()
    return {"message": f"Avançando para: {browser_history['paginaAtual']}", "history": browser_history}

@app.get("/day11/browser/status", response_model=BrowserStatusOutput)
def get_browser_status():
    return browser_history

@app.post("/day11/browser/reset")
def reset_browser_history():
    global browser_history
    browser_history = {
        "pilhaVoltar": [],
        "pilhaAvancar": [],
        "paginaAtual": None
    }
    return {"message": "Histórico de navegação resetado."}


# --- Day 12: Fila Drive-Thru (Estado) ---
@app.post("/day12/drivethru_queue/enqueue", response_model=DriveThruQueueStatusOutput)
def drivethru_enqueue(input: DriveThruEnqueueInput):
    drivethru_queue.append({"placa": input.placaDoCarro, "pedido": input.pedido})
    return {"totalCarros": len(drivethru_queue), "filaAtual": [item["placa"] for item in drivethru_queue]}

@app.post("/day12/drivethru_queue/serve_car", response_model=DriveThruQueueStatusOutput)
def drivethru_serve_car():
    if not drivethru_queue:
        return {"totalCarros": 0, "filaAtual": [], "message": "Não há carros na fila."}
    
    carro_atendido = drivethru_queue.pop(0)
    return {"totalCarros": len(drivethru_queue), "filaAtual": [item["placa"] for item in drivethru_queue],
            "message": f"Carro {carro_atendido['placa']} com o pedido: {carro_atendido['pedido']} foi atendido."}

@app.get("/day12/drivethru_queue/status", response_model=DriveThruQueueStatusOutput)
def get_drivethru_queue_status():
    return {"totalCarros": len(drivethru_queue), "filaAtual": [item["placa"] for item in drivethru_queue]}

@app.post("/day12/drivethru_queue/reset")
def reset_drivethru_queue():
    global drivethru_queue
    drivethru_queue = []
    return {"message": "Fila do Drive-Thru resetada."}


# --- Day 13: Deque (Gerenciamento de Tarefas - Estado) ---
@app.post("/day13/deque/insert_front", response_model=DequeStatusOutput)
def deque_insert_front(input: TaskInput):
    tasks_deque.appendleft(input.tarefa)
    return {"tarefas": list(tasks_deque), "message": f"Tarefa '{input.tarefa}' adicionada com alta prioridade."}

@app.post("/day13/deque/insert_end", response_model=DequeStatusOutput)
def deque_insert_end(input: TaskInput):
    tasks_deque.append(input.tarefa)
    return {"tarefas": list(tasks_deque), "message": f"Tarefa '{input.tarefa}' adicionada com baixa prioridade."}

@app.post("/day13/deque/remove_front", response_model=DequeStatusOutput)
def deque_remove_front():
    if tasks_deque:
        removed_task = tasks_deque.popleft()
        return {"tarefas": list(tasks_deque), "message": f"Tarefa '{removed_task}' com alta prioridade foi removida."}
    else:
        return {"tarefas": list(tasks_deque), "message": "Não há tarefas para remover."}

@app.post("/day13/deque/remove_end", response_model=DequeStatusOutput)
def deque_remove_end():
    if tasks_deque:
        removed_task = tasks_deque.pop()
        return {"tarefas": list(tasks_deque), "message": f"Tarefa '{removed_task}' com baixa prioridade foi removida."}
    else:
        return {"tarefas": list(tasks_deque), "message": "Não há tarefas para remover."}

@app.post("/day13/deque/increase_priority", response_model=DequeStatusOutput)
def deque_increase_priority(input: TaskInput):
    try:
        index = list(tasks_deque).index(input.tarefa) # Convert to list to find index
        if index > 0:
            tasks_deque[index], tasks_deque[index - 1] = tasks_deque[index - 1], tasks_deque[index] # Swap
            return {"tarefas": list(tasks_deque), "message": f"Prioridade da tarefa '{input.tarefa}' foi aumentada."}
        else:
            return {"tarefas": list(tasks_deque), "message": "A tarefa já está com a máxima prioridade ou não existe."}
    except ValueError:
        return {"tarefas": list(tasks_deque), "message": "Tarefa não encontrada."}

@app.post("/day13/deque/decrease_priority", response_model=DequeStatusOutput)
def deque_decrease_priority(input: TaskInput):
    try:
        index = list(tasks_deque).index(input.tarefa) # Convert to list to find index
        if index != -1 and index < len(tasks_deque) - 1:
            tasks_deque[index], tasks_deque[index + 1] = tasks_deque[index + 1], tasks_deque[index] # Swap
            return {"tarefas": list(tasks_deque), "message": f"Prioridade da tarefa '{input.tarefa}' foi diminuída."}
        else:
            return {"tarefas": list(tasks_deque), "message": "A tarefa já está com a mínima prioridade ou não existe."}
    except ValueError:
        return {"tarefas": list(tasks_deque), "message": "Tarefa não encontrada."}

@app.get("/day13/deque/get_tasks", response_model=DequeStatusOutput)
def deque_get_tasks():
    return {"tarefas": list(tasks_deque), "message": "Tarefas atuais."}

@app.post("/day13/deque/reset")
def reset_tasks_deque():
    global tasks_deque
    tasks_deque = collections.deque()
    return {"message": "Deque de tarefas resetado."}


# --- Day 14: Múltiplas Filas (Caixas - Estado) ---
@app.post("/day14/multi_queue/enqueue", response_model=CashierQueuesStatusOutput)
def multi_queue_enqueue(input: CashierEnqueueInput):
    if input.caixa in cashier_queues:
        cashier_queues[input.caixa].append(input.nome)
        return {"filasCaixas": cashier_queues, "message": f"{input.nome} entrou na fila do {input.caixa}."}
    else:
        raise HTTPException(status_code=400, detail=f"O {input.caixa} não existe.")

@app.post("/day14/multi_queue/serve_customer", response_model=CashierQueuesStatusOutput)
def multi_queue_serve_customer(caixa: str):
    if caixa in cashier_queues and len(cashier_queues[caixa]) > 0:
        cliente_atendido = cashier_queues[caixa].pop(0)
        return {"filasCaixas": cashier_queues, "message": f"{cliente_atendido} foi atendido no {caixa}."}
    elif caixa in cashier_queues:
        return {"filasCaixas": cashier_queues, "message": f"A fila do {caixa} está vazia."}
    else:
        raise HTTPException(status_code=400, detail=f"O {caixa} não existe.")

@app.get("/day14/multi_queue/status", response_model=CashierQueuesStatusOutput)
def get_multi_queue_status():
    return {"filasCaixas": cashier_queues}

@app.post("/day14/multi_queue/reset")
def reset_cashier_queues():
    global cashier_queues
    cashier_queues = {f"caixa{i}": [] for i in range(1, 11)}
    return {"message": "Filas dos caixas resetadas."}


# --- Day 15: Lista Encadeada (Estado) ---
@app.post("/day15/linked_list/insert_first")
def linked_list_insert_first(input: LinkedListInput):
    _insert_first_ll(input.elemento)
    return {"message": f"'{input.elemento}' inserido no início.", "list": _get_linked_list_elements()}

@app.post("/day15/linked_list/insert_last")
def linked_list_insert_last(input: LinkedListInput):
    _insert_last_ll(input.elemento)
    return {"message": f"'{input.elemento}' inserido no final.", "list": _get_linked_list_elements()}

@app.post("/day15/linked_list/insert_at")
def linked_list_insert_at(input: LinkedListInput):
    _insert_at_ll(input.elemento, input.posicao)
    return {"message": f"'{input.elemento}' inserido na posição {input.posicao}.", "list": _get_linked_list_elements()}

@app.post("/day15/linked_list/delete_at")
def linked_list_delete_at(input: LinkedListDeleteInput):
    removed = _delete_at_ll(input.posicao)
    return {"message": f"'{removed}' removido da posição {input.posicao}.", "list": _get_linked_list_elements()}

@app.get("/day15/linked_list/search_at")
def linked_list_search_at(posicao: int):
    found = _search_at_ll(posicao)
    return {"element": found, "message": f"Elemento na posição {posicao} é '{found}'."}

@app.get("/day15/linked_list/traverse", response_model=LinkedListTraversalOutput)
def linked_list_traverse():
    return {"elements": _get_linked_list_elements()}

@app.get("/day15/linked_list/index_of")
def linked_list_index_of(elemento: Any):
    index = _index_of_ll(elemento)
    return {"index": index, "message": f"Elemento '{elemento}' encontrado no índice {index}."}

@app.post("/day15/linked_list/reset")
def reset_linked_list():
    global linked_list_head
    linked_list_head = None
    return {"message": "Lista encadeada resetada."}


# --- Day 16 & 18: Playlist (Estado e Ordenação) ---
@app.post("/day16_18/playlist/add_song", response_model=PlaylistStatusOutput)
def add_song_to_playlist(input: MusicaInput):
    nova_musica = _create_musica(input.nome, input.artista, input.tempo)
    playlist_state["musicas"].insert(0, nova_musica) # Adiciona no início
    return {"musicas": playlist_state["musicas"], "message": f"🎶 Música '{input.nome}' adicionada à playlist!"}

@app.post("/day16_18/playlist/remove_song", response_model=PlaylistStatusOutput)
def remove_song_from_playlist(nome: str):
    original_len = len(playlist_state["musicas"])
    playlist_state["musicas"] = [m for m in playlist_state["musicas"] if m["nome"] != nome]
    if len(playlist_state["musicas"]) < original_len:
        return {"musicas": playlist_state["musicas"], "message": f"❌ Música '{nome}' removida da playlist."}
    else:
        return {"musicas": playlist_state["musicas"], "message": f"⚠️ Música '{nome}' não encontrada."}

@app.post("/day16_18/playlist/move_song", response_model=PlaylistStatusOutput)
def move_song_in_playlist(nome: str, novaPosicao: int):
    index = -1
    for i, musica in enumerate(playlist_state["musicas"]):
        if musica["nome"] == nome:
            index = i
            break
    
    if index == -1:
        return {"musicas": playlist_state["musicas"], "message": f"⚠️ Música '{nome}' não encontrada."}
    
    musica = playlist_state["musicas"].pop(index)
    
    # Ensure novaPosicao is within bounds
    if novaPosicao < 0:
        novaPosicao = 0
    if novaPosicao > len(playlist_state["musicas"]):
        novaPosicao = len(playlist_state["musicas"])

    playlist_state["musicas"].insert(novaPosicao, musica)
    return {"musicas": playlist_state["musicas"], "message": f"🔄 Música '{nome}' movida para a posição {novaPosicao + 1}."}

@app.post("/day16_18/playlist/play_all", response_model=PlaylistStatusOutput)
def play_all_songs():
    if not playlist_state["musicas"]:
        return {"musicas": playlist_state["musicas"], "message": "⚠️ A playlist está vazia."}
    
    messages = ["🎼 Tocando a playlist:"]
    for musica in playlist_state["musicas"]:
        musica["reproducoes"] += 1
        messages.append(f"▶️ Tocando: {musica['nome']} - {musica['artista']} ({musica['tempo']})")
    
    return {"musicas": playlist_state["musicas"], "message": "\n".join(messages)}

@app.post("/day16_18/playlist/play_song", response_model=PlaylistStatusOutput)
def play_specific_song(nome: str):
    for musica in playlist_state["musicas"]:
        if musica["nome"] == nome:
            musica["reproducoes"] += 1
            return {"musicas": playlist_state["musicas"], "message": f"🎵 Tocando: {musica['nome']} - {musica['artista']} ({musica['tempo']})"}
    return {"musicas": playlist_state["musicas"], "message": f"⚠️ Música '{nome}' não encontrada."}

@app.get("/day16_18/playlist/show_playlist", response_model=PlaylistStatusOutput)
def show_playlist():
    if not playlist_state["musicas"]:
        return {"musicas": playlist_state["musicas"], "message": "📭 A playlist está vazia."}
    return {"musicas": playlist_state["musicas"], "message": "🎶 Playlist Atual."}

@app.post("/day16_18/playlist/sort_by_name_bubble", response_model=PlaylistStatusOutput)
def sort_playlist_by_name_bubble():
    n = len(playlist_state["musicas"])
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if playlist_state["musicas"][i]["nome"].lower() > playlist_state["musicas"][i + 1]["nome"].lower():
                playlist_state["musicas"][i], playlist_state["musicas"][i + 1] = playlist_state["musicas"][i + 1], playlist_state["musicas"][i]
                swapped = True
    return {"musicas": playlist_state["musicas"], "message": "🔤 Playlist ordenada por Nome (Bubble Sort)."}

@app.post("/day16_18/playlist/sort_by_plays_selection", response_model=PlaylistStatusOutput)
def sort_playlist_by_plays_selection():
    n = len(playlist_state["musicas"])
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if playlist_state["musicas"][j]["reproducoes"] > playlist_state["musicas"][max_index]["reproducoes"]:
                max_index = j
        playlist_state["musicas"][i], playlist_state["musicas"][max_index] = playlist_state["musicas"][max_index], playlist_state["musicas"][i]
    return {"musicas": playlist_state["musicas"], "message": "🔢 Playlist ordenada por Número de Reproduções (Selection Sort)."}

@app.post("/day16_18/playlist/sort_by_name_js", response_model=PlaylistStatusOutput)
def sort_playlist_by_name_js():
    playlist_state["musicas"].sort(key=lambda x: x["nome"].lower())
    return {"musicas": playlist_state["musicas"], "message": "🔤 Playlist ordenada por Nome (Python Sort)."}

@app.post("/day16_18/playlist/sort_by_plays_js", response_model=PlaylistStatusOutput)
def sort_playlist_by_plays_js():
    playlist_state["musicas"].sort(key=lambda x: x["reproducoes"], reverse=True)
    return {"musicas": playlist_state["musicas"], "message": "🔢 Playlist ordenada por Número de Reproduções (Python Sort)."}

@app.post("/day16_18/playlist/reset")
def reset_playlist():
    global playlist_state
    playlist_state = {"musicas": []}
    return {"message": "Playlist resetada."}


# --- Day 17: Ordenação de Arrays (Produtos) ---
initial_products = [
    {"nome": "Arroz", "preco": 25.99},
    {"nome": "Feijão", "preco": 12.50},
    {"nome": "Leite", "preco": 6.49},
    {"nome": "Óleo", "preco": 8.99},
    {"nome": "Pão", "preco": 7.00},
    {"nome": "Café", "preco": 15.30},
    {"nome": "Açúcar", "preco": 4.89},
    {"nome": "Sal", "preco": 3.25},
    {"nome": "Macarrão", "preco": 5.79},
    {"nome": "Manteiga", "preco": 9.99}
]

@app.get("/day17/sorting/get_products", response_model=ProductsListOutput)
def get_products():
    return {"products": initial_products}

@app.post("/day17/sorting/sort_by_name", response_model=ProductsListOutput)
def sort_products_by_name():
    sorted_products = sorted(initial_products, key=lambda x: x["nome"].lower())
    return {"products": sorted_products}

@app.post("/day17/sorting/sort_by_price", response_model=ProductsListOutput)
def sort_products_by_price():
    sorted_products = sorted(initial_products, key=lambda x: x["preco"])
    return {"products": sorted_products}


# --- Day 19: Recursão (Cálculo de Fatura) ---
@app.post("/day19/recursion/calculate_invoice_total", response_model=InvoiceTotalOutput)
def calculate_invoice_total(fatura: List[InvoiceItem]):
    def _calculate_total_recursive(items):
        total = 0
        for item in items:
            total += item.valor
            if item.parcelas:
                total += _calculate_total_recursive(item.parcelas)
        return total
    
    total_fatura = _calculate_total_recursive(fatura)
    return {"totalFatura": round(total_fatura, 2)}


# --- Day 20: Recursão (Busca Binária e Busca de Mensagens) ---
@app.post("/day20/recursion/binary_search")
def binary_search_recursive(input: BinarySearchInput):
    lista = sorted(input.lista) # Binary search requires sorted list
    valor = input.valor

    def _binary_search(arr, val, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if arr[mid] == val:
            return mid
        
        if val < arr[mid]:
            return _binary_search(arr, val, low, mid - 1)
        
        return _binary_search(arr, val, mid + 1, high)
    
    result_index = _binary_search(lista, valor, 0, len(lista) - 1)
    
    if result_index != -1:
        # Return the original index if found
        try:
            original_index = input.lista.index(valor)
            return {"index": original_index, "message": f"Valor '{valor}' encontrado no índice {original_index} (após ordenação, estava no índice {result_index})."}
        except ValueError:
            return {"index": result_index, "message": f"Valor '{valor}' encontrado no índice {result_index} (lista ordenada)."}
    else:
        return {"index": -1, "message": f"Valor '{valor}' não encontrado na lista."}


@app.post("/day20/recursion/search_messages_by_word", response_model=SearchMessagesOutput)
def search_messages_by_word_recursive(input: SearchMessagesInput):
    
    def _search_recursive(messages_list, word, index=0, found_messages=[]):
        if index >= len(messages_list):
            return found_messages

        msg = messages_list[index].mensagem.lower()
        term = word.lower()

        if term in msg:
            found_messages.append({
                "nome": messages_list[index].nome,
                "mensagem": messages_list[index].mensagem,
                "telefone": messages_list[index].telefone,
                "data": messages_list[index].data,
                "original_index": index # Adiciona o índice original para referência
            })

        return _search_recursive(messages_list, word, index + 1, found_messages)

    found_results = _search_recursive(input.mensagens, input.palavra)
    return {"encontrados": found_results}


# --- Day 21: Sistema Bancário Pix (Estado) ---
@app.get("/day21/pix_banking/status", response_model=BankingStatusOutput)
def get_pix_banking_status():
    # Reutiliza a função de status do Day 07, pois o estado é compartilhado
    return get_banking_status()

@app.post("/day21/pix_banking/send_pix")
def send_pix(input: PixInput):
    chave_pix = input.chavePix
    valor = input.valor
    mensagem = input.mensagem
    data = input.data

    # Calcula o total já transferido para essa chave
    if chave_pix not in banking_state["totalPorChave"]:
        banking_state["totalPorChave"][chave_pix] = 0.0

    total_para_essa_chave = banking_state["totalPorChave"][chave_pix]
    
    # O limite permitido é o maior entre o limite diário e o total já transferido para essa chave
    # (Lógica da resolução JS: se já transferiu mais que o limite diário, o limite "aumenta" para o total já transferido)
    limite_permitido = max(banking_state["limiteDiario"], total_para_essa_chave)

    # Calcula o total transferido hoje (com base no histórico)
    total_hoje = sum(
        t["valor"] for t in banking_state["historicoTransacoes"]
        if t["data"] == data and t["tipo"] == "PIX"
    )

    # Validações
    if total_hoje + valor > limite_permitido:
        raise HTTPException(status_code=400, detail=f"❌ Limite diário de R$ {limite_permitido:.2f} excedido para hoje.")

    if banking_state["saldo"] < valor:
        raise HTTPException(status_code=400, detail="❌ Saldo insuficiente.")

    # Realiza a transferência
    banking_state["saldo"] -= valor
    banking_state["totalPorChave"][chave_pix] += valor

    banking_state["historicoTransacoes"].append({
        "tipo": "PIX",
        "chavePix": chave_pix,
        "valor": valor,
        "mensagem": mensagem,
        "data": data
    })

    return {"message": f"✅ Pix de R${valor:.2f} enviado para {chave_pix} em {data}."}

@app.post("/day21/pix_banking/cancel_pix")
def cancel_pix(input: CancelPixInput):
    # Simplificando a lógica de cancelamento para usar apenas o índice
    # A versão JS original usa dataTransacao, mas o exemplo de uso só passa o índice.
    # Vamos assumir que o índice é da lista atual de historicoTransacoes.
    
    if input.indiceTransacao < 0 or input.indiceTransacao >= len(banking_state["historicoTransacoes"]):
        raise HTTPException(status_code=400, detail="❌ Índice de transação inválido para cancelamento.")
    
    transacao = banking_state["historicoTransacoes"][input.indiceTransacao]

    if transacao["tipo"] != "PIX":
        raise HTTPException(status_code=400, detail="❌ Transação inválida para cancelamento (não é um PIX).")

    chave_pix = transacao["chavePix"]
    valor = transacao["valor"]

    # Estorna o valor
    banking_state["saldo"] += valor

    # Atualiza total por chave
    banking_state["totalPorChave"][chave_pix] -= valor

    # Registra o reembolso (como uma nova transação no histórico)
    banking_state["historicoTransacoes"].append({
        "tipo": "REEMBOLSO",
        "chavePix": chave_pix,
        "valor": valor,
        "mensagem": "Reembolso de Pix",
        "data": input.dataTransacao if input.dataTransacao else "Data do cancelamento" # Usar data fornecida ou genérica
    })
    
    # Opcional: remover a transação original de PIX do histórico se for um cancelamento "real"
    # Se mantiver, o histórico terá tanto o PIX quanto o REEMBOLSO.
    # Exemplo: banking_state["historicoTransacoes"].pop(input.indiceTransacao)

    return {"message": f"↩️ Pix cancelado. Valor de R${valor:.2f} devolvido para a conta."}

@app.post("/day21/pix_banking/reset")
def reset_pix_banking_state():
    global banking_state
    banking_state = {
        "saldo": 50000.0,
        "limiteDiario": 10000.0,
        "totalTransferidoHoje": 0.0,
        "historicoTransacoes": [],
        "totalPorChave": {}
    }
    # Resetar também as contas do Day 07 se elas compartilham o mesmo estado 'banking_state'
    # O Day 07 e Day 21 usam a mesma variável global 'banking_state', então o reset de um afeta o outro.
    # Se fossem independentes, precisariam de variáveis de estado separadas.
    return {"message": "Estado do sistema bancário Pix resetado."}

# Inicializa o saldo e limites para o Day 21 Pix Banking
# Isso precisa ser feito APÓS a definição de banking_state, para que o saldo exista.
banking_state["saldo"] = 50000.0
banking_state["limiteDiario"] = 10000.0
