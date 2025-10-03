import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from datetime import datetime

def fetch_unread_emails(sender, password, summarizer, settings, max_emails=10):
    emails = []
    imap = None
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com", timeout=15)
        imap.login(sender, password)
        imap.select("INBOX")
        status, messages = imap.search(None, "UNSEEN")
        if status != "OK":
            return emails
        email_ids = messages[0].split()[-max_emails:]
        for eid in email_ids:
            try:
                status, msg_data = imap.fetch(eid, "(RFC822)")
                if status != "OK" or not msg_data or not msg_data[0]:
                    continue
                raw = msg_data[0][1]
                msg = email.message_from_bytes(raw)
                emails.append({'id': eid, 'msg': msg})
            except:
                continue
    except Exception as e:
        logging.error(f"Error fetching emails: {e}")
    finally:
        if imap:
            try:
                imap.close()
                imap.logout()
            except:
                pass
    return emails

def send_email_with_draft(sender, password, to_email, subject, body):
    try:
        reply = MIMEMultipart()
        reply["From"] = sender
        reply["To"] = to_email
        reply["Subject"] = f"Re: {subject}"
        reply.attach(MIMEText(body, "plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, to_email, reply.as_string())
        return True, "Email sent successfully"
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        return False, str(e)

def mark_email_as_read(sender, password, email_id):
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com", timeout=10)
        imap.login(sender, password)
        imap.select("INBOX")
        imap.store(email_id, '+FLAGS', '\\Seen')
        imap.close()
        imap.logout()
        return True
    except Exception as e:
        logging.error(f"Error marking email as read: {e}")
        return False
