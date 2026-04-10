# Tina Singh Portfolio — Setup Guide

Everything you need to deploy, edit, and extend this portfolio.

---

## Folder Structure

```
tina-portfolio/
├── index.html                        ← Main portfolio page
├── case-studies/
│   ├── portfolio-as-product.html     ← Case study #1
│   └── [your-next-case-study].html   ← Add new ones here
├── vercel.json                       ← Security headers + URL routing
├── .gitignore                        ← Keeps junk out of your repo
└── SETUP.md                          ← This file
```

---

## Deploy to Vercel

### First time

1. Push this folder to a GitHub repo (public or private — both work)
2. Go to [vercel.com](https://vercel.com) → **Add New Project**
3. Import your GitHub repo
4. Framework: **Other** (no framework needed — this is pure HTML)
5. Root directory: leave as `/` (or point to `tina-portfolio/` if it's inside a larger repo)
6. Click **Deploy**

Vercel will auto-detect `index.html` and serve it as the root. Done.

### Every update after that

Just push to `main`. Vercel redeploys automatically within ~30 seconds.

### Custom domain

In Vercel dashboard → your project → **Settings → Domains** → add your domain.
HTTPS (TLS) is automatic. HSTS is handled by Vercel's edge.

---

## Editing Content

All content lives directly in the HTML files. No build step, no CMS.

### Change your name / title / headline

In `index.html`, find and edit:

```html
<!-- Page title -->
<title>Tina Singh — Senior Product Designer</title>

<!-- Nav -->
<div class="nav-name">Tina Singh</div>

<!-- Hero tag -->
<div class="hero-tag"><span>Senior Product Designer</span></div>

<!-- Hero headline -->
<span class="h1-tagline">Systems thinker. Pixel-level craft.</span>
<span class="h1-main">I design systems that make complex products usable.</span>

<!-- Hero description -->
<p class="hero-desc">...</p>
```

### Edit a work card

Each card is a `<div class="card">` block. Edit the text directly:

```html
<div class="card-title">Your Project Title</div>
<div class="card-desc" id="desc1">One sharp sentence. Action + impact.</div>
<div class="card-outcome" id="outcome1">Metric · Metric · Metric</div>
```

### Change the card link (Coming Soon → real URL)

```html
<!-- Change this: -->
<a href="#" class="card-link">Coming Soon</a>

<!-- To this: -->
<a href="case-studies/your-slug.html" class="card-link">View Case Study</a>
```

### Edit Proof Points (metrics)

```html
<div class="metric-num">340<sup>+</sup></div>
<div class="metric-label">Components shipped</div>
```

### Update contact email / links

```html
<a href="mailto:your@email.com" class="contact-email">your@email.com</a>

<!-- Footer links -->
<a href="YOUR_LINKEDIN_URL" class="contact-link">LinkedIn</a>
<a href="YOUR_RESUME_URL" class="contact-link">Resume PDF</a>
```

---

## Adding a New Case Study

### Step 1 — Copy the template

Duplicate `case-studies/portfolio-as-product.html` and rename it:

```
case-studies/your-project-slug.html
```

Use lowercase, hyphens only. Examples:
- `shield-design-system.html`
- `ai-a11y-pipeline.html`
- `ai-interaction-patterns.html`

### Step 2 — Update the case study content

Open your new file. Edit the following sections in order:

```html
<!-- Page title -->
<title>Your Case Study Title — Tina Singh</title>

<!-- Back link — keep this pointing to ../index.html -->
<a href="../index.html" class="nav-back">← Back to Work</a>

<!-- Case study header -->
<div class="cs-tag">Case Study · Your Category</div>
<h1 class="cs-title">Your Project Title</h1>
<p class="cs-sub">One sentence that reframes what this project is really about.</p>

<!-- Reframe statement (the sharp opener) -->
<p class="cs-reframe-line">This is not a [X] project.<br><em>It's a [what it really is] project.</em></p>

<!-- Meta row — edit the 4 values -->
<div class="cs-meta-val">Your Role</div>
<div class="cs-meta-val">Timeline</div>
<div class="cs-meta-val">Scope</div>
<div class="cs-meta-val">Your Key Outcome</div>
```

Then fill in each section: What This Proves, Key Decisions, The Problem, My Role, Constraints, Outcome, Why It Mattered, What I Learned.

### Step 3 — Link it from index.html

In `index.html`, find the card for this project and update the link:

```html
<a href="case-studies/your-project-slug.html" class="card-link">View Case Study</a>
```

Also update the `featured-cs` block if this becomes your new featured case study:

```html
<a href="case-studies/your-project-slug.html" class="featured-cs fade-in">
  <div class="featured-cs-title">Your Project Title</div>
  <div class="featured-cs-desc">One sentence description.</div>
</a>
```

### Step 4 — Test locally before pushing

Open both files in a browser:
- `index.html` — check the card link goes to the right place
- `case-studies/your-slug.html` — check the back link returns to index
- Test light/dark toggle on both pages

---

## Security Checklist

Run this before every push:

- [ ] **No API keys** anywhere in the HTML or JS
- [ ] **No secrets** in comments (`<!-- TODO: remove password -->` style)
- [ ] **Email address** — if you're worried about scraping, replace with a contact form service (Formspree, Web3Forms) instead of `mailto:`
- [ ] **No personal data** beyond what you intentionally put on a public portfolio (email, LinkedIn, city)
- [ ] `.gitignore` is in place — confirm `.env` and `.DS_Store` are listed
- [ ] After pushing, view source in an incognito window and scan for anything you didn't mean to publish

### What vercel.json protects you from

| Header | Protects against |
|--------|-----------------|
| `X-Frame-Options: DENY` | Clickjacking — prevents your page from being embedded in an iframe on another site |
| `X-Content-Type-Options: nosniff` | MIME sniffing attacks |
| `Content-Security-Policy` | XSS — restricts what scripts and resources can load. Currently allows `unsafe-inline` because all JS/CSS is inline in the HTML files. If you ever externalize scripts, tighten this. |
| `Referrer-Policy` | Controls what URL info leaks to third parties when visitors click links |
| `Permissions-Policy` | Blocks camera, microphone, geolocation access (nothing in this portfolio uses them) |
| `frame-ancestors 'none'` | Reinforces X-Frame-Options at the CSP level |

### What Vercel handles automatically

- HTTPS / TLS certificate — forced on all traffic
- HSTS (HTTP Strict Transport Security) — enforced at Vercel's edge
- DDoS mitigation — handled by Vercel's infrastructure

### Things that are safe because of how this is built

- **No database** — no SQL injection surface
- **No server-side code** — no RCE surface
- **No auth** — no session hijacking surface
- **No npm packages** — no supply chain attack surface
- **No external scripts** except Google Fonts — and fonts are load-only, no JS execution

---

## Updating the Pixel Art

The pixel art frames are defined in `index.html` inside the `frames` array in the `<script>` block.

Each frame is a 20×20 grid of palette indices:

```js
{ label: 'YourFrame', grid: [
  // 20 rows, each with 20 numbers
  // 0 = transparent, 1-35 = colors from the P[] palette
  [0,0,0,0,...],
  ...
] }
```

The palette `P[]` is defined just above. To add a new color, append to the array and reference the new index in your grid.

---

## Changing the Theme Colors

All colors are CSS custom properties in `:root` (dark mode) and `[data-theme="light"]` (light mode).

```css
:root {
  --accent: #e05a42;  /* Change this to change all accent/red highlights */
  --yellow: #ffd700;  /* Metric numbers */
  --bg:     #0a0a12;  /* Page background */
}
```

Change `--accent` in both `:root` and `[data-theme="light"]` to rebrand the whole portfolio to a new accent color.

---

## Recruiter Mode

Recruiter Mode is toggled via the nav button. When ON:
- Hero description and skill tags are hidden
- Cards show bullets + outcome only (no narrative desc)
- About section paragraphs are hidden

To edit what shows in recruiter mode, find each card's bullet list:

```html
<ul class="card-bullets" id="bullets1">
  <li>0→1 design system across 8 enterprise products</li>
  <li>340+ components with Figma + code token parity</li>
  <li>FORK token model: primitives never chain through semantic</li>
</ul>
```

Keep bullets tight: one fact per line, number-first where possible.
