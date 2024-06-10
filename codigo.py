from funçoes import *

usuarios_cadastrados = 0
usuarios = 0
clientes = []
filmes = [
    {'titulo': 'Os Vingadores', 'sala': 'Sala 1', 'horario': '15:00', 'capacidade': 100, 'valor': 20.0},
    {'titulo': 'Titanic', 'sala': 'Sala 2', 'horario': '18:30', 'capacidade': 80, 'valor': 15.0},
    {'titulo': 'Jurassic Park', 'sala': 'Sala 3', 'horario': '20:00', 'capacidade': 120, 'valor': 18.0}
]

lanches = [
    {'nome': 'sanduiche', 'valor': 7.30},
    {'nome': 'uva', 'valor': 2.25},
    {'nome': 'caju', 'valor': 7.50}
]

bebidas = []
recibo = []
admin = {'admin': '12345'}

def menu_cliente(cliente_nome):
    while True:
        print("\n### Menu Cliente ###")
        print("1. Ver filmes disponíveis")
        print("2. Comprar ingresso")
        print("3. Ver lanches disponíveis")
        print("4. Comprar lanche")
        print("5. Ver recibo")
        print("6. Salvar recibo em arquivo")
        print("7. Sair")
        print("--------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar__filmes(filmes)
        elif opcao == '2':
            ingressos(filmes, recibo)
        elif opcao == '3':
            mostrarlanches
            (lanches)
        elif opcao == '4':
            lanche(lanches, recibo)
        elif opcao == '5':
            recibo_(recibo)
        elif opcao == '6':
            gerar_arquivo_ingressos(recibo, cliente_nome)
        elif opcao == '7':
            print("Saindo do menu cliente...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu_admin():
    while True:
        print('==========================   PAINEL ADMINISTRADOR ==========================')
        print('1. Cadastro de filme')
        print('2. Atualizar filmes')
        print('3. Remover filme')
        print('4. Remover todos os Filmes')
        print('5. Adicionar lanches')
        print('6. Remover lanches')
        print('7. Cadastrar novo Admin')
        print('8. Sair')
        
        opp_adm = input('Digite o número da opção desejada: ')

        if opp_adm == '1':
            cadastrar_filme(filmes)
        elif opp_adm == '2':
            att_filme(filmes)
        elif opp_adm == '3':
            limpar_filme(filmes)
        elif opp_adm == '4':
            cyf(filmes)
        elif opp_adm == '5':
            cad_comida(lanches)
        elif opp_adm == '6':
            rem_comida(lanches)
        elif opp_adm == '7':
            login_adm = input('Digite o login que deseja cadastrar: ')
            senha_adm = input('Digite a senha que deseja cadastrar: ')
            cad_adm(admin, login_adm, senha_adm)
        elif opp_adm == '8':
            print("Saindo do painel administrador...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def main():
    while True:
        print('===== Menu Inicial =====')
        print('1. Quero fazer meu cadastro')
        print('2. Login')
        print('3. Sair')
        print("--------------------")

        menu_principal = input('Digite a opção desejada: ')

        if menu_principal == '1':
            cliente(clientes)
        elif menu_principal == '2':
            tipo_usuario, cliente_nome = login(clientes, admin)
            if tipo_usuario == 'cliente':
                menu_cliente(cliente_nome)
            elif tipo_usuario == 'admin':
                menu_admin()
        elif menu_principal == '3':
            print('Saindo do programa...')
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
