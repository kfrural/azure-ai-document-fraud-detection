import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(message):
    #tem que mudar para o os dados reais aqui
    sender_email = "seu@email.com"
    receiver_email = "destinatario@email.com"
    password = "sua_senha_apenas_para_exemplo"

    server = smtplib.SMTP('smtp.seu-provedor.com', 587)
    server.starttls()
    server.login(sender_email, password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Alerta de Fraude Detectada"
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server.send_message(msg)
    print("E-mail enviado com sucesso.")
    server.quit()

if __name__ == "__main__":
    message = "Fraude detectada no documento ID 12345."
    send_alert(message)
