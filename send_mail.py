from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email='gideonmandu@gmail.com'
    from_password='Q059:01j'
    to_email=email

    subject='Height data'
    message=f"Hey there, your height is <strong>{height}</strong>. <br> Average  height of all is <strong>{average_height}</strong> and is calculated out of <strong>{count}</strong> people. <br> Thank you!" 

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)