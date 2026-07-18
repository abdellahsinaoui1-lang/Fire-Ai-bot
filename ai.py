from groq import Groq

from config import GROQ_KEY

# ===========================
# AI Client
# ===========================

client = Groq(api_key=GROQ_KEY)

# ===========================
# Model
# ===========================

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# ===========================
# System Prompt
# ===========================

SYSTEM_PROMPT = """
أنت F7 Bot.

تحدث باللغة العربية فقط.

استخدم اللهجة المصرية بشكل طبيعي.

أنت بوت لإدارة سيرفرات Discord.

يمكنك مساعدة المستخدمين وإنشاء الرومات والرتب وإدارة السيرفر.

إذا كان المستخدم يتحدث معك بشكل عادي فقم بالرد بشكل طبيعي.

إذا طلب تنفيذ شيء متعلق بالسيرفر فاشرح له ما ستفعله.
"""

# ===========================
# Chat Function
# ===========================

def ask_ai(prompt: str, guild):

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
