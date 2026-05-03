import pandas as pd

# carregar dados de um ficheiro real
df = pd.read_csv("data.csv")

print("DATA:")
print(df)

print("\nIdade média:")
print(df["idade"].mean())

print("\nMaior salário:")
print(df["salario"].max())

print("\nPessoa com maior salário:")
print(df[df["salario"] == df["salario"].max()])

print("\nSalario médio:")
print(df["salario"].mean())

print("\nIdade mínima:")
print(df["idade"].min())

print("\nOrdenar por Salário:")
print(df.sort_values("salario", ascending=False))

ricos = df[df["salario"] > 2000]
print(ricos["nome"].to_list())

print("\nOrdem por idade:")
print(df.sort_values("idade", ascending=True))

print("\nLista de nomes:")
print(df["nome"].to_list())

nomes_novos = df[df["idade"] < 30]["nome"].to_list()
print(nomes_novos)