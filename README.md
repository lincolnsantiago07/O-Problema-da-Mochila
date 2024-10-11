# Algoritmo Genético para o Problema da Mochila em Python

## 📌 Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Configurações](#configurações)
- [Exemplo de Saída](#exemplo-de-saída)
- [Considerações Finais](#considerações-finais)

---

## 📝 Descrição

Este projeto implementa um **Algoritmo Genético** (AG) em Python para resolver o **Problema da Mochila**. O objetivo é selecionar um conjunto de itens com pesos e valores específicos para maximizar o valor total sem exceder um peso máximo permitido.

### **Problema da Mochila**

Dada uma lista de itens, cada um com um peso e um valor, o algoritmo deve determinar quais itens incluir na mochila de forma a maximizar o valor total, sem que o peso total exceda o limite máximo da mochila.

---

## 🚀 Funcionalidades

- **Codificação Binária**: Representa cada solução como um vetor binário, onde cada gene indica a inclusão (`1`) ou exclusão (`0`) de um item na mochila.
- **População Inicial Configurável**: Define o número de cromossomos/indivíduos na população inicial.
- **Taxa de Mutação Ajustável**: Controla a probabilidade de alteração de bits nos cromossomos.
- **Crossover de Ponto Único**: Combina genes de dois pais para gerar novos filhos.
- **Seleção por Torneio**: Seleciona os melhores indivíduos para a reprodução com base em competições entre subconjuntos da população.
- **Elitismo Opcional**: Preserva os melhores indivíduos de cada geração para garantir a qualidade das soluções.
- **Critério de Parada Configurável**: Define o número máximo de gerações que o algoritmo irá executar.
- **Saída Organizada**: Exibe as melhores soluções encontradas de forma clara e estruturada.

---

## 📋 Requisitos

- **Python 3.6** ou superior
- Nenhuma biblioteca externa é necessária; utiliza apenas módulos padrão do Python (`random`, `copy`, `pprint`).

---

## 🔧 Instalação

1. **Clone o Repositório** (se aplicável) ou **baixe o script** diretamente.

   ```bash
   git clone https://github.com/lincolnsantiago07/O-Problema-da-Mochila.git
Navegue até o Diretório do Projeto


## ▶️ Como Executar
Certifique-se de ter o Python Instalado

Verifique a versão do Python instalada:

python --version
Deve retornar algo como Python 3.8.5.

Execute o Script

No terminal ou prompt de comando, execute:

python genetic_algorithm_knapsack.py
Substitua genetic_algorithm_knapsack.py pelo nome do arquivo onde o código foi salvo.

Acompanhe a Saída

O algoritmo exibirá as melhores soluções encontradas após as gerações definidas, mostrando o valor total e a seleção dos itens para a mochila.

## ⚙️ Configurações
As principais configurações do algoritmo estão definidas no início do script. Você pode ajustar os parâmetros conforme necessário para adequar o comportamento do AG às suas necessidades.

Parâmetros Configuráveis
weights_e_valores: Lista de itens, onde cada item é representado por [peso, valor].

peso_maximo: Peso máximo permitido na mochila.

numero_de_cromossomos: Número de indivíduos na população.

geracoes: Número de gerações a serem executadas pelo algoritmo.

tamanho_cromossomo: Número de genes em cada cromossomo, igual ao número de itens.

Parâmetros do Algoritmo Genético

taxa_mutacao: Taxa de mutação aplicada aos cromossomos (5%).

elitismo: Ativa ou desativa o elitismo (True).

numero_melhores: Número de melhores indivíduos a serem retornados após todas as gerações (5).

numero_elites: Número de indivíduos a serem mantidos por elitismo em cada geração (2).

Para ajustar qualquer configuração, simplesmente modifique os valores correspondentes no início do script antes de executar.

## 📈 Exemplo de Saída
Ao executar o algoritmo, você verá uma saída semelhante a esta no terminal:

Melhores Soluções Encontradas:
1. Valor Total: 830.0
   Seleção dos Itens: [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]

2. Valor Total: 830.0
   Seleção dos Itens: [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]

3. Valor Total: 830.0
   Seleção dos Itens: [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]

4. Valor Total: 830.0
   Seleção dos Itens: [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]

5. Valor Total: 830.0
   Seleção dos Itens: [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
   
Interpretação:

Valor Total: Valor total dos itens selecionados.

Seleção dos Itens: Lista binária onde cada posição indica se o item correspondente está incluído (1) ou não (0) na mochila.

Nota: Devido à natureza aleatória dos algoritmos genéticos, os resultados podem variar a cada execução. Se todas as soluções são iguais, isso pode indicar que o algoritmo convergiu para uma solução ótima.

## 🧠 Considerações Finais
Diversidade Genética: A taxa de mutação de 5% ajuda a manter a diversidade na população, prevenindo a convergência prematura para soluções subótimas.
Elitismo: Preservar os melhores indivíduos de cada geração garante que as melhores soluções sejam mantidas ao longo das gerações.
Ajuste de Parâmetros: Experimentar diferentes configurações (como tamanho da população, taxa de mutação, número de gerações) pode levar a melhores resultados ou acelerar a convergência.
Precisão vs. Desempenho: O número de cromossomos e a taxa de mutação influenciam a precisão e o tempo de processamento do algoritmo.
