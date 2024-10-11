import random
import copy
from pprint import pprint

# Definições do problema
weights_e_valores = [
    [2, 10], [4, 30], [6, 300], [8, 10], [8, 30],
    [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]
]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50
tamanho_cromossomo = len(weights_e_valores)

# Parâmetros do Algoritmo Genético
taxa_mutacao = 0.05  # Aumentada para manter diversidade
elitismo = True
numero_melhores = 5  # Número de melhores indivíduos a serem retornados
numero_elites = 2    # Número de indivíduos a serem mantidos por elitismo

# Função de avaliação da aptidão
def avaliar_fitness(cromossomo):
    total_peso = 0
    total_valor = 0
    for gene, (peso, valor) in zip(cromossomo, weights_e_valores):
        if gene == 1:
            total_peso += peso
            total_valor += valor
    if total_peso > peso_maximo:
        return 0  # Penaliza soluções que excedem o peso máximo
    return total_valor

# Inicialização da população
def inicializar_populacao(tamanho_populacao, tamanho_cromossomo):
    populacao = []
    for _ in range(tamanho_populacao):
        cromossomo = [random.randint(0,1) for _ in range(tamanho_cromossomo)]
        populacao.append(cromossomo)
    return populacao

# Seleção por torneio
def selecao_torneio(populacao, fitness_populacao, torneio_size=3):
    selecionados = []
    for _ in range(len(populacao)):
        participantes = random.sample(list(zip(populacao, fitness_populacao)), torneio_size)
        vencedor = max(participantes, key=lambda x: x[1])
        selecionados.append(copy.deepcopy(vencedor[0]))
    return selecionados

# Cruzamento (Single Point Crossover)
def cruzamento(populacao_selecionada):
    nova_populacao = []
    for i in range(0, len(populacao_selecionada), 2):
        pai1 = populacao_selecionada[i]
        if i+1 < len(populacao_selecionada):
            pai2 = populacao_selecionada[i+1]
        else:
            pai2 = populacao_selecionada[0]
        ponto = random.randint(1, tamanho_cromossomo-1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        nova_populacao.extend([filho1, filho2])
    return nova_populacao

# Mutação
def mutacao(populacao, taxa_mutacao):
    for cromossomo in populacao:
        for i in range(len(cromossomo)):
            if random.random() < taxa_mutacao:
                cromossomo[i] = 1 - cromossomo[i]
    return populacao

# Algoritmo Genético
def algoritmo_genetico():
    populacao = inicializar_populacao(numero_de_cromossomos, tamanho_cromossomo)
    historico_melhores = []

    for geracao in range(geracoes):
        fitness_populacao = [avaliar_fitness(crom) for crom in populacao]
        
        # Ordenar população por fitness descendente
        populacao_e_fitness = list(zip(populacao, fitness_populacao))
        populacao_e_fitness.sort(key=lambda x: x[1], reverse=True)
        populacao = [crom for crom, fit in populacao_e_fitness]
        fitness_populacao = [fit for crom, fit in populacao_e_fitness]
        
        # Registrar os melhores da geração
        melhores_da_geracao = populacao_e_fitness[:numero_elites]
        for crom, fit in melhores_da_geracao:
            historico_melhores.append([round(fit, 2), crom])
        
        # Seleção
        populacao_selecionada = selecao_torneio(populacao, fitness_populacao)
        
        # Cruzamento
        nova_populacao = cruzamento(populacao_selecionada)
        
        # Mutação
        nova_populacao = mutacao(nova_populacao, taxa_mutacao)
        
        # Elitismo: manter os melhores indivíduos
        if elitismo:
            nova_populacao[:numero_elites] = [crom for crom, fit in melhores_da_geracao]
        
        populacao = nova_populacao

    # Após todas as gerações, selecionar os melhores indivíduos
    fitness_final = [avaliar_fitness(crom) for crom in populacao]
    populacao_e_fitness_final = list(zip(populacao, fitness_final))
    populacao_e_fitness_final.sort(key=lambda x: x[1], reverse=True)
    
    # Selecionar os melhores únicos
    melhores = []
    vistos = set()
    for crom, fit in populacao_e_fitness_final:
        crom_tuple = tuple(crom)
        if crom_tuple not in vistos and fit > 0:
            melhores.append([round(fit, 2), crom])
            vistos.add(crom_tuple)
        if len(melhores) >= numero_melhores:
            break
    
    return melhores

# Executar o Algoritmo Genético
melhores_solucao = algoritmo_genetico()

# Exibir as melhores soluções de forma organizada
print("Melhores Soluções Encontradas:")
for idx, (valor, cromossomo) in enumerate(melhores_solucao, start=1):
    print(f"{idx}. Valor Total: {valor}")
    print(f"   Seleção dos Itens: {cromossomo}")
    print()


