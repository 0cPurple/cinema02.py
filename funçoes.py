#Função pra cadatrar meu filme

def cadastrar_filme(filmes):
    titulo = input("Digite o título do filme: ")
    sala = input("Digite a sala do filme: ")

    while True:
        horario = input("Digite o horário do filme (formato HH:MM): ")
        try:
            horas, minutos = map(int, horario.split(':'))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                break
            else:
                print("Horário inválido. Por favor, digite um horário entre 00:00 e 23:59.")
        except ValueError:
            print("Formato de horário inválido. Por favor, use o formato HH:MM.")

    while True:
        try:
            capacidade = int(input("Digite a capacidade da sala: "))
            if capacidade > 0 and capacidade <= 70:
                break
            else:
                print("A capacidade deve ser um número positivo.")
        except ValueError:
            print("Capacidade inválida. Por favor, digite um número inteiro positivo.")

    while True:
        try:
            valor = float(input("Digite o valor do ingresso: "))
            if valor > 0:
                break
            else:
                print("O valor do ingresso deve ser um número positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número positivo.")

    novo_filme = {
        'titulo': titulo,
        'sala': sala,
        'horario': horario,
        'capacidade': capacidade,
        'valor': valor
    }

    filmes.append(novo_filme)
    print(f"Filme '{titulo}' cadastrado com sucesso!")

#########################################################################################################################

# função pra atualizar o filme 

def att_filme(filmes):
    titulo = input("Digite o título do filme a ser atualizado: ")
    
    for filme in filmes:
        if filme['titulo'].lower() == titulo.lower():
            print(f"Atualizando informações do filme: {filme['titulo']}")
            
            novo_titulo = input(f"Digite o novo título do filme (ou pressione Enter para manter '{filme['titulo']}'): ")
            if novo_titulo:
                filme['titulo'] = novo_titulo

            nova_sala = input(f"Digite a nova sala do filme (ou pressione Enter para manter '{filme['sala']}'): ")
            if nova_sala:
                filme['sala'] = nova_sala
            
            while True:
                novo_horario = input(f"Digite o novo horário do filme (formato HH:MM, ou Enter para manter '{filme['horario']}'): ")
                if not novo_horario:
                    break
                try:
                    horas, minutos = map(int, novo_horario.split(':'))
                    if 0 <= horas < 24 and 0 <= minutos < 60:
                        filme['horario'] = novo_horario
                        break
                    else:
                        print("Horário inválido. Por favor, digite um horário entre 00:00 e 23:59.")
                except ValueError:
                    print("Formato de horário inválido. Por favor, use o formato HH:MM.")

            while True:
                nova_capacidade = input(f"Digite a nova capacidade da sala (ou Enter para manter '{filme['capacidade']}'): ")
                if not nova_capacidade:
                    break
                try:
                    capacidade = int(nova_capacidade)
                    if capacidade > 0:
                        filme['capacidade'] = capacidade
                        break
                    else:
                        print("A capacidade deve ser um número positivo.")
                except ValueError:
                    print("Capacidade inválida. Por favor, digite um número inteiro positivo.")

            while True:
                novo_valor = input(f"Digite o novo valor do ingresso (ou Enter para manter '{filme['valor']}'): ")
                if not novo_valor:
                    break
                try:
                    valor = float(novo_valor)
                    if valor > 0:
                        filme['valor'] = valor
                        break
                    else:
                        print("O valor do ingresso deve ser um número positivo.")
                except ValueError:
                    print("Valor inválido. Por favor, digite um número positivo.")

            print(f"Filme '{filme['titulo']}' atualizado com sucesso!")
            return
    
    print("Filme não encontrado.")

    ###########################################################################################

  # minah função para Remover filmes

def limpar_filme(filmes):
    titulo = input("Digite o título do filme que deseja remover: ")
    
    for i, filme in enumerate(filmes):
        if filme['titulo'].lower() == titulo.lower():
            del filmes[i]
            print(f"Filme '{titulo}' removido com sucesso!")
            return
    
    print(f"Filme com título '{titulo}' não encontrado.")


######################################################################################

#minha função para limpar todos os filmes #(Adicional do ADM 01)

def cyf(filmes):
    filmes.clear()
    print("Todos os filmes foram removidos com sucesso!")

#####################################################################################

#lanches

def cad_comida(lanches):
    nome = input("Digite o nome do lanche: ")

    while True:
        try:
            valor = float(input("Digite o valor do lanche: "))
            if valor >= 0:
                break
            else:
                print("O valor do lanche não pode ser negativo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    novo_lanche = {
        'nome': nome,
        'valor': valor
    }

    lanches.append(novo_lanche)
    print(f"Lanche '{nome}' cadastrado com sucesso!")

    ##################################################################################

    #minha função remover lanches

def rem_comida(lanches):
    nome = input("Digite o nome do lanche que deseja remover: ")

    for i, lanche in enumerate(lanches):
        if lanche['nome'].lower() == nome.lower():
            del lanches[i]
            print(f"Lanche '{nome}' removido com sucesso!")
            return
    
    print(f"Lanche com nome '{nome}' não encontrado.")

    #######################################################################

def cad_adm(admin, nome, senha):
    admin[nome] = senha
    print(f"Novo administrador '{nome}' cadastrado com sucesso!")

# #######################################################################3
# exibir os filmes

def mostrar__filmes(filmes):
    if not filmes:
        print("Nenhum filme disponível no momento.")
        return
    
    print("\n### Filmes Disponíveis ###")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. Título: {filme['titulo']}, Sala: {filme['sala']}, Horário: {filme['horario']}, Capacidade: {filme['capacidade']}, Valor: R$ {filme['valor']:.2f}")
    print("############################")


###################################################################

# Mostrar o lanches

def mostrarlanches(lanches):
    if not lanches:
        print("Nenhum lanche disponível no momento.")
        return
    
    print("\n### Lanches Disponíveis ###")
    for lanche in lanches:
        print(f"Nome: {lanche['nome']}, Valor: R${lanche['valor']:.2f}")
    print("############################")

######################################################################

def ingressos(filmes, recibo):
    if not filmes:
        print("Nenhum filme disponível no momento.")
        return
    
    mostrar__filmes(filmes)
    
    while True:
        try:
            filme_escolhido = int(input("Escolha o número do filme que deseja assistir (ou 0 para cancelar): ")) - 1
            if filme_escolhido == -1:
                print("Compra de ingressos cancelada.")
                return
            if filme_escolhido < 0 or filme_escolhido >= len(filmes):
                print("Filme inválido. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    filme = filmes[filme_escolhido]
    print(f"Você escolheu assistir '{filme['titulo']}' na {filme['sala']} às {filme['horario']}")
    
    while True:
        try:
            cadeiras = int(input("Quantos ingressos você deseja comprar? "))
            if cadeiras <= 0:
                print("Número de cadeiras inválido. Tente novamente.")
                continue
            if cadeiras > filme['capacidade']:
                print(f"Desculpe, não há lugares suficientes disponíveis. Apenas {filme['capacidade']} lugares restantes.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    filme['capacidade'] -= cadeiras
    total = cadeiras * filme['valor']
    
    recibo.append({'nome': f"Ingressos para {filme['titulo']}", 'valor': total})
    print(f"Você comprou {cadeiras} ingressos para '{filme['titulo']}'. Total: R$ {total:.2f}")



#######################################################################################

# casastro de cliente

def cliente(clientes):
    print("Certo, vamos fazer o seu cadastro.")

    while True:
        nome = input("Digite um Login: ")
        if len(nome) < 4:
            print("O nome de usuário deve ter pelo menos 4 caracteres.")
            continue

        senha = input("Digite sua senha: ")
        if len(senha) < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
            continue

        clientes.append({'login': nome, 'senha': senha})
        print(f"Novo cliente '{nome}' cadastrado com sucesso!")
        break

###################################################################

#login para o cliente

def login(clientes, administradores):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verificar se é um administrador
    if usuario in administradores and administradores[usuario] == senha:
        print("Login de administrador bem-sucedido!")
        return 'admin', usuario

    # Verificar se é um cliente
    for cliente in clientes:
        if cliente['login'] == usuario and cliente['senha'] == senha:
            print("Login de cliente bem-sucedido!")
            return 'cliente', usuario

    print("Nome de usuário ou senha incorretos.")
    return None, None


###################################################################

#fUNÇÃO COMPRAR LANCHES

def lanche(lanches, recibo):
    while True:
        print("\n### Lanches Disponíveis ###")
        for i, lanche in enumerate(lanches):
            print(f"{i + 1}. {lanche['nome']} - R$ {lanche['valor']:.2f}")

        escolha = input("Escolha o número do lanche que deseja comprar (ou 'sair' para voltar): ")

        if escolha.lower() == 'sair':
            break

        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(lanches):
                print("Escolha inválida. Por favor, selecione um lanche disponível.")
                continue

            lanche_selecionado = lanches[escolha - 1]
            recibo.append(lanche_selecionado)
            print(f"Você comprou um {lanche_selecionado['nome']} por R$ {lanche_selecionado['valor']:.2f}.")
        except ValueError:
            print("Escolha inválida. Por favor, digite um número ou 'sair' para voltar.")

######################################################

# ver recibos

def recibo_(recibo):
    if not recibo:
        print("Você não tem compras registradas.")
        return

    total = 0  # Inicializa o total para o recibo atual
    print("\n### Seu Recibo ###")
    for item in recibo:
        print(f" - {item['nome']}: R$ {item['valor']:.2f}")
        total += item['valor']  # Adiciona o valor do item ao total
    print(f"Total: R$ {total:.2f}")
    print("-----------------------")



############################################

def gerar_arquivo_ingressos(recibo, cliente_nome):
    if not recibo:
        print("Você não tem compras registradas.")
        return

    total = 0
    nome_arquivo = f"recibo_{cliente_nome}.txt"
    with open(nome_arquivo, 'w') as file:
        file.write("### Seu Recibo ###\n")
        for item in recibo:
            file.write(f" - {item['nome']}: R$ {item['valor']:.2f}\n")
            total += item['valor']
        file.write(f"Total: R$ {total:.2f}\n")
        file.write("-----------------------\n")

    print(f"Recibo salvo no arquivo: {nome_arquivo}")


##########################################################