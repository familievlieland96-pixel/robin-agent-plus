#!/usr/bin/env python3
"""
WillDoThat Back Office Email Client
Separate account for WillDoThat (the Captain's right hand).
Personal by design: the repo ships NO real address or password.
Copy .env.example to .env and fill WILL_EMAIL / WILL_APP_PASSWORD
(on a new machine, create the account fresh - it does not travel).
Uses App Password for Gmail.
"""
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from datetime import datetime

EMAIL = os.getenv("WILL_EMAIL", "")
APP_PASSWORD = os.getenv("WILL_APP_PASSWORD", "")
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"

def _configured():
    if not EMAIL or not APP_PASSWORD:
        return "WILL_EMAIL / WILL_APP_PASSWORD not set. Copy .env.example to .env and fill them in (see FIRST_BOOT.md)."
    return None

def check_inbox(max_messages=5):
    uncfg = _configured()
    if uncfg:
        return {"status": "error", "account": "WillDoThat", "error": uncfg, "timestamp": datetime.now().isoformat()}
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, APP_PASSWORD)
        mail.select('inbox')
        _, data = mail.search(None, 'UNSEEN')
        unread_ids = data[0].split()[:max_messages]
        messages = []
        for num in unread_ids:
            _, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            messages.append({
                'id': num.decode(),
                'from': msg['from'],
                'subject': msg['subject'],
                'date': msg['date']
            })
        mail.logout()
        return {"status": "success", "account": "WillDoThat", "unread": len(messages), "messages": messages, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        return {"status": "error", "account": "WillDoThat", "error": str(e), "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        print(json.dumps(check_inbox(), indent=2))
    else:
        print(json.dumps(check_inbox(), indent=2))
