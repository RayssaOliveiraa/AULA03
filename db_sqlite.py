import sqlite3

class BancoDeDados:
    def __init__(self) -> None:
        # realizando conexão e criando o banco de dados
        self.connection = sqlite3.connect("banco.db")

        # método cursor para executar querys sql
        self.cursor = self.connection.cursor()


    def criar_tabela(self):
        # criando tabela de contas
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS conta (numero INTEGER PRIMARY KEY, saldo REAL)")
            #print(f'Tabela criada com sucesso')
        except:
            pass


    def _checando_se_valor_existe(self, numero):
        self.cursor.execute(f"SELECT * from conta where numero == {numero}")
        retorno = self.cursor.fetchall()

        if len(retorno) != 0:
            return True
        else:
            return False


    def inserir_valores(self, numero):
        # inserindo dado teste (numero 100, saldo 0)
        try:
            checar = self._checando_se_valor_existe(numero)
            if checar:
                print(f'Já existe uma conta com o número {numero} cadastrada!')
            else:
                self.cursor.execute(f"INSERT INTO conta VALUES ({numero}, 0)")
                # salvando no banco de dados
                self.connection.commit()
                print(f'Conta de número {numero} criada com sucesso')
        except:
            print('Erro interno do servidor')


    def pegar_todos_valores(self):
        try:
            self.cursor.execute("SELECT * from conta")
            retorno = self.cursor.fetchall()
            print(retorno)
        except:
            print('Erro interno do servidor')



