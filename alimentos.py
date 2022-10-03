from time import sleep 

class Servico_Quarto:

    def __init__(self):
        self.cafe_manha = 'Café Com Pão'
        self.almoco = 'Arroz, Feijão, Carne, Fruta, Suco'
        self.jantar = 'Arroz, Feijão, Frango'
        self.lanche = 'Suco, Pastel'


    def cardapio(self):
        print(f'0 -> {self.cafe_manha}| Preço: R$: 10')
        print(f'1 -> {self.almoco}| Preço: R$: 40 ')
        print(f'2 -> {self.jantar}| Preço: R$: 35')
        print(f'3 -> {self.lanche}| Preço: R$: 7')


    def fazer_pedido(self, pedir):
        if pedir >= 0 and pedir <= 3:
            print('PIX: CNPJ | 34134819312')
            sleep(4)
        else:
            print('Invalido')
            sleep(2)


if __name__ == "__main__":
    cliente = Servico_Quarto()
    cliente.cardapio()
    fazer_pedido = int(input('Escolha o Pedido: '))
    cliente.fazer_pedido(fazer_pedido)
