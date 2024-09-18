import json

def faturamento_dia():
    dados = [
        {"dia": "2024-09-01", "faturamento": 0},
        {"dia": "2024-09-02", "faturamento": 1200},
        {"dia": "2024-09-03", "faturamento": 1500},
        {"dia": "2024-09-04", "faturamento": 500},
        {"dia": "2024-09-05", "faturamento": 800},
        {"dia": "2024-09-06", "faturamento": 1300},
        {"dia": "2024-09-07", "faturamento": 2200},
        {"dia": "2024-09-08", "faturamento": 0},
        {"dia": "2024-09-09", "faturamento": 1300},
        {"dia": "2024-09-10", "faturamento": 1700},
        {"dia": "2024-09-11", "faturamento": 2200},
        {"dia": "2024-09-12", "faturamento": 600},
        {"dia": "2024-09-13", "faturamento": 1350},
        {"dia": "2024-09-14", "faturamento": 1800},
        {"dia": "2024-09-15", "faturamento": 0},
        {"dia": "2024-09-16", "faturamento": 1400},
        {"dia": "2024-09-17", "faturamento": 1900}
    ]

    with open('faturamento.json', 'w') as file:
        json.dump(dados, file, indent=4)

def calcular_faturamento(caminho_arquivo_json):
    with open(caminho_arquivo_json, 'r') as file:
        dados = json.load(file)

    faturamentos = [item['faturamento'] for item in dados if item['faturamento'] > 0]

    if not faturamentos:
        return "Não há faturamento para calcular a média."

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_media = sum(1 for f in faturamentos if f > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    faturamento_dia()

    caminho_arquivo_json = 'faturamento.json'

    resultado = calcular_faturamento(caminho_arquivo_json)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        menor, maior, acima_media = resultado
        print(f"Menor valor de faturamento: {menor}")
        print(f"Maior valor de faturamento: {maior}")
        print(f"Número de dias com faturamento acima da média: {acima_media}")

main()