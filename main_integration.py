#!/usr/bin/env python3
"""
Total Robin Agent + Addon Integration
Orchestrates the original Robin simplicity with the Plus addon layer (Odoo CRM, backoffice emails,
Google Workspace, skills from Hermes).
Keeps client Robin untouched — this is the pro layer for The Block / island businesses.

Usage:
  python main_integration.py --help
"""
import argparse
import json
import os
from pathlib import Path

# Load .env
env_path = Path("~/.hermes/.env").expanduser()
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.partition('=')
                os.environ[key.strip()] = value.strip()

# Import components (graceful if missing)
try:
    from odoo_crm import create_lead, add_followup
    ODOO_AVAILABLE = True
except ImportError:
    ODOO_AVAILABLE = False
    def create_lead(*args, **kwargs): return {"status": "unavailable", "error": "odoo_crm not fully loaded"}
    def add_followup(*args, **kwargs): return {"status": "unavailable", "error": "odoo_crm not fully loaded"}

try:
    from backoffice_email import check_inbox as boss_check_inbox, send_email as boss_send
    from willdothat_email import check_inbox as will_check_inbox
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False
    def boss_check_inbox(*args, **kwargs): return {"status": "unavailable"}
    def will_check_inbox(*args, **kwargs): return {"status": "unavailable"}
    def boss_send(*args, **kwargs): return {"status": "unavailable"}

def run_crm_example():
    """Example of full CRM + email + calendar flow."""
    if not ODOO_AVAILABLE:
        return {"status": "error", "message": "Odoo module not available. Install odoorpc and check imports."}
    result = create_lead(
        name="Test Island Business Lead",
        email="test@example.com",
        phone="+1-555-0123",
        source="Website",
        description="Interested in green energy solutions for San Pedro."
    )
    print(json.dumps(result, indent=2))
    return result

def run_email_check():
    """Check both backoffice inboxes."""
    if not EMAIL_AVAILABLE:
        return {"status": "error", "message": "Email modules not available."}
    boss = boss_check_inbox(max_messages=3)
    will = will_check_inbox(max_messages=3)
    combined = {
        "status": "success",
        "boss": boss,
        "will": will,
        "timestamp": "now"
    }
    print(json.dumps(combined, indent=2))
    return combined

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Total Robin Agent Plus Integration - Bossman Orchestrator")
    parser.add_argument("--crm", action="store_true", help="Run CRM lead creation example")
    parser.add_argument("--email-check", action="store_true", help="Check backoffice inboxes")
    parser.add_argument("--full-demo", action="store_true", help="Run full integration demo")
    
    args = parser.parse_args()
    
    if args.crm or args.full_demo:
        print("=== Running Odoo CRM + Google Integration Example ===")
        run_crm_example()
    if args.email_check or args.full_demo:
        print("\n=== Running Backoffice Email Check (Bossman + WillDoThat) ===")
        run_email_check()
    if not any([args.crm, args.email_check, args.full_demo]):
        parser.print_help()
        print("\nTotal integration ready. Set up .env from .env.example, install requirements, then run with --full-demo.")
        print("This layers the addon on original Robin Agent without touching the client version.")
