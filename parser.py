import json

from ai import client, MODEL


PARSER_PROMPT = """
أنت محلل أوامر لـ F7 Bot.

مهمتك هي تحويل كلام المستخدم إلى JSON فقط.

لا تكتب أي شرح.

لا تكتب Markdown.

لا تكتب ```json

إذا لم يستطع البوت تنفيذ الطلب أرجع:

{
    "NoSkill0": {
        "Reply": "لا أستطيع تنفيذ هذا الطلب."
    }
}

الأوامر المدعومة حالياً:

- CreateChannel
- DeleteChannel
- EditChannelName
- CreateRole
- GrantRole
- CreateCategory

أمثلة:

اعمل روم اسمه chat

↓

{
    "CreateChannel0":{
        "Name":"chat",
        "Type":"text",
        "Category":null
    }
}

اعمل روم صوتي اسمه Music

↓

{
    "CreateChannel0":{
        "Name":"Music",
        "Type":"voice",
        "Category":null
    }
}
"""


def parse_command(prompt: str, server_info: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": PARSER_PROMPT + "\n\nServer Information:\n" + server_info
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)

    except Exception:
        return {
            "NoSkill0": {
                "Reply": text
            }
        }
