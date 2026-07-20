import json

from ai import client, MODEL


PARSER_PROMPT = """
أنت محلل أوامر لـ F7 Bot.

مهمتك هي تحويل كلام المستخدم إلى JSON فقط.

القواعد:

- أرجع JSON صالح فقط.
- لا تكتب أي شرح.
- لا تستخدم Markdown.
- لا تستخدم ```json.
- إذا لم تعرف الطلب استخدم NoSkill0.

إذا لم يستطع البوت تنفيذ الطلب أرجع:

{
    "NoSkill0":{
        "Reply":"لا أستطيع تنفيذ هذا الطلب."
    }
}

==========================
المهارات المدعومة
==========================

CreateChannel
DeleteChannel
EditChannelName

CreateCategory
DeleteCategory

CreateRole
DeleteRole

GrantRole
RemoveRole

BanMember
KickMember
TimeoutMember

SendMessage
PurgeMessages

ChangeNickname

==========================
أمثلة
==========================

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

اعمل كاتيجوري اسمها الإدارة

↓

{
    "CreateCategory0":{
        "Name":"الإدارة"
    }
}

اعمل رتبة اسمها Staff

↓

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":null,
        "Permissions":[]
    }
}

اعمل رتبة اسمها Staff لونها أحمر

↓

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":"احمر",
        "Permissions":[]
    }
}

اعمل رتبة اسمها Staff لونها أحمر وتقدر تحذف الرسائل وتطرد الأعضاء

↓

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":"احمر",
        "Permissions":[
            "manage_messages",
            "kick_members"
        ]
    }
}

اعمل رتبة اسمها Owner بكل الصلاحيات

↓

{
    "CreateRole0":{
        "Name":"Owner",
        "Color":null,
        "Permissions":[
            "administrator"
        ]
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

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:

        return {
            "NoSkill0": {
                "Reply": text
            }
        }
