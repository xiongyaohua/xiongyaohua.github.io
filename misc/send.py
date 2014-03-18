import smtplib

from email.mime.text import MIMEText

with open("reply_to_huang.txt", "r", encoding="utf-8") as f:
    s = f.read()
    msg = MIMEText(s)

me = "xiongyaohua@gmail.com"
you = "willhwn@gmail.com"
msg["Subject"] = "Re. 近况"
msg["From"] = me
msg["To"] = you

s = smtplib.SMTP("localhost")
s.sendmail(me, [you, me], as_string())
s.quit()

