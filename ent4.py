# LISTA SEGURA

def adicionar_item(lista, item):
    nova_lista = lista.copy()  # Cria uma cópia da lista original
    nova_lista.append(item)    # Adiciona o item à cópia
    return nova_lista          # Retorna a nova lista


# Exemplo de utilização
lista_original = [10, 20, 30]

lista_nova = adicionar_item(lista_original, 40)

print("Lista original:", lista_original)
print("Lista nova:", lista_nova)