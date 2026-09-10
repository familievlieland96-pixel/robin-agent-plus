---
name: robin-addon
description: "Enhances Robin Agent with our tools for inventory, fulfillment, social posting, ads monitoring, documents, analytics, reviews, and video. No Microsoft tools."
version: 1.0.0
author: Tony (ykycportal), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [addon, dropshipping, ecommerce, research, automation]
    related_skills: [google-workspace, himalaya, xurl, product-price-monitor, pdf, docx, xlsx, maps, ascii-video]
---
# Robin Addon

This addon makes Robin Agent stronger by using our existing tools to cover the 8 gaps you listed (4,5,8,10,14,15,18,20). No Microsoft/Playwright. Everything stays clean, lean, and under our control.

It connects research, Google Workspace, email, PDF generation, and our scraping tools into a cohesive system for dropshipping and island businesses.

## Covered Gaps (how we do it with our tools)

4. **Inventory Management** — Use `xlsx` + `product-price-monitor` + our research skills to track stock, prices, and send reorder alerts via Gmail.

5. **Order Fulfillment** — Use `maps` for delivery routes, `himalaya` for supplier emails, and research skills for supplier discovery. We connect to actual ordering via email automation.

8. **Social Media Posting** — Use `xurl` for X/Twitter posting and scheduling. For other platforms we use browser automation through our existing `terminal` + lightweight scripts (no Microsoft).

10. **Paid Ads Management** — Use our research skills to monitor Meta/Google/TikTok ads (scrape performance data) and `google-workspace` for dashboards. We avoid direct API integration to keep it simple and secure.

14. **Contract & Document Generation** — We already have strong tools (`pdf`, `docx`, `xlsx`, `nano-pdf`, `ocr-and-documents`). The addon adds templates and automation for contracts, invoices, and legal documents.

15. **Analytics Dashboards** — Use `google-workspace` (Sheets + Docs), `xlsx`, and our python scripts to create revenue, SEO, and financial dashboards. WillDoThat reviews them automatically.

18. **Review Management** — Use our research skills + `himalaya` to collect reviews from multiple sites and auto-reply via email or our social tools.

20. **Video Production** — Use `ascii-video`, `manim-video`, and our image tools to generate simple product videos or ad frames. For real video we use terminal commands with ffmpeg (no Microsoft).

## Prerequisites
- Robin Agent installed for the client
- Our Google Workspace setup (already done)
- The skills above loaded (`google-workspace`, `himalaya`, `xurl`, `product-price-monitor`, `pdf`, `docx`, `xlsx`, `maps`, `ascii-video`)

## Procedure
1. Identify which gap the client needs.
   - Completion: Clear requirement (e.g. "inventory tracking").
2. Use the matching tool from our stack.
   - Completion: Command run and output saved to Google Drive or Sheets.
3. Add AI layer (WillDoThat reviews, Secretary sends summary, Bossman orchestrates).
   - Completion: Actionable output delivered to the client.
4. Log everything in our system for future improvement.
   - Completion: Entry in memory or Supabase.

## Pitfalls
- Robin Agent is for beginners — keep the addon simple so the client doesn't get overwhelmed.
- Avoid heavy dependencies — we use only what we already have.
- Test on the client's hardware (Apple and Windows) before delivery.
- Security first — always scan any new code with our environment-aware-scanner.

## Verification
- Run a test for each gap (e.g. create a sample inventory sheet, generate a contract, monitor a social post).
- The client should be able to use the addon without understanding AI.
- Check that no Microsoft code is included.
- The addon should make Robin Agent noticeably better without complicating it.

This addon turns Robin into a more complete business tool while keeping it beginner-friendly and 100% under our control. No Microsoft in our hair.

**Status**: Built as addon for the client by Bossman for Tony
