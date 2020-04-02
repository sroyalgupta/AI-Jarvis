import smtplib

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sagarguptasargam123@gmail.com','srg@2909')
    server.sendmail('sagarguptasargam123@gmail.com',to,content)
    server.close()

sendmail('sroyalgupta@gmail.com','hello')
