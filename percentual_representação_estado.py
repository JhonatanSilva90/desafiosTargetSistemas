def calcular_percentuais(faturamento):

    total = sum(faturamento.values())

    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

    return percentuais

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais = calcular_percentuais(faturamento)

    for estado, percentual in percentuais.items():
        print(f"O percentual de representação de {estado} é: {percentual:.2f}%")

main()