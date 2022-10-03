from time import sleep
from cadastro import Reservar_Cliente

class Frigobar(Reservar_Cliente):

    def __init__(self, bebida, quantidade, preco, cpf) -> None:
        super().__init__(None, cpf, None)
        self._bebida = bebida
        self._quantidade = quantidade
        self._preco = preco


    def frigobar_pedido(self):
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+str(self.cpf)+"'")
        if len(self.resultado) >= 1:
            print(f'CPF Valido {self.resultado}')
            self.n_quarto = int(input('N° Quarto: '))
            self.comando_dql("SELECT itens, quantidade, preco_item FROM frigobar WHERE idfrigobar = '"+str(self.n_quarto)+"'")
            for x, y in enumerate(self.resultado):
                print(f'''
                - Produto: {y[:1],'Preço:',y[2:], 'Quantidade: ',y[1:2]}
                ''')
            self.comprar = input('Deseja Comprar [S/N]: ').upper()
            if self.comprar == 'S':
                self.item = int(input('Digite a quantidade: '))
                # Foi Necessario Criar uma view temporaria para calcular e mostra o resultado
                self.comando_dql("SELECT (quantidade - '"+str(self.item)+"') AS quant FROM frigobar WHERE idfrigobar = '"+str(self.n_quarto)+"'")
                print('Quantidade Restante: ',self.resultado)
                self.conectar()
                # Necessitei de uma view para armazena o valor do calculo
                c = "CREATE VIEW quant_tirada AS SELECT (quantidade - '"+str(self.item)+"') AS quant FROM frigobar WHERE idfrigobar = '"+str(self.n_quarto)+"'"
                self.cu.execute(c)
                self.con.commit()
                self.desconectar()
                self.conectar()
                # Em seguida usei o valor que estava na view e coloque em quantidade de item do frigobar
                sql = "UPDATE frigobar, quant_tirada SET quantidade = quant_tirada.quant WHERE idfrigobar = '"+str(self.n_quarto)+"'"
                self.cu.execute(sql)
                self.con.commit()
                self.desconectar()
                self.conectar()
                # Deletei a view
                sql = "DROP VIEW quant_tirada"
                self.cu.execute(sql)
                self.con.commit()
                self.desconectar()
                if self.n_quarto == 1:
                    calculo = 10*self.item
                    print(f'''
                    Categoria Simples
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == 2:
                    calculo = 70*self.item
                    print(f'''
                    Categoria Casal
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == 3:
                    calculo = 250*self.item
                    print(f'''
                    Categoria Luxo
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
                elif self.n_quarto == 4:
                    calculo = 15*self.item
                    print(f'''
                    Categoria Duplo
                    Preço: {calculo}
                    |PAGAMENTO|
                    PIX: CNPJ | 34134819312''')
                    sleep(2)
            else:
                print('OK!')
                sleep(1)
        else:
            print('CPF Invalido!')
            sleep(1)


if __name__ == "__main__":
    cpf = int(input('CPF: '))
    cliente = Frigobar(None,None, None, cpf)
    cliente.frigobar_pedido()
