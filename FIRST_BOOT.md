# FIRST_BOOT.md — connections checklist (step 1 on any new device)

**The rule: the agents move, the connections never do.**
This repo ships the agents and code (Bossman orchestrator, WillDoThat,
7of9 Secretary, Odoo addon, skills). It ships **zero** personal
connections: no API keys, no passwords, no IDs, no tokens, no email
accounts. Everything personal was deliberately left on the device where
it was created.

When this repo is implemented on **another device with another human**
(a client, a VPS, a USB image), do this checklist **first, in order**,
before running anything else:

## 1. LLM / model provider (Agnes or OpenRouter)
- [ ] Owner's model-provider token, stored on THIS device only.
- [ ] Verify: one completion, read the reply.

## 2. Google Workspace / Gmail
- [ ] Create a FRESH email account on the new device — mailboxes do
      not travel. Create the App Passwords on that account.
- [ ] OAuth (Drive/Calendar/Sheets): console.cloud.google.com -> enable
      APIs -> OAuth client (Desktop app) -> client secret ->
      `GOOGLE_CREDENTIALS_PATH` in .env.
- [ ] Fill .env: BOSS_EMAIL, BOSS_APP_PASSWORD, WILL_EMAIL,
      WILL_APP_PASSWORD.
- [ ] Verify: `python backoffice_email.py check` -> status success.
      (Before .env is filled it fails loudly with the exact var names.)

## 3. GitHub
- [ ] The new human's own token (theirs, not ours), on this device only.
- [ ] Verify: one read-only API call or `gh auth status`.

## 4. Odoo
- [ ] Their Odoo instance URL / db / user / password into .env.
- [ ] Verify: `python main_integration.py --crm` returns a created lead.

## 5. API / connection skills (X, YouTube, scrapers, ads)
- [ ] Any skill that expects a personal key (YouTube Data API, X,
      ad platforms) gets the new owner's own key, on this device.
- [ ] Repo code stays generic; nothing personal is committed, ever.

## Standing rules
- Personal secrets live in `.env` on the current device (gitignored).
- Repos carry unmistakable placeholders only (`your_*`).
- Every module fails loudly with the exact var name if a placeholder
  is still sitting there. No silent no-ops, no invented defaults.
