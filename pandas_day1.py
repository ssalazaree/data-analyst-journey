import pandas as pd

# criar dataset simples (tipo dados reais)
data = {
    "nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
    "idade": [23, 35, 29, 41, 38],
    "salario": [1100, 2500, 1800, 4000, 2500]
}

df = pd.DataFrame(data)

# ver dados
print("DATASET:")
print(df)

# média de salários
print("\nMédia de idade:")
print(df["idade"].mean())

# pessoa com menor salário
print("\nMenor salário:")
print(df[df["salario"] == df["salario"].min()])

