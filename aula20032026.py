

# dados_entrada = []
# print('Digite 5 nomes de filmes:')
# for i in range(5):
#     nome = input(f"filme{i+1}:")
#     dados_entrada.append(nome)

# print("-" * 30)

# #Armazenamento e Exibição: 
# # 1. LISTA: 
# lista_filmes = dados_entrada
# print(lista_filmes) 
 
# # 2. TUPLA: 
# tupla_filmes = tuple(dados_entrada) 
# print(tupla_filmes)
# # 3. SET:  
# set_filmes = set(dados_entrada) 
# print(set_filmes)
# # 4. DICIONÁRIO: Usando o índice como chave (ex: 1: 'Filme A') 
# dicionario_filmes = {} 
# for i in range(len(dados_entrada)): # Repetição pelo tamanho da lista 
#     # Usando o índice (i+1) como CHAVE e o nome como VALOR 
#     dicionario_filmes[i + 1] = dados_entrada[i]  
 
# print(f"LISTA (Flexível): {lista_filmes}") 
# print(f"TUPLA (Fixa): {tupla_filmes}") 
# print(f"SET (Apenas Únicos): {set_filmes}") 
# print(f"DICIONÁRIO (Chave: Valor): {dicionario_filmes}")


# =========== FUNÇÃO ======================

# import time

# def dar_boas_vindas():
#     print("-"*40)
#     print("  Bem-vindo ao nosso aplicativo! ☺")
#     print("-"*40)

# print("Início do programa.")
# print('Por favor, aguarde...')
# time.sleep(2)
# dar_boas_vindas()
# print("Meio do programa.")
# dar_boas_vindas()
# print("Fim do programa.")

# def boas_vindas_personalizado(nome_da_pessoa):
#     print("-"*40)
#     print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! ☺")
#     print("-"*40)

# boas_vindas_personalizado("Maria")
# boas_vindas_personalizado("João")

import random # Sempre no topo do arquivo!

def gerar_dados(qtd, min_val, max_val):
    """
    Gera uma LISTA de números aleatórios.
    - qtd: quantos números queremos na lista
    - min_val: o valor mínimo (inclusivo)
    - max_val: o valor máximo (inclusivo)
    """
    
    # A estrutura a seguir se chama "List Comprehension". 
    # É um jeito rápido de criar uma lista usando um loop.
    lista_de_dados = [random.randint(min_val, max_val) for _ in range(qtd)]
    
    return lista_de_dados



#testemunhando a função 

import random

dados_aleatorios = gerar_dados(10, 1, 100) # Gerar numeros da quantidade(10) determinada de 1 a 100 
print(f"Dados gerados:{dados_aleatorios}")

lista_de_dados = []
for _ in range(qtd):
    numero=random.randint(min_val,max_val)
    lista_de_dados.append(numero)

returnlista_de_dados

