import os
from time import sleep
from frigobar import Frigobar
from lavanderia import Lavanderia
from quartos import Quarto_Simples,Quarto_Duplo,Quarto_Casal,Quarto_Luxo
from data import Check_An, Check_In
from pagamento import Pagamento
import conexao
from cadastro import Reservar_Cliente

def main():
    os.system("clear")
    print(f"\n+{'-'*30}+")
    print(f"|{'HOTEL OSCAR'.center(30)}|")
    print(f"+{'-'*30}+")
    print(f"| 1 | ->{'Reserva'.center(23)}|")
    print(f"| 2 | ->{'Cadastrar'.center(23)}|")
    print(f"| 3 | ->{'Serviço'.center(23)}|")
    print(f"| 0 | ->{'Sair'.center(23)}|")
    print(f"+{'-'*30}+\n")
    
    op = str(input("-> "))

    if op == "1":
        tela_reserva()
    elif op == "2":
        name = input('Nome: ')
        ident = input('CPF: ')
        telef = input('PHONE: ')
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
        print('| 0 | -> VOLTAR')
        desej = input('Serviço Desejado: ')
        if desej == '1':
            cliente = Frigobar(None, None ,None,None)
            cliente.frigobar_pedido()
            return main()
        elif desej == '2':
            ident = input('CPF: ')
            com = conexao.Conectar_bd()
            sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
            vall = (ident,)
            com.conectar()
            com.cu.execute(sql, vall)
            resultado = com.cu.fetchall()
            if len(resultado) >= 1:
                cliente = Lavanderia(None, None, None)
                cliente.mostrar()
                cliente.passar_roupa()
                cliente.lavar_roupa()
                return main()
            else:
                print('CPF INVALIDO!')
                main()
        else:
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
        cliente1 = Quarto_Simples(None,None,None,None,None,None,None,None,None)
        cpf = int(input('Digite CPF: '))
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
            cliente1.check_in_quarto()
            year1 = int(input('ANO: '))
            month1 = int(input('MÊS: '))
            day1 = int(input('DIA: '))
            cliente1 = Check_An(year1, month1, day1, n_quarto=n)
            cliente1.saida()
            cliente1.check_an_quarto()
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
        cliente2 = Quarto_Duplo(None,None,None,None,None,None,None,None,None,None)
        cpf = int(input('Digite CPF: '))
        veri = conexao.Conectar_bd()
        sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val = (cpf,)
        veri.conectar()
        veri.cu.execute(sql, val)
        result = veri.cu.fetchall()
        if len(result) >= 1:
            cliente2.inserir_dados()
            n2 = input('Nº Quarto: ')
            yearr = int(input('ANO: '))
            monthh = int(input('MÊS: '))
            dayy = int(input('DIA: '))
            cliente2 = Check_In(yearr, monthh, dayy, n_quarto=n2)
            cliente2.entrada()
            cliente2.check_in_quarto()
            year2 = int(input('ANO: '))
            month2 = int(input('MÊS: '))
            day2 = int(input('DIA: '))
            cliente2 = Check_An(year2, month2, day2, n_quarto=n2)
            cliente2.saida()
            cliente2.check_an_quarto()
            cliente2 = Pagamento(None)
            cliente2.pagamento_duplo()
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
    elif op == "3":
        cliente3 = Quarto_Casal(None,None,None,None,None,None,None,None,None,None,None,None,None)
        cpf = int(input('Digite CPF: '))
        veri = conexao.Conectar_bd()
        sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val = (cpf,)
        veri.conectar()
        veri.cu.execute(sql, val)
        result = veri.cu.fetchall()
        if len(result) >= 1:
            cliente3.inserir_infor()
            n3 = input('Nº Quarto: ')
            yearq = int(input('ANO: '))
            monthq = int(input('MÊS: '))
            dayq = int(input('DIA: '))
            cliente3 = Check_In(yearq, monthq, dayq,  n_quarto=n3)
            cliente3.entrada()
            cliente3.check_in_quarto()
            year3 = int(input('ANO: '))
            month3 = int(input('MÊS: '))
            day3 = int(input('DIA: '))
            cliente3 = Check_An(year3, month3, day3, n_quarto=n3)
            cliente3.saida()
            cliente3.check_an_quarto()
            cliente3 = Pagamento(None)
            cliente3.pagamento_casal()
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
    elif op == "4":
        cliente4 = Quarto_Luxo(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
        cpf = int(input('Digite CPF: '))
        veri = conexao.Conectar_bd()
        sql = "SELECT cpf FROM cadastro WHERE cpf = %s"
        val = (cpf,)
        veri.conectar()
        veri.cu.execute(sql, val)
        result = veri.cu.fetchall()
        if len(result) >= 1:
            cliente4.inserir_l()
            n4 = input('Nº Quarto: ')
            yearw = int(input('ANO: '))
            monthw = int(input('MÊS: '))
            dayw = int(input('DIA: '))
            cliente4 = Check_In(yearw, monthw, dayw, n_quarto=n4)
            cliente4.entrada()
            cliente4.check_in_quarto()
            print('Check_an')
            year4 = int(input('ANO: '))
            month4 = int(input('MÊS: '))
            day4 = int(input('DIA: '))
            cliente4 = Check_An(year4, month4, day4, n_quarto=n4)
            cliente4.saida()
            cliente4.check_an_quarto()
            cliente4 = Pagamento(None)
            cliente4.pagamento_luxo()
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
    elif op == "0":
        main()
    else:
        tela_reserva()

if __name__ == "__main__": # Executar o código apenas se o arquivo foi executado diretamente e não importado
    main()