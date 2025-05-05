import smtplib
from email.message import EmailMessage
from config import ALERT_EMAIL_FROM, ALERT_EMAIL_TO, SMTP_SERVER


def send_sync_report(removed_emails):
    if not removed_emails:
        return

    msg = EmailMessage()
    msg["Subject"] = "OnOffboarder Sync: Removed Emails"
    msg["From"] = ALERT_EMAIL_FROM
    msg["To"] = ALERT_EMAIL_TO
    msg.set_content("\n".join(removed_emails))

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.send_message(msg)
