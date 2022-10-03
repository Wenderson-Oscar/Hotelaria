from cadastro import Reservar_Cliente

class Quarto_Simples(Reservar_Cliente):

    def __init__(self, cpf, reservado, preco, n_quarto):
        super().__init__(None, cpf, None)
        self.reservado = reservado
        self.preco = preco
        self.n_quarto = n_quarto


    def inserir_informacao(self):
        self.comando_dql("SELECT idquarto_simples FROM quarto_simples WHERE reservado = 'F' ")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do quarto desejado: ')
        self.conectar()
        sql = "UPDATE quarto_simples SET reservado = %s, cpf_cliente = %s WHERE idquarto_simples = %s"
        val = ('V', self.cpf ,self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

    
""" 
cpf = input('CPF: ')
cliente = Quarto_Simples(cpf, None, None, None)
cliente.inserir_informacao()
cliente.insercao_s() """

class Quarto_Duplo(Quarto_Simples):
        
    def __init__(self, cpf, n_quarto, reservado, preco):
        Quarto_Simples.__init__(self, cpf, reservado, preco, n_quarto)


    def inserir_dados(self):
        self.comando_dql("SELECT idquarto_duplo FROM quarto_duplo WHERE reservado = 'F'")
        print(self.resultado)            
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_duplo SET reservado = %s, cpf_cliente = %s WHERE idquarto_duplo = %s"
        val = ('V', self.cpf ,self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

""" cpf = input('CPF: ')
cliente = Quarto_Duplo(cpf, None, None, None)
cliente.inserir_dados()
 """
class Quarto_Casal(Reservar_Cliente):
        
    def __init__(self, cpf, n_quarto, reservado, preco):
        super().__init__(None, cpf, None)
        self.n_quarto = n_quarto
        self.reservado = reservado
        self.preco = preco


    def inserir_infor(self):
        self.comando_dql("SELECT idquarto_casal FROM quarto_casal WHERE reservado = 'F'")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_casal SET reservado = %s, cpf_cliente = %s WHERE idquarto_casal = %s"
        val = ('V', self.cpf ,self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

""" cpf = input('CPF: ')
cliente = Quarto_Casal(cpf,None,None,None)
cliente.inserir_infor() """

class Quarto_Luxo(Reservar_Cliente):

    def __init__(self, cpf, n_quarto, reservado, preco):
        super().__init__(None, cpf, None)
        self.n_quarto = n_quarto
        self.reservado = reservado
        self.preco = preco


    def inserir_l(self):
        self.comando_dql("SELECT idquarto_luxo FROM quarto_luxo WHERE reservado = 'F'")
        print(self.resultado)
        self.n_quarto = input('Escolha o Número do Quarto Desejado: ')
        self.conectar()
        sql = "UPDATE quarto_luxo SET reservado = %s, cpf_cliente = %s WHERE idquarto_luxo = %s"
        val = ('V', self.cpf ,self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

""" cpf = input('CPF: ')
cliente = Quarto_Luxo(cpf,None,None,None)
cliente.inserir_l()
 """