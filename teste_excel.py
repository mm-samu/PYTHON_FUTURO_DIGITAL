import pandas as pd

# Caminho do arquivo Excel
caminho = r"C:\Users\rbmme\Downloads\NOVA TABELA.xlsx"

# Ler a planilha
df = pd.read_excel(caminho)

# Exibir as primeiras linhas para confirmar leitura
print("Prévia dos dados:")
print(df.head(), "\n")

# Calcular a matriz de correlação (entre todas as colunas numéricas)
corr = df.corr(numeric_only=True)

# Exibir a matriz de correlação
print("Matriz de Correlação:")
print(corr, "\n")

# Salvar o resultado em um novo arquivo Excel
saida = r"C:\Users\rbmme\Downloads\Matriz_de_Correlacao.xlsx"
corr.to_excel(saida, index=True)

print(f"✅ Matriz de correlação salva com sucesso em:\n{saida}")
