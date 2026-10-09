
from alunos import cadastrar_aluno, exibir_aluno
from operacoes import calcular_media, verificar_aprovacao


def main():
    aluno = cadastrar_aluno("João Silva", 17)

    print("=== DADOS DO ALUNO ===")
    exibir_aluno(aluno)

    nota1 = 8.0
    nota2 = 6.0

    media = calcular_media(nota1, nota2)
    situacao = verificar_aprovacao(media)

    print("\n=== RESULTADO FINAL ===")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()