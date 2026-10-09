# MODULO CALCULADORA

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Divide dois números, tratando a divisão por zero."""
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None

    resultado = a / b
    return resultado


# Exemplos de utilização
if __name__ == "__main__":
    print("Soma:", somar(10, 5))
    print("Subtração:", subtrair(10, 5))
    print("Multiplicação:", multiplicar(10, 5))
    print("Divisão:", dividir(10, 5))
    print(dividir(10, 1))