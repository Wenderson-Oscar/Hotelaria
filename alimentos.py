from conexao import Conectar_bd

class Servico_Quarto(Conectar_bd):

    def __init__(self, cafe_manha, almoco, jantar, lanche) -> None:
        self._cafe_manha = cafe_manha
        self._almoco = almoco 
        self._jantar = jantar
        self._lanche = lanche


    def fazer_pedido(self):
        print('''
        ''')
        self.comando_dql("SELECT a.cafe_manha, pa.cafe, a.almoco, pa.almoco, a.jantar, pa.jantar, a.lanche, pa.lanche FROM preco_alimentos pa, alimentos a")
        for p, v in enumerate(self.resultado):
            print(f'''
            {p} = {v[:2]}
            {p+1} = {v[2:4]}
            {p+2} = {v[4:6]}
            {p+3} = {v[6:]}''')
        self.pedir = input('Fazer Pedido: ')
        self.conectar()
        sql = "UPDATE alimentos SET cliente = %s WHERE idalimentos = %s"
        val = (self.pedir, 1)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Pedido feito com Sucesso')
        self.total = list(self.pedir)


#cliente = Servico_Quarto(None, None, None, None)
#cliente.fazer_pedido()
