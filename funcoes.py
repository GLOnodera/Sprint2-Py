def listar_produtos(catalogo):
    for nome, produto in catalogo.items():
        print(nome)

def produto_maiscaro(catalogo):
    x = None
    for nome, produto in catalogo.items():
        for preco in produto.values():
            if x is None or preco > x:
                n = nome
                x = preco
    print(f'O produto de maior valor é o {n} e ele custa {x}')

def produto_maisbarato(catalogo):
    y = None
    for nome, produto in catalogo.items():
        for preco in produto.values():
            if y is None or preco < y:
                n = nome
                y = preco
    print(f'O produto de menor valor é o {n} e ele custa {y}')

def orcar_produtos(catalogo, prod1, prod2):
    valor1 = 0
    valor2 = 0
    for nome, produto in catalogo.items():
        for preco in produto.values():
            if prod1 == nome:
                valor1 = preco
            if prod2 == nome:
                valor2 = preco
            soma = valor1 + valor2
    print(f"O orçamento para {prod1} e {prod2} é {soma}")
