import os

TOKEN = os.getenv("TOKEN")
GROQ_KEY = os.getenv("GROQ_KEY")

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

if TOKEN is None:
    raise Exception("TOKEN variable not found.")

if GROQ_KEY is None:
    raise Exception("GROQ_KEY variable not found.")
    # Role allowed to use F7 Bot
ALLOWED_ROLE_ID = 1528082462897475674
