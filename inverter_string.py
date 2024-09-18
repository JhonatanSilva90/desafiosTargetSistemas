def inverter_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

def main_inversao():
    string = input("Digite uma palavra: ")
    invertida = inverter_string(string)
    print(f"A palavra invertida é: {invertida}")

main_inversao()
