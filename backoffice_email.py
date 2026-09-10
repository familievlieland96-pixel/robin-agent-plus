#!/usr/bin/env python3
"""
Back Office Email Client for Bossman (islabossmann@gmail.com)
Managed by Secretary for Bossman.
Uses App Password for IMAP/SMTP.
"""
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from datetime import datetime

EMAIL = "islabossmann@gmail.com"
APP_PASSWORD = "fketsdauloxpeami"  # From latest user input (fket sdau loxp eami)
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"

def check_inbox(max_messages=10):
    """Check inbox for new messages."""
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
                'date': msg['date'],
                'snippet': str(msg.get_payload()[:100]) if msg.is_multipart() else "No snippet"
            })
        
        mail.logout()
        return {"status": "success", "unread_count": len(messages), "messages": messages, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        return {"status": "error", "error": str(e), "timestamp": datetime.now().isoformat()}

def send_email(to, subject, body, html=False):
    """Send email from Bossman's account."""
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = f"Bossman <{EMAIL}>"
        msg['To'] = to
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html' if html else 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return {"status": "sent", "to": to, "subject": subject}
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        result = check_inbox()
        print(json.dumps(result, indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "send":
        if len(sys.argv) >= 5:
            result = send_email(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
            print(json.dumps(result, indent=2))
    else:
        print("Usage: python backoffice_email.py check | send <to> <subject> <body>")
        print("Current status for islabossmann@gmail.com (Bossman account managed by Secretary)")
        print(json.dumps(check_inbox(), indent=2))
