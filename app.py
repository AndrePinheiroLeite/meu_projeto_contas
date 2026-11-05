import sqlite3#Cria automaticamente o ficheiro da base de dados no teu computador se ele ainda não existir.

def conectar():
    return sqlite3.connect("minhas_contas.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devedor TEXT NOT NULL,
            vencimento TEXT,
            valor REAL,
            status TEXT
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_conta(devedor, vencimento, valor, status):#Caso se escolha a opção 1 ele vem chamar essa função
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO contas (devedor, vencimento, valor, status)
        VALUES (?, ?, ?, ?)
    """, (devedor, vencimento, valor, status))
    conexao.commit()
    conexao.close()
    print("\n✅ Conta adicionada com sucesso!")

def listar_contas():#Caso se ecolha a opção 2, ele vai listar todas as contas usando um select
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas")
    contas = cursor.fetchall()
    conexao.close()
    
    print("\n--- AS SUAS CONTAS ---")

    valor_total = 0.0 #criação da variavel para atualizar o valor
    # 5. Verifica se a lista de contas está vazia antes de tentar percorrê-la
    if not contas:
        print("Nenhuma conta cadastrada ainda.")
    # Se houver contas, percorre cada linha retornada pela base de dados
    else:
        for conta in contas:
            # Imprime os dados formatados usando os índices das colunas da tabela:
            print(f"ID: {conta[0]} | Devedor: {conta[1]} | Vencimento: {conta[2]} | Valor: R$ {conta[3]:.2f} | Status: {conta[4]}")
            valor_total += conta[3]#Aqui se faz a atribuição e somatoria
    print(f"valor total = R$ {valor_total:.2f}")#Aqui o valor se atualiza caso some ou diminua mais
    print("-" * 25)

def atualizar_status(id_conta, novo_status):#Caso digite a opção 3, ele vai fazer um update(atualizar) 
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE contas 
        SET status = ? 
        WHERE id = ?
    """, (novo_status, id_conta))
    conexao.commit()
    conexao.close()
    print("\n🔄 Status da conta atualizado com sucesso!")

def deletar_conta(id_conta):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM contas WHERE id = ?", (id_conta,))
    conexao.commit()
    conexao.close()
    print("\n🗑️ Conta apagada com sucesso!")

# --- PROGRAMA PRINCIPAL (MENU) ---
criar_tabela()

while True: # O programa se inicia aparti daqui para escolher uma das opção
    print("\n=== MENU CONTROLO DE CONTAS ===")
    print("1. Adicionar nova conta")
    print("2. Listar contas")
    print("3. Atualizar status da conta")
    print("4. Apagar conta")
    print("5. Sair")
    
    opcao = input("Escolhe uma opção: ")
    
    if opcao == "1":#Caso ele digite a opção 1
        print("\n--- NOVA CONTA ---")
        devedor = input("Nome do devedor: ")
        vencimento = input("Data de vencimento (ex: 10/11/2026): ")
        valor = float(input("Valor (ex: 150.00): "))
        status = input("Status (ex: Pendente / Pago): ")
        adicionar_conta(devedor, vencimento, valor, status) #Aqui ele chama a função adicionar_conta() passando os valores
        
    elif opcao == "2":#Caso ele digite a opção 2 ele chama a função listar_contas()
        listar_contas()
        
    elif opcao == "3":#Caso digite a opção 3, para atualizar
        print("\n--- ATUALIZAR STATUS ---")
        listar_contas()
        id_conta = input("Digite o ID da conta que quer atualizar: ")
        novo_status = input("Digite o novo status (ex: Pago): ")
        atualizar_status(id_conta, novo_status)
        
    elif opcao == "4":#Caso digite a opção 4, para apagar uma conta
        print("\n--- APAGAR CONTA ---")
        listar_contas()
        id_conta = input("Digite o ID da conta que quer apagar: ")
        deletar_conta(id_conta)
        
    elif opcao == "5":
        print("\nA sair do programa. Até logo!")
        break
    else:
        print("\n❌ Opção inválida! Escolhe de 1 a 5.")