# P P - AI Employee (Chat + AI Brain starter)

## Included
- Streamlit chat interface
- Department selector
- Upload and text extraction for XLSX/XLSM, CSV, PDF, DOCX, TXT, MD
- Loads `PP_Knowledge_Base_v1.md` as operating reference
- OpenAI Responses API integration

## Deploy
1. Replace the repository's `streamlit_app.py` with this version.
2. Replace `requirements.txt` with the included version.
3. Keep `PP_Knowledge_Base_v1.md` in the repository root.
4. In Streamlit Cloud, open App settings -> Secrets and add:

```toml
OPENAI_API_KEY = "your-api-key"
OPENAI_MODEL = "gpt-5.4-mini"
```

5. Save and reboot the app.

Never commit API keys to GitHub. OpenAI API usage is billed separately from ChatGPT subscriptions and may incur charges.

## Safety
P P reads uploaded files for analysis but does not edit or overwrite the originals. This starter does not yet create edited Excel/Word/PDF output files or automate external actions.
