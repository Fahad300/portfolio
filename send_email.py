import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    usr = "faadeemian512@gmail.com"
    pwd = "oyol hpwt rymx wjew"
    context = ssl.create_default_context()
    receiver = "faadeemian512@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(usr, pwd)
        server.sendmail(usr, receiver, message)
