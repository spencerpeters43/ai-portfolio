# Spencer Peters — AI Portfolio

Django-based portfolio site showcasing six AI/MIS projects.

---

## Quick Start

### 1. Create and activate a virtual environment

```bash
cd ~/Desktop/ai-portfolio
python -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### 5. Start the development server

```bash
python manage.py runserver
```

The site is now live at **http://127.0.0.1:8000**

---

## Populating Content

### Admin panel

Go to **http://127.0.0.1:8000/admin** and log in with your superuser credentials.

**Add Projects** — `Portfolio > Projects > Add Project`

| Field | Notes |
|---|---|
| Title | Project name |
| Slug | Auto-filled from the title — leave as-is |
| Summary | One sentence shown on the projects grid |
| Project type | chatbot / workflow / code / video / web_app |
| Is featured | Check to show on the home page |
| Order | Lower numbers appear first (use 1–6) |
| Business problem … What I learned | The six detail fields shown on the project page |
| Tools used | One tool per line — renders as pill badges |
| Key features | One feature per line — renders as a bullet list |
| Screenshot | Upload to `media/screenshots/` |
| Video | Upload MP4 to `media/videos/` |
| Video URL | YouTube/Vimeo URL for iframe embed (used if no video file) |
| Downloadable file | Upload ZIP/JSON to `media/downloads/` |
| GitHub link / Live demo link | Optional URLs — only shown when present |

**Add Skills** — `Portfolio > Skills > Add Skill`

Enter each skill with a category (e.g. `AI/ML`, `Programming Languages`, `Frameworks`, `Tools`) and proficiency level. Skills are grouped by category on the Skills page.

**Read contact messages** — `Portfolio > Contact Messages`

Messages submitted through the contact form appear here. Mark them read with the `Is read` checkbox in the list view.

---

## Adding Your Resume

Drop your PDF into:

```
media/downloads/resume.pdf
```

The Resume page will display and link to it automatically.

---

## Personalizing the Site

| What to change | Where |
|---|---|
| GitHub URL in navbar footer | `templates/base.html` — search `YOUR_USERNAME` |
| LinkedIn URL in navbar footer | `templates/base.html` — search `YOUR_USERNAME` |
| GitHub / LinkedIn on Contact page | `templates/contact.html` — search `YOUR_USERNAME` |
| Profile photo | Drop `profile.jpg` into `static/img/`, then update `templates/about.html` per the comment |
| Bio text | `templates/about.html` — marked with `<!-- UPDATE -->` comments |
| Botpress chatbot embed | Paste snippet into `templates/base.html` at the `<!-- BOTPRESS CHATBOT EMBED GOES HERE -->` comment |

---

## Project Structure

```
ai-portfolio/
├── ai_portfolio/       # Django project (settings, urls, wsgi)
├── portfolio/          # App (models, views, admin, forms, urls)
├── templates/          # All HTML templates
├── static/css/         # styles.css — blue theme + custom classes
├── media/
│   ├── screenshots/    # Project screenshot uploads
│   ├── videos/         # Project video uploads
│   └── downloads/      # Downloadable files + resume.pdf
├── manage.py
└── requirements.txt
```

---

## Six Projects Reference

| # | Title | Type | Notes |
|---|---|---|---|
| 1 | Botpress Chatbot | chatbot | Embed in base.html; detail page has screenshot + description |
| 2 | n8n Agent Workflow | workflow | Screenshot + video upload; downloadable JSON; demo link = Google Form |
| 3 | LangChain Agent | code | Downloadable ZIP + GitHub link |
| 4 | Google AI Studio / Nano Banana Video | video | Video is the primary visual — use video field or video_url |
| 5 | Machine Learning Project | code | Downloadable ZIP + GitHub link |
| 6 | Campus SkillSwap | web_app | Live demo link + GitHub link |
