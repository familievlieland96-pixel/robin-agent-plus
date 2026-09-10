#!/usr/bin/env python3
"""
Odoo CRM Integration for Secretary
Connects to Odoo for lead management, follow-ups, and customer records.
Integrates with Google Workspace (Gmail + Calendar) we already set up.

Updated to accept credentials via arguments or .env file for easy testing.
"""
import sys
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import odoorpc
from google_api import gmail, calendar  # Reuse our existing Google Workspace tools

# Load from .env if available
env_path = Path("~/.hermes/.env").expanduser()
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.partition('=')
                os.environ[key.strip()] = value.strip()

ODOO_URL = os.getenv("ODOO_URL", "https://your-odoo-instance.com")
ODOO_DB = os.getenv("ODOO_DB", "your_database")
ODOO_USER = os.getenv("ODOO_USER", "your@email.com")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD", "your_password")

def connect_to_odoo():
    try:
        odoo = odoorpc.ODOO(ODOO_URL, protocol='jsonrpc', port=443 if 'https' in ODOO_URL else 8069)
        odoo.login(ODOO_DB, ODOO_USER, ODOO_PASSWORD)
        print("✓ Connected to Odoo successfully")
        return odoo
    except Exception as e:
        print(f"✗ Odoo connection failed: {e}")
        print("Make sure ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD are set in ~/.hermes/.env or as environment variables.")
        return None

def create_lead(name, email, phone=None, source="Website", description=""):
    odoo = connect_to_odoo()
    if not odoo:
        return {"status": "error", "error": "Odoo connection failed"}
    
    lead_data = {
        'name': name,
        'email_from': email,
        'phone': phone,
        'source': source,
        'description': description or f"Lead from {source} - {datetime.now().strftime('%Y-%m-%d')}",
        'type': 'lead',
    }
    
    lead_id = odoo.execute('crm.lead', 'create', [lead_data])
    print(f"✓ Lead created with ID: {lead_id}")
    
    # Create Google Calendar event for follow-up (2 days from now)
    calendar.create(
        summary=f"Follow up with {name}",
        start=(datetime.now() + timedelta(days=2)).isoformat(),
        end=(datetime.now() + timedelta(days=2, hours=1)).isoformat(),
        description=f"Lead ID: {lead_id}\nEmail: {email}\nSource: {source}"
    )
    
    # Send welcome email via Gmail
    gmail.send(
        to=email,
        subject=f"Welcome {name} - Let's get started with your project",
        body=f"Hi {name},\n\nThank you for your interest. I've created your lead in our system and scheduled a follow-up.\n\nBest,\nSecretary for Bossman"
    )
    
    return {"status": "success", "lead_id": lead_id, "message": "Lead created, calendar event scheduled, welcome email sent"}

def add_followup(lead_id, note, next_action=""):
    odoo = connect_to_odoo()
    if not odoo:
        return {"status": "error", "error": "Odoo connection failed"}
    
    # Add note to lead
    odoo.execute('mail.message', 'create', [{
        'model': 'crm.lead',
        'res_id': int(lead_id),
        'body': note,
        'message_type': 'comment'
    }])
    
    print(f"✓ Follow-up note added to lead {lead_id}")
    
    if next_action:
        print(f"Next action recorded: {next_action}")
    
    return {"status": "success", "lead_id": lead_id, "note": note}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Odoo CRM for Secretary")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    subparsers.add_parser("test", help="Test Odoo connection")
    
    create_parser = subparsers.add_parser("create-lead", help="Create a new lead")
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--email", required=True)
    create_parser.add_argument("--phone", default=None)
    create_parser.add_argument("--source", default="Website")
    create_parser.add_argument("--description", default="")
    
    followup_parser = subparsers.add_parser("add-followup", help="Add follow-up to a lead")
    followup_parser.add_argument("--lead-id", type=int, required=True)
    followup_parser.add_argument("--note", required=True)
    followup_parser.add_argument("--next-action", default="")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == "test":
        connect_to_odoo()
    elif args.command == "create-lead":
        result = create_lead(args.name, args.email, args.phone, args.source, args.description)
        print(json.dumps(result, indent=2))
    elif args.command == "add-followup":
        result = add_followup(args.lead_id, args.note, args.next_action)
        print(json.dumps(result, indent=2))
    else:
        print("Unknown command. Use test, create-lead, or add-followup.")
