# MODULO UTILIDADES

# 1. Conversor de temperatura
def conversor_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# 2. Validador de senha
def validador_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


# 3. Caixa com *precos
def caixa(*precos):
    total = sum(precos)
    return total


# 4. Ficha do aluno com **dados
def ficha_aluno(**dados):
    print("\n===== FICHA DO ALUNO =====")

    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

    print("==========================")


# Testando as funções
if __name__ == "__main__":

    # Conversor de temperatura
    temperatura = 25
    resultado = conversor_temperatura(temperatura)
    print("===== CONVERSOR DE TEMPERATURA =====")
    print(f"{temperatura}°C equivale a {resultado}°F")

    # Validador de senha
    print("\n===== VALIDADOR DE SENHA =====")
    senha = input("Digite uma senha: ")

    if validador_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida! A senha deve ter pelo menos 8 caracteres.")

    # Caixa com vários preços
    print("\n===== CAIXA =====")
    total = caixa(10.50, 20.00, 15.75)
    print(f"Total das compras: R$ {total:.2f}")

    # Ficha do aluno
    ficha_aluno(
        nome="João",
        idade=18,
        curso="Python",
        nota=9.5
    )