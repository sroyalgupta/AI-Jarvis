import smtplib

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sagarguptasargam123@gmail.com','He he,you will not get it easily..')
    server.sendmail('sagarguptasargam123@gmail.com',to,content)
    server.close()

sendmail('sroyalgupta@gmail.com','hello')
