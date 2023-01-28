
import mysql.connector

class BancoMysql():

    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='bdbanco'
        )

        self.cursor = self.connection.cursor()

    
    def _checando_se_valor_existe(self, numero):
        self.cursor.execute(f"SELECT * from conta where numero = {numero}")
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
                self.cursor.close()
        except Exception as err:
            print(f'Erro interno do servidor {err}')

