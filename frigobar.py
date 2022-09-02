from time import sleep
from cadastro import Reservar_Cliente

class Frigobar(Reservar_Cliente):

    def __init__(self, bebida, quantidade, preco, cpf) -> None:
        super().__init__(None, cpf, None)
        self._bebida = bebida
        self._quantidade = quantidade
        self._preco = preco


    def frigobar_pedido(self):
        self.cpf = input('CPF: ')
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+self.cpf+"'")
        ra = self.resultado
        print(ra)
        if len(ra) >= 1:
            self.n_quarto = input('N° Quarto: ')
            self.comando_dql("SELECT itens, quantidade, preco_item FROM frigobar WHERE idfrigobar = '"+self.n_quarto+"'")
            for x, y in enumerate(self.resultado):
                print(f'''
                - Produto: {y[:1],'Preço:',y[2:], 'Quantidade: ',y[1:2]}
                ''')
            self.comprar = input('Deseja Comprar [S/N]: ').upper()
            if self.comprar == 'S':
                self.item = int(input('Digite a quantidade: '))
                self.comando_dql("SELECT quantidade FROM frigobar WHERE idfrigobar = '"+self.n_quarto+"'")
                """ a = len(self.resultado)
                diminuir = a - self.item """
                self.conectar()
                sql = "UPDATE frigobar SET quantidade = %s WHERE idfrigobar = %s"
                val = (self.item, self.n_quarto)
                self.cu.execute(sql, val)
                self.con.commit()
                #self.comando_dql("SELECT quantidade FROM frigobar WHERE idfrigobar = '"+self.n_quarto+"'")
                if self.n_quarto == '1':
                    calculo = 10*self.item
                    print(f'''
                    Quarto Simples
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == '2':
                    calculo = 70*self.item
                    print(f'''
                    Quarto Casal
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == '3':
                    calculo = 250*self.item
                    print(f'''
                    Quarto Luxo
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == '4':
                    calculo = 15*self.item
                    print(f'''
                    Quarto Duplo
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
            else:
                print('OK!')
        else:
            print('CPF Invalido!')


#cliente = Frigobar(None, None, None, None)
#cliente.frigobar_pedido()
