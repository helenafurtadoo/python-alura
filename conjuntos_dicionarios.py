# exercico 1
#n ter repeticoes = conjunto --> remover repeticoes
# solictiar o nome dos convidados , e no final exibir a lista organizada 
# #sem repeticoes
# receber os nomes, ate o usuario digitar 'sair' 3 no final mostrar a litas
listaNomes = set()
while True:
    nome = input('Digite o nome do convidado (ou "sair" para parar): ')
    if nome.lower() == "sair":
#nome.lowe() para dxar todas as letras minusculas, para evitar erros
        break
    else:
        listaNomes.add(nome)
print(f'Convidados confirmados: {sorted(listaNomes)}')
# ou:
# listaNomes = set()

# while True:
#     nome = input('Digite o nome do convidado (ou "sair" para parar): ')
#     if nome.lower() == "sair":
#         break
#     listaNomes.add(nome)

# print("\nConvidados confirmados:")
# for nome in sorted(listaNomes):
    # print(f"- {nome}")