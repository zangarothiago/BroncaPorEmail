from ast import If
import sounddevice as sd
from numpy import linalg as LA
import numpy as np

print('***********************************************************')
print('****************** Bronca por e-mail **********************')
print('***********************************************************')

duration = 604800  # segundos a executar a escuta - 7 dias

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    
    # 300 é um volume de corte aceitavel...
    if (volume_norm>300): 

        print('e-mail enviado! Medicao Barulho atual em DB:  '+(str(volume_norm)))

        import smtplib

        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        from email.mime.base import MIMEBase
        from email import encoders

        #S M T P - Simple Mail transfer protocol 
        #Para criar o servidor e enviar o e-mail

        #1- STARTAR O SERVIDOR SMTP 
        host = "smtp.gmail.com"
        port = "587"
        login = "jaodedeus@gmail.com"
        senha = "123456789"

        #Dando start no servidor 
        server = smtplib.SMTP(host,port)
        server.ehlo()
        server.starttls()
        server.login(login,senha)


        #2- CONSTRUIR O EMAIL TIPO MIME
        corpo = "<b>Medição do barulho atual em Decibéis:  </b>"+(str(volume_norm))

        #montando e-mail 
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = "joana@gmail.com, bernadao@gmail.com"
        email_msg['Subject'] = "Alerta, muito barulho no ambiente!"
        email_msg.attach(MIMEText(corpo,'html'))

        #3- ENVIAR o EMAIL tipo MIME no SERVIDOR SMTP 
        server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
        server.quit()

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)