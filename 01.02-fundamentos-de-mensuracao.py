import pandas as pd
dados = {
    "Indicador": [
        "Faturamento",
        "Pedidos",
        "Clientes compradores"
    ],
    "Agosto": [
        100000,
        500,
        250
    ],
    "Setembro": [
        120000,
        600,
        300
    ]
}

df = pd.DataFrame(dados)

print(df)