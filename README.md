# Portfolio site

Plain HTML/CSS/JS — no build step, no framework. Files:

- `index.html` — all content
- `style.css` — design system (colors/type/layout as CSS variables at the top)
- `script.js` — one small thing: highlights the current section in the nav

## Deploy to GitHub Pages (free)

1. Create a new GitHub repo. If you want it at `https://<username>.github.io`
   directly, name the repo exactly `<username>.github.io`. Otherwise any name
   works and it'll be served at `https://<username>.github.io/<repo-name>`.
2. Push these three files (`index.html`, `style.css`, `script.js`) to the
   repo's default branch (usually `main`).
3. In the repo: **Settings → Pages → Source → Deploy from a branch**, pick
   `main` and `/ (root)`, save.
4. Wait ~1 minute, then visit the URL GitHub shows on that same Pages
   settings page.

## Using a custom domain (optional)

1. Buy a domain (Namecheap, Google Domains successor, Porkbun, etc. — a
   `.com` or `.dev` for a name like yours is usually $10–15/year).
2. In your DNS provider, add either:
   - an **A record** for the root domain pointing to GitHub's IPs:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - or a **CNAME record** for a subdomain (e.g. `www`) pointing to
     `<username>.github.io`
3. In the repo: **Settings → Pages → Custom domain**, enter your domain, save.
   This creates a `CNAME` file in your repo automatically — don't delete it.
4. Check "Enforce HTTPS" once GitHub finishes provisioning the certificate
   (can take up to 24h, usually much faster).

## Editing content later

Everything is in `index.html` as plain text inside semantic sections
(`<section id="about">`, `<section id="projects">`, etc.) — no CMS, just
edit the text directly and push. Colors, fonts, and spacing all live as
`:root` variables at the top of `style.css` if you want to adjust the theme.

## Before you publish

- Swap the placeholder social links if any are wrong (`mailto:`, LinkedIn,
  GitHub — currently pointing to the ones from your resume).
- Add a real favicon if you want one (currently none is set).
- Consider adding an actual headshot/photo somewhere in `About` if you'd
  like a personal photo on the page — the current design intentionally
  doesn't use one, but it's easy to add.
