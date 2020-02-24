import yagmail as yg
import sys
import os

def get_server():
    user = input('\nDigite o email remetente: ')
    password = input('Digite a senha: ')
    wrong_login = True
    while wrong_login:
        try:
            server = yg.sender.SMTP(user, password)
        except SMTPAuthenticationError:
            print('\nEmail ou senha inválidos! Digite-os novamente.')
            user = input('\nDigite o email remetente: ')
            password = input('Digite a senha: ')
        except:
            input('\nErro desconhecido. Não foi possível completar o login. Aperte [ENTER] para sair.')
            sys.exit()
        else:
            wrong_login = False
    return server

remetente = 'arrozefeijao504'
senha = 'arrozfeijaoepica'
to = ['arrozefeijao504@gmail.com', 'vitor_simoni@yahoo.com', 'vitor.martin.simoni@gmail.com']
to = to[0]
subject = 'Esse eh o assunto'
body = 'Esse eh o corpo'
attachment = 'picture.png'

# server = get_server()
server = yg.sender.SMTP('arrozefeijao504@gmail.com', 'arrozfeijaoepic')
print('Loggin sucedido')



server.send(to=to, subject=subject, contents=body, attachments=attachment)

print('Email enviado')