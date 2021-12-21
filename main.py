import smtplib

my_email = "sendermail@gmail.com"
my_password = "xxxxxxxxx"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
for _ in range(50):
    connection.sendmail(from_addr=my_email, to_addrs="receivermail@gmail.com", msg="type_your_message")
connection.close()