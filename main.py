import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

credentials = __import__("credentials")
email_address = credentials.email
password = credentials.app_password

msg = MIMEMultipart()
msg['From'] = "Mad Max"
msg["To"] = "pydevelops@gmail.com"
msg["Subject"] = "Hello nerd, its Mad Max"

with open("message.txt", 'r') as message:
    subject = message.read()
    msg.attach(MIMEText(subject, "plain"))

attached_file = "mad_max.png"
with open(attached_file, "rb") as attachment:
    payload = MIMEBase("application", "octet-stream")
    payload.set_payload(attachment.read())

    encoders.encode_base64(payload)
    payload.add_header("Content-Disposition", f"attachment; filename={attached_file}")
    msg.attach(payload)


text = msg.as_string()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email_address, password)
    server.sendmail(email_address, "pydevelops@gmail.com", text)
