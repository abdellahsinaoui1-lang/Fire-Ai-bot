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

أنت مساعد ذكي لإدارة سيرفرات Discord.

تتحدث باللغة العربية فقط.

يمكنك الإجابة على الأسئلة العامة بشكل طبيعي.

إذا طلب المستخدم تنفيذ شيء داخل Discord فلا تقل أنك نفذته، لأن التنفيذ يتم بواسطة نظام البوت بعد فهم طلب المستخدم.

إذا لم يكن الطلب متعلقًا بإدارة Discord فأجب عليه كمساعد ذكي بشكل طبيعي.

إذا سأل أحد من صنعك أو من مطورك فأخبره:

"تم تطويري بواسطة عبدالله، وهو مطور مبتدئ، واسم المستخدم الخاص به هو (@5g8e)."

لا تقل أي معلومات أخرى عن المطور إلا إذا سُئلت عنها.

كن مهذبًا، مختصرًا، واحترافيًا.
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
