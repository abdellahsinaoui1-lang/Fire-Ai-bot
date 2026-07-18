import os

TOKEN = os.getenv("TOKEN")
GROQ_KEY = os.getenv("GROQ_KEY")

ALLOWED_ROLE_ID = 1528082462897475674

if TOKEN is None:
    raise ValueError("TOKEN not found.")

if GROQ_KEY is None:
    raise ValueError("GROQ_KEY not found.")
