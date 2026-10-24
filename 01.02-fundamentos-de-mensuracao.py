
import pandas as pd

# 1. Armazenar os dados
dados = {
    "Agosto": {
        "faturamento": 100000,
        "pedidos": 500,
        "clientes": 250
    },
    "Setembro": {
        "faturamento": 120000,
        "pedidos": 600,
        "clientes": 300
    }
}

# 2. Transformar os dados em tabela
tabela = pd.DataFrame(dados)

# 3. Renomear os indicadores
tabela.index = [
    "Faturamento",
    "Pedidos",
    "Clientes compradores"
]



# Transformar em tabela
tabela = pd.DataFrame(dados)

# Visualizar
print(tabela.to_string())

"""
# 4. Exibir a tabela formatada
try:
    from IPython.display import display
    display(tabela)
except ImportError:
    print(tabela.to_string())
"""

# 5. Calcular o crescimento do faturamento
crescimento = (
    dados["Setembro"]["faturamento"]
    / dados["Agosto"]["faturamento"] - 1
) * 100

# 6. Calcular o faturamento por pedido
ticket_agosto = (
    dados["Agosto"]["faturamento"]
    / dados["Agosto"]["pedidos"]
)

ticket_setembro = (
    dados["Setembro"]["faturamento"]
    / dados["Setembro"]["pedidos"]
)

# 7. Calcular o faturamento por cliente
cliente_agosto = (
    dados["Agosto"]["faturamento"]
    / dados["Agosto"]["clientes"]
)

cliente_setembro = (
    dados["Setembro"]["faturamento"]
    / dados["Setembro"]["clientes"]
)

# 8. Exibir os resultados
print("\n=== ANÁLISE COMERCIAL ===")

print(f"Crescimento do faturamento: {crescimento:.1f}%")

print(f"Faturamento por pedido em agosto: R$ {ticket_agosto:.2f}")
print(f"Faturamento por pedido em setembro: R$ {ticket_setembro:.2f}")

print(f"Faturamento por cliente em agosto: R$ {cliente_agosto:.2f}")
print(f"Faturamento por cliente em setembro: R$ {cliente_setembro:.2f}")
