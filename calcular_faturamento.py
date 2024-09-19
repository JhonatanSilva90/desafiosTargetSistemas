import json

def faturamento_dia():
    dados = [
        {
            "dia": 1,
            "valor": 22174.1664
        },
        {
            "dia": 2,
            "valor": 24537.6698
        },
        {
            "dia": 3,
            "valor": 26139.6134
        },
        {
            "dia": 4,
            "valor": 0.0
        },
        {
            "dia": 5,
            "valor": 0.0
        },
        {
            "dia": 6,
            "valor": 26742.6612
        },
        {
            "dia": 7,
            "valor": 0.0
        },
        {
            "dia": 8,
            "valor": 42889.2258
        },
        {
            "dia": 9,
            "valor": 46251.174
        },
        {
            "dia": 10,
            "valor": 11191.4722
        },
        {
            "dia": 11,
            "valor": 0.0
        },
        {
            "dia": 12,
            "valor": 0.0
        },
        {
            "dia": 13,
            "valor": 3847.4823
        },
        {
            "dia": 14,
            "valor": 373.7838
        },
        {
            "dia": 15,
            "valor": 2659.7563
        },
        {
            "dia": 16,
            "valor": 48924.2448
        },
        {
            "dia": 17,
            "valor": 18419.2614
        },
        {
            "dia": 18,
            "valor": 0.0
        },
        {
            "dia": 19,
            "valor": 0.0
        },
        {
            "dia": 20,
            "valor": 35240.1826
        },
        {
            "dia": 21,
            "valor": 43829.1667
        },
        {
            "dia": 22,
            "valor": 18235.6852
        },
        {
            "dia": 23,
            "valor": 4355.0662
        },
        {
            "dia": 24,
            "valor": 13327.1025
        },
        {
            "dia": 25,
            "valor": 0.0
        },
        {
            "dia": 26,
            "valor": 0.0
        },
        {
            "dia": 27,
            "valor": 25681.8318
        },
        {
            "dia": 28,
            "valor": 1718.1221
        },
        {
            "dia": 29,
            "valor": 13220.495
        },
        {
            "dia": 30,
            "valor": 8414.61
        }
    ]

    with open('faturamento.json', 'w') as file:
        json.dump(dados, file, indent=4)

def calcular_faturamento(caminho_arquivo_json):
    with open(caminho_arquivo_json, 'r') as file:
        dados = json.load(file)

    faturamentos = [item['valor'] for item in dados if item['valor'] > 0]

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
