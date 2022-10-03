import datetime
from conexao import Conectar_bd

class Check_In(Conectar_bd):
    
    def __init__(self, ano, mes, dia, n_quarto):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.n_quarto = n_quarto


    def entrada(self):
        self.data_entrada = datetime.date(self.ano, self.mes, self.dia)
        print(f'Reserva Feita na data: {self.data_entrada.strftime("%x")}')


    def check_in_quarto_simples(self):
        self.conectar()
        sql = "UPDATE quarto_simples SET check_in = %s WHERE idquarto_simples = %s"
        val = (self.data_entrada, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Check_in Realizado Com Sucesso')


    def check_in_quarto_duplo(self):
        self.conectar()
        sql = "UPDATE quarto_duplo SET check_in = %s WHERE idquarto_duplo = %s"
        val = (self.data_entrada, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Check_in Realizado Com Sucesso')

    
    def check_in_quarto_casal(self):
        self.conectar()
        sql = "UPDATE quarto_casal SET check_in = %s WHERE idquarto_casal = %s"
        val = (self.data_entrada, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Check_in Realizado Com Sucesso')


    def check_in_quarto_luxo(self):
        self.conectar()
        sql = "UPDATE quarto_luxo SET check_in = %s WHERE idquarto_luxo = %s"
        val = (self.data_entrada, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Check_in Realizado Com Sucesso')


class Check_An(Check_In):
    def __init__(self, ano, mes, dia, n_quarto):
        super().__init__(ano, mes, dia, n_quarto)


    def saida(self):
        self.data_saida = datetime.date(self.ano, self.mes, self.dia)
        print(f'Fim da Estadia: {self.data_saida.strftime("%x")}')


    def check_an_quarto_simples(self):
        self.conectar()
        sql = "UPDATE quarto_simples SET check_an = %s WHERE idquarto_simples = %s"
        val = (self.data_saida, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

    
    def check_an_quarto_duplo(self):
        self.conectar()
        sql = "UPDATE quarto_duplo SET check_an = %s WHERE idquarto_duplo = %s"
        val = (self.data_saida, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()


    def check_an_quarto_casal(self):
        self.conectar()
        sql = "UPDATE quarto_casal SET check_an = %s WHERE idquarto_casal = %s"
        val = (self.data_saida, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()

    
    def check_an_quarto_luxo(self):
        self.conectar()
        sql = "UPDATE quarto_luxo SET check_an = %s WHERE idquarto_luxo = %s"
        val = (self.data_saida, self.n_quarto)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()


""" cliente = Check_In(a,da,sa,None)
cliente.entrada()
cliente.check_in_quarto_simples()
cliente = Check_An(2021,4,22,None)
cliente.saida()
cliente.check_an_quarto_simples()
  """