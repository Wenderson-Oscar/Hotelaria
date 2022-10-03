from conexao import Conectar_bd

class Listar_Q_Cliente(Conectar_bd):

    def __init__(self, cpf):
        self.cpf = cpf


    def quarto_simples(self):
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+self.cpf+"'")
        if len(self.resultado) >= 1:
            self.comando_dql("SELECT * FROM quarto_simples WHERE cpf_cliente = '"+self.cpf+"'")
            print(self.resultado)
        else:
            print('CPF Invalido')

    
    def quarto_duplo(self):
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+self.cpf+"'")
        if len(self.resultado) >= 1:
            self.comando_dql("SELECT * FROM quarto_duplo WHERE cpf_cliente = '"+self.cpf+"'")
            print(self.resultado)
        else:
            print('CPF Invalido')


    def quarto_casal(self):
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+self.cpf+"'")
        if len(self.resultado) >= 1:
            self.comando_dql("SELECT * FROM quarto_casal WHERE cpf_cliente = '"+self.cpf+"'")
            print(self.resultado)
        else:
            print('CPF Invalido')


    def quarto_luxo(self):
        self.comando_dql("SELECT cpf FROM cadastro WHERE cpf = '"+self.cpf+"'")
        if len(self.resultado) >= 1:
            self.comando_dql("SELECT * FROM quarto_luxo WHERE cpf_cliente = '"+self.cpf+"'")
            print(self.resultado)
        else:
            print('CPF Invalido')


class Listar_Q_Reservado(Conectar_bd):


    def listar(self):
        self.comando_dql("SELECT * FROM quarto_simples WHERE reservado = 'V'")
        print('Simples:')
        print()
        for x, y in enumerate(self.resultado):
               print(f'Nº: {y[0]}| Reservado: {y[1]}| Check_in: {y[3]}| Check_an: {y[4]}| CPF Cliente: {y[5]}\n')
        self.comando_dql("SELECT * FROM quarto_duplo WHERE reservado = 'V'")
        print('Duplo:')
        print()
        for x, y in enumerate(self.resultado):
               print(f'Nº: {y[0]}| Reservado: {y[1]}| Check_in: {y[3]}| Check_an: {y[4]}| CPF Cliente: {y[5]}\n')
        self.comando_dql("SELECT * FROM quarto_casal WHERE reservado = 'V'")
        print('Casal:')
        print()
        for x, y in enumerate(self.resultado):
               print(f'Nº: {y[0]}| Reservado: {y[1]}| Check_in: {y[3]}| Check_an: {y[4]}| CPF Cliente: {y[5]}\n')
        self.comando_dql("SELECT * FROM quarto_luxo WHERE reservado = 'V'")
        print('Luxo:')
        print()
        for x, y in enumerate(self.resultado):
               print(f'Nº: {y[0]}| Reservado: {y[1]}| Check_in: {y[3]}| Check_an: {y[4]}| CPF Cliente: {y[5]}\n')

    
    def cancelar_reserva(self, n_quarto, opc):
        if opc == '0':
            self.conectar()
            sql = "UPDATE quarto_simples SET reservado = %s, check_in = null, check_an = null, cpf_cliente = null WHERE idquarto_simples = %s "
            val = ('F', n_quarto)
            self.cu.execute(sql, val)
            self.con.commit()
            self.desconectar()
            print('Quarto Desocupado')
        elif opc == '1':
            self.conectar()
            sql = "UPDATE quarto_duplo SET reservado = %s, check_in = null, check_an = null, cpf_cliente = null WHERE idquarto_duplo = %s "
            val = ('F', n_quarto)
            self.cu.execute(sql, val)
            self.con.commit()
            self.desconectar()
            print('Quarto Desocupado')
        elif opc == '2':
            self.conectar()
            sql = "UPDATE quarto_casal SET reservado = %s, check_in = null, check_an = null, cpf_cliente = null WHERE idquarto_casal = %s "
            val = ('F', n_quarto)
            self.cu.execute(sql, val)
            self.con.commit()
            self.desconectar()
            print('Quarto Desocupado')
        elif opc == '3':
            self.conectar()
            sql = "UPDATE quarto_luxo SET reservado = %s, check_in = null, check_an = null, cpf_cliente = null WHERE idquarto_luxo = %s "
            val = ('F', n_quarto)
            self.cu.execute(sql, val)
            self.con.commit()
            self.desconectar()
            print('Quarto Desocupado')
        else:
            print('Categoria Invalida')


if __name__ == "__main__":
    cpf = input('CPF: ')
    cp = Listar_Q_Cliente(cpf)
    cp.quarto_simples()
    cp.quarto_duplo()
    cp.quarto_casal()
    cp.quarto_luxo()
    cl = Listar_Q_Reservado()
    cl.listar()
    print('''
        0 -> Simples
        1 -> Duplo
        2 -> Casal
        3 -> Luxo
        ''')
    opc = input('Qual Categoria de Quarto Deseja Desocupar: ')
    n_quarto = input('Nº Que Deseja Desocupar: ')
    cl.cancelar_reserva(n_quarto, opc)
