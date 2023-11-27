import json
from funcoes import listar_produtos, produto_maiscaro, produto_maisbarato, orcar_produtos

def carregar_catalogo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return json.load(file)

def salvar_catalogo(catalogo, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(catalogo, file, indent=4)

def menu():
    catalogo = carregar_catalogo('catalogo.json')

    while True:
        print('''MENU SALESFORCE
            [1] Listar produtos
            [2] Ver produto com maior valor
            [3] Ver produto com menor valor
            [4] Orçar 2 produtos
            [5] Encerrar menu''')

        opcao = input('Digite o número da opção escolhida: ')

        if opcao == "1":
            listar_produtos(catalogo)

        elif opcao == "2":
            produto_maiscaro(catalogo)

        elif opcao == "3":
            produto_maisbarato(catalogo)

        elif opcao == "4":
            prod1 = input("Qual produto: ")
            prod2 = input("Qual produto: ")
            if (prod1 or prod2) not in catalogo:
                print('Orçamento invalido. Não encontramos os produtos mencionados')
            else:
                orcar_produtos(catalogo, prod1, prod2)

        elif opcao == "5":
            print("Obrigado, encerrando por aqui!")
            salvar_catalogo(catalogo, 'catalogo.json')
            break

        else:
            print(f"opção {opcao} inválida! Escolha uma opção válida")

if __name__ == "__main__":
    menu()
