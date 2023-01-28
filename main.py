from BancoLib import Banco
from db_sqlite import BancoDeDados
from db_mysql import BancoMysql


def imprimeMenu():
    print("Menu")
    print("0 - Sair")
    print("1 - Criar uma Nova Conta")
    print("2 - Consultar Saldo Conta")
    print("3 - Depositar na Conta")
    print("4 - Sacar na Conta")


print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
imprimeMenu()
escolha = int(input("digite a opção desejada:"))

# criando banco de dados
banco_de_dados_sqlite3 = BancoDeDados()
banco_de_dados_mysql = BancoMysql()

while escolha > 0:
    if escolha == 1:
        # criar uma conta

        # ajuste para banco de dados
        print("Criando Conta...")
        numConta = bancoUfrpe.criarConta()

        banco_de_dados_sqlite3.criar_tabela()
        banco_de_dados_sqlite3.inserir_valores(numero=numConta)
        banco_de_dados_mysql.inserir_valores(numero=numConta)

        #print("Conta criada:", numConta)
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é", saldo, "R$")
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoUfrpe.depositar(numConta, valor)
        print("Valor Depositado")
    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")
    imprimeMenu()
    escolha = int(input("digite a opção desejada:"))