import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


'''
CALL: email_destinatario - string contendo todos os emails, separados por "," e sem espaço
      nome_arquivo       - nome do arquivo que será anexado no corpo do email,
      é necessário especificar a extensão (por exemplo .csv)
'''


#email pra qual vc quer mandar
email_destinatario = ""
#precisa mandar um arquivo, fiquei com preguica de concertar isso
#nem que seja um txt em branco
#precisa incluir path pro arquivo (sempre usando '/' em vez de '\')
#ou coloca o arquivo junto com o script
nome_arquivo = ""
#SEU email que vai mandar o spam
#PRECISA ser gmail
email_remetente = ""
subject = ""
body = ""
#quantidade de emails a serem mandados
spam = 50
#Senha do seu email
senha = ''



#nao mexe nisso
lista_mensagens=[]
i=0
smtp_server= "smtp.gmail.com"
port = 465



#    email_destinatario = ('hfsantana1@gmail.com,andledrao@gmail.com')
# Divide a mensagem em várias partes
lista_emails = email_destinatario.split(',')
print(lista_emails)
mensagem = MIMEMultipart()
mensagem["From"] = email_remetente
mensagem["Subject"] = subject
mensagem.attach(MIMEText(body, "plain"))
# Open PDF file in binary mode

with open(nome_arquivo, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

for __email__ in lista_emails:
    mensagem["To"] = __email__
# Adiciona o cabeçalho e a chave para o arquivo anexado
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {nome_arquivo}",
)
# Adiciona a mensagem arquivada e converte para string
mensagem.attach(part)
text = mensagem.as_string()
lista_mensagens.append(text)
    

# Fazer conexão no servidor e mandar o email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(email_remetente, senha)

    for i in range(spam):
        server.sendmail(email_remetente, lista_emails[0], lista_mensagens[0])
        print('email %i enviado'%i)