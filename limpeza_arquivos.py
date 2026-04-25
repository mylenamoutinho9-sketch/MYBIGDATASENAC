
import pandas as pd

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="evolução_gasolina"
)


# Lendo o arquivo e corrigindo o erro de acentuação
df = pd.read_csv('precos-gasolina-etanol-11(1)', encoding='utf-8') 
# Se o erro persistir, tente:
# df = pd.read_csv('seu_arquivo.csv', encoding='latin1'

# De String para Float
df['Numero Rua'] = df['Numero Rua'].astype(float)
# De String para Int
df['Numero Rua'] = df['Numero Rua'].astype(int)

df = df.rename(columns={
 'Num_rua': 'Numero Rua',
 'Nome_rua': 'Nome da Rua',
 'CNPJ_Revenda': 'CNPJ da Revenda'
})



