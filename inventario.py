
inventario = {}
1
def adicionar_produto(codigo, nome, preco, quantidade):
    inventario[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(codigo):
    if codigo in inventario:
        nome = inventario[codigo]["nome"]
        del inventario[codigo]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print("Produto não encontrado!")

def listar_produtos():
    if inventario:
        print("\nInventário de Produtos:")
        for codigo, info in inventario.items():
            print(f"Código: {codigo} | Nome: {info['nome']} | Preço: R${info['preco']:.2f} | Quantidade: {info['quantidade']}")
    else:
        print("O inventário está vazio!")

# Menu de opções
while True:
    print("\nMenu de Inventário:")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Listar Produtos")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        adicionar_produto(codigo, nome, preco, quantidade)
    
    elif opcao == "2":
        codigo = input("Digite o código do produto que deseja remover: ")
        remover_produto(codigo)
    
    elif opcao == "3":
        listar_produtos()
    
    elif opcao == "4":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
