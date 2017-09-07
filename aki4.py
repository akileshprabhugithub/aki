#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("yourmail@gmail.com","yourpassword")
message="hi"
s.sendmail("yourmail@gmail.com","receivermail@gmail.com",message)
s.close()