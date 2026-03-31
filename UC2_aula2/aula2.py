import pandas as pd

# #Ler o arquivo Excel para um dataframe
  # df = pd.read_excel('C:\\Users\\mylena.lima\\Downloads\\base_invest.xlsx', sheet_name= 'Transacoes')
 # df_vendas = pd.read_excel('"C:\\Users\\mylena.lima\Downloads\\base_invest.xlsx"', sheet_name=)


# df_transacoes = pd.read_excel('C:\\Users\\mylena.lima\\Downloads\\base_invest.xlsx', sheet_name='Transacoes')
# # df_ativo = pd.read_excel('C:\\Users\\mylena.lima\\Downloads\\base_invest.xlsx', sheet_name='ativo')

# #Quais são as máximas e mínimas de operação de compra e venda das transações?
# #variavel nova   tabela   [filtro]
# df_compra = df_transacoes[df_transacoes['operacao']== 'compra']
# df_venda = df_transacoes[df_transacoes['operacao']== 'venda']

# print(df_compra)
# print(df_venda)


# max_compra_preco = df_compra['preco'].max()
# min_compra_preco = df_compra['preco'].min()
# max_venda_preco = df_venda['preco'].min()
# min_venda_preco = df_venda['preco'].min()

# print("--- Preços máximos e mínimos das operações ---")
# print(f"Preço máximo de compra: {max_compra_preco}")
# print(f"Preço mínimo de compra: {min_compra_preco}")
# print(f"Preço máximo de venda: {max_venda_preco}")
# print(f"Preço mínimo de venda: {min_venda_preco}")
# print("\n")

#Qual CNPJ tem o ativo de maior valor?

df_transacoes = pd.read_excel('C:\\Users\\mylena.lima\\Downloads\\base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('C:\\Users\\mylena.lima\\Downloads\\base_invest.xlsx', sheet_name='Ativo')

df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']

valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
# print(valor_por_ativo)
id_ativo_maior_valor = valor_por_ativo.idxmax()

cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print(f"O CNPJ para o ativo total com maior valor é: {cnpj_maior_valor}")



# import pandas as pd

# # idades_lista = [25, 30, 22, 28]

# # idades_series = pd.Series([25, 30, 22, 28])


# notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])
# notas_ajustadas = notas*1.10
# # print(notas)

# # print(notas[notas > 8])
# # print(notas.describe())
# # print(notas.mean())
# print(notas_ajustadas)

# notas_exame_final = pd.Series([10.0, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana'])

# diferenca = abs(notas_exame_final - notas_ajustadas)
# # diferenca = notas_ajustadas - notas_exame_final == add abs()
# print(diferenca)
