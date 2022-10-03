from time import sleep
from quartos import Quarto_Simples

class Pagamento(Quarto_Simples):

    def __init__(self, preco):
        super().__init__(None,None,preco, None)


    def pagamento_simples(self):
        
        self.comando_dql("SELECT preco FROM quarto_simples WHERE idquarto_simples = 1")
        print('Quarto Simples Reservado')
        print(f'''
        |PAGAMENTO|
        R$: {self.resultado}
        PIX: CNPJ | 34134819312''')
        self.comando_dql("SELECT nome_funcionario FROM servico_quarto WHERE idservico_quarto = 1")
        print(f'Nome Funcionario: {self.resultado}')
        sleep(2)

    def pagamento_duplo(self):

        self.comando_dql("SELECT preco FROM quarto_duplo WHERE idquarto_duplo = 2")
        print('Quarto Duplo Reservado')
        print(f'''
        |PAGAMENTO|
        R$: {self.resultado}
        PIX: CNPJ | 34134819312''')
        self.comando_dql("SELECT nome_funcionario FROM servico_quarto WHERE idservico_quarto = 2")
        print(f'Nome Funcionario: {self.resultado}')
        sleep(2)


    def pagamento_casal(self):

        self.comando_dql("SELECT preco FROM quarto_casal WHERE idquarto_casal = 3")
        print('Quarto Casal Reservado')
        print(f'''
        |PAGAMENTO|
        R$: {self.resultado}
        PIX: CNPJ | 34134819312''')
        self.comando_dql("SELECT nome_funcionario FROM servico_quarto WHERE idservico_quarto = 3")
        print(f'Nome Funcionario: {self.resultado}')
        sleep(2)


    def pagamento_luxo(self):

        self.comando_dql("SELECT preco FROM quarto_luxo WHERE idquarto_luxo = 4")
        print('Quarto Luxo Reservado')
        print(f'''
        |PAGAMENTO|
        R$: {self.resultado}
        PIX: CNPJ | 34134819312''')
        self.comando_dql("SELECT nome_funcionario FROM servico_quarto WHERE idservico_quarto = 4")
        print(f'Nome Funcionario: {self.resultado}')
        sleep(2)


if __name__ == "__main__":
    cliente = Pagamento(None)
    cliente.pagamento_simples()
    cliente.pagamento_duplo()
    cliente.pagamento_casal()
    cliente.pagamento_luxo()