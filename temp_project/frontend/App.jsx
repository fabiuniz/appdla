import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

// API call utility with debugging
const callApi = async (method, endpoint, data = null) => {
    console.log(`[callApi] Starting ${method} to ${endpoint}`, { data });
    try {
        const response = await fetch(`http://vmlinuxd:8000${endpoint}`, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: data ? JSON.stringify(data) : null,
        });
        console.log(`[callApi] Response status: ${response.status}`);
        const result = await response.json();
        console.log(`[callApi] Response data:`, result);
        return { success: response.ok, data: result, error: response.ok ? null : result.detail || 'Request failed' };
    } catch (error) {
        console.error(`[callApi] Error:`, error.message);
        return { success: false, error: error.message };
    }
};

// Reusable FunctionCard component
const FunctionCard = ({ title, description, children }) => (
    <div className="bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-xl font-semibold text-gray-800 mb-2">{title}</h3>
        <p className="text-sm text-gray-600 mb-4">{description}</p>
        {children}
    </div>
);

// Day 03: Basic Operations
const Day03 = () => {
    const [val1, setVal1] = useState('');
    const [val2, setVal2] = useState('');
    const [sumResult, setSumResult] = useState(null);
    const [hours, setHours] = useState({ segunda: '', terca: '', quarta: '', quinta: '', sexta: '' });
    const [hoursResult, setHoursResult] = useState(null);

    const handleSum = async () => {
        if (!val1 || !val2) {
            alert('Por favor, insira ambos os valores.');
            return;
        }
        const data = { val1: parseFloat(val1), val2: parseFloat(val2) };
        const res = await callApi('POST', '/day03/sum', data);
        if (res.success) setSumResult(res.data.result);
        else alert(`Erro: ${res.error}`);
    };

    const handleTotalHours = async () => {
        const { segunda, terca, quarta, quinta, sexta } = hours;
        if (!segunda || !terca || !quarta || !quinta || !sexta) {
            alert('Por favor, preencha todas as horas.');
            return;
        }
        const data = {
            segunda: parseFloat(segunda),
            terca: parseFloat(terca),
            quarta: parseFloat(quarta),
            quinta: parseFloat(quinta),
            sexta: parseFloat(sexta),
        };
        const res = await callApi('POST', '/day03/total_hours', data);
        if (res.success) setHoursResult(res.data.result);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Soma" description="Calcula a soma de dois números. Exemplo: val1=5, val2=3 retorna 8.">
                <input type="number" value={val1} onChange={(e) => setVal1(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Valor 1" />
                <input type="number" value={val2} onChange={(e) => setVal2(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Valor 2" />
                <button onClick={handleSum} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
                {sumResult !== null && <p className="mt-2">Resultado: {sumResult}</p>}
            </FunctionCard>
            <FunctionCard title="Total de Horas" description="Soma as horas trabalhadas na semana. Exemplo: 8, 8, 8, 8, 8 retorna 40.">
                <input type="number" value={hours.segunda} onChange={(e) => setHours({ ...hours, segunda: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Segunda" />
                <input type="number" value={hours.terca} onChange={(e) => setHours({ ...hours, terca: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Terça" />
                <input type="number" value={hours.quarta} onChange={(e) => setHours({ ...hours, quarta: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Quarta" />
                <input type="number" value={hours.quinta} onChange={(e) => setHours({ ...hours, quinta: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Quinta" />
                <input type="number" value={hours.sexta} onChange={(e) => setHours({ ...hours, sexta: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Sexta" />
                <button onClick={handleTotalHours} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
                {hoursResult !== null && <p className="mt-2">Total de Horas: {hoursResult}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 04: Conditionals
const Day04 = () => {
    const [cnhInput, setCnhInput] = useState({ idade: '', primeiraHabilitacao: false });
    const [cnhResult, setCnhResult] = useState(null);
    const [nota, setNota] = useState('');
    const [gradeResult, setGradeResult] = useState(null);

    const handleCnhRenewal = async () => {
        if (!cnhInput.idade) {
            alert('Por favor, insira a idade.');
            return;
        }
        const data = { idade: parseInt(cnhInput.idade), primeiraHabilitacao: cnhInput.primeiraHabilitacao };
        const res = await callApi('POST', '/day04/cnh_renewal', data);
        if (res.success) setCnhResult(res.data.prazo_renovacao);
        else alert(`Erro: ${res.error}`);
    };

    const handleGradeEvaluation = async () => {
        if (!nota) {
            alert('Por favor, insira a nota.');
            return;
        }
        const data = { nota: parseFloat(nota) };
        const res = await callApi('POST', '/day04/grade_evaluation', data);
        if (res.success) setGradeResult(res.data.status);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Renovação de CNH" description="Calcula o prazo de renovação da CNH com base na idade e se é a primeira habilitação.">
                <input type="number" value={cnhInput.idade} onChange={(e) => setCnhInput({ ...cnhInput, idade: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Idade" />
                <label className="flex items-center mb-4">
                    <input type="checkbox" checked={cnhInput.primeiraHabilitacao} onChange={(e) => setCnhInput({ ...cnhInput, primeiraHabilitacao: e.target.checked })} className="mr-2" />
                    Primeira Habilitação
                </label>
                <button onClick={handleCnhRenewal} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
                {cnhResult && <p className="mt-2">Prazo de Renovação: {cnhResult}</p>}
            </FunctionCard>
            <FunctionCard title="Avaliação de Nota" description="Avalia a nota de um aluno e retorna o status (ex.: Insuficiente, Regular, Bom).">
                <input type="number" value={nota} onChange={(e) => setNota(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Nota (0-10)" />
                <button onClick={handleGradeEvaluation} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Avaliar</button>
                {gradeResult && <p className="mt-2">Status: {gradeResult}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 05: Loops
const Day05 = () => {
    const [investmentInput, setInvestmentInput] = useState({ valorInvestido: '', taxaJuros: '', anosInvestimento: '' });
    const [investmentResult, setInvestmentResult] = useState(null);
    const [countdownResult, setCountdownResult] = useState(null);

    const handleCompoundInterest = async () => {
        const { valorInvestido, taxaJuros, anosInvestimento } = investmentInput;
        if (!valorInvestido || !taxaJuros || !anosInvestimento) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = {
            valorInvestido: parseFloat(valorInvestido),
            taxaJuros: parseFloat(taxaJuros),
            anosInvestimento: parseInt(anosInvestimento),
        };
        const res = await callApi('POST', '/day05/compound_interest_yearly', data);
        if (res.success) setInvestmentResult(res.data.results);
        else alert(`Erro: ${res.error}`);
    };

    const handleCountdown = async () => {
        const res = await callApi('POST', '/day05/countdown');
        if (res.success) setCountdownResult(res.data.countdown_messages);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Juros Compostos" description="Calcula o valor acumulado com juros compostos ao longo dos anos.">
                <input type="number" value={investmentInput.valorInvestido} onChange={(e) => setInvestmentInput({ ...investmentInput, valorInvestido: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Valor Investido" />
                <input type="number" value={investmentInput.taxaJuros} onChange={(e) => setInvestmentInput({ ...investmentInput, taxaJuros: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Taxa de Juros (ex.: 0.05)" />
                <input type="number" value={investmentInput.anosInvestimento} onChange={(e) => setInvestmentInput({ ...investmentInput, anosInvestimento: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Anos de Investimento" />
                <button onClick={handleCompoundInterest} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
                {investmentResult && (
                    <ul className="mt-2 max-h-64 overflow-y-auto bg-gray-50 p-2 rounded-md">
                        {investmentResult.map((item, index) => (
                            <li key={index}>Ano {item.ano}: R${item.valor_investido}</li>
                        ))}
                    </ul>
                )}
            </FunctionCard>
            <FunctionCard title="Contagem Regressiva" description="Realiza uma contagem regressiva de 10 até o lançamento.">
                <button onClick={handleCountdown} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Iniciar</button>
                {countdownResult && (
                    <ul className="mt-2 max-h-64 overflow-y-auto bg-gray-50 p-2 rounded-md">
                        {countdownResult.map((msg, index) => (
                            <li key={index}>{msg}</li>
                        ))}
                    </ul>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 06: Functions
const Day06 = () => {
    const [imcInput, setImcInput] = useState({ peso: '', altura: '' });
    const [imcResult, setImcResult] = useState(null);
    const [dia, setDia] = useState('');
    const [dayResult, setDayResult] = useState(null);

    const handleImc = async () => {
        const { peso, altura } = imcInput;
        if (!peso || !altura) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = { peso: parseFloat(peso), altura: parseFloat(altura) };
        const res = await callApi('POST', '/day06/calculate_imc', data);
        if (res.success) setImcResult(res.data.imc);
        else alert(`Erro: ${res.error}`);
    };

    const handleDayOfWeek = async () => {
        if (!dia) {
            alert('Por favor, insira o número do dia.');
            return;
        }
        const data = { dia: parseInt(dia) };
        const res = await callApi('POST', '/day06/get_day_of_week', data);
        if (res.success) setDayResult(res.data.dia_da_semana);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Calcular IMC" description="Calcula o Índice de Massa Corporal (IMC). Exemplo: peso=70, altura=1.75 retorna 22.86.">
                <input type="number" value={imcInput.peso} onChange={(e) => setImcInput({ ...imcInput, peso: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Peso (kg)" />
                <input type="number" value={imcInput.altura} onChange={(e) => setImcInput({ ...imcInput, altura: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Altura (m)" />
                <button onClick={handleImc} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
                {imcResult !== null && <p className="mt-2">IMC: {imcResult}</p>}
            </FunctionCard>
            <FunctionCard title="Dia da Semana" description="Retorna o dia da semana com base no número (1-7). Exemplo: dia=1 retorna Domingo.">
                <input type="number" value={dia} onChange={(e) => setDia(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Dia (1-7)" />
                <button onClick={handleDayOfWeek} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Verificar</button>
                {dayResult && <p className="mt-2">Dia: {dayResult}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 07: Banking Operations
const Day07 = () => {
    const [result, setResult] = useState(null);
    const [depositInput, setDepositInput] = useState({ conta: '', valor: '' });
    const [depositResult, setDepositResult] = useState(null);

    const handleStatus = async () => {
        const res = await callApi('GET', '/day07/banking/status');
        if (res.success) setResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleDeposit = async () => {
        const { conta, valor } = depositInput;
        if (!conta || !valor) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = { conta: parseInt(conta), valor: parseFloat(valor) };
        const res = await callApi('POST', '/day07/banking/deposit', data);
        if (res.success) {
            setDepositResult(res.data.message);
            handleStatus(); // Atualizar status após depósito
        } else {
            alert(`Erro: ${res.error}`);
        }
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Status Bancário" description="Retorna o status das contas bancárias. Inclui saldo de duas contas, saldo total e limite.">
                <button onClick={handleStatus} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Ver Status</button>
                {result && (
                    <div className="mt-2">
                        <p>Saldo Conta 1: R${result.saldoConta1}</p>
                        <p>Saldo Conta 2: R${result.saldoConta2}</p>
                        <p>Saldo Total: R${result.saldoTotal}</p>
                        <p>Limite: R${result.limite}</p>
                        <p>Juros de Limite: R${result.jurosLimite}</p>
                    </div>
                )}
            </FunctionCard>
            <FunctionCard title="Depósito" description="Realiza um depósito em uma conta (1 ou 2).">
                <select value={depositInput.conta} onChange={(e) => setDepositInput({ ...depositInput, conta: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2">
                    <option value="">Selecione a Conta</option>
                    <option value="1">Conta 1</option>
                    <option value="2">Conta 2</option>
                </select>
                <input type="number" value={depositInput.valor} onChange={(e) => setDepositInput({ ...depositInput, valor: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Valor do Depósito" />
                <button onClick={handleDeposit} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Depositar</button>
                {depositResult && <p className="mt-2">{depositResult}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 08: Simple Queue
const Day08 = () => {
    const [nome, setNome] = useState('');
    const [queueResult, setQueueResult] = useState(null);
    const [dequeueResult, setDequeueResult] = useState(null);

    const handleEnqueue = async () => {
        if (!nome) {
            alert('Por favor, insira o nome.');
            return;
        }
        const data = { nome };
        const res = await callApi('POST', '/day08/queue/enqueue', data);
        if (res.success) setQueueResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleDequeue = async () => {
        const res = await callApi('POST', '/day08/queue/dequeue');
        if (res.success) setDequeueResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Adicionar à Fila" description="Adiciona um cliente à fila. Exemplo: nome='João' adiciona João à fila.">
                <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Nome do Cliente" />
                <button onClick={handleEnqueue} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {queueResult && <p className="mt-2">{queueResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Atender Cliente" description="Atende o próximo cliente da fila.">
                <button onClick={handleDequeue} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Atender</button>
                {dequeueResult && (
                    <div className="mt-2">
                        <p>{dequeueResult.message}</p>
                        <p>Fila Atual: {dequeueResult.queue.join(', ') || 'Vazia'}</p>
                    </div>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 09: Array Operations
const Day09 = () => {
    const [arrayInput, setArrayInput] = useState('');
    const [elemento, setElemento] = useState('');
    const [indexResult, setIndexResult] = useState(null);
    const [includesResult, setIncludesResult] = useState(null);

    const parseArray = (str) => {
        try {
            return JSON.parse(str);
        } catch (e) {
            alert('Por favor, insira um array válido (ex.: [1,2,3]).');
            return [];
        }
    };

    const handleIndexOf = async () => {
        if (!arrayInput || !elemento) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const array = parseArray(arrayInput);
        const data = { array, elemento: parseFloat(elemento) || elemento };
        const res = await callApi('POST', '/day09/array/my_index_of', data);
        if (res.success) setIndexResult(res.data.index);
        else alert(`Erro: ${res.error}`);
    };

    const handleIncludes = async () => {
        if (!arrayInput || !elemento) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const array = parseArray(arrayInput);
        const data = { array, elemento: parseFloat(elemento) || elemento };
        const res = await callApi('POST', '/day09/array/my_includes', data);
        if (res.success) setIncludesResult(res.data.includes);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Índice no Array" description="Encontra o índice de um elemento no array. Exemplo: array=[1,2,3], elemento=2 retorna 1.">
                <input type="text" value={arrayInput} onChange={(e) => setArrayInput(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Array (ex.: [1,2,3])" />
                <input type="text" value={elemento} onChange={(e) => setElemento(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Elemento" />
                <button onClick={handleIndexOf} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Buscar</button>
                {indexResult !== null && <p className="mt-2">Índice: {indexResult}</p>}
            </FunctionCard>
            <FunctionCard title="Contém no Array" description="Verifica se um elemento está no array. Exemplo: array=[1,2,3], elemento=2 retorna true.">
                <input type="text" value={arrayInput} onChange={(e) => setArrayInput(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Array (ex.: [1,2,3])" />
                <input type="text" value={elemento} onChange={(e) => setElemento(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Elemento" />
                <button onClick={handleIncludes} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Verificar</button>
                {includesResult !== null && <p className="mt-2">Contém: {includesResult ? 'Sim' : 'Não'}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 10: Product Stack
const Day10 = () => {
    const [produto, setProduto] = useState('');
    const [stackResult, setStackResult] = useState(null);
    const [statusResult, setStatusResult] = useState(null);

    const handlePushProduct = async () => {
        if (!produto) {
            alert('Por favor, insira o nome do produto.');
            return;
        }
        const data = { produto };
        const res = await callApi('POST', '/day10/stack/push_product', data);
        if (res.success) setStackResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleStatus = async () => {
        const res = await callApi('GET', '/day10/stack/status');
        if (res.success) setStatusResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Empilhar Produto" description="Adiciona um produto à pilha. Capacidade máxima: 10 produtos.">
                <input type="text" value={produto} onChange={(e) => setProduto(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Nome do Produto" />
                <button onClick={handlePushProduct} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Empilhar</button>
                {stackResult && <p className="mt-2">{stackResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Status da Pilha" description="Mostra o estado atual da pilha de produtos.">
                <button onClick={handleStatus} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Ver Status</button>
                {statusResult && (
                    <div className="mt-2">
                        <p>{statusResult.message}</p>
                        <p>Pilha: {statusResult.stack.join(', ') || 'Vazia'}</p>
                    </div>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 11: Browser Navigation
const Day11 = () => {
    const [pagina, setPagina] = useState('');
    const [navigateResult, setNavigateResult] = useState(null);
    const [backResult, setBackResult] = useState(null);
    const [forwardResult, setForwardResult] = useState(null);

    const handleNavigate = async () => {
        if (!pagina) {
            alert('Por favor, insira a página.');
            return;
        }
        const data = { pagina };
        const res = await callApi('POST', '/day11/browser/navigate_to', data);
        if (res.success) setNavigateResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleGoBack = async () => {
        const res = await callApi('POST', '/day11/browser/go_back');
        if (res.success) setBackResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleGoForward = async () => {
        const res = await callApi('POST', '/day11/browser/go_forward');
        if (res.success) setForwardResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <FunctionCard title="Navegar" description="Navega para uma nova página.">
                <input type="text" value={pagina} onChange={(e) => setPagina(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Página (ex.: google.com)" />
                <button onClick={handleNavigate} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Navegar</button>
                {navigateResult && <p className="mt-2">{navigateResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Voltar" description="Volta para a página anterior.">
                <button onClick={handleGoBack} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Voltar</button>
                {backResult && <p className="mt-2">{backResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Avançar" description="Avança para a próxima página.">
                <button onClick={handleGoForward} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Avançar</button>
                {forwardResult && <p className="mt-2">{forwardResult.message}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 12: Drive-Thru Queue
const Day12 = () => {
    const [carInput, setCarInput] = useState({ placaDoCarro: '', pedido: '' });
    const [enqueueResult, setEnqueueResult] = useState(null);
    const [serveResult, setServeResult] = useState(null);

    const handleEnqueue = async () => {
        const { placaDoCarro, pedido } = carInput;
        if (!placaDoCarro || !pedido) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = { placaDoCarro, pedido };
        const res = await callApi('POST', '/day12/drivethru_queue/enqueue', data);
        if (res.success) setEnqueueResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleServe = async () => {
        const res = await callApi('POST', '/day12/drivethru_queue/serve_car');
        if (res.success) setServeResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Adicionar Carro" description="Adiciona um carro à fila do drive-thru.">
                <input type="text" value={carInput.placaDoCarro} onChange={(e) => setCarInput({ ...carInput, placaDoCarro: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Placa do Carro" />
                <input type="text" value={carInput.pedido} onChange={(e) => setCarInput({ ...carInput, pedido: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Pedido" />
                <button onClick={handleEnqueue} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {enqueueResult && <p className="mt-2">Total de Carros: {enqueueResult.totalCarros}</p>}
            </FunctionCard>
            <FunctionCard title="Atender Carro" description="Atende o próximo carro na fila do drive-thru.">
                <button onClick={handleServe} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Atender</button>
                {serveResult && (
                    <div className="mt-2">
                        <p>{serveResult.message || `Total de Carros: ${serveResult.totalCarros}`}</p>
                        <p>Fila Atual: {serveResult.filaAtual.join(', ') || 'Vazia'}</p>
                    </div>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 13: Task Deque
const Day13 = () => {
    const [tarefa, setTarefa] = useState('');
    const [frontResult, setFrontResult] = useState(null);
    const [endResult, setEndResult] = useState(null);

    const handleInsertFront = async () => {
        if (!tarefa) {
            alert('Por favor, insira a tarefa.');
            return;
        }
        const data = { tarefa };
        const res = await callApi('POST', '/day13/deque/insert_front', data);
        if (res.success) setFrontResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleInsertEnd = async () => {
        if (!tarefa) {
            alert('Por favor, insira a tarefa.');
            return;
        }
        const data = { tarefa };
        const res = await callApi('POST', '/day13/deque/insert_end', data);
        if (res.success) setEndResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Adicionar Tarefa (Alta Prioridade)" description="Adiciona uma tarefa no início do deque (alta prioridade).">
                <input type="text" value={tarefa} onChange={(e) => setTarefa(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Tarefa" />
                <button onClick={handleInsertFront} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {frontResult && <p className="mt-2">{frontResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Adicionar Tarefa (Baixa Prioridade)" description="Adiciona uma tarefa no final do deque (baixa prioridade).">
                <input type="text" value={tarefa} onChange={(e) => setTarefa(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Tarefa" />
                <button onClick={handleInsertEnd} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {endResult && <p className="mt-2">{endResult.message}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 14: Multiple Queues (Cashiers)
const Day14 = () => {
    const [enqueueInput, setEnqueueInput] = useState({ caixa: '', nome: '' });
    const [enqueueResult, setEnqueueResult] = useState(null);
    const [serveCaixa, setServeCaixa] = useState('');
    const [serveResult, setServeResult] = useState(null);

    const handleEnqueue = async () => {
        const { caixa, nome } = enqueueInput;
        if (!caixa || !nome) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = { caixa, nome };
        const res = await callApi('POST', '/day14/multi_queue/enqueue', data);
        if (res.success) setEnqueueResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleServe = async () => {
        if (!serveCaixa) {
            alert('Por favor, selecione o caixa.');
            return;
        }
        const res = await callApi('POST', `/day14/multi_queue/serve_customer?caixa=${serveCaixa}`);
        if (res.success) setServeResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Adicionar Cliente a Caixa" description="Adiciona um cliente a uma fila de caixa (caixa1 a caixa10).">
                <select value={enqueueInput.caixa} onChange={(e) => setEnqueueInput({ ...enqueueInput, caixa: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2">
                    <option value="">Selecione o Caixa</option>
                    {[...Array(10)].map((_, i) => (
                        <option key={i} value={`caixa${i + 1}`}>Caixa {i + 1}</option>
                    ))}
                </select>
                <input type="text" value={enqueueInput.nome} onChange={(e) => setEnqueueInput({ ...enqueueInput, nome: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Nome do Cliente" />
                <button onClick={handleEnqueue} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {enqueueResult && <p className="mt-2">{enqueueResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Atender Cliente" description="Atende o próximo cliente de um caixa específico.">
                <select value={serveCaixa} onChange={(e) => setServeCaixa(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4">
                    <option value="">Selecione o Caixa</option>
                    {[...Array(10)].map((_, i) => (
                        <option key={i} value={`caixa${i + 1}`}>Caixa {i + 1}</option>
                    ))}
                </select>
                <button onClick={handleServe} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Atender</button>
                {serveResult && <p className="mt-2">{serveResult.message}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 15: Linked List
const Day15 = () => {
    const [insertInput, setInsertInput] = useState({ elemento: '' });
    const [insertFirstResult, setInsertFirstResult] = useState(null);
    const [insertLastResult, setInsertLastResult] = useState(null);

    const handleInsertFirst = async () => {
        if (!insertInput.elemento) {
            alert('Por favor, insira o elemento.');
            return;
        }
        const data = { elemento: insertInput.elemento };
        const res = await callApi('POST', '/day15/linked_list/insert_first', data);
        if (res.success) setInsertFirstResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleInsertLast = async () => {
        if (!insertInput.elemento) {
            alert('Por favor, insira o elemento.');
            return;
        }
        const data = { elemento: insertInput.elemento };
        const res = await callApi('POST', '/day15/linked_list/insert_last', data);
        if (res.success) setInsertLastResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Inserir no Início" description="Insere um elemento no início da lista encadeada.">
                <input type="text" value={insertInput.elemento} onChange={(e) => setInsertInput({ ...insertInput, elemento: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Elemento" />
                <button onClick={handleInsertFirst} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Inserir</button>
                {insertFirstResult && <p className="mt-2">{insertFirstResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Inserir no Final" description="Insere um elemento no final da lista encadeada.">
                <input type="text" value={insertInput.elemento} onChange={(e) => setInsertInput({ ...insertInput, elemento: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Elemento" />
                <button onClick={handleInsertLast} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Inserir</button>
                {insertLastResult && <p className="mt-2">{insertLastResult.message}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 16_18: Playlist
const Day16_18 = () => {
    const [musicaInput, setMusicaInput] = useState({ nome: '', artista: '', tempo: '' });
    const [addResult, setAddResult] = useState(null);
    const [removeNome, setRemoveNome] = useState('');
    const [removeResult, setRemoveResult] = useState(null);

    const handleAddSong = async () => {
        const { nome, artista, tempo } = musicaInput;
        if (!nome || !artista || !tempo) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        const data = { nome, artista, tempo };
        const res = await callApi('POST', '/day16_18/playlist/add_song', data);
        if (res.success) setAddResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleRemoveSong = async () => {
        if (!removeNome) {
            alert('Por favor, insira o nome da música.');
            return;
        }
        const res = await callApi('POST', `/day16_18/playlist/remove_song?nome=${encodeURIComponent(removeNome)}`);
        if (res.success) setRemoveResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Adicionar Música" description="Adiciona uma música à playlist.">
                <input type="text" value={musicaInput.nome} onChange={(e) => setMusicaInput({ ...musicaInput, nome: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Nome da Música" />
                <input type="text" value={musicaInput.artista} onChange={(e) => setMusicaInput({ ...musicaInput, artista: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Artista" />
                <input type="text" value={musicaInput.tempo} onChange={(e) => setMusicaInput({ ...musicaInput, tempo: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Duração (ex.: 3:45)" />
                <button onClick={handleAddSong} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Adicionar</button>
                {addResult && <p className="mt-2">{addResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Remover Música" description="Remove uma música da playlist pelo nome.">
                <input type="text" value={removeNome} onChange={(e) => setRemoveNome(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Nome da Música" />
                <button onClick={handleRemoveSong} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Remover</button>
                {removeResult && <p className="mt-2">{removeResult.message}</p>}
            </FunctionCard>
        </div>
    );
};

// Day 17: Sorting Products
const Day17 = () => {
    const [productsResult, setProductsResult] = useState(null);
    const [sortNameResult, setSortNameResult] = useState(null);

    const handleGetProducts = async () => {
        const res = await callApi('GET', '/day17/sorting/get_products');
        if (res.success) setProductsResult(res.data.products);
        else alert(`Erro: ${res.error}`);
    };

    const handleSortByName = async () => {
        const res = await callApi('POST', '/day17/sorting/sort_by_name');
        if (res.success) setSortNameResult(res.data.products);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Lista de Produtos" description="Obtém a lista inicial de produtos.">
                <button onClick={handleGetProducts} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Obter Produtos</button>
                {productsResult && (
                    <ul className="mt-2 max-h-64 overflow-y-auto bg-gray-50 p-2 rounded-md">
                        {productsResult.map((product, index) => (
                            <li key={index}>{product.nome}: R${product.preco}</li>
                        ))}
                    </ul>
                )}
            </FunctionCard>
            <FunctionCard title="Ordenar por Nome" description="Ordena os produtos por nome.">
                <button onClick={handleSortByName} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Ordenar</button>
                {sortNameResult && (
                    <ul className="mt-2 max-h-64 overflow-y-auto bg-gray-50 p-2 rounded-md">
                        {sortNameResult.map((product, index) => (
                            <li key={index}>{product.nome}: R${product.preco}</li>
                        ))}
                    </ul>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 19: Invoice Recursion
const Day19 = () => {
    const [invoiceInput, setInvoiceInput] = useState('[{"descricao": "Item 1", "valor": 100}, {"descricao": "Item 2", "valor": 200}]');
    const [invoiceResult, setInvoiceResult] = useState(null);

    const parseJson = (str) => {
        try {
            return JSON.parse(str);
        } catch (e) {
            alert('Por favor, insira um JSON válido.');
            return [];
        }
    };

    const handleCalculateInvoice = async () => {
        const fatura = parseJson(invoiceInput);
        const res = await callApi('POST', '/day19/recursion/calculate_invoice_total', fatura);
        if (res.success) setInvoiceResult(res.data.totalFatura);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <FunctionCard title="Calcular Total da Fatura" description="Calcula o total de uma fatura com itens aninhados. Exemplo: [{'descricao': 'Item 1', 'valor': 100}] retorna 100.">
            <textarea value={invoiceInput} onChange={(e) => setInvoiceInput(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4 h-32 font-mono text-xs" placeholder="JSON da Fatura" />
            <button onClick={handleCalculateInvoice} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Calcular</button>
            {invoiceResult !== null && <p className="mt-2">Total da Fatura: R${invoiceResult}</p>}
        </FunctionCard>
    );
};

// Day 20: Recursion (Search)
const Day20 = () => {
    const [binaryList, setBinaryList] = useState('[5,10,15,20,25,30,35,40]');
    const [binaryValue, setBinaryValue] = useState('');
    const [binaryResult, setBinaryResult] = useState(null);
    const [messagesJson, setMessagesJson] = useState(`[
        {"nome": "Ana", "mensagem": "Oi, tudo bem?", "telefone": "123", "data": "2025-05-26"},
        {"nome": "Bob", "mensagem": "Tudo ótimo por aqui!", "telefone": "456", "data": "2025-05-26"}
    ]`);
    const [keyword, setKeyword] = useState('tudo');
    const [messageResult, setMessageResult] = useState(null);

    const parseArray = (str) => {
        try {
            return JSON.parse(str);
        } catch (e) {
            alert('Formato JSON inválido. Use: [item1, item2, ...]');
            return [];
        }
    };

    const parseJson = (str) => {
        try {
            return JSON.parse(str);
        } catch (e) {
            alert(`Erro no JSON: ${e.message}`);
            return [];
        }
    };

    const handleBinarySearch = async () => {
        if (!binaryValue) {
            alert('Por favor, insira um valor para buscar.');
            return;
        }
        const lista = parseArray(binaryList);
        const data = { lista, valor: parseFloat(binaryValue) };
        const res = await callApi('POST', '/day20/recursion/binary_search', data);
        if (res.success) setBinaryResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    const handleMessageSearch = async () => {
        if (!keyword) {
            alert('Por favor, insira uma palavra-chave.');
            return;
        }
        const mensagens = parseJson(messagesJson);
        const data = { mensagens, palavra: keyword };
        const res = await callApi('POST', '/day20/recursion/search_messages_by_word', data);
        if (res.success) setMessageResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Busca Binária" description="Realiza busca binária em um array ordenado para encontrar o índice de um valor.">
                <input type="text" value={binaryList} onChange={(e) => setBinaryList(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Array (JSON, ex.: [5,10,15])" />
                <input type="number" value={binaryValue} onChange={(e) => setBinaryValue(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Valor a buscar" />
                <button onClick={handleBinarySearch} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Buscar</button>
                {binaryResult && <p className="mt-2">{binaryResult.message}</p>}
            </FunctionCard>
            <FunctionCard title="Busca em Mensagens" description="Busca recursivamente uma palavra-chave em mensagens.">
                <textarea value={messagesJson} onChange={(e) => setMessagesJson(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2 h-64 font-mono text-xs" placeholder="JSON de mensagens" />
                <input type="text" value={keyword} onChange={(e) => setKeyword(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Palavra-chave" />
                <button onClick={handleMessageSearch} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Buscar</button>
                {messageResult && messageResult.encontrados && (
                    <ul className="mt-2 text-sm max-h-64 overflow-y-auto bg-gray-50 p-2 rounded-md">
                        {messageResult.encontrados.map((msg, i) => (
                            <li key={i}>{msg.nome}: {msg.mensagem}</li>
                        ))}
                    </ul>
                )}
            </FunctionCard>
        </div>
    );
};

// Day 21: Pix Banking
const Day21 = () => {
    const [pixInput, setPixInput] = useState({ chavePix: '', valor: '', mensagem: '', data: '2025-05-26' });
    const [pixResult, setPixResult] = useState(null);
    const [statusResult, setStatusResult] = useState(null);

    const handleSendPix = async () => {
        const { chavePix, valor, mensagem, data } = pixInput;
        if (!chavePix || !valor || !data) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }
        const dataPayload = { chavePix, valor: parseFloat(valor), mensagem, data };
        const res = await callApi('POST', '/day21/pix_banking/send_pix', dataPayload);
        if (res.success) {
            setPixResult(res.data.message);
            handleStatus(); // Atualizar status após o Pix
        } else {
            alert(`Erro: ${res.error}`);
        }
    };

    const handleStatus = async () => {
        const res = await callApi('GET', '/day21/pix_banking/status');
        if (res.success) setStatusResult(res.data);
        else alert(`Erro: ${res.error}`);
    };

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <FunctionCard title="Enviar Pix" description="Envia um Pix para uma chave especificada.">
                <input type="text" value={pixInput.chavePix} onChange={(e) => setPixInput({ ...pixInput, chavePix: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Chave Pix" />
                <input type="number" value={pixInput.valor} onChange={(e) => setPixInput({ ...pixInput, valor: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Valor" />
                <input type="text" value={pixInput.mensagem} onChange={(e) => setPixInput({ ...pixInput, mensagem: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-2" placeholder="Mensagem (opcional)" />
                <input type="text" value={pixInput.data} onChange={(e) => setPixInput({ ...pixInput, data: e.target.value })} className="w-full p-2 border border-gray-300 rounded-md focus:border-blue-600 outline-none mb-4" placeholder="Data (ex.: 2025-05-26)" />
                <button onClick={handleSendPix} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Enviar Pix</button>
                {pixResult && <p className="mt-2">{pixResult}</p>}
            </FunctionCard>
            <FunctionCard title="Status Bancário (Pix)" description="Mostra o status do sistema bancário Pix.">
                <button onClick={handleStatus} className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Ver Status</button>
                {statusResult && (
                    <div className="mt-2">
                        <p>Saldo Conta 1: R${statusResult.saldoConta1}</p>
                        <p>Saldo Conta 2: R${statusResult.saldoConta2}</p>
                        <p>Saldo Total: R${statusResult.saldoTotal}</p>
                        <p>Limite: R${statusResult.limite}</p>
                    </div>
                )}
            </FunctionCard>
        </div>
    );
};

// Main App Component
const App = () => {
    const [activeDay, setActiveDay] = useState('03');

    const days = {
        '03': <Day03 />,
        '04': <Day04 />,
        '05': <Day05 />,
        '06': <Day06 />,
        '07': <Day07 />,
        '08': <Day08 />,
        '09': <Day09 />,
        '10': <Day10 />,
        '11': <Day11 />,
        '12': <Day12 />,
        '13': <Day13 />,
        '14': <Day14 />,
        '15': <Day15 />,
        '16_18': <Day16_18 />,
        '17': <Day17 />,
        '19': <Day19 />,
        '20': <Day20 />,
        '21': <Day21 />,
    };

    return (
        <div className="min-h-screen bg-gray-50">
            <header className="bg-blue-600 text-white py-6 shadow-md">
                <div className="container mx-auto px-4">
                    <h1 className="text-3xl font-bold">Desafio 21 Dias de Código Fonte TV</h1>
                    <p className="mt-2">Explore as funcionalidades implementadas em cada dia do desafio!</p>
                </div>
            </header>
            <nav className="bg-white shadow-md">
                <div className="container mx-auto px-4 py-4">
                    <ul className="flex flex-wrap gap-4">
                        {['03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16_18', '17', '19', '20', '21'].map((day) => (
                            <li key={day}>
                                <button
                                    onClick={() => {
                                        console.log(`[Nav] Switching to Day ${day}`);
                                        setActiveDay(day);
                                    }}
                                    className={`px-4 py-2 rounded-md ${activeDay === day ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-800 hover:bg-gray-300'}`}
                                >
                                    Dia {day.replace('_', ' e ')}
                                </button>
                            </li>
                        ))}
                    </ul>
                </div>
            </nav>
            <main className="container mx-auto px-4 py-8">
                {days[activeDay]}
            </main>
            <footer className="bg-gray-800 text-white py-4">
                <div className="container mx-auto px-4 text-center">
                    <p>© 2025 Desafio 21 Dias. Todos os direitos reservados.</p>
                </div>
            </footer>
        </div>
    );
};

// Render the App
const root = createRoot(document.getElementById('root'));
root.render(<App />);