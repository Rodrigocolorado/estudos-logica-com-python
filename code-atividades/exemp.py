# Função para calcular a divisão da soma de dois números
def divisao_de_somas(numero1, numero2, numero3, numero4):
    # Soma dos dois primeiros números
    soma1 = numero1 + numero2
    # Soma dos dois últimos números
    soma2 = numero3 + numero4
    # Verifica se o segundo valor (divisor) não é zero para evitar divisão por zero
    if soma2 == 0:
        return "Divisão por zero não é permitida."
    else:
        # Calcula a divisão
        resultado = soma1 / soma2
        return resultado

# Exemplo de uso
numero1 = 10
numero2 = 5
numero3 = 3
numero4 = 2

resultado = divisao_de_somas(numero1, numero2, numero3, numero4)
print(f"O resultado da divisão das somas é: {resultado}")
