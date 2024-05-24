#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os
import sqlite3
from datetime import datetime
saldo=0
estrato = []
os.system('cls')


#txt
def extrato():
    arquivo_estrato = open("CRUD\cadastrotxt.txt", "w")
    arquivo_estrato.write(f"{'EXTRATO':^50}\n")
    arquivo_estrato.write(f"{username:^50}\n")
    for i, (usuario, hora, relatorio) in enumerate(estrato):
        arquivo_estrato.write(f"{relatorio} {hora} \n")


#txt
def Cadastro_usuario(username, password):
    usuarios=[]
    
    arquivo_cadastrotxt= open ("CRUD\cadastrotxt.txt", "r")
    for linha in arquivo_cadastrotxt:
        usuario,senha,saldo=linha.split(",")
        usuarios.append(usuario)
        usuarios.append(senha)
        usuarios.append(saldo)
    arquivo_cadastrotxt.close()
    if username in usuarios:
        return "\033[91mNome de usuário já existe. Por favor, escolha outro.\033[0m"
    elif username in usuarios:
        return "\033[91mUsuario e senhas iguais, tente novamente\033[0m"
    elif username != '' and password != "":
        cadastrar=  open ("cadastrotxt", "a")
        cadastrar.write(f"{username},{password},{saldo}\n")
        cadastrar.close()
        return "\033[92mCadastro realizado com sucesso!\033[0m"
    else:
        return "\033[91mUsuário ou senha vazio\033[0m"
    

#txt
def Login_usuario(username, password):
    usuarios={}
    arquivo_cadastrotxt= open ("CRUD\cadastrotxt.txt", "r")
    for linha in arquivo_cadastrotxt:       
            usuario, senha = linha.split(",")
            usuarios[usuario] = [senha,saldo]
            print(usuarios)
    if username in usuarios and usuarios[username] == password:
        return "\033[91mLogin correto\033[0m"
    elif username not in usuarios:
        return "\033[91mUsuário não encontrado\033[0m"
    else:
        return "\033[91mSenha incorreta\033[0m"


def horario():
    hora = datetime.now()
    hora = hora.strftime("%d/%m/%Y %H:%M")
    return hora

#SQLITE (NÃO PRECISA MUDAR NADA - THAIS DO PASSADO)
def opcoes_banco(username, saldo):
    while True:
        print("=" * 33)
        print("\033[94mDIGITE A OPERAÇÃO DESEJADA\033[0m")
        print("\033[94m1) Consultar saldo\033[0m")
        print("\033[94m2) Saque\033[0m")
        print("\033[94m3) Depositar\033[0m")
        print("\033[94m4) Deletar conta\033[0m")
        print("\033[94m5) Pesquisar conta\033[0m")
        print("\033[94m0) Encerrar sessão\033[0m")
        print("=" * 33)
        opc1 = input()
        if opc1 == "1":
            print("Seu saldo é de R$", saldo)
        elif opc1 == "2":
            try:
                saque = float(input("Qual valor você deseja sacar? "))
                
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                if saldo < saque:
                    print("\033[91mValor insuficiente\033[0m")
                else:
                    saldo -= saque
                    #SAQUE COM TXT
                    relato_saque = f"Saque de R$ {saque:.2f} realizado com sucesso."
                    print("\033[92m" + relato_saque + "\033[0m")
                    estrato.append([username, relato_saque, horario()])
            
        elif opc1 == "3":
            try:
                deposito = float(input("Qual valor que deseja depositar? "))
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                saldo += deposito
                #DEPOSITO COM TXT
                relato_deposito = f"Depósito de R$ {deposito} realizado."
                print("\033[92m" + relato_deposito + "\033[0m")
                estrato.append([username, relato_deposito, horario()])
        elif opc1 == "4":
            deletar_conta = input("Deseja deletar sua conta? (S/N)")
            if deletar_conta.lower() == "s":
            #DELETAR COM TXT
                
                print("\033[92mConta deletada.\033[0m")
                return
        elif opc1 == '5':
            pesquisa = input("digite nome do usuário ")
            #PESQUISA COM TXT E APARECER TUDU MUNDO
            if pesquisa:
                print("\033[92mUsuário {} encontrado\033[0m".format(pesquisa[0]))
            else:
                print("\033[91mNão encontrado\033[0m")
        elif opc1 == "0":
            print("\033[92mEncerrando sessão...\033[0m")
            return
        else:
            print("\033[91mOpção inválida.\033[0m")


while True:
    print("=" * 33)
    print("\033[94m1. Cadastrar\033[0m")
    print("\033[94m2. Login\033[0m")
    print("\033[94m3. Sair\033[0m")
    print("=" * 33)

    opc = input("Escolha uma opção: ")

    if opc == "1":
        username = input("Digite um nome de usuário: ")
        password = input("Digite uma senha: ")
        print(Cadastro_usuario(username, password))
    elif opc == "2":
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        user = Login_usuario(username, password)
        if user:
            print("\033[92mLogin bem-sucedido!\033[0m")
            opcoes_banco(username,saldo)  # Passa o username e o saldo do usuário
        else:
            print("\033[91mNome de usuário ou senha incorretos. Tente novamente.\033[0m")
    elif opc == "3":
        print("\033[92mSaindo...\033[0m")
        break
    else:
        print("\033[91mOpção inválida. Por favor, escolha novamente.\033[0m")

extrato()


while True:
    print("=" * 33)
    print("\033[94m1. Cadastrar\033[0m")
    print("\033[94m2. Login\033[0m")
    print("\033[94m3. Sair\033[0m")
    print("=" * 33)

    opc = input("Escolha uma opção: ")

    if opc == "1":
        username = input("Digite um nome de usuário: ")
        password = input("Digite uma senha: ")
        print(Cadastro_usuario(username, password))
    elif opc == "2":
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        user = Login_usuario(username, password)
        if user:
            print("\033[92mLogin bem-sucedido!\033[0m")
            opcoes_banco(username, user[2])  # Passa o username e o saldo do usuário
        else:
            print("\033[91mNome de usuário ou senha incorretos. Tente novamente.\033[0m")
    elif opc == "3":
        print("\033[92mSaindo...\033[0m")
        break
    else:
        print("\033[91mOpção inválida. Por favor, escolha novamente.\033[0m")

extrato()
