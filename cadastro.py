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


   def listar_cliente(self, cpf, opc):
      if opc == "0":
         self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+str(cpf)+"'")
         if len(self.resultado) >= 0:
            print('Cliente Cadastrado'.center(55))
            print()
            self.comando_dql("SELECT * FROM cadastro WHERE cpf = '"+str(cpf)+"'")
            for x, y in enumerate(self.resultado):
               print(f'Nº: {y[0]}| NOME: {y[1]}| CPF: {y[2]}| TELEFONE: {y[3]}\n')
         else:
            print('CPF Não Cadastrado')
      elif opc == "1":
         self.comando_dql("SELECT * FROM cadastro")
         print('Lista de Cliente Cadastrados'.center(55))
         print()
         for x, y in enumerate(self.resultado):
            print(f'Nº: {y[0]}| NOME: {y[1]}| CPF: {y[2]}| TELEFONE: {y[3]}\n')
      else:
         pass


if __name__ == "__main__":
   nome = str(input('Nome: '))
   cpf = int(input('cpf: '))
   phone = int(input('Phone: '))
   cliente = Reservar_Cliente(nome, cpf, phone)
   cliente.inserir()
   print('''
   0 -> Listar um Cliente
   1 -> Listar Todos os Clientes
   2 - > SAIR
   ''')
   opc = str(input('Opção: '))
   if opc == '0':
      cpf = int(input('CPF Cliente: '))
      cliente.listar_cliente(cpf, opc)
   elif opc == '1':
      cliente.listar_cliente(None, opc)
   else:
      pass
