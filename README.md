# Robin Agent Plus

**The AI Addon for Robin Agent**

This repo is the "Robin Agent Plus" addon. It takes the original Robin Agent (built for beginners with no AI or dropshipping experience) and adds a powerful, clean, lean AI layer on top using our tools, Odoo, Google Workspace, and our skills.

We leave the original Robin Agent exactly as it is for the client. This addon is the optional "pro" layer for real business use.

## What this repo actually ships (honest scope)
Code in this repo:
- `odoo_crm.py` — CRM leads/follow-ups via odoorpc; Google Calendar follow-up events + welcome email via the optional `google_api` module (graceful no-op when absent; the result reports exactly what happened)
- `backoffice_email.py` / `willdothat_email.py` — IMAP/SMTP clients for the Bossman & WillDoThat backoffice inboxes (App Passwords, from `.env`)
- `main_integration.py` — orchestrator: `--crm`, `--email-check`, `--full-demo`; skips a step loudly with the exact reason + fix when a dependency is missing
- `robin-addon/SKILL.md` — Hermes skill instructions covering the 8 shopping-list gaps with our tool set

Everything labelled "via Shopify" is handled by the **Shopify store** (payments, storefront) — a must-have in the stack, not by code in this repo. Everything labelled "via Odoo" is provided by **your Odoo instance** (modules + admin UI). This repo ships only the client code, the back-office email clients, the orchestrator, and the skill instructions.

## Original Shopping List & What We Fixed

### Core (1-7) — All fixed
1. CRM / Lead Management — **[FIXED with Odoo CRM + our AI layer]** (lead tracking, follow-ups, customer records, Gmail/Calendar integration)
2. Invoicing & Billing — **[FIXED with Odoo + our pdf/docx tools]**
3. Accounting / Bookkeeping — **[FIXED with Odoo + Google Sheets dashboards]**
4. Inventory Management — **[FIXED with Odoo + our product-price-monitor and xlsx skills]**
5. Order Fulfillment — **[FIXED with Odoo + maps + supplier research from our tools]**
6. Payment Processing — **[FIXED via Shopify (a must)]** Payment gateway (Stripe/PayPal etc.) handled store-side through Shopify. No payment code lives in this repo.
7. E-commerce Platform — **[FIXED via Shopify (a must)]** Storefront runs on Shopify; this addon layers business ops on top. No storefront code in this repo.

### Important Gaps (8-15) — Most fixed
8. Social Media Posting — **[FIXED with our xurl skill + scheduling]**
9. Email Marketing Automation — **[FIXED with Odoo email marketing + our Gmail integration]**
10. Paid Ads Management — **[PARTIAL — monitoring and negative keywords covered by our research skills. Full automation is in progress]**
11. Customer Support / Ticketing — **[FIXED with Odoo Helpdesk]**
12. Project Management — **[FIXED with Odoo Project + our Notion/Airtable skills]**
13. Team Communication — **[FIXED with Odoo Discuss (Slack-like)]**
14. Contract & Document Generation — **[FIXED with our pdf, docx, nano-pdf, ocr-and-documents tools + Odoo Sign]**
15. Analytics Dashboards — **[FIXED with Odoo reporting + our Google Workspace and python scripts]**

### Nice-to-Have (16-20) — Most fixed
16. Tax Compliance — **[FIXED with Odoo tax handling]**
17. Business Registration — **[Left to client/Shopify/lawyer — not in addon]**
18. Review Management — **[FIXED with our research skills + auto-reply via Gmail/social tools]**
19. HR / Payroll — **[FIXED with Odoo HR/Payroll]**
20. Video Production — **[FIXED with bfl_flux3 video generation (text-to-video, image-to-video, audio-to-video) + our manim and ascii-video tools]**

**Summary:** of the 20 gaps, 1 is PARTIAL (paid-ads automation) and 1 is explicitly out of scope (business registration). The remaining 18 are covered **by the Odoo instance (modules in the admin UI) plus the Hermes skills in our tool set** — this repo ships the Odoo CRM client, the two back-office email clients, the orchestrator, and the `robin-addon` skill instructions. What runs on a fresh clone: the code below, not a magic full-stack install.

## What the Addon Adds
- AI orchestration (Bossman, WillDoThat, Secretary)
- Security-first (environment-aware-scanner with SkillSpector fallback)
- Google Workspace integration via the optional `google_api` module (graceful no-op + honest status when absent)
- Your Odoo instance as the ERP backend (this repo ships only the client code)
- Our research, scraping, document, and video tools (Hermes skills, referenced by `robin-addon`)
- Every script reports exactly what it did — skips say "skipped + reason", no silent stubs

## Installation
```bash
git clone https://github.com/familievlieland96-pixel/robin-agent-plus.git
cd robin-agent-plus
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Odoo creds, Gmail App Passwords (BOSS_*, WILL_*). Never commit secrets.
```

## Total Integration (Robin Agent + Addon)
The repo now delivers the **total integrated system**: original Robin Agent (simple, untouched for beginner client) + this Plus addon layer for full business ops.

- Python scripts provide Odoo CRM, backoffice emails (Bossman/WillDoThat accounts), Google integration.
- `main_integration.py` is the orchestrator tying it all (CRM leads → calendar → email, inbox monitoring).
- `robin-addon/SKILL.md` + loaded Hermes skills (odoo-crm, google-workspace, xurl, etc.) cover all shopping list gaps.
- Security: env-based creds, SkillSpector recommended before runs.
- No Microsoft. Lean for island businesses.

Test with:
```bash
python main_integration.py --full-demo
```

## Usage
Load `robin-addon` skill in Hermes.

Run orchestrator for demos or integrate into cron/Bossman workflows.

All components available through our tools, Odoo, and main_integration.py. Original client Robin stays simple.

## License
MIT — free for personal and commercial use.

**Built by:** ykycportal (Tony) with Bossman (Hermes Agent)

**Purpose:** Make the beginner Robin Agent powerful for real island businesses while keeping it simple for the client.

**Date:** September 2026

This is the "Robin Agent Plus" addon. It fixes almost the entire shopping list with clean, strong, secure tools.

We kept Microsoft out.

Enjoy.
