# Robin Agent Plus

**The AI Addon for Robin Agent**

This repo is the "Robin Agent Plus" addon. It takes the original Robin Agent (built for beginners with no AI or dropshipping experience) and adds a powerful, clean, lean AI layer on top using our tools, Odoo, Google Workspace, and our skills.

We leave the original Robin Agent exactly as it is for the client. This addon is the optional "pro" layer for real business use.

## Original Shopping List & What We Fixed

### Core (1-7) — All fixed
1. CRM / Lead Management — **[FIXED with Odoo CRM + our AI layer]** (lead tracking, follow-ups, customer records, Gmail/Calendar integration)
2. Invoicing & Billing — **[FIXED with Odoo + our pdf/docx tools]**
3. Accounting / Bookkeeping — **[FIXED with Odoo + Google Sheets dashboards]**
4. Inventory Management — **[FIXED with Odoo + our product-price-monitor and xlsx skills]**
5. Order Fulfillment — **[FIXED with Odoo + maps + supplier research from our tools]**
6. Payment Processing — **[FIXED with Odoo + Stripe/PayPal via Supabase]**
7. E-commerce Platform — **[FIXED with Odoo website + Shopify connector]**

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

**Summary:** 18 of the 20 gaps are now covered. The addon turns Robin into a complete business operating system while keeping the original simple for the beginner client.

## What the Addon Adds
- AI orchestration (Bossman, WillDoThat, Secretary)
- Security-first (environment-aware-scanner with SkillSpector fallback)
- Integration with Google Workspace (Gmail, Calendar, Drive, Sheets, Docs)
- Odoo as the ERP backend
- Our research, scraping, document, and video tools
- Clean approval workflows and logging

## Installation
```bash
git clone https://github.com/familievlieland96-pixel/robin-agent-plus.git
cd robin-agent-plus
pip install -r requirements.txt  # if any
# Copy .env.example to .env and fill credentials
```

## Usage
Load the `robin-addon` skill in Hermes Agent.

All commands are available through our tools and the Odoo connection.

## License
MIT — free for personal and commercial use.

**Built by:** ykycportal (Tony) with Bossman (Hermes Agent)

**Purpose:** Make the beginner Robin Agent powerful for real island businesses while keeping it simple for the client.

**Date:** September 2026

This is the "Robin Agent Plus" addon. It fixes almost the entire shopping list with clean, strong, secure tools.

We kept Microsoft out.

Enjoy.
