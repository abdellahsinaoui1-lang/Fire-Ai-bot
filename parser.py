import json

from ai import client, MODEL


PARSER_PROMPT = """
أنت محلل أوامر لـ F7 Bot.

حول كلام المستخدم إلى JSON فقط.

لا تكتب أي شرح.

لا تكتب Markdown.

لا تكتب ```json

القواعد:

- أرجع JSON صالح فقط.
- إذا لم يوجد أمر مناسب استخدم NoSkill0.
- يمكن أن يكون هناك أكثر من أمر في نفس الرسالة.
- استخدم المفاتيح:
CreateChannel0
CreateRole0
DeleteRole0
GrantRole0
...

=========================
الأوامر المدعومة
=========================

CreateChannel
DeleteChannel

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

=========================
أمثلة
=========================

اعمل روم اسمه chat

{
    "CreateChannel0":{
        "Name":"chat",
        "Type":"text",
        "Category":null
    }
}

اعمل روم صوتي اسمه Music

{
    "CreateChannel0":{
        "Name":"Music",
        "Type":"voice",
        "Category":null
    }
}

اعمل كاتيجوري اسمها الإدارة

{
    "CreateCategory0":{
        "Name":"الإدارة"
    }
}

احذف كاتيجوري الإدارة

{
    "DeleteCategory0":{
        "Name":"الإدارة"
    }
}

اعمل رتبة اسمها Staff

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":null,
        "Permissions":[]
    }
}

اعمل رتبة اسمها Staff لونها أحمر

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":"احمر",
        "Permissions":[]
    }
}

اعمل رتبة اسمها Moderator لونها أزرق وصلاحياتها إدارة الرومات وحذف الرسائل وباند

{
    "CreateRole0":{
        "Name":"Moderator",
        "Color":"ازرق",
        "Permissions":[
            "manage_channels",
            "manage_messages",
            "ban_members"
        ]
    }
}

احذف رتبة Staff

{
    "DeleteRole0":{
        "Name":"Staff"
    }
}

اعط أحمد رتبة Staff

{
    "GrantRole0":{
        "Member":"Ahmed",
        "Role":"Staff"
    }
}

شيل رتبة Staff من أحمد

{
    "RemoveRole0":{
        "Member":"Ahmed",
        "Role":"Staff"
    }
}

احذف روم chat

{
    "DeleteChannel0":{
        "Name":"chat"
    }
}

إذا لم تستطع تنفيذ الطلب:

{
    "NoSkill0":{
        "Reply":"لا أستطيع تنفيذ هذا الطلب."
    }
}
"""


def parse_command(prompt: str, server_info: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": PARSER_PROMPT
                + "\n\nServer Information:\n"
                + server_info
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
