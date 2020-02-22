import yagmail

receiver = "arrozefeijao504@gmail.com"
body = "Hello there from Yagmail"
filename = "picture.png"

yag = yagmail.SMTP(user="arrozefeijao504@gmail.com", password='arrozfeijaoepica')
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)