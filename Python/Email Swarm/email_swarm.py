#Modules ====================================================
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
import os
os.system('cls')


#Functions ==================================================
def get_contacts(filename, separator):
    '''
    Returns a list of emails.
    '''
    emails = []
    with open(filename, mode='r', encoding='utf-8') as file:
        contacts = file.read()
        emails = contacts.split(separator)
    return emails

def get_body(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        body = file.read()
    return body


#Variables ==================================================
attachment_file_name = input('Digite o nome do arquivo a ser anexado COM extensão: ')
# attachment_file_name = 'picture.png'
wrong_attachment = True
while wrong_attachment:
    try:
        attachment_file = open(attachment_file_name, 'rb')
    except:
        print('\nNome do anexado errado! Verifique o nome do arquivo e sua extensão.')
        attachment_file_name = input('Digite o nome do arquivo a ser anexado COM extensão: ')
    else:
        wrong_attachment = False
        print()

contacts_file = 'contacts.txt'
contacts_separator = '\n'
emails = get_contacts(contacts_file, contacts_separator)

subject = input('Digite o assunto do email: ')
print()

body_file = 'message.txt'
source_body = get_body(body_file)

host = 'smtp.gmail.com'
port = 465


#Creating server and ending email ===========================
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    #Logging to email account while catching wrong email or password
    remetente = input('Digite o email remetente: ')
    senha = input('Digite a senha do email remetente: ')
    # remetente = 'arrozefeijao504@gmail.com'
    # senha = 'arrozfeijaoepica'
    wrong_password = True
    print('Fazendo login no seu email...', end='\n\n')
    while wrong_password:
        try:
            server.login(remetente, senha)
        except:
            print('Email ou senha incorretos!')
            remetente = input('Digite o email remetente: ')
            senha = input('Digite a senha do email remetente: ')
            print()
        else:
            wrong_password = False
    server.login(remetente, senha)

    i=0
    for email in emails:
        i += 1

        #Creating email
        message = MIMEMultipart()
        message['From'] = remetente
        message['To'] = email
        message['Bcc'] = email
        message['Subject'] = subject
        body = source_body
        message.attach(MIMEText(body, 'plain'))

        #Adding attachment
        attachment_file = open(attachment_file_name, 'rb')

        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attachment_file).read())
        encoders.encode_base64(payload)
        payload.add_header(
            'Content-Disposition',
            f'attachment; filename= {attachment_file_name}'
        )
        message.attach(payload)
        
        print('Enviando email número %i...' % i, end='\n\n')
        server.sendmail(remetente, email, message.as_string())

        del message

input('Fim do processo. Para sair, aperte [ENTER]\n')
