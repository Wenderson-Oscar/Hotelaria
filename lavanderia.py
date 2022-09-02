from cadastro import Reservar_Cliente

class Lavanderia(Reservar_Cliente):

    def __init__(self, passar, lavar, cpf):
        super().__init__(None, cpf, None)
        self.passar = passar
        self.lavar = lavar


    def mostrar(self):
        print(f'''
        |Passar | R$: 10
        |Lavar  | R$: 25
        ''')


    def passar_roupa(self):
        self.lavar = input('Deseja Lavar [S/N]: ').upper()
        if self.lavar == 'S':
            self.quantidade = int(input('Quantidade de peças: '))
            print('Obrigado, Volte Sempre')
            calculo = 10*self.quantidade
            print(f'Preço: {calculo}')
            print('|PAGAMENTO|')
            self.pix = 'PIX: CNPJ | 34134819312'
            print(self.pix)
        else:
            print('Volte Sempre')


    def lavar_roupa(self):
        self.passar = input('Deseja Passar [S/N]: ').upper()
        if self.passar == 'S':
            self.quantidade = int(input('Quantidade de peças: '))
            calculo = 25*self.quantidade
            print(f'Preço: {calculo}')
            print('|PAGAMENTO|')
            self.pix = 'PIX: CNPJ | 34134819312'
            print(self.pix)
        else:
            print('Volte Sempre')


""" cliente = Lavanderia(None, None, None)
cliente.mostrar()
cliente.passar_roupa()
cliente.lavar_roupa()
 """