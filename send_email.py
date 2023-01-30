import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "valenpendragon@gmail.com"
password = "rldroiqxoegokvzq"

receiver = "valenpendragon@hotmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you:
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)