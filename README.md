
# 🌦 AI Second Brain

A personal, AI-powered knowledge management system built to organize  studies, notes, and projects — powered by Google Gemini and built with Streamlit.

## What It Does

AI Second Brain takes raw text or uploaded files (PDF / DOCX / TXT) and runs them through AI-powered workflows to instantly generate:

- 📚 **Flashcards** — spaced-repetition Q&A pairs from any text
- 📝 **Summaries** — concise breakdowns of long material
- 🩺 **Explanations** — plain-language explainers with formulas and clinical context
- 🛠️ **Project Plans** — structured phases, tools, risks, and timelines from raw ideas
- 🗂️ **Note Organization** — cleans and classifies messy notes for my Obsidian vault
- 🔬 **Research Analysis** — summarizes findings, methodology, strengths/limitations
- 📔 **Journaling** — reflective prompts and pattern-spotting from journal entries

Every result is automatically saved as a Markdown file so it slots straight into my Obsidian vault.

## Tech Stack

- **Streamlit** — UI
- **Google Gemini API** (`google-genai`) — AI processing
- **Obsidian** — knowledge vault / note storage
- **Python** — backend logic
- **Git & GitHub** — version control

## Project Structure

```
AI-Second-Brain/
├── app.py                  # Streamlit entry point
├── ai/
│   ├── gemini.py            # Gemini API wrapper
│   ├── router.py            # Routes a task to its prompt + saves output
│   ├── config_loader.py      # Loads workflows.json
│   ├── prompt_loader.py      # Loads prompt templates
│   ├── file_loader.py        # Reads PDF/DOCX/TXT uploads
│   └── output_manager.py     # Saves AI output to markdown files
├── ui/
│   ├── workspace.py          # Main workspace UI
│   └── biomedical.py         # Biomedical explainer UI
├── prompts/                 # System prompt templates per workflow
├── config/
│   └── workflows.json        # Maps each task to its prompt + output location
├── inbox/                   # Quick capture notes
├── revision/                 # Generated flashcards
├── projects/                 # Generated project plans
└── .env                      # Gemini API key (not committed)
```

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## How It Works

1. Choose a workflow (flashcards, summary, biomedical, project, organize, research, journal)
2. Paste text or upload a file
3. Click **Process** — the app loads the matching prompt template, sends it to Gemini along with your text, and returns a structured result
4. Output is displayed in-app and saved automatically to the right folder for that workflow
