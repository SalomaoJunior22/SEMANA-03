def cadastrar_aluno(nome, idade):
    return {
        "nome": nome,
        "idade": idade
    }


def exibir_aluno(aluno):
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")