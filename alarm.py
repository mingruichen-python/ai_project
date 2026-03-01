import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

gmail_user = input("login with gmail:")
gmail_app_password = input("app password")

def send_email():
    to_email = input("Receiver: ").strip()
    subject = input("Subject: ").strip()

    print("Content (end with empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = Header(subject, "utf-8")
    msg.attach(MIMEText(content, "plain", "utf-8"))
    def timer()：
        try:
            print("For how many times would you like to set for your alarm?(don't leave empty place please, just put a zero there.)")
            while True:
                time_hours=int(input("Hours>>>"))
            if isinstance(time_hours,int):
                break
            while True:
                time_minutes=int(input("Minutes>>>"))
            if isinstance(time_minutes,int):
                break
            while True:
                time_seconds=int(input("Seconds>>>"))
            if isinstance(time_seconds,int):
                break
            times=int(time_hours*60*60+time_minutes*60+time_seconds)
            time.sleep(times)
        except Exception as e:
                print("Error:", e)



    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465,timeout=len(content))
        server.login(gmail_user, gmail_app_password)
        timer()
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print("Error:", e)



send_email()

