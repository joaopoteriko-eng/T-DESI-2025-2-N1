# ==========================================
# 1. PREPARANDO O TERRENO
# ==========================================
# Criando o dicionário para o estoque e a lista para o histórico
estoque = {}
historico_vendas = []

# ==========================================
# 2. CADASTRANDO NOVOS PRODUTOS
# ==========================================
def cadastrar_produto():
    print("\n--- Novo Cadastro ---")
    nome = input("Digite o nome do produto: ").strip()
    
    # Validação: verifica se a chave já existe no dicionário
    if nome in estoque:
        print(f"Aviso: O produto '{nome}' já está cadastrado no sistema!")
    else:
        # Lê a quantidade e o preço, convertendo para os tipos corretos (int e float)
        quantidade = int(input("Digite a quantidade inicial: "))
        preco = float(input("Digite o preço unitário (ex: 10.50): "))
        
        # Salva a lista [quantidade, preço] na chave do produto
        estoque[nome] = [quantidade, preco]
        print(f"Sucesso: '{nome}' cadastrado com {quantidade} unidades a R$ {preco:.2f}.")

# ==========================================
# 3. SIMULANDO A VENDA
# ==========================================
def simular_venda():
    print("\n--- Painel de Vendas ---")
    nome_produto = input("Qual produto o cliente deseja comprar? ").strip()
    
    # Verifica se o produto existe no dicionário
    if nome_produto in estoque:
        qtd_desejada = int(input("Qual a quantidade desejada? "))
        
        qtd_disponivel = estoque[nome_produto][0]
        preco_unitario = estoque[nome_produto][1]
        
        # Verifica se há estoque suficiente
        if qtd_desejada <= qtd_disponivel:
            # Subtrai a quantidade do estoque atual
            estoque[nome_produto][0] -= qtd_desejada
            valor_total = qtd_desejada * preco_unitario
            
            # Cria um dicionário com os detalhes da transação e adiciona ao histórico
            transacao = {
                "produto": nome_produto,
                "quantidade": qtd_desejada,
                "valor_total": valor_total
            }
            historico_vendas.append(transacao)
            
            print(f"Venda confirmada! Total a pagar: R$ {valor_total:.2f}")
        else:
            print(f"Erro: Estoque insuficiente. Temos apenas {qtd_disponivel} unidade(s) de '{nome_produto}'.")
    else:
        print(f"Erro: O produto '{nome_produto}' não existe no nosso sistema.")

# ==========================================
# 4. EXIBINDO O RELATÓRIO DE INVENTÁRIO
# ==========================================
def exibir_relatorio():
    print("\n--- Relatório Atual de Inventário ---")
    
    # Verifica se o estoque está vazio
    if len(estoque) == 0:
        print("O estoque está vazio no momento.")
    else:
        # Usa o laço for com .items() para percorrer chave e valor
        for chave, valor in estoque.items():
            qtd = valor[0]
            preco = valor[1]
            print(f"Produto: {chave} | Em estoque: {qtd} | Preço Un.: R$ {preco:.2f}")

# ==========================================
# MENU INTERATIVO PARA TESTAR NO VS CODE
# ==========================================
# Este loop 'while' mantém o programa rodando até você escolher a opção 4
while True:
    print("\n" + "="*30)
    print("1 - Cadastrar Produto")
    print("2 - Realizar Venda")
    print("3 - Ver Inventário")
    print("4 - Sair do Sistema")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        simular_venda()
    elif opcao == '3':
        exibir_relatorio()
    elif opcao == '4':
        print("Encerrando o sistema... Até logo!")
        # Mostra o histórico final antes de fechar
        print(f"\nHistórico de Vendas do Dia: {historico_vendas}")
        break
    else:
        print("Opção inválida. Tente novamente.")