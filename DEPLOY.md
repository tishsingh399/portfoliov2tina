# Deploy Playbook — Tina Portfolio

Step-by-step from zero to live URL. Do this once, then every update is just two commands.

---

## PART 1 — One-time setup

### Step 1 — Check if Git is installed

Open Terminal (press `Cmd + Space`, type `Terminal`, hit Enter).

Type this and press Enter:
```
git --version
```

If you see something like `git version 2.x.x` → you're good, skip to Step 2.

If you see `command not found` → run this:
```
xcode-select --install
```
A popup will appear. Click Install. Wait for it to finish. Then re-run `git --version` to confirm.

---

### Step 2 — Configure Git with your name and email (first time only)

```
git config --global user.name "Tina Singh"
git config --global user.email "your@email.com"
```

Replace with your actual email. This just labels your commits — it's not public-facing unless you make your repo public.

---

### Step 3 — Create a GitHub account (if you don't have one)

Go to [github.com](https://github.com) → Sign up → Free plan is fine.

---

### Step 4 — Create a new repository on GitHub

1. Log in to GitHub
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - **Repository name:** `tina-portfolio` (or anything you want)
   - **Description:** My design portfolio
   - **Visibility:** Private (safer — you can make it public later)
   - ✅ Leave "Initialize this repository" **unchecked** (you already have the files)
4. Click **Create repository**
5. GitHub will show you a page with setup instructions — keep this tab open

---

### Step 5 — Connect your local folder to GitHub

In Terminal, navigate to your portfolio folder:
```
cd ~/tina-portfolio
```

Initialize Git, connect to GitHub, and push:
```
git init
git add .
git commit -m "Initial portfolio deploy"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/tina-portfolio.git
git push -u origin main
```

**Replace `YOUR_GITHUB_USERNAME`** with your actual GitHub username (visible in the URL on GitHub).

When prompted for a password: GitHub no longer accepts passwords here. You need a **Personal Access Token** — see the note below.

---

### Note — GitHub authentication (Personal Access Token)

GitHub requires a token instead of a password when pushing from Terminal.

1. Go to GitHub → click your profile photo (top right) → **Settings**
2. Scroll to the bottom of the left sidebar → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**
4. Note: `Portfolio deploy`
5. Expiration: 90 days (or No expiration if you don't want to repeat this)
6. Check the box: ✅ **repo** (that's all you need)
7. Click **Generate token**
8. **Copy the token immediately** — you won't see it again

When Terminal asks for your GitHub password, **paste this token** instead.

To avoid typing it every time:
```
git config --global credential.helper osxkeychain
```
After you enter the token once, macOS Keychain saves it.

---

## PART 2 — Deploy to Vercel

### Step 6 — Create a Vercel account

Go to [vercel.com](https://vercel.com) → **Sign Up** → choose **Continue with GitHub**.

This connects Vercel to your GitHub automatically — no extra setup needed.

---

### Step 7 — Import your repo

1. On the Vercel dashboard, click **Add New → Project**
2. You'll see your GitHub repos listed — find `tina-portfolio` and click **Import**
3. On the configure screen:
   - **Framework Preset:** Other (leave as is — this is plain HTML)
   - **Root Directory:** `./` (leave as is)
   - **Build Command:** leave empty
   - **Output Directory:** leave empty
4. Click **Deploy**

Vercel will build and deploy in about 30 seconds.

---

### Step 8 — Get your live URL

After deploy, Vercel gives you a URL like:
```
https://tina-portfolio-abc123.vercel.app
```

You can also set a custom domain — go to your project → **Settings → Domains** → add your domain.

---

## PART 3 — Every update after that

This is all you need from now on. Every time you edit the HTML and want it live:

```
cd ~/tina-portfolio
git add .
git commit -m "Update portfolio content"
git push
```

Vercel detects the push automatically and redeploys within ~30 seconds. No login, no dashboard.

---

## PART 4 — Adding a new case study

When you're ready to add a case study page:

1. Duplicate `case-studies/portfolio-as-product.html`
2. Rename it to match your project, e.g. `case-studies/shield-design-system.html`
3. Edit the content inside
4. In `index.html`, find the matching work card and update:
   ```html
   <a href="case-studies/shield-design-system.html" class="card-link">View Case Study</a>
   ```
5. Save both files
6. Push:
   ```
   cd ~/tina-portfolio
   git add .
   git commit -m "Add Shield DS case study"
   git push
   ```
Live in 30 seconds.

---

## PART 5 — When you're job hunting

When you want to activate the availability signal on the homepage:

1. Open `index.html` in a text editor (TextEdit works, or download [VS Code](https://code.visualstudio.com) — it's free and much better)
2. Find this line (around line 1210):
   ```js
   const SHOW_AVAILABILITY = false;
   ```
3. Change `false` to `true`
4. Update the text in the HTML (search for `hero-avail`):
   ```html
   <span class="avail-text">Open to senior IC and lead roles</span>
   ```
   Change to whatever reflects your situation
5. Push:
   ```
   git add .
   git commit -m "Enable availability signal"
   git push
   ```

To send recruiter mode to a hiring manager, share this URL:
```
https://your-vercel-url.vercel.app?r=1
```

The `?r=1` auto-activates the condensed recruiter view.

---

## Quick reference — commands you'll use repeatedly

| What you want to do | Command |
|---|---|
| Go to your portfolio folder | `cd ~/tina-portfolio` |
| See what files changed | `git status` |
| Stage all changes | `git add .` |
| Commit with a message | `git commit -m "your message here"` |
| Push to GitHub (triggers Vercel deploy) | `git push` |
| Check your push history | `git log --oneline` |

---

## Troubleshooting

**"fatal: not a git repository"**
→ You're not in the right folder. Run `cd ~/tina-portfolio` first.

**"error: remote origin already exists"**
→ Run `git remote remove origin` then re-run the `git remote add origin ...` line.

**"rejected — non-fast-forward"**
→ Run `git pull origin main --rebase` then `git push` again.

**Vercel shows old version after push**
→ Go to Vercel dashboard → your project → **Deployments** tab → check if a new deployment triggered. If not, click **Redeploy** on the latest deployment.

**Page looks broken on Vercel but fine locally**
→ Check the file paths. Vercel is case-sensitive. `Index.html` ≠ `index.html`. Keep everything lowercase.
