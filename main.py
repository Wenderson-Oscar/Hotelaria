import os
from time import sleep
from frigobar import Frigobar
from lavanderia import Lavanderia
from alimentos import Servico_Quarto
from quartos import Quarto_Simples,Quarto_Duplo,Quarto_Casal,Quarto_Luxo
from data import Check_An, Check_In
from pagamento import Pagamento
import conexao
from cadastro import Reservar_Cliente
from listar_quartos import Listar_Q_Cliente, Listar_Q_Reservado

def main():
    os.system("clear")
    print(f"\n+{'-'*30}+")
    print(f"|{'HOTEL OSCAR'.center(30)}|")
    print(f"+{'-'*30}+")
    print(f"| 1 | ->{'Reserva'.center(23)}|")
    print(f"| 2 | ->{'Cadastrar'.center(23)}|")
    print(f"| 3 | ->{'Serviço'.center(23)}|")
    print(f"| 4 | -> {'Listar Clientes'.center(22)}|")
    print(f"| 5 | -> {'List Quartos d Cliente'.center(22)}|")
    print(f"| 6 | -> {'Desocupar Quarto'.center(22)}|")
    print(f"| 0 | ->{'Sair'.center(23)}|")
    print(f"+{'-'*30}+\n")
    
    op = str(input("-> "))

    if op == "1":
        tela_reserva()
    elif op == "2":
        name = str(input('Nome: '))
        ident = int(input('CPF: '))
        telef = int(input('PHONE: '))
        com = conexao.Conectar_bd()
        sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
        vall = (ident,)
        com.conectar()
        com.cu.execute(sql, vall)
        resultado = com.cu.fetchall()
        if len(resultado) <= 0:
            print('Cadastro realizado!')
            sleep(2)
            clientes = Reservar_Cliente(name, ident, telef)
            clientes.inserir()
            return main()
        else:
            print('JÁ EXISTE UM CADASTRO COM ESSE CPF!')
            sleep(2)
            return main()
    elif op == "3":
        print('Serviços')
        print('| 1 | -> Frigobar')
        print('| 2 | -> Lavanderia')
        print('| 3 | -> Alimentos')
        print('| 0 | -> VOLTAR')
        desej = input('Serviço Desejado: ')
        if desej == '1':
            cpf = int(input('CPF: '))
            cliente = Frigobar(None, None ,None,cpf)
            cliente.frigobar_pedido()
            return main()
        elif desej == '2':
            ident = int(input('CPF: '))
            com = conexao.Conectar_bd()
            sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
            vall = (ident,)
            com.conectar()
            com.cu.execute(sql, vall)
            resultado = com.cu.fetchall()
            print(resultado)
            if len(resultado) >= 1:
                cliente = Lavanderia.mostrar()
                lavar = input('Deseja Lavar [S/N]: ').upper()
                passar = input('Deseja Passar [S/N]: ').upper()
                cliente = Lavanderia(passar, lavar, ident)
                cliente.passar_roupa()
                cliente.lavar_roupa()
                return main()
            else:
                print('CPF INVALIDO!')
                main()
        elif desej == '3':
            cliente = Servico_Quarto()
            cliente.cardapio()
            fazer_pedido = int(input('Escolha o Pedido: '))
            cliente.fazer_pedido(fazer_pedido)
            return main()
        else:
            return main()
    
    elif op == "4":
        print('''
        0 -> Listar um Cliente
        1 -> Listar Todos os Clientes
        2 - > SAIR
        ''')
        opc = str(input('Opção: '))
        if opc == '0':
            cliente = Reservar_Cliente(None, None, None)
            cpf = int(input('CPF Cliente: '))
            cliente.listar_cliente(cpf, opc)
            sleep(5)
            return main()
        elif opc == '1':
            cliente = Reservar_Cliente(None, None, None)
            cliente.listar_cliente(None, opc)
            sleep(10)
            return main()
        else:
            return main()
    elif op == "5":
        cpf = input('CPF: ')
        cp = Listar_Q_Cliente(cpf)
        cp.quarto_simples()
        cp.quarto_duplo()
        cp.quarto_casal()
        cp.quarto_luxo()
        sleep(6)
        return main()
    elif op == "6":
        cl = Listar_Q_Reservado()
        print('Lista de Quartos ocupados')
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
        sleep(2)
        return main()
    elif op == "0":
        exit() 
    else:
        main()

def tela_reserva():
    os.system("clear")
    print(f"\n+{'-'*30}+")
    print(f"|{'CATEGORIA DE QUARTOS'.center(30)}|")
    print(f"+{'-'*30}+")
    print(f"| 1 | ->{'SIMPLES'.center(23)}|")
    print(f"| 2 | ->{'DUPLO'.center(23)}|")
    print(f"| 3 | ->{'CASAL'.center(23)}|")
    print(f"| 4 | ->{'LUXO'.center(23)}|")
    print(f"| 0 | ->{'VOLTAR'.center(23)}|")
    print(f"+{'-'*30}+\n")
    
    op = str(input("-> "))

    if op == "1":
        cpf = int(input('Digite CPF: '))
        cliente1 = Quarto_Simples(cpf,None,None, None)
        veri = conexao.Conectar_bd()
        sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val = (cpf,)
        veri.conectar()
        veri.cu.execute(sql, val)
        result = veri.cu.fetchall()
        if len(result) >= 1:
            cliente1.inserir_informacao()
            n = input('Nº Quarto: ')
            year = int(input('ANO: '))
            month = int(input('MÊS: '))
            day = int(input('DIA: '))
            cliente1 = Check_In(year, month, day, n_quarto=n)
            cliente1.entrada()
            cliente1.check_in_quarto_simples()
            year1 = int(input('ANO: '))
            month1 = int(input('MÊS: '))
            day1 = int(input('DIA: '))
            cliente1 = Check_An(year1, month1, day1, n_quarto=n)
            cliente1.saida()
            cliente1.check_an_quarto_simples()
            cliente1 = Pagamento(None)
            cliente1.pagamento_simples()
            return main()
        else:
            print('Não existe Cadastro com esse CPF')
            sair = input('Deseja fazer o cadastro [S/N]: ').upper()
            if sair == 'S':
                print('| Cadastro |')
                nome = input('Nome: ')
                ident = input('CPF: ')
                phone = input('Telefone: ')
                cliente1 = Reservar_Cliente(nome=nome, cpf=ident, phone=phone)
                cliente1.inserir()
                print('| 0 | -> VOLTAR')
                return main()
            else:
                print('Volte Sempre')
                sleep(2)
                return main()
    elif op == "2":
        cpf2 = int(input('Digite CPF: '))
        cliente2 = Quarto_Duplo(cpf2,None,None,None)
        veri1 = conexao.Conectar_bd()
        sql1 = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val1 = (cpf2,)
        veri1.conectar()
        veri1.cu.execute(sql1, val1)
        result2 = veri1.cu.fetchall()
        if len(result2) >= 1:
            cliente2.inserir_dados()
            n2 = input('Nº Quarto: ')
            yearr = int(input('ANO: '))
            monthh = int(input('MÊS: '))
            dayy = int(input('DIA: '))
            cliente2 = Check_In(yearr, monthh, dayy, n_quarto=n2)
            cliente2.entrada()
            cliente2.check_in_quarto_duplo()
            year2 = int(input('ANO: '))
            month2 = int(input('MÊS: '))
            day2 = int(input('DIA: '))
            cliente2 = Check_An(year2, month2, day2, n_quarto=n2)
            cliente2.saida()
            cliente2.check_an_quarto_duplo()
            cliente2 = Pagamento(None)
            cliente2.pagamento_duplo()
            return main()
        else:
            print('Não existe Cadastro com esse CPF')
            sair1 = input('Deseja fazer o cadastro [S/N]: ').upper()
            if sair1 == 'S':
                print('| Cadastro |')
                nome1 = input('Nome: ')
                ident1 = input('CPF: ')
                phone1 = input('Telefone: ')
                cliente2 = Reservar_Cliente(nome=nome1, cpf=ident1, phone=phone1)
                cliente2.inserir()
                print('| 0 | -> VOLTAR')
                return main()
            else:
                print('Volte Sempre')
                sleep(2)
                return main()
    elif op == "3":
        cpf3 = int(input('Digite CPF: '))
        cliente3 = Quarto_Casal(cpf3,None,None,None)
        veri2 = conexao.Conectar_bd()
        sql2 = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val2 = (cpf3,)
        veri2.conectar()
        veri2.cu.execute(sql2, val2)
        result3 = veri2.cu.fetchall()
        if len(result3) >= 1:
            cliente3.inserir_infor()
            n3 = input('Nº Quarto: ')
            yearq = int(input('ANO: '))
            monthq = int(input('MÊS: '))
            dayq = int(input('DIA: '))
            cliente3 = Check_In(yearq, monthq, dayq,  n_quarto=n3)
            cliente3.entrada()
            cliente3.check_in_quarto_casal()
            year3 = int(input('ANO: '))
            month3 = int(input('MÊS: '))
            day3 = int(input('DIA: '))
            cliente3 = Check_An(year3, month3, day3, n_quarto=n3)
            cliente3.saida()
            cliente3.check_an_quarto_casal()
            cliente3 = Pagamento(None)
            cliente3.pagamento_casal()
            return main()
        else:
            print('Não existe Cadastro com esse CPF')
            sair2 = input('Deseja fazer o cadastro [S/N]: ').upper()
            if sair2 == 'S':
                print('| Cadastro |')
                nome2 = input('Nome: ')
                ident2 = input('CPF: ')
                phone2 = input('Telefone: ')
                cliente3 = Reservar_Cliente(nome=nome2, cpf=ident2, phone=phone2)
                cliente3.inserir()
                print('| 0 | -> VOLTAR')
                return main()
            else:
                print('Volte Sempre')
                sleep(2)
                return main()
    elif op == "4":
        cpf4 = int(input('Digite CPF: '))
        cliente4 = Quarto_Luxo(cpf4,None,None,None)
        veri3 = conexao.Conectar_bd()
        sql3 = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val3 = (cpf4,)
        veri3.conectar()
        veri3.cu.execute(sql3, val3)
        result4 = veri3.cu.fetchall()
        if len(result4) >= 1:
            cliente4.inserir_l()
            n4 = input('Nº Quarto: ')
            yearw = int(input('ANO: '))
            monthw = int(input('MÊS: '))
            dayw = int(input('DIA: '))
            cliente4 = Check_In(yearw, monthw, dayw, n_quarto=n4)
            cliente4.entrada()
            cliente4.check_in_quarto_luxo()
            print('Check_an')
            year4 = int(input('ANO: '))
            month4 = int(input('MÊS: '))
            day4 = int(input('DIA: '))
            cliente4 = Check_An(year4, month4, day4, n_quarto=n4)
            cliente4.saida()
            cliente4.check_an_quarto_luxo()
            cliente4 = Pagamento(None)
            cliente4.pagamento_luxo()
            return main()
        else:
            print('Não existe Cadastro com esse CPF')
            sair4 = input('Deseja fazer o cadastro [S/N]: ').upper()
            if sair4 == 'S':
                print('| Cadastro |')
                nome4 = input('Nome: ')
                ident4 = input('CPF: ')
                phone4 = input('Telefone: ')
                cliente4 = Reservar_Cliente(nome=nome4, cpf=ident4, phone=phone4)
                cliente4.inserir()
                print('| 0 | -> VOLTAR')
                return main()
            else:
                print('Volte Sempre')
                sleep(2)
                return main()
    elif op == "0":
        main()
    else:
        tela_reserva()

if __name__ == "__main__": # Executar o código apenas se o arquivo foi executado diretamente e não importado
    main()