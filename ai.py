from groq import Groq

from config import GROQ_KEY

# ===========================
# AI Client
# ===========================

client = Groq(api_key=GROQ_KEY)

# ===========================
# Model
# ===========================

MODEL = "llama-3.3-70b-versatile"

# ===========================
# System Prompt
# ===========================

SYSTEM_PROMPT = """
أنت F7 Bot.

تتحدث باللغة العربية فقط.

أنت مساعد ذكي لإدارة سيرفرات Discord.

إذا كان المستخدم يتحدث معك بشكل عادي، رد عليه بشكل طبيعي.

إذا كان يريد تنفيذ أمر داخل Discord فلا تقل أنك نفذت الأمر، لأن التنفيذ يتم بواسطة النظام.
اشرح فقط ما يريده إذا لزم الأمر.
"""

# ===========================
# Chat Function
# ===========================

def chat(prompt: str, guild):

    server_name = guild.name if guild else "Unknown"

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT + f"\nاسم السيرفر: {server_name}"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=700
    )

    return response.choices[0].message.content
