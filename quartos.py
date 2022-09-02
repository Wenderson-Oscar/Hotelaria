from cadastro import Reservar_Cliente

class Quarto_Simples(Reservar_Cliente):

    def __init__(self, cpf, n_quarto, reservado, nome_funcionario, servico_quarto, banheira, wife, cama, preco):
        super().__init__(None, cpf, None)
        self.n_quarto = n_quarto
        self.reservado = reservado
        self.nome_funcionario = nome_funcionario
        self.servico_quarto = servico_quarto
        self.banheiro = banheira
        self.wife = wife
        self.cama = cama
        self.preco = preco


    def inserir_informacao(self):
        self.comando_dql("SELECT idquarto_simples FROM quarto_simples WHERE reservado = 'F' ")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do quarto desejado: ')
        self.conectar()
        sql = "UPDATE quarto_simples SET reservado = %s WHERE idquarto_simples = %s"
        val = ('V', self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        

""" cliente = Quarto_Simples(None,None,None,None,None,None,None,None,None)
cliente.inserir_informacao() """

class Quarto_Duplo(Quarto_Simples):
        
    def __init__(self, cpf, n_quarto, reservado, nome_funcionario, servico_quarto, banheira, wife, cama, preco, tv):
        Quarto_Simples.__init__(self,cpf, n_quarto, reservado, nome_funcionario, servico_quarto,
        banheira, wife, cama, preco)
        self.tv = tv


    def inserir_dados(self):
        self.comando_dql("SELECT idquarto_duplo FROM quarto_duplo WHERE reservado = 'F'")
        print(self.resultado)            
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_duplo SET reservado = %s WHERE idquarto_duplo = %s"
        val = ('V', self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()


#cliente = Quarto_Duplo(None, None, None, None, None, None, None, None, None, None)
#cliente.inserir_dados()

class Quarto_Casal(Reservar_Cliente):
        
    def __init__(self, cpf, n_quarto, reservado, nome_funcionario, servico_quarto, banheira, wife, cama, preco, tv, idromassagem, cozinha_americana, cama_agua):
        super().__init__(None, cpf, None)
        self.n_quarto = n_quarto
        self.reservado = reservado
        self.diaria = nome_funcionario
        self.servico_quarto = servico_quarto
        self.banheira = banheira
        self.wife = wife
        self.cama = cama
        self.preco = preco
        self.tv = tv
        self.idromassagem = idromassagem
        self.cozinha_americana = cozinha_americana
        self.cama_agua = cama_agua    


    def inserir_infor(self):
        self.comando_dql("SELECT idquarto_casal FROM quarto_casal WHERE reservado = 'F'")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_casal SET reservado = %s WHERE idquarto_casal = %s"
        val = ('V', self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()


#cliente = Quarto_Casal(None,None,None,None,None,None,None,None,None,None,None,None,None)
#cliente.inserir_infor()

class Quarto_Luxo(Reservar_Cliente):

    def __init__(self, cpf, n_quarto, reservado, nome_funcionario, servico_quarto, banheira, wife, cama, preco, tv, cama_agua, idromassagem ,banheira_idromassagem, potrona_idromassagem, cozinha_americana, aquario_parede, piscina, mesa_jantar, video_game_pro, closet):
        super().__init__(None, cpf, None)
        self.n_quarto = n_quarto
        self.reservado = reservado
        self.diaria = nome_funcionario
        self.servico_quarto = servico_quarto
        self.banheira = banheira
        self.wife = wife
        self.cozinha_americana = cozinha_americana
        self.aquario_parede = aquario_parede
        self.piscina = piscina
        self.mesa_jantar = mesa_jantar
        self.video_game_pro = video_game_pro
        self.closet = closet
        self.banheira_idromassagem = banheira_idromassagem
        self.potrona_idromassagem = potrona_idromassagem


    def inserir_l(self):
        self.comando_dql("SELECT idquarto_luxo FROM quarto_luxo WHERE reservado = 'F'")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_luxo SET reservado = %s WHERE idquarto_luxo = %s"
        val = ('V', self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

#cliente = Quarto_Luxo(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
#cliente.inserir()
