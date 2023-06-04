import email.message
import smtplib

def dicionarioEmail(tipo,mensagem):
    corpo_do_email_senha = f"""
            <p>Acho que você esqueceu sua senha!</p>

            <p>A sua senha é esta daqui: {mensagem}</p>
            
            <p>Não a perca novamente em!</p>

            <p>Att,</p>
            <p>ADM.</p>
        """

    corpo_do_email_confirmacao = f"""
                <p>Obrigado por realizar o cadastro na nossa plataforma!</p>

                <p>Esperamos fornecer o melhor serviço possível</p>

                <p>Att,</p>
                <p>ADM.</p>
            """

    dic = {'senha':corpo_do_email_senha,'confirmar':corpo_do_email_confirmacao}

    return dic[tipo]

def envioEmail(destino,assunto,mensagem,tipo):

    try:
        corpo_do_email = dicionarioEmail(tipo,mensagem)
        msg = email.message.Message()
        msg['Subject'] = assunto
        msg['From'] = 'braincaseadm@gmail.com'
        msg['To'] = destino
        password = 'twnarciddeydzjur'
        msg.add_header('Content-Type','text/html')
        msg.set_payload(corpo_do_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'],password)
        s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
        return True

    except Exception:
        return False