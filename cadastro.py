from conexao import Conectar_bd

class Reservar_Cliente(Conectar_bd):

     def __init__(self, nome, cpf, phone):
        self.nome = nome
        self.cpf = cpf
        self.phone = phone 


     def inserir(self):
        self.conectar()        
        sql = "INSERT INTO cadastro (name, cpf, telefone) VALUES (%s, %s, %s)"
        val = (self.nome, self.cpf, self.phone)
        self.cu.execute(sql, val)
        self.con.commit()
        self.desconectar()
        print('Cadastro Realizado com Sucesso!')


if __name__ == "__main__":
   nome = str(input('Nome: '))
   cpf = int(input('cpf: '))
   phone = int(input('Phone: '))
   cliente = Reservar_Cliente(nome, cpf, phone)
   cliente.inserir()


