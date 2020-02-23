#Modules ====================================================
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
from string import Template
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
    return Template(body)


#Variables ==================================================
remetente = input('Digite o email remetente: ')
senha = input('Digite a senha do email remetente: ')

# remetente = 'arrozefeijao504@gmail.com'
# senha = 'arrozfeijaoepica'

contacts_file = 'contacts.txt'
contacts_separator = '\n'
emails = get_contacts(contacts_file, contacts_separator)

subject = 'Livro do Professor doidão!'

body_file = 'message.txt'
source_body = get_body(body_file)

attachment_file_name = input('Digite o nome do arquivo a ser anexado COM extensão: ')
# attachment_file_name = 'picture.png'

host = 'smtp.gmail.com'
port = 465


#Creating server and ending email ===========================
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    print('Fazendo login no seu email...', end='\n\n')
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
        body = source_body.substitute(email_count=i)
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